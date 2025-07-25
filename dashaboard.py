import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("📊 Progresso Real vs Metas - Peso e Força")

semanas = list(range(1, 13))
peso_meta = np.linspace(65, 72, 12)
forca_meta = np.linspace(50, 75, 12)

peso_real = []
forca_real = []

st.subheader("🔍 Digite seus resultados reais por semana:")

for i in range(12):
    col1, col2 = st.columns(2)
    with col1:
        peso = st.number_input(f"Semana {i+1} - Peso (kg)", value=float(round(peso_meta[i], 1)))
    with col2:
        forca = st.number_input(f"Semana {i+1} - Força (kg)", value=float(round(forca_meta[i], 1)))
    peso_real.append(peso)
    forca_real.append(forca)

# Gráfico
fig = go.Figure()
fig.add_trace(go.Scatter(x=semanas, y=peso_meta, name='Meta de Peso', line=dict(dash='dash', color='blue')))
fig.add_trace(go.Scatter(x=semanas, y=forca_meta, name='Meta de Força', line=dict(dash='dash', color='green')))
fig.add_trace(go.Scatter(x=semanas, y=peso_real, name='Peso Real', mode='lines+markers', line=dict(color='blue')))
fig.add_trace(go.Scatter(x=semanas, y=forca_real, name='Força Real', mode='lines+markers', line=dict(color='green')))

fig.update_layout(
    title="📈 Comparativo de Progresso",
    xaxis_title="Semana",
    yaxis_title="Peso / Força (kg)",
    hovermode="x unified"
)

st.plotly_chart(fig, use_container_width=True)
