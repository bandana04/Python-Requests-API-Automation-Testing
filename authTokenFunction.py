import requests
def AuthTokenFunction():
    url = "https://braimyapi-hxc3h7gwd8cna7aq.centralindia-01.azurewebsites.net/"
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'plain/text',
        'x-tenant-subdomain': 'byjus'
    }
    body = {
        "phoneNumber": "+9779840437941",
        "password": "Admin@123"
    }
    response = requests.post(url + '/tenant-auth/login-with-phone', headers=headers, json=body)
    print(response.status_code)
    data = response.json()
    auth_token = data['data']['accessToken']
    print("Auth token :", auth_token)
    return auth_token
AuthTokenFunction()
