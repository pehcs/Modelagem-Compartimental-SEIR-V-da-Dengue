from __future__ import annotations
from dataclasses import dataclass
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

@dataclass(frozen=True)
class SEIRVParams:
    beta_h: float   # Transmissão mosquito -> humano
    beta_v: float   # Transmissão humano -> mosquito
    gamma: float    # Recuperação humana (1/dias de infecção)
    epsilon: float  # Período de incubação no humano (1/dias)
    mu_v: float     # Mortalidade natural do mosquito
    N_h: int        # População humana total

def seirv_rhs(t, y, p: SEIRVParams):
    S, E, I, R, Sv, Iv = y
    
    # Dinâmica Humana
    # Força de infecção depende do número de mosquitos infectados (Iv)
    lambda_h = p.beta_h * Iv / p.N_h
    dS = -lambda_h * S
    dE = lambda_h * S - p.epsilon * E
    dI = p.epsilon * E - p.gamma * I
    dR = p.gamma * I

    # Dinâmica do Vetor (População de mosquitos considerada constante p/ simplificar)
    Nv = Sv + Iv
    lambda_v = p.beta_v * I / p.N_h
    dSv = p.mu_v * Nv - lambda_v * Sv - p.mu_v * Sv
    dIv = lambda_v * Sv - p.mu_v * Iv

    return [dS, dE, dI, dR, dSv, dIv]

# Exemplo de Simulação (Main)
def main():
    # Parâmetros baseados em literatura de arboviroses
    params = SEIRVParams(
        beta_h=0.35,   # Probabilidade de infecção humano/mosquito
        beta_v=0.15,   # Probabilidade de infecção mosquito/humano
        gamma=1/7,     # 7 dias para recuperar
        epsilon=1/5,   # 5 dias de incubação
        mu_v=1/14,     # Mosquito vive ~14 dias
        N_h=100000     # 100 mil habitantes (ex: um bairro de Recife)
    )

    y0 = [99990, 0, 10, 0, 200000, 500] # 10 humanos infectados, 500 mosquitos infectados
    t_span = (0, 120) # 4 meses de surto
    
    sol = solve_ivp(seirv_rhs, t_span, y0, args=(params,), t_eval=np.linspace(0, 120, 120))
    
    plt.plot(sol.t, sol.y[2], label="Infectados (Humanos)")
    plt.plot(sol.t, sol.y[5] / 2, label="Infectados (Vetores) / 2") # Escalonado p/ visualização
    plt.legend()
    plt.title("Simulação SEIR-V: Surto de Dengue")
    plt.show()

if __name__ == "__main__":
    main()