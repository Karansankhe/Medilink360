from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

load_dotenv()  
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, image[0], prompt])
    return response.text


def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

def get_emergency_information_india():
    emergency_info_india = """
    In case of emergency in India, please follow these general guidelines:

    1. **Call for Help:** Dial emergency services immediately. In India, the emergency number is **112** for all emergency services.
    2. **Stay Calm:** Try to remain as calm as possible.
    3. **Provide Information:** Share your location, nature of the emergency, and any relevant details. Mention the type of help you need.
    4. **Basic First Aid:** Administer basic first aid if you are trained to do so. If unsure, wait for professional help.
    5. **Do Not Panic:** Panic can worsen the situation; stay composed and follow instructions.

    Remember, this information is general in nature. Seek professional medical help for specific advice.
    """
    return emergency_info_india


st.set_page_config(page_title="personal nutritionist")

st.header("Gemini Health App")
input_prompt = """
You are an expert in nutritionist where you need to see the food items from the image
               and calculate the total calories, also provide the details of every food items with calories intake
               is below format

               1. Item 1 - no of calories
               2. Item 2 - no of calories
               ----
               ----
"""

input_text = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Tell me the total calories")


if submit:
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input_text)
    st.subheader("The Response is")
    st.write(response)

st.sidebar.title("Emergency Information (India)")
st.sidebar.write(get_emergency_information_india())


st.header("Educational Videos")

if st.button("Nutrition Tips"):
  
    nutrition_video_url = "https://www.youtube.com/watch?v=example_nutrition_video"
    st.subheader("Nutrition Tips")
    st.video(nutrition_video_url)

if st.button("Emergency First Aid"):
   
    first_aid_video_url = "https://www.youtube.com/watch?v=example_first_aid_video"
    st.subheader("Emergency First Aid")
    st.video(first_aid_video_url)
