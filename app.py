# app.py
# Grupo: Nome1; Nome2; Nome3; Nome4
# Disciplina: Modelagem e Simulação de Sistemas
# Data: 01/12/2025

import streamlit as st
import numpy as np
import pandas as pd
from pathlib import Path

# ---- Carregar CSS externo ----
css_path = Path("style.css")
if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
else:
    st.warning("style.css não encontrado. Coloque o arquivo na mesma pasta.")

st.set_page_config(page_title="Simulador de Filas — Suporte HelpDesk", layout="wide")

st.title("Simulador de Filas — Suporte HelpDesk")
st.write("Insira as informações na barra lateral para gerar o funcionamento do sistema.")

# ---- Sidebar ----
with st.sidebar:
    st.markdown("## Entradas do Sistema")
    N = st.number_input("Quantidade de clientes (N)", min_value=1, value=100, step=1)
    fixed_ic = st.number_input("Intervalo entre chegadas (min)", min_value=0.01, value=1.00, step=0.01, format="%.2f")
    fixed_service = st.number_input("Duração do atendimento (min)", min_value=0.01, value=2.00, step=0.01, format="%.2f")
    st.markdown("---")
    st.caption("Modelo: 1 servidor (FIFO) • Tempos determinísticos")

# ---- Simulação ----
arrivals = np.cumsum([fixed_ic] * N)
services = np.array([fixed_service] * N)

def simulate(arrivals, services):
    n = len(arrivals)
    start = np.zeros(n)
    end = np.zeros(n)
    wait = np.zeros(n)
    server_free = 0.0

    for i in range(n):
        start_time = max(arrivals[i], server_free)
        end_time = start_time + services[i]
        start[i] = start_time
        end[i] = end_time
        wait[i] = start_time - arrivals[i]
        server_free = end_time

    return start, end, wait

start, end, wait = simulate(arrivals, services)

# ---- Métricas ----
IC_mean = np.mean(np.diff(arrivals)) if N > 1 else fixed_ic
TA_mean = np.mean(services)
TF_mean = np.mean(wait)
TS_mean = np.mean(end - arrivals)
lambda_min = 1 / IC_mean
NF_est = lambda_min * TF_mean

# ---- Exibição ----
st.subheader("Resultados do Sistema")

# Linha 1 – 3 métricas
col1, col2, col3 = st.columns(3)
col1.metric("Intervalo médio entre chegadas (min)", f"{IC_mean:.2f}")
col2.metric("Duração média do atendimento (min)", f"{TA_mean:.2f}")
col3.metric("Tempo médio de espera na fila (min)", f"{TF_mean:.2f}")

st.write("")

# Linha 2 – 3 colunas para manter alinhamento perfeito
col4, col5, col6 = st.columns(3)
col4.metric("Tempo médio no sistema (TS) (min)", f"{TS_mean:.2f}")
col5.metric("Tamanho médio da fila estimado (NF)", f"{NF_est:.3f}")
col6.markdown("<div class='metric-placeholder'></div>", unsafe_allow_html=True)

st.markdown("---")

# ---- Tabela ----
df = pd.DataFrame({
    "Cliente": np.arange(1, N+1),
    "Chegada (min)": arrivals,
    "Início atendimento (min)": start,
    "Fim atendimento (min)": end,
    "Tempo de atendimento (min)": services,
    "Espera na fila (min)": wait
})

st.subheader("Tabela de Funcionamento do Sistema")
st.dataframe(df.style.format({
    "Chegada (min)": "{:.2f}",
    "Início atendimento (min)": "{:.2f}",
    "Fim atendimento (min)": "{:.2f}",
    "Tempo de atendimento (min)": "{:.2f}",
    "Espera na fila (min)": "{:.2f}"
}), use_container_width=True)

csv = df.to_csv(index=False).encode("utf-8")
st.download_button("Baixar tabela em CSV", csv, "tabela_eventos.csv", "text/csv")

st.markdown("---")
st.write("Modelo didático com 1 servidor e tempos determinísticos.")
