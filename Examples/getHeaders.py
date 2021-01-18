import requests

url = 'https://httpbin.org/get'
headers = {'T1': 'abc', 'T2': '123'}

response = requests.get(url, headers=headers)

print(response.json())