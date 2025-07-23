import io
import pandas as pd
import plotly.express as px
import streamlit as st

st.title('Análisis de Datos de Vehículos Usados')

# Cargar datos
# asegúrate de que el archivo esté en el mismo directorio
car_data = pd.read_csv(vehicles_us.csv')
# Botón para construir histograma
if st.button('Construir histograma'):
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de vehículos')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Casilla de verificación adicional
if st.checkbox('Mostrar histograma alternativo'):
    st.write('Construyendo un histograma alternativo para la columna odómetro')
    fig2 = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig2, use_container_width=True)
# Casilla de verificación para mostrar datos
if st.checkbox('Mostrar datos del conjunto de vehículos usados'):
    st.write('Datos del conjunto de vehículos usados:')
    st.dataframe(car_data)
# Casilla de verificación para mostrar estadísticas descriptivas
if st.checkbox('Mostrar estadísticas descriptivas'):
    st.write('Estadísticas descriptivas del conjunto de datos:')
    st.dataframe(car_data.describe())
# Casilla de verificación para mostrar información del DataFrame
if st.checkbox('Mostrar información del DataFrame'):
    st.write('Información del DataFrame:')
    buffer = io.StringIO()
    car_data.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)
# Casilla de verificación para mostrar tipos de datos
if st.checkbox('Mostrar tipos de datos del DataFrame'):
    st.write('Tipos de datos del DataFrame:')
    st.dataframe(car_data.dtypes)
# Casilla de verificación para mostrar valores únicos
if st.checkbox('Mostrar valores únicos por columna'):
    st.write('Valores únicos por columna:')
    unique_values = {col: car_data[col].nunique() for col in car_data.columns}
    st.json(unique_values)
# Casilla de verificación para mostrar valores nulos
if st.checkbox('Mostrar valores nulos por columna'):
    st.write('Valores nulos por columna:')
    null_values = car_data.isnull().sum()
    st.json(null_values[null_values > 0].to_dict())
# Casilla de verificación para mostrar histogramas de columnas numéricas
if st.checkbox('Mostrar histogramas de columnas numéricas'):
    st.write('Histogramas de columnas numéricas:')
    numeric_cols = car_data.select_dtypes(include=['number']).columns
    for col in numeric_cols:
        fig = px.histogram(car_data, x=col)
        st.plotly_chart(fig, use_container_width=True)
# Casilla de verificación para mostrar gráficos de dispersión
if st.checkbox('Mostrar gráficos de dispersión entre columnas numéricas'):
    st.write('Gráficos de dispersión entre columnas numéricas:')
    numeric_cols = car_data.select_dtypes(include=['number']).columns
    if len(numeric_cols) >= 2:
        for i in range(len(numeric_cols)):
            for j in range(i + 1, len(numeric_cols)):
                fig = px.scatter(
                    car_data, x=numeric_cols[i], y=numeric_cols[j])
                st.plotly_chart(fig, use_container_width=True)
    else:
        st.write(
            'No hay suficientes columnas numéricas para mostrar gráficos de dispersión.')
