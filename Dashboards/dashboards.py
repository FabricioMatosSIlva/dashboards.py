import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

# Carregar dados
df = pd.read_csv("supermarket_sales.csv", sep=";", decimal=",")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

# Criar coluna de mês
df["Month"] = df["Date"].apply(lambda x: str(x.year) + "-" + str(x.month))

# Filtros na barra lateral
st.sidebar.title("Filtros")
month = st.sidebar.selectbox("Selecione o mês", df["Month"].unique())

# Filtrar dados por mês
df_month = df[df["Month"] == month]

# Filtro de filiais
cities = df_month["City"].unique()
selected_cities = st.sidebar.multiselect("Selecione a(s) filial(is)", options=list(cities), default=list(cities))

# Aplicar filtro de cidades
df_filtered = df_month[df_month["City"].isin(selected_cities)]

# Layout dos gráficos
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

# Faturamento por dia
fig_date = px.bar(df_filtered, x="Date", y="Total", color="City", title="Faturamento por dia")
col1.plotly_chart(fig_date, use_container_width=True)

# Faturamento por tipo de produto
fig_prod = px.bar(df_filtered, x="Product line", y="Total", 
                  color="City", title="Faturamento por tipo de produto")
col2.plotly_chart(fig_prod, use_container_width=True)

# Faturamento por filial
city_total = df_filtered.groupby("City")[["Total"]].sum().reset_index()
fig_city = px.bar(city_total, x="City", y="Total", title="Faturamento por filial")
col3.plotly_chart(fig_city, use_container_width=True)

# Faturamento por tipo de pagamento
fig_kind = px.pie(df_filtered, values="Total", names="Payment", title="Faturamento por tipo de pagamento")
col4.plotly_chart(fig_kind, use_container_width=True)

# Avaliação média por filial
city_rating = df_filtered.groupby("City")[["Rating"]].mean().reset_index()
fig_rating = px.bar(city_rating, x="City", y="Rating", title="Avaliação média por filial")
col5.plotly_chart(fig_rating, use_container_width=True)
