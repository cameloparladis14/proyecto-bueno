import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header('Análisis de anuncios de venta de coches')

build_histogram = st.checkbox('Construir un histograma')

if build_histogram:

    st.write('Construcción de un histograma para la columna odómetro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_scatter:

    st.write('Construcción de un gráfico de dispersión: Precio vs Odómetro')
    fig2 = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig2, use_container_width=True)
