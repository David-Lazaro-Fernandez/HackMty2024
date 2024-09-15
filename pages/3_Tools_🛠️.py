import streamlit as st
from PIL import Image



# Set page configuration
st.set_page_config(
    page_title="ClientHero",
    page_icon="🚀",
)

st.image('./images/Logo 1.png', width=300)

# Function to resize images
def resize_image(image_path, size=(500, 350)):
    image = Image.open(image_path)
    return image.resize(size)

# Function to navigate to another page
def navigate_to(page):
    st.query_params.update(page=page)
     # Rerun the app to apply the query params

# Check the query parameters to determine which page to display
query_params = st.query_params
page = query_params.get("page", "home")

if page == "home":
    st.subheader(":violet[Our main tools]")
    st.divider()

    # Container for images and descriptions
    col1, col2, col3 = st.columns(3)

    with col1:
        resized_image = resize_image('./images/Video.png')
        st.image(resized_image, use_column_width=True)
        st.write("Choose from several metrics from tagged video or important heatmap zones to view user behavior using OpenVino")
        if st.button("View", key="1"):
            navigate_to("page1")

    with col2:
        resized_image = resize_image('./images/Foto1.jpeg')
        st.image(resized_image, use_column_width=True)
        st.write("Use of GenAI tools to generate insights on calls between customers and vendors using FRIDA, OpenAI and Whisper")
        if st.button("View", key="2"):
            navigate_to("page2")

    with col3:
        resized_image = resize_image('./images/Foto2.png')
        st.image(resized_image, use_column_width=True)
        st.write("Compare video and audio to analyze interaction between both parties using live comparison in between")
        if st.button("View", key="3"):
            navigate_to("page3")

elif page == "page1":
    st.subheader("Upload videos to start analyzing.")
    st.divider()
    uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi", "mkv"])
    
    if uploaded_file is not None:
        st.write("Uploaded file:", uploaded_file.name)
    
    if st.button("Back to Home"):
        navigate_to("home")

elif page == "page2":
    st.subheader("Upload videos to start analyzing.")
    st.divider()
    uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi", "mkv"])
    
    if uploaded_file is not None:
        st.write("Uploaded file:", uploaded_file.name)
    
    if st.button("Back to Home"):
        navigate_to("home")

elif page == "page3":
    st.subheader("Upload videos to start analyzing.")
    st.divider()
    uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi", "mkv"])
    
    if uploaded_file is not None:
        st.write("Uploaded file:", uploaded_file.name)
    
    if st.button("Back to Home"):
        navigate_to("home")