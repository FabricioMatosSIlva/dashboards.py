import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# Carregar dados
df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")
df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))

# Inicializar Session State
if "selected_month" not in st.session_state:
    st.session_state.selected_month = df["Month"].unique()[0]
if "selected_cities" not in st.session_state:
    st.session_state.selected_cities = []

# Sidebar - filtro de mês
month = st.sidebar.selectbox("Selecione o mês", df["Month"].unique(), key="selected_month")

# Filtrar dados por mês
df_month = df[df["Month"] == month]
cities = df_month["City"].unique()

# Resetar seleção de cidades se o mês mudou
if month != st.session_state.selected_month:
    st.session_state.selected_cities = []
    st.session_state.selected_month = month

# Sidebar - filtro de cidades (sem seleção inicial)
selected_cities = st.sidebar.multiselect(
    "Selecione a(s) filial(is)",
    options=list(cities),
    default=st.session_state.selected_cities,
    key="selected_cities"
)

# Aplicar filtro
if not selected_cities:
    df_filtered = df_month
else:
    df_filtered = df_month[df_month["City"].isin(selected_cities)]

# Layout
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_date = px.bar(df_filtered, x="Date", y="Total", color="City", title="Faturamento por dia")
col1.plotly_chart(fig_date, use_container_width=True)

fig_prod = px.bar(df_filtered, x="Product line", y="Total", 
                  color="City", title="Faturamento por tipo de produto")
col2.plotly_chart(fig_prod, use_container_width=True)

city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()
fig_city = px.bar(city_total, x="City", y="Total", title="Faturamento por filial")
col3.plotly_chart(fig_city, use_container_width=True)

fig_kind = px.pie(df_filtered, values="Total", names="Payment", title="Faturamento por tipo de pagamento")
col4.plotly_chart(fig_kind, use_container_width=True)

city_rating = df_filtered.groupby("City")[["Rating"]].mean().reset_index()
fig_rating = px.bar(city_rating, x="City", y="Rating", title="Avaliação média por filial")
col5.plotly_chart(fig_rating, use_container_width=True)
