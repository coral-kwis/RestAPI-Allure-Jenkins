import requests
import json
import jsonpath

# API URL
url = 'https://reqres.in/api/users'

# Read input json file
file = open('../data/createUser.json', 'r')
data = file.read()
data_json = json.loads(data)

# Make POST Request with Json input body
response = requests.post(url, data_json)
print(response.content)

# Validating Response code
assert response.status_code == 201

# Fetch Header from Response
print(response.headers.get('Content-Length'))

# Parse Response to Json format
response_json = json.loads(response.text)

# Pick id using json path
id = jsonpath.jsonpath(response_json, 'id')
print(id[0])
