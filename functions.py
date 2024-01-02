import unicodecsv
import google.generativeai as genai
import csv


def read_csv(file_path):
    with open(file_path, 'rb') as csvfile:
        csv_reader = unicodecsv.DictReader(csvfile)
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
    genai.configure(api_key="YOU API KEY") # get the API key from https://makersuite.google.com/app/apikey . It is FREE

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