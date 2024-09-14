import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

# Función para generar datos simulados
def generate_data_for_day(selected_date):
    hours = list(range(9, 19))  # De 9:00 a 18:00
    max_retention_time = np.random.randint(10, 60, size=len(hours))  # Simular tiempos de retención entre 10 y 60 minutos
    return pd.DataFrame({
        'Hora': [f"{hour}:00" for hour in hours],
        'Tiempo Máximo de Retención (min)': max_retention_time
    })

# Página de Insights
def insights_page():
    st.title("📊 Insights de Retención en Zona A")
    
    # Seleccionar fecha
    st.write("Selecciona un día en el calendario para ver los datos de retención de clientes en la Zona A.")
    selected_date = st.date_input("Selecciona una fecha", value=datetime.today())
    
    # Generar los datos para el día seleccionado
    st.write(f"Datos de retención para la fecha: {selected_date.strftime('%Y-%m-%d')}")
    data = generate_data_for_day(selected_date)
    
    # Mostrar gráfico de barras
    st.write("Gráfico de retención de clientes por hora del día:")
    
    fig, ax = plt.subplots()
    ax.bar(data['Hora'], data['Tiempo Máximo de Retención (min)'], color='skyblue')
    ax.set_xlabel('Hora del Día')
    ax.set_ylabel('Tiempo Máximo de Retención (minutos)')
    ax.set_title('Tiempo Máximo de Retención de Clientes en Zona A')
    
    st.pyplot(fig)

# Ejecutar la página de insights
insights_page()
