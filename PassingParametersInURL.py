import requests
from authTokenFunction import AuthTokenFunction
access_token = AuthTokenFunction()
#This API doesn't support parameters so error will occur
parameters = {
    'page' : 1,
    'limit' : 10
}
headers = {
    'Content-Type': 'application/json',
    'Accept': 'plain/text',
    'x-tenant-subdomain':'byjus',
    'Authorization':f'Bearer {access_token}'
}
url = 'https://braimyapi-hxc3h7gwd8cna7aq.centralindia-01.azurewebsites.net/'
response = requests.get(url + "/public/qna", params = parameters, headers=headers)
published_qna = response.json()
print(published_qna)



