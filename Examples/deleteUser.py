import requests
import pprint

url = 'https://reqres.in/api/users/2'

response = requests.delete(url)

pprint.pprint(response.status_code)

assert response.status_code == '204'