import requests
import json

# Define the URL and JSON payload
url = 'http://localhost:11434/api/generate'
payload = {
    "model": "llama3",
    "prompt": "Why is the sky blue?"
}
headers = {
    "Content-Type": "application/json"
}

# Convert payload to JSON string
json_payload = json.dumps(payload)

# Send POST request
response = requests.post(url, headers=headers, data=json_payload)

# Check if request was successful (status code 200)
if response.status_code == 200:
    # Extract 'response' field from JSON response
    response_data = response.json()
    response_text = response_data.get('response', '')

    # Print or save the 'response' text to a file
    print(response_text)

    # Save response text to a file
    with open('response.txt', 'w', encoding='utf-8') as f:
        f.write(response_text)
else:
    print(f"Error: {response.status_code} - {response.text}")
