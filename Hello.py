#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import streamlit as st

import config
from utils import load_model, infer_uploaded_image, infer_uploaded_video, infer_uploaded_webcam

# Configuración de la página
import streamlit as st

st.set_page_config(
    page_title="Welcome",
    page_icon="👋",
)

st.image('./images/Logo 1.png', width=300)
st.divider()
st.markdown(
    """
**Client Hero** es una aplicación diseñada para empresas que desean mejorar y optimizar su experiencia de cliente (**Customer Experience**). La plataforma ofrece un conjunto de herramientas avanzadas que permiten a las organizaciones entender mejor el comportamiento de sus clientes, analizar interacciones clave y tomar decisiones basadas en datos.

### 🚀 Funcionalidades Clave

### 1. 📊 **Análisis de Retención**
Client Hero ofrece un sistema de análisis detallado sobre el tiempo de retención de los clientes en diferentes zonas de la empresa, permitiendo identificar áreas de mejora y puntos críticos en el servicio.

### 2. 📅 **Calendario Interactivo**
Con nuestro calendario interactivo, los administradores pueden seleccionar cualquier día para analizar el rendimiento de la atención al cliente en ese período específico, obteniendo insights valiosos.

### 3. 🕒 **Retención por Hora**
Visualiza cómo cambia la retención de clientes a lo largo del día. El gráfico de barras muestra los tiempos máximos de retención por hora, desde las 9:00 AM hasta las 6:00 PM. Esto ayuda a identificar las horas pico y mejorar la gestión de los recursos.

### 4. 🧑‍💼 **Gestión de Zonas de Atención**
Client Hero permite segmentar los datos por zonas del centro de atención, proporcionando insights personalizados para cada área, lo que facilita la optimización de los servicios donde sea necesario.

## #💡 ¿Por Qué Elegir Client Hero?

- **Fácil de Usar**: Su interfaz intuitiva permite a cualquier miembro del equipo acceder a datos e insights clave de forma rápida y sencilla.
- **Basado en Datos**: Todas las métricas proporcionadas están basadas en datos reales de las interacciones con los clientes, lo que garantiza un enfoque preciso y accionable.
- **Optimización de Recursos**: Con un análisis detallado de la retención y el comportamiento de los clientes, las empresas pueden ajustar sus estrategias y recursos para mejorar la satisfacción y eficiencia.

"""
)