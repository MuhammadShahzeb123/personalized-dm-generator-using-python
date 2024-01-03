# from functions import *
# import streamlit as st

# st.title("Process CSVs Easily")
# st.header("The Niche and Other Variables will be added Automatically.")
# message = st.text_area("Write something that Gemini can edit. You don't need to write the full email yourself. Also, just tell the Niche of your Prospects to Gemini down the Variable. You can also put the Prompt here.")

# prompt = f"Please craft a personalized direct message for Instagram outreach. Use the following structure and personalize each message based on the provided data: - Start with a greeting. Use the first name from this full name {full_name} of the Instagram user if available; otherwise, start with 'Hi there'. - Reference something from their bio, Here is the bio: {bio} to show that the message is personalized. - Introduce the client's offer in a conversational and indirect manner. - The message should be short and genuine. Avoid formal introductions or conclusions. - Keep the tone friendly and human-like.  Example: Hi {first_name}! I came across your profile and was really impressed by [something from bio]. It got me thinking, have you ever considered {clients_offer}? It could really complement what you're doing. Anyways, just wanted to say keep up the good work. Remember, no formal sign-off is needed. Keep it real and approachable."

# niche = st.text_input("Niche: ")
# clients_offer = st.text_area("Write the Offer you want to pitch the client")
# autors = st.text_input("Enter the Copywriter you love | Copy his Style of Writing. ")
# st.write("I like Alex Cattoni Writing Style")

# uploaded_file = st.file_uploader("Upload a CSV file")

# if st.button("Fire the Emails!!!"):
#     if uploaded_file is not None:
#         batch_size = 10  # Number of rows to process before creating a new CSV file
#         try:
#             data = read_csv(uploaded_file)
#             extracted_data = extract_data(data)

#             for i in range(0, len(data), batch_size):
#                 batch_data = extracted_data[i:i + batch_size]

#                 with open(f'dm{i//batch_size}.csv', 'a', newline='', encoding='utf-8') as output_csv:
#                     csv_writer = csv.writer(output_csv)

#                     for data in batch_data:
#                         full_name = data['Full Name']
#                         public_email = data['Public Email']
#                         bio = data['Bio']
#                         first_name = full_name.split(" ")[0]
#                         prompt = f"{full_name} is the person I want to reach out to. His Instagram bio is {bio}. This the offer I want to pitch to the client {clients_offer} but my main focus will be to set an appointment with them regarding this offer. The Prospect's Niche is {niche}. I want you to use the Copywriting style of {autors} becuase I strongly admire them and they are awesome"
#                         message = gemeni(f"{message} {prompt}")

#                         csv_writer.writerow([full_name, public_email, message])

#         except Exception as e:
#             print(f"Error reading the CSV file: {e}")

import streamlit as st
from functions import *


default_message = "My name is Reagan Stock. Please craft a personalized direct message for Instagram outreach. Use the following structure and personalize each message based on the provided data: - Start with a greeting. Use the first name from this full name , it is given at the end, of the Instagram user if available; otherwise, start with 'Hi there'. - Reference something from their bio, Here is the bio: Bio is given at the End to show that the message is personalized. - Introduce the client's offer in a conversational and indirect manner. - The message should be short and genuine. Avoid formal introductions or conclusions. - Keep the tone friendly and human-like.  Example: Hi first_name! I came across your profile and was really impressed by [something from bio]. It got me thinking, have you ever considered `clients_offer` (Client offer is also given at the end)? It could really complement what you're doing. Anyways, just wanted to say keep up the good work. Remember, no formal sign-off is needed. Keep it real and approachable."
clients_offer = "Helping wellness entrepreneurs build their dream lifestyle business generating 30k+ in monthly recurring revenue organically within 90 days without using ads or manipulative sales tactics guarantee results or we work with you until you do."
niche = "Enterprenuer Wellness"
autors = "Alex Cattoni"

prompt_choice = st.radio(
    "Choose a prompt option:",
    options=["Use default prompt", "Write my own prompts"]
)

if prompt_choice == "Use default prompt":
    uploaded_file = st.file_uploader("Upload a CSV file")
    if st.button("Get the DMs!!!"):
        if uploaded_file is not None:
            batch_size = 10
            data = read_csv(uploaded_file)
            extracted_data = extract_data(data)

            i = 0  # Track the batch number
            for batch_data in (extracted_data[i:i + batch_size] for i in range(0, len(extracted_data), batch_size)):
                output_filename = f'dm{i}.csv'
                with open(output_filename, 'w', newline='', encoding='utf-8') as output_csv:
                    csv_writer = csv.writer(output_csv)

                    for row in batch_data:
                        full_name = row['Full Name']
                        public_email = row['Public Email']
                        bio = row['Bio']
                        first_name = full_name.split(" ")[0]
                        prompt = f"{full_name} is the person I want to reach out to. His Instagram bio is {bio}. This the offer I want to pitch to the client {clients_offer} but my main focus will be to set an appointment with them regarding this offer. The Prospect's Niche is {niche}. I want you to use the Copywriting style of {autors} becuase I strongly admire them and they are awesome"
                        message = gemeni(f"{default_message} {prompt}")

                        csv_writer.writerow([full_name, public_email, message])

                i += 1  # Increment batch number for the next file

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
                batch_size = 10
                data = read_csv(uploaded_file)
                extracted_data = extract_data(data)

                i = 0  # Track the batch number
                for batch_data in (extracted_data[i:i + batch_size] for i in range(0, len(extracted_data), batch_size)):
                    output_filename = f'dm{i}.csv'
                    with open(output_filename, 'w', newline='', encoding='utf-8') as output_csv:
                        csv_writer = csv.writer(output_csv)

                        for row in batch_data:
                            full_name = row['Full Name']
                            public_email = row['Public Email']
                            bio = row['Bio']
                            first_name = full_name.split(" ")[0]
                            prompt = f"{full_name} is the person I want to reach out to. His Instagram bio is {bio}. This the offer I want to pitch to the client {clients_offer} but my main focus will be to set an appointment with them regarding this offer. The Prospect's Niche is {niche}. I want you to use the Copywriting style of {autors} becuase I strongly admire them and they are awesome"
                            message = gemeni(f"{default_message} {prompt}")

                            csv_writer.writerow([full_name, public_email, message])

                    i += 1  # Increment batch number for the next file