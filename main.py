import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

import requests

api_key = os.getenv("LMNT_API_KEY")
api_url = "https://api.lmnt.com/v1/ai/speech"
input_text = "THIS IS WORKING!"
querystring = {"X-API-Key":api_key,"text":input_text,"voice":"480dd7fe-d9f2-45ef-bece-df09f5e2f5fa"}

response = requests.request("GET", api_url, params=querystring)

# Check if the request was successful
if response.status_code == 200:
    # Save the audio content to a file
    with open("output_audio.mp3", "wb") as audio_file:
        audio_file.write(response.content)
    print("Audio saved as output_audio.mp3")
else:
    print(f"Failed to synthesize speech. Status code: {response.status_code}")
    print("Response:", response.text)







