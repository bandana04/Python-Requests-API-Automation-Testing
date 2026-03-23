import requests
head = {
    "Accept": "text/plain",
}

response1 = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Activities', headers=head)
print(response1.status_code)
print(response1.json())

assert response1.status_code == 200