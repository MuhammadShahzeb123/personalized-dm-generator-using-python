import streamlit as st
from functions import *


prompt_choice = st.radio(
    "Choose a prompt option:",
    options=["Use default prompt", "Write my own prompts"]
)

if prompt_choice == "Use default prompt":
    uploaded_file = st.file_uploader("Upload a CSV file")
    if st.button("Get the DMs!!!"):
        process_csv(uploaded_file)

else:  # User wants to write their own prompt
    # Display prompt input box and other relevant elements
    message = st.text_area("Write your prompt:", value=default_message)
    niche = st.text_input("Niche: ", value=niche)
    clients_offer = st.text_area("Write the Offer you want to pitch the client", value=clients_offer)
    autors = st.text_input("Enter the Copywriter you love | Copy his Style of Writing. ", value=autors)
    st.write("I like Alex Cattoni Writing Style")

    uploaded_file = st.file_uploader("Upload a CSV file")
    if st.button("Get the DMs!!!"):
            if uploaded_file is not None:
                process_csv(uploaded_file)