
# Instagram Outreach Message Generator

This tool automates the creation of personalized direct messages for Instagram outreach, leveraging the power of AI to craft engaging and effective messages.

## Features

- Personalized messages: Generates unique messages for each recipient based on their name, bio, and other relevant information.
- AI-powered creativity: Utilizes the Gemini Pro language model to craft compelling and human-like messages that resonate with potential leads.
- Conversational tone: Avoids overly salesy or promotional language, promoting natural and engaging conversations.
- Efficient outreach: Streamlines the outreach process by generating a CSV file of personalized messages, ready to be sent via Instagram.
- Customizable prompts: Allows for tailoring of message structure and tone to align with specific brand voice and messaging goals.


## Getting Started

Install dependencies:
```Bash
pip install -r requirements.txt
```

Obtain a Google AI API key:
Visit https://makersuite.google.com/app/apikey to get a free API key.

Replace placeholder in functions.py:
Update the YOU API KEY placeholder with your actual API key.


## Usage

Run the script:
```Bash
python main.py
```

Provide lead list path:
When prompted, enter the path to your CSV file containing leads' information (names, emails, bios).

Generated messages:
The tool will generate personalized messages for each lead and save them to a dm.csv file.

## CSV File Format

The input CSV file should have the following headers:

- Full name
- Public email
- Biography

## Additional Notes

Custom prompts: Modify the prompt in the main.py file to adjust message structure and tone.
Ethical use: Use this tool responsibly and ethically, respecting the privacy of individuals and avoiding any form of spam or harassment.

I hope this README helps you get started with the tool!