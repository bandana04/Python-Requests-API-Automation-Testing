import requests
import pytest
def test_getUser():
    url = "https://fakestoreapi.com/users"
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'plain/text'
    }
    response = requests.get(url, headers=headers)
    assert 200 == response.status_code
    print(response.text)
