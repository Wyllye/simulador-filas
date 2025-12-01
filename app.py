import streamlit as st
import numpy as np
import pandas as pd
from pathlib import Path

css_path = Path("style.css")
if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(page_title="Simulador de Filas — Suporte HelpDesk", layout="wide")

st.title("Simulador de Filas — Suporte HelpDesk")
st.write("Insira as informações na barra lateral para gerar o funcionamento do sistema.")

with st.sidebar:
    st.markdown("## Entradas do Sistema")
    N = st.number_input("Quantidade de clientes (N)", min_value=1, value=100, step=1)
    atendentes = st.number_input("Quantidade de atendentes", min_value=1, value=1, step=1)
    fixed_ic = st.number_input("Intervalo entre chegadas (min)", min_value=0.01, value=1.00, step=0.01, format="%.2f")
    fixed_service = st.number_input("Duração do atendimento (min)", min_value=0.01, value=2.00, step=0.01, format="%.2f")
    st.markdown("---")
    st.caption("Modelo: c atendentes (FIFO) • Tempos determinísticos")

arrivals = np.cumsum([fixed_ic] * N)
services = np.array([fixed_service] * N)

def simulate_multiserver(arrivals, services, c):
    n = len(arrivals)
    start_times = np.zeros(n)
    end_times = np.zeros(n)
    wait_times = np.zeros(n)
    servers = np.zeros(c)

    for i in range(n):
        idx = np.argmin(servers)
        start = max(arrivals[i], servers[idx])
        end = start + services[i]
        start_times[i] = start
        end_times[i] = end
        wait_times[i] = start - arrivals[i]
        servers[idx] = end

    return start_times, end_times, wait_times

start, end, wait = simulate_multiserver(arrivals, services, atendentes)

IC_mean = np.mean(np.diff(arrivals)) if N > 1 else fixed_ic
TA_mean = np.mean(services)
TF_mean = np.mean(wait)
TS_mean = np.mean(end - arrivals)
lambda_min = 1 / IC_mean
NF_est = lambda_min * TF_mean

st.subheader("Resultados do Sistema")

col1, col2, col3 = st.columns(3)
col1.metric("Intervalo médio entre chegadas (min)", f"{IC_mean:.2f}")
col2.metric("Duração média do atendimento (min)", f"{TA_mean:.2f}")
col3.metric("Tempo médio de espera (TF)", f"{TF_mean:.2f}")

st.write("")

col4, col5, col6 = st.columns(3)
col4.metric("Tempo médio no sistema (TS)", f"{TS_mean:.2f}")
col5.metric("Tamanho médio da fila (NF)", f"{NF_est:.3f}")
col6.metric("Atendentes ativos", f"{atendentes}")

st.markdown("---")

df = pd.DataFrame({
    "Cliente": np.arange(1, N+1),
    "Chegada (min)": arrivals,
    "Início (min)": start,
    "Fim (min)": end,
    "Serviço (min)": services,
    "Espera (min)": wait
})

df_display = df.set_index("Cliente")

st.subheader("Tabela de Funcionamento do Sistema")
st.dataframe(df_display.style.format({
    "Chegada (min)": "{:.2f}",
    "Início (min)": "{:.2f}",
    "Fim (min)": "{:.2f}",
    "Serviço (min)": "{:.2f}",
    "Espera (min)": "{:.2f}"
}), use_container_width=True)

csv = df.to_csv(index=False).encode("utf-8")
st.download_button("Baixar tabela em CSV", csv, "tabela_eventos.csv", "text/csv")

st.markdown("---")
st.write(f"Simulação realizada com {atendentes} atendente(s). Modelo FIFO com tempos determinísticos.")
