import unicodecsv
import google.generativeai as genai
import csv


default_message = "My name is Reagan Stock. Please craft a personalized direct message for Instagram outreach. Use the following structure and personalize each message based on the provided data: - Start with a greeting. Use the first name from this full name , it is given at the end, of the Instagram user if available; otherwise, start with 'Hi there'. - Reference something from their bio, Here is the bio: Bio is given at the End to show that the message is personalized. - Introduce the client's offer in a conversational and indirect manner. - The message should be short and genuine. Avoid formal introductions or conclusions. - Keep the tone friendly and human-like.  Example: Hi first_name! I came across your profile and was really impressed by [something from bio]. It got me thinking, have you ever considered `clients_offer` (Client offer is also given at the end)? It could really complement what you're doing. Anyways, just wanted to say keep up the good work. Remember, no formal sign-off is needed. Keep it real and approachable."
clients_offer = "Helping wellness entrepreneurs build their dream lifestyle business generating 30k+ in monthly recurring revenue organically within 90 days without using ads or manipulative sales tactics guarantee results or we work with you until you do."
niche = "Enterprenuer Wellness"
autors = "Alex Cattoni"

def read_csv2(file_path):
    with open(file_path, 'rb') as csvfile:
        csv_reader = unicodecsv.DictReader(csvfile)
        return list(csv_reader)

def read_csv(file_object):
    csv_reader = unicodecsv.DictReader(file_object)
    return list(csv_reader)

def extract_data(csv_data):
    extracted_data = []

    for row in csv_data:
        full_name = row.get('Full name', '')
        public_email = row.get('Public email', '')
        bio = row.get('Biography', '')

        extracted_data.append({
            'Full Name': full_name,
            'Public Email': public_email,
            'Bio': bio,
        })

    return extracted_data

def gemeni(prompt: str) -> str:
    genai.configure(api_key="YOU_API_KEY") # get the API key from https://makersuite.google.com/app/apikey . It is FREE YOU_API_KEY

    model = genai.GenerativeModel(
        model_name="gemini-pro",
        generation_config={
            "temperature": 0.9,
            "top_p": 1,
            "top_k": 1,
            "max_output_tokens": 2048,
        },
        safety_settings=[
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
        ],
    )

    response = model.generate_content(prompt)
    return response.text

def process_csv(data) -> str:
    if data is not None:
        batch_size = 1000
        data = read_csv(data)
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
                    prompt = f"{full_name} is the person I want to reach out to. His Instagram bio is {bio}. This the offer I want to pitch to the client {clients_offer} but my main focus will be to set an appointment with them regarding this offer. The Prospect's Niche is {niche}. I want you to use the Copywriting style of {autors} becuase I strongly admire them and they are awesome"
                    message = gemeni(f"{default_message} {prompt}")

                    csv_writer.writerow([full_name, public_email, message])

            i += 1  # Increment batch number for the next file    