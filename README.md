# Modelagem Epidemiológica da Dengue (SEIR-V)

Este repositório contém a implementação computacional de um modelo compartimental determinístico para a dinâmica de transmissão da Dengue, desenvolvido para a disciplina de **Epidemiologia Computacional** do **DEINFO/UFRPE**[cite: 3, 4, 5].

## 📌 Sobre o Modelo
Este projeto utiliza uma abordagem **SEIR-V**. Ele modela a interação entre humanos e o vetor (*Aedes aegypti*), considerando:
- **S**: Suscetíveis
- **E**: Expostos (Latência humana)
- **I**: Infectados
- **R**: Recuperados
- **Sv/Iv**: Dinâmica do Vetor (Suscetíveis e Infectados)

## 🚀 Como Rodar

### Pré-requisitos
- Python 3.9+ (Testado em Python 3.14)
- Pip

### Instalação
1. Clone o repositório e acesse a pasta:
   ```bash
   git https://github.com/pehcs/Modelagem-Compartimental-SEIR-V-da-Dengue
   cd Modelagem-Compartimental-SEIR-V-da-Dengue
```

2. Crie e ative o ambiente virtual:
```bash
python3 -m venv venv
source venv/bin/activate  # No macOS/Linux

```


3. Instale as dependências:
```bash
pip install -r requirements.txt

```

### Execução
Para gerar a simulação e visualizar o gráfico do surto:

```bash
python3 model.py

```

## 📊 Metodologia

A resolução das equações diferenciais ordinárias é realizada via método de **Runge-Kutta adaptativo**, utilizando a biblioteca `SciPy` (`solve_ivp`). Os resultados permitem avaliar o impacto de intervenções como o controle vetorial na curva de infectados humanos.
