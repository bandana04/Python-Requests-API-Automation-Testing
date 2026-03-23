import requests
header = {
    'Accept': 'text/plain',
    'Content-Type': 'application/json',
}
request_payload = {
  "id": 1,
  "title": "Book Title by Bandana updated",
  "dueDate": "2026-03-23T01:32:17.522Z",
  "completed": True
}
response = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Activities", json=request_payload, headers=header)
print(response.status_code)
print(response.json())

data = response.json()       #Storing response in data variable
print(data['id'])

assert response.status_code == 200
assert data['id'] == 1       #Validating if the if we kept matches or not