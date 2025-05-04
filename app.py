import streamlit as st
import pandas as pd
import plotly.express as px

# Encabezado
st.header("Panel de anuncios de vehículos - Exploración de datos")

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

# Renombrar las columnas "odometer" a "kilometraje" y "price" a "precio"
car_data = car_data.rename(columns={"odometer": "kilometraje", "price": "precio"})

# Mostrar la tabla de datos (DataFrame)
st.subheader("Tabla de datos")
st.dataframe(car_data)

# Filtros interactivos (Selección múltiple de tipo de vehículo o marca)
st.subheader("Filtrar datos")

# Selección múltiple de tipo de vehículo
tipos_vehiculo = st.multiselect("Selecciona los tipos de vehículo:", car_data['type'].unique())

# Selección múltiple de marca
marcas_vehiculo = st.multiselect("Selecciona las marcas:", car_data['model'].dropna().unique())

# Filtrar los datos por los tipos de vehículo y marcas seleccionados
filtered_data = car_data[car_data['type'].isin(tipos_vehiculo)]
filtered_data = filtered_data[filtered_data['model'].str.contains('|'.join(marcas_vehiculo), case=False, na=False)]

# Histograma filtrado por "kilometraje"
show_histogram = st.checkbox('Mostrar histograma del kilometraje')
if show_histogram:
    st.write(f"Histograma del kilometraje (km) para {', '.join(tipos_vehiculo)} - {', '.join(marcas_vehiculo)}")
    fig_hist = px.histogram(filtered_data, x="kilometraje", color="type", 
                            title=f"Histograma del kilometraje ({', '.join(tipos_vehiculo)} - {', '.join(marcas_vehiculo)})",
                            color_discrete_sequence=px.colors.qualitative.Set1)  # Más colores
    st.plotly_chart(fig_hist, use_container_width=True)

# Gráfico de dispersión filtrado por "precio" vs "kilometraje"
show_scatter = st.checkbox('Mostrar gráfico de dispersión precio vs kilometraje')
if show_scatter:
    st.write(f"Gráfico de dispersión: precio vs kilometraje para {', '.join(tipos_vehiculo)} - {', '.join(marcas_vehiculo)}")
    fig_scatter = px.scatter(filtered_data, x="kilometraje", y="precio", color="type", 
                             title=f"Dispersión precio vs kilometraje ({', '.join(tipos_vehiculo)} - {', '.join(marcas_vehiculo)})",
                             color_discrete_sequence=px.colors.qualitative.Set1)  # Más colores
    st.plotly_chart(fig_scatter, use_container_width=True)

# Gráfico de tipo de vehículo vs marca con un checkbox para activar/desactivar
show_vehicle_brand = st.checkbox('Mostrar gráfico de tipo de vehículo vs marca')
if show_vehicle_brand:
    st.write(f"Gráfico de tipo de vehículo vs marca para {', '.join(tipos_vehiculo)} - {', '.join(marcas_vehiculo)}")
    fig_vehicle_brand = px.bar(filtered_data, x="model", color="type", 
                               title=f"Tipo de vehículo vs Marca ({', '.join(tipos_vehiculo)} - {', '.join(marcas_vehiculo)})",
                               color_discrete_sequence=px.colors.qualitative.Set1)  # Más colores
    st.plotly_chart(fig_vehicle_brand, use_container_width=True)