from functions import *

def main(path):
    batch_size = 10  # Number of rows to process before creating a new CSV file
    file_path = path

    try:
        csv_data = read_csv2(file_path)
        extracted_data = extract_data(csv_data)

        for i in range(0, len(csv_data), batch_size):
            batch_data = extracted_data[i:i + batch_size]

            with open(f'dm{i//batch_size}.csv', 'a', newline='', encoding='utf-8') as output_csv:
                csv_writer = csv.writer(output_csv)

                for data in batch_data:
                    full_name = data['Full Name']
                    public_email = data['Public Email']
                    bio = data['Bio']
                    first_name = full_name.split(" ")[0]
                    clients_offer = "Helping wellness entrepreneurs build their dream lifestyle business generating 30k+ in monthly recurring revenue organically within 90 days without using ads or manipulative sales tactics guarantee results or we work with you until you do."
                    prompt = f"Please craft a personalized direct message for Instagram outreach. Use the following structure and personalize each message based on the provided data: - Start with a greeting. Use the first name from this full name {full_name} of the Instagram user if available; otherwise, start with 'Hi there'. - Reference something from their bio, Here is the bio: {bio} to show that the message is personalized. - Introduce the client's offer in a conversational and indirect manner. - The message should be short and genuine. Avoid formal introductions or conclusions. - Keep the tone friendly and human-like.  Example: Hi {first_name}! I came across your profile and was really impressed by [something from bio]. It got me thinking, have you ever considered {clients_offer}? It could really complement what you're doing. Anyways, just wanted to say keep up the good work. Remember, no formal sign-off is needed. Keep it real and approachable."
                    message = gemeni(prompt)

                    # Append data to the CSV file
                    csv_writer.writerow([full_name, public_email, message])

    except Exception as e:
        print(f"Error reading the CSV file: {e}")

if __name__ == "__main__":
    path = input("Lead List: ")
    main(path)
