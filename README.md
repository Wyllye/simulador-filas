# Simulador de Filas 

**Grupo:** Luiz Gustavo Przygoda, Marco Antônio Borghetti, Maria Isabel Wirth Marafon e Vinícius Andrei Wille
**Disciplina:** Modelagem e Simulação de Sistemas  

---

## Descrição do projeto

Aplicação web simples (Streamlit) que simula o funcionamento de um sistema de fila com **1 servidor** e disciplina **FIFO**.  
O usuário informa as três entradas principais: **Quantidade de clientes (N)**, **Intervalo entre chegadas (min)** e **Duração do atendimento (min)**. O app gera a tabela de eventos (chegada, início/fim de atendimento, espera) e calcula as métricas solicitadas no enunciado (IC médio, TA médio, tamanho médio da fila estimado, tempo médio de espera, tempo médio no sistema).

---

## Link do Deploy
    ```bash
    https://simulador-filas-jzintdwbugfl5xomahe3zp.streamlit.app/

---

## Estrutura do repositório

### 📦 simulador-filas/
  - 📃 app.py
  - 📃 style.css
  - 📃requirements.txt
  - 📃README.md

---

## Como executar localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/Wyllye/simulador-filas.git
   cd simulador-filas
   
2. Instale as Dependências
   ```bash
    pip install -r requirements.txt

4. Rode o app
   ```bash
   streamlit run app.py
