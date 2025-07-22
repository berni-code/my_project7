import streamlit as st
import pandas as pd
import plotly.express as px
# Load the dataset
car_data = pd.read_csv('vehicles_us.csv')
# Create a histogram of the 'odometer' column
hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
# Create a scatter plot between 'odometer' and 'price'
scatter_button = st.button('Construir gráfico de dispersión')  # crear un botón

build_histogram = st.checkbox('Construir un histograma')
if build_histogram:  # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para la columna odómetro')
    fig2 = px.scatter(car_data, x="odometer", y="price",
                      title="Odometer vs Price")
    # mostrar el gráfico de dispersión
    st.plotly_chart(fig2, use_container_width=True)
if scatter_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    # crear un gráfico de dispersión
    fig2 = px.scatter(car_data, x="odometer", y="price", title
                      "Odometer vs Price")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig2, use_container_width=True)
# Import necessary components from Streamlit
_main = st._main
# Import components from Streamlit's main module
checkbox = _main.checkbox
code = _main.code
columns = _main.columns
tabs = _main.tabs
container = _main.container
dataframe = _main.dataframe
data_editor = _main.data_editor
date_input = _main.date_input
divider = _main.divider
download_button = _main.download_button
expander = _main.expander
