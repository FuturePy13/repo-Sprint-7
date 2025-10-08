import pandas as pd
import plotly.express as px
import streamlit as st
     
car_data = pd.read_csv('vehicles_us.csv') # leer los datos
hist_button = st.button('Construir histograma') # crear un botón
     
if hist_button: # al hacer clic en el botón
         # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
            # crear un histograma
    fig_hist = px.histogram(car_data, x="odometer")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_hist, use_container_width=True)

scatt_button = st.button('Construir diagrama de dispersion') # crear un botón
     
if scatt_button: # al hacer clic en el botón
         # escribir un mensaje
    st.write('Creación de un diagrama de dispersion para el conjunto de datos de anuncios de venta de coches')
            
            # crear un diagrama de dispersion
    fig_scatt = px.scatter(car_data, x="odometer", y="price")
        
            # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_scatt, use_container_width=True)