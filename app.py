import streamlit as st
from uuid import uuid4
from claude import Text, Vision

# Function to handle vision analysis
def analyze_image(prompt, image_file, session_id):
    vision_analyzer = Vision()
    response = vision_analyzer.run(prompt=prompt, image=image_file, session_id=session_id)
    return response

# Function to handle text generation
def generate_text(prompt):
    text_generator = Text()
    response = text_generator.run(prompt=prompt)
    return response

# Streamlit app
st.title("Claude AI Toolkit")
session_id = str(uuid4())  # Generate a unique session ID for each session

st.sidebar.title("Modes")
app_mode = st.sidebar.selectbox("Choose the mode", ["Text Generation", "Vision Analysis"])

if app_mode == "Text Generation":
    st.header("Text Generation")
    prompt = st.text_input("Enter your prompt", "Write a haiku about robots.")
    if st.button("Generate Text"):
        with st.spinner("Generating text..."):
            response = generate_text(prompt)
        st.subheader("Generated Text")
        st.write(response)

elif app_mode == "Vision Analysis":
    st.header("Vision Analysis")
    prompt = st.text_input("Enter your prompt", "Describe this image.")
    image_file = st.file_uploader("Upload an image or PDF", type=["jpg", "jpeg", "png", "webp", "gif", "pdf"])
    if st.button("Analyze Image"):
        if image_file is not None:
            with st.spinner("Analyzing image..."):
                response = analyze_image(prompt, image_file, session_id)
            st.subheader("Image Analysis")
            st.write(response)
        else:
            st.error("Please upload an image or PDF file.")