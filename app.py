import streamlit as st
import plotly.express as px

st.title("Mi tercera publicación")
st.header("Introducción")
st.write("Esta es la primera que me sale algo")

st.write("Este es un gráfico de barras simple.")
fig = px.bar(
    x=["A", "B", "C"],
    y=[1, 2, 3],
    title="Gráfico de barras",
)
st.plotly_chart(fig)