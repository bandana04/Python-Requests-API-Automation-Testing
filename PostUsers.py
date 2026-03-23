import requests

url = "https://fakestoreapi.com/users"
headers = {
    'Content-Type': 'application/json',
    'Accept': 'plain/text'
}
payload_body = {
  "id": 1,
  "username": "Bandana Tigela Limbu",
  "email": "bandanatigela04@gmail.com",
  "password": "bandana123"
}
response = requests.request("POST", url, headers=headers, json = payload_body)
print(response.status_code)
if response.status_code == 201:
    print("User created successfully")
else:
    print("User creation failed")

