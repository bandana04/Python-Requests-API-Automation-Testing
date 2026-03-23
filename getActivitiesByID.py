import requests
head = {
    'Accept': 'text/plain',
    'Content-Type': 'application/json',
}

get_response_by_id = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Activities/1")
print(get_response_by_id.status_code)
print(get_response_by_id.json())
assert get_response_by_id.status_code == 200