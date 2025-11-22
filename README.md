# Simulador de Filas — Projeto (Versão Simplificada)

**Grupo:** ; Luiz Gustavo Przygoda, Marco Antônio Borghetti, Maria Isabel Wirth Marafon e Vinícius Andrei Wille
**Disciplina:** Modelagem e Simulação de Sistemas  

---

## Descrição rápida

Aplicação web simples (Streamlit) que simula o funcionamento de um sistema de fila com **1 servidor** e disciplina **FIFO**.  
O usuário informa as três entradas principais: **Quantidade de clientes (N)**, **Intervalo entre chegadas (min)** e **Duração do atendimento (min)**. O app gera a tabela de eventos (chegada, início/fim de atendimento, espera) e calcula as métricas solicitadas no enunciado (IC médio, TA médio, tamanho médio da fila estimado, tempo médio de espera, tempo médio no sistema).

> Arquivo principal do app: `app.py`. :contentReference[oaicite:1]{index=1}

---

## Estrutura do repositório

simulador-filas/
```├── app.py # Aplicação Streamlit (entrada do sistema)```
```├── style.css # Estilo visual (opcional)```
```├── requirements.txt```
```└── README.md```

---

## Como executar localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/SEU_USUARIO/simulador-filas.git
   cd simulador-filas
   
2. Instale as Dependências
    pip install -r requirements.txt

3. Rode o app
   streamlit run app.py
