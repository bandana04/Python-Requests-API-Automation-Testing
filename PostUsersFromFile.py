import requests
import json

url = "https://fakestoreapi.com/users"
headers = {
    'Content-Type': 'application/json',
    'Accept': 'plain/text'
}
json_file = open('/home/bandana/Desktop/Automation/SDET QA API Testing/users.json')
json_payload = json.load(json_file)
user = json_payload[0]

response = requests.post( url, headers=headers, json=json_payload)
print(response.status_code)
print(response.text)
if response.status_code == 201:
    print("User created successfully")
else:
    print("User creation failed")

