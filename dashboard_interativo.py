import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objs as go

# --- Dados básicos ---
dados_basicos = {
    "Altura": "1,73 m",
    "Peso": "65 kg",
    "Objetivo": "Ganho de Massa Muscular",
    "Treino": "Noturno (~20h)",
    "Suplementação": "Creatina 6g/dia dividida + Hipercalórico Dark Mass 1 dose pós-treino",
    "Restrições": "Livre de glúten, sem whey, sem restrição à lactose"
}

# --- Plano alimentar ---
refeicoes = {
    "Café da Manhã": [
        "2 ovos mexidos com azeite + 2 fatias de pão sem gluten (milho/arroz) + banana com canela + 3g creatina + suco natural",
        "Mingau de aveia sem gluten com bebida vegetal + 1 colher de pasta de amendoim + 1 fruta (maca ou pera)",
        "Cuscuz de milho com queijo coalho + 1 copo de leite integral + mamao picado"
    ],
    "Lanche da Manhã": [
        "Shake de proteina vegetal (ervilha ou arroz) + 1 colher de pasta de amendoim + 200 ml de bebida vegetal + aveia sem gluten",
        "1 iogurte natural integral + mix de castanhas + 1 fruta (laranja ou tangerina)",
        "Tapioca com queijo minas + 1 copo de suco de fruta natural (limao ou abacaxi)"
    ],
    "Almoço": [
        "120g de peito de frango grelhado + arroz integral + feijao + salada com azeite e sementes (linhaca/chia)",
        "Carne bovina magra (patinho ou coxao mole) + batata doce + brocolis refogado + salada verde",
        "Peixe assado + quinoa + legumes no vapor + cuscuz de milho (porcao pequena)"
    ],
    "Pré-treino": [
        "1 banana + 1 colher de mel + 1 colher de pasta de amendoim",
        "Shake de proteina vegetal + 1 fruta (maca ou pera)",
        "Cuscuz com ovos mexidos + 1 copo de suco natural"
    ],
    "Pós-treino": [
        "1 dose de Dark Mass + 3g creatina + 1 banana ou cacau puro",
        "Shake de proteina vegetal + 1 fruta + 3g creatina",
        "1 tapioca com pasta de amendoim + 1 copo de leite integral + 3g creatina"
    ],
    "Jantar": [
        "2 ovos inteiros + 2 claras + quinoa + abobora refogada + azeite",
        "Peito de frango desfiado + arroz integral + salada de couve + tomate",
        "Omelete com legumes variados + cuscuz + 1 copo de bebida vegetal"
    ],
    "Ceia (Opcional)": [
        "Bebida vegetal + 2 colheres de farinha de amendoim + cacau em po",
        "Iogurte natural integral + castanhas",
        "1 copo de leite integral + 2 fatias de queijo minas"
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
    "Consulte nutricionista para ajustes personalizados"
]

# --- Montar DataFrame do plano alimentar para filtro ---
data = {
    "Refeição": [],
    "Opção": [],
    "Descrição": []
}

for refeicao, opcoes in refeicoes.items():
    for i, opcao in enumerate(opcoes, 1):
        data["Refeição"].append(refeicao)
        data["Opção"].append(f"Opção {i}")
        data["Descrição"].append(opcao)

df = pd.DataFrame(data)

# --- Streamlit app ---
st.title("Plano Alimentar Completo para Ganho de Massa Muscular - Eduardo Holanda")

st.header("📋 Dados Básicos")
for k, v in dados_basicos.items():
    st.write(f"**{k}:** {v}")

st.header("🍽️ Plano Alimentar Diário")
refeicao_selecionada = st.selectbox("Selecione a Refeição para ver as opções:", options=df["Refeição"].unique())

filtro = st.text_input("Filtro por palavra-chave (ex: cuscuz, fruta, proteina)")

df_filtrado = df[df["Refeição"] == refeicao_selecionada]
if filtro:
    filtro = filtro.lower()
    df_filtrado = df_filtrado[df_filtrado["Descrição"].str.lower().str.contains(filtro)]

for idx, row in df_filtrado.iterrows():
    st.markdown(f"**{row['Opção']}**: {row['Descrição']}")

st.header("💊 Suplementação Recomendada")
for item in suplementacao:
    st.write(f"- {item}")

st.header("⚠️ Dicas Finais")
for dica in dicas_finais:
    st.write(f"- {dica}")

# --- Gráficos interativos de progresso ---
st.header("📈 Progresso Interativo")

import plotly.graph_objects as go
import numpy as np

# Dados simulados
semanas = list(range(1, 13))
peso = np.linspace(65, 72, 12)
forca = np.linspace(50, 75, 12)

fig = go.Figure()

fig.add_trace(go.Scatter(x=semanas, y=peso, mode='lines+markers', name='Peso corporal (kg)', line=dict(color='blue')))
fig.add_trace(go.Scatter(x=semanas, y=forca, mode='lines+markers', name='Força (supino kg)', line=dict(color='green')))

fig.update_layout(
    title='Progresso estimado em 12 semanas',
    xaxis_title='Semanas',
    yaxis_title='Valor',
    hovermode='x unified'
)

st.plotly_chart(fig, use_container_width=True)

# --- Contadores diários simulados ---
st.header("📊 Contadores Diários (Simulados)")

calorias_meta = 2800
proteina_meta = 135

calorias_hoje = st.slider("Calorias consumidas hoje (kcal):", 0, 4000, 2500)
proteina_hoje = st.slider("Proteína consumida hoje (g):", 0, 200, 110)

col1, col2 = st.columns(2)
with col1:
    st.metric("Calorias (meta)", f"{calorias_hoje} / {calorias_meta} kcal",
              delta=f"{calorias_hoje - calorias_meta} kcal",
              delta_color="normal" if calorias_hoje >= calorias_meta else "inverse")

with col2:
    st.metric("Proteína (meta)", f"{proteina_hoje} / {proteina_meta} g",
              delta=f"{proteina_hoje - proteina_meta} g",
              delta_color="normal" if proteina_hoje >= proteina_meta else "inverse")

# --- Alertas personalizados ---
st.header("⚠️ Alertas e Recomendações")

if calorias_hoje < calorias_meta:
    st.warning("⚠️ Você está consumindo menos calorias que a meta diária. Aumente a ingestão para otimizar o ganho de massa.")
else:
    st.success("🎉 Calorias dentro da meta diária.")

if proteina_hoje < proteina_meta:
    st.warning("⚠️ Proteína abaixo da meta. Garanta o consumo adequado para manter a hipertrofia.")
else:
    st.success("🎉 Proteína adequada para o objetivo.")

st.info("Consulte seu nutricionista regularmente para ajustes personalizados.")
