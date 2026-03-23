import requests

headers = {
    'Content-Type': 'application/json',
    'Accept': 'text/plain'
}
request_body = {
  "id": 1,
  "title": "Updated Book Title by Bandana",
  "dueDate": "2026-03-23T01:32:17.522Z",
  "completed": True
}

response_before_update = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/12", headers=headers)
print(response_before_update.status_code)
print("Before Update")
print(response_before_update.json())

response_after_update = requests.put("https://fakerestapi.azurewebsites.net/api/v1/Activities/12", json=request_body,headers=headers)
print(response_after_update.status_code)
print("After Update")
print(response_after_update.json())
