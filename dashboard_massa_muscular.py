import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# --- Dados básicos ---
dados_basicos = {
    "Altura": "1,73 m",
    "Peso": "65 kg",
    "Objetivo": "Ganho de Massa Muscular",
    "Treino": "Noturno (~20h)",
    "Suplementação": "Creatina 6g/dia dividida + Hipercalórico Dark Mass 1 dose pós-treino",
    "Restrições": "Livre de glúten, sem whey, sem restrição à lactose"
}

# --- Plano alimentar detalhado ---
refeicoes_detalhadas = {
    "Café da Manhã": [
        {"Descrição": "2 ovos inteiros (fritos no azeite ou cozidos)", "Quantidade": "2 unid.", "Kcal": 140},
        {"Descrição": "Pão sem glúten (milho/arroz/tapioca)", "Quantidade": "2 fatias", "Kcal": 180},
        {"Descrição": "Banana média fatiada com canela", "Quantidade": "1 unid.", "Kcal": 90},
        {"Descrição": "Suco natural (laranja ou abacaxi com hortelã)", "Quantidade": "200 ml", "Kcal": 80},
        {"Descrição": "Creatina", "Quantidade": "3g", "Kcal": 0},
    ],
    "Almoço": [
        {"Descrição": "Peito de frango grelhado", "Quantidade": "120g", "Kcal": 198},
        {"Descrição": "Arroz integral cozido (1 concha)", "Quantidade": "100–120g", "Kcal": 130},
        {"Descrição": "Feijão cozido (1 concha)", "Quantidade": "100g", "Kcal": 70},
        {"Descrição": "Salada + azeite + sementes de chia/linhaça", "Quantidade": "À vontade", "Kcal": 80},
        {"Descrição": "Legumes cozidos (cenoura, abóbora, vagem) - opcional", "Quantidade": "100g", "Kcal": 40},
        {"Descrição": "Opção 2: Substituir arroz por batata-doce", "Quantidade": "120g cozida", "Kcal": 110},
        {"Descrição": "Opção 3: Substituir arroz por quinoa e cuscuz", "Quantidade": "60–80g cuscuz", "Kcal": 120},
    ],
    "Jantar": [
        {"Descrição": "Peito de frango ou omelete", "Quantidade": "120g", "Kcal": 198},
        {"Descrição": "Arroz integral cozido (meia a 1 concha)", "Quantidade": "50–100g", "Kcal": 70},
        {"Descrição": "Legumes variados", "Quantidade": "100g", "Kcal": 40}
    ],
    "Pós-Treino": [
        {"Descrição": "Hipercalórico Dark Mass", "Quantidade": "1 dose (120g)", "Kcal": 457},
        {"Descrição": "Creatina", "Quantidade": "3g", "Kcal": 0},
        {"Descrição": "Banana ou 1 colher de cacau puro (opcional)", "Quantidade": "1 unid./1 col", "Kcal": 90},
        {"Descrição": "Alternativa: Shake caseiro com fruta + pasta de amendoim + proteína vegetal", "Quantidade": "1 porção", "Kcal": 400},
    ],
    "Shake (Pré/Pós)": [
        {"Descrição": "Bebida vegetal (arroz, amêndoa, soja, aveia s/glúten)", "Quantidade": "200 ml", "Kcal": 70},
        {"Descrição": "Banana madura", "Quantidade": "1 unid.", "Kcal": 90},
        {"Descrição": "Proteína vegetal (ervilha, arroz, soja isolada)", "Quantidade": "1 scoop (30g)", "Kcal": 120},
        {"Descrição": "Aveia sem glúten (opcional)", "Quantidade": "1 colher sopa", "Kcal": 40},
        {"Descrição": "Pasta de amendoim", "Quantidade": "1 colher sopa", "Kcal": 90},
        {"Descrição": "Canela ou cacau (a gosto)", "Quantidade": "1 colher chá", "Kcal": 5},
        {"Descrição": "*Versão calórica*: Adicione óleo de coco ou 1/2 abacate", "Quantidade": "1 colher ou 1/2 unid.", "Kcal": 100}
    ],
    "Ceia": [
        {"Descrição": "Leite integral quente", "Quantidade": "200 ml", "Kcal": 124},
        {"Descrição": "Queijo minas frescal ou farinha de amendoim", "Quantidade": "50g ou 2 colheres", "Kcal": 130},
        {"Descrição": "Cacau em pó ou canela", "Quantidade": "1 colher chá", "Kcal": 10}
    ]
}

# --- Suplementação ---
suplementacao = [
    "Creatina monohidratada: 6 g por dia dividida em 2 doses (3 g pela manhã e 3 g pós-treino)",
    "Hipercalórico Dark Mass: 1 dose pós-treino",
    "Proteína vegetal isolada (ervilha/arroz/soja): 1–2 doses/dia para complementar proteínas",
    "Ômega-3 (vegano ou tradicional): 1.000–2.000 mg/dia",
    "Multivitamínico sem glúten: 1 vez ao dia"
]

# --- Dicas finais ---
dicas_finais = [
    "Mantenha hidratação adequada (2,5 a 3 litros/dia)",
    "Evite substituir refeições principais pelo hipercalórico",
    "Ajuste as quantidades conforme a evolução semanal (peso, medidas, força)",
    "Durma de 7 a 9 horas por noite para recuperação",
    "Consulte nutricionista para ajustes personalizados",
    "➡️ Quantidade total estimada de arroz por dia: 100 a 200g (cozido). Para ganho calórico extra, até 300g/dia."
    "🕗 Café da manhã (6h–7h)"
    "🕙 Lanche da manhã (9h)"
    "🕛 Almoço (12h–13h)"
    "🕒 Merenda(15h–16h)"
    "🏋️‍♂️ Pré-treino (18h–19h)"
    "🌙 Jantar | 🛌 Ceia (22h–23h)"
]

# --- Streamlit app ---
st.title("Plano Alimentar Completo para Ganho de Massa Muscular - Eduardo Holanda")

st.header("📋 Dados Básicos")
for k, v in dados_basicos.items():
    st.write(f"**{k}:** {v}")

# --- Tabela alimentar detalhada ---
st.header("🍽️ Plano Alimentar com Detalhamento Nutricional")
refeicao = st.selectbox("Selecione a refeição para ver os itens detalhados:", list(refeicoes_detalhadas.keys()))
df_refeicao = pd.DataFrame(refeicoes_detalhadas[refeicao])
df_refeicao['Kcal'] = df_refeicao['Kcal'].astype(int)
total_kcal = df_refeicao['Kcal'].sum()
st.dataframe(df_refeicao, use_container_width=True)
st.markdown(f"**Total calórico da refeição:** {total_kcal} kcal")

# --- Suplementação ---
st.header("💊 Suplementação Recomendada")
for item in suplementacao:
    st.write(f"- {item}")

# --- Dicas finais ---
st.header("⚠️ Dicas Finais")
for dica in dicas_finais:
    st.write(f"- {dica}")

# --- Gráfico de progresso ---
st.header("📈 Progresso Real vs Meta - Peso e Força")

semanas = list(range(1, 13))
peso_meta = np.linspace(65, 72, 12)
forca_meta = np.linspace(50, 75, 12)

peso_real = []
forca_real = []

st.subheader("🔍 Digite seus dados reais por semana:")

for i in range(12):
    col1, col2 = st.columns(2)
    with col1:
        peso = st.number_input(f"Semana {i+1} - Peso (kg)", value=float(round(peso_meta[i], 1)), key=f"peso_{i}")
    with col2:
        forca = st.number_input(f"Semana {i+1} - Força (kg)", value=float(round(forca_meta[i], 1)), key=f"forca_{i}")
    peso_real.append(peso)
    forca_real.append(forca)

# Gráfico interativo
fig = go.Figure()
fig.add_trace(go.Scatter(x=semanas, y=peso_meta, name='Meta de Peso', line=dict(dash='dash', color='blue')))
fig.add_trace(go.Scatter(x=semanas, y=forca_meta, name='Meta de Força', line=dict(dash='dash', color='green')))
fig.add_trace(go.Scatter(x=semanas, y=peso_real, name='Peso Real', mode='lines+markers', line=dict(color='blue')))
fig.add_trace(go.Scatter(x=semanas, y=forca_real, name='Força Real', mode='lines+markers', line=dict(color='green')))

fig.update_layout(
    title="📊 Comparativo de Progresso",
    xaxis_title="Semana",
    yaxis_title="Peso / Força (kg)",
    hovermode="x unified"
)

st.plotly_chart(fig, use_container_width=True)
