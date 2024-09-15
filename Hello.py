#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pathlib import Path
import streamlit as st

import config
from utils import load_model, infer_uploaded_image, infer_uploaded_video, infer_uploaded_webcam

# Configuración de la página
import streamlit as st

st.set_page_config(
    page_title="ClientHero",
    page_icon="🚀",
)

st.image('./images/Logo 1.png', width=300)

st.title(':violet[Welcome to ClientHero 🚀]')

st.write('Client Hero is an application designed for companies that want to improve and optimize their customer experience. The platform offers a set of advanced tools that enable organizations to better understand their customer behavior, analyze key interactions, and make data-driven decisions.')

col1, col2 = st.columns(2)
col1.subheader(":violet[Video Analysis]")
col1.divider()
col1.write("- Use of computer vision tools to monitor sentiment analysis and attention levels of students")
col1.write("- Fetch data on a dynamic dashboard to view different metrics")
col1.write("- Mantain privacy of students using only tags and not saving biometric data")
col1.write("- Generate reports and reccomendations in relation to the results from lessons")
col1.write("- Identify in which section of the class the students where most engaged, and what was the content being displayed")

col2.subheader(":violet[Voice interaction analysis]")
col2.divider()
col2.write("- Use of generative artificial intelligence to create content for your lessons")
col2.write("- Direct voice interaction and conversation with an assistant to generate the desired content")
col2.write("- Text integration and audios to increase dynamic interaction")
col2.write("- Selection between creating a study plan or lesson content by filling a form")
col2.write("- Visualization of study plan on a calendar depending on the time and content of the lesson")

st.divider()
st.subheader(":violet[We combine the use of several tools to make your customer and vendor analysis easier]")

col3, col4 = st.columns(2)
col3.subheader("📌 Computer Vision")
col3.write("1. OpenCV")
col3.write("2. Example")


col4.subheader("📌 Natural Language Processing")
col4.write("1. gpt-3.5 turbo")
col4.write("2. Example")

col5, col6 = st.columns(2)
col5.subheader("📌 Generative AI")
col5.write("1. gpt4-o")
col5.write("2. Example")

col6.subheader("📌 Data Visualization")
col6.write("1. Plotly")
col6.write("2. Example")

st.divider()

st.subheader(":violet[Main Features]")

st.markdown(
    """
### 1. 📊 **Retention Analysis**
Client Hero offers a detailed analysis system on customer retention time in different areas of the company, allowing the identification of areas for improvement and critical points in the service.

### 2. 📅 **Interactive Calendar**
With our interactive calendar, administrators can select any day to analyze customer service performance in that specific period, earning valuable insights.

### 3. 🕒 **Hourly Retention**
Visualize how customer retention changes throughout the day. The bar graph shows the maximum retention times per hour, from 9:00 AM to 6:00 PM. This helps identify peak hours and improve resource management.

### 4. 🗾 **Management of Service Zones**
Client Hero allows data to be segmented by focus area, providing custom insights for each area, making it easy to optimize services where necessary.

"""
)
st.divider()

st.subheader(":violet[Why Choose ClientHero?]")
st.markdown(
    """
- **Easy to Use**: Its intuitive interface allows any team member to access key data and insights quickly and easily.
- **Data Based**: All metrics provided are based on actual data from customer interactions, ensuring an accurate and actionable approach.
- **Resource Optimization**: With a detailed analysis of customer retention and behavior, companies can adjust their strategies and resources to improve satisfaction and efficiency.
    """
)

st.subheader(":violet[Get Started]")
st.page_link("pages/2_Instructions_🔧.py", label="See Instructions 🔧")

st.divider()

st.markdown("<span style='margin-left: 250px; font-weight: 20px; font-size: 15px'>Thanks for using ClientHero 🚀</span>", unsafe_allow_html=True)
