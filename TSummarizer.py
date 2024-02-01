import streamlit as st
import speech_recognition as sr
from summarizer import Summarizer

def speech_to_text():
    
    recognizer = sr.Recognizer()

    
    with sr.Microphone() as source:
        st.info("Listening... Speak into your microphone.")

    
        recognizer.adjust_for_ambient_noise(source)

        try:
           
            audio = recognizer.listen(source)
            text = recognizer.recognize_sphinx(audio)
            st.success(f"You said: {text}")

           
            summarizer = Summarizer()
            summary = summarizer(text)
            st.info("Summary:")
            st.write(summary)

        except sr.UnknownValueError:
            st.warning("Could not understand audio. Please try again.")
        except sr.RequestError as e:
            st.error(f"Error during speech recognition: {e}")

def main():
    st.title("Voice Prescription")
    st.markdown("### Welcome to the Voice Prescription App")

    st.write("Click the button below and speak into your microphone.")

    if st.button("Give Voice Prescription"):
        speech_to_text()

    # Additional information and credits
    st.sidebar.markdown("#### About")
    st.sidebar.info(
        "This app demonstrates speech-to-text functionality using pocketsphinx."
    )
    st.sidebar.markdown("#### Credits")
    st.sidebar.info(
        "Built with Streamlit by Your Name\n"
        "Icons made by Freepik from www.flaticon.com"
    )

if __name__ == "__main__":
    main()
