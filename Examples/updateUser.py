import requests
import json
import jsonpath

#API URL
url='https://reqres.in/api/users/2'

#Read input json file
file = open('../data/createUser.json', 'r')
data = file.read()
data_json = json.loads(data)

#Make PUT Request with Json input body
response = requests.put(url,data_json)

#Validating Response code
assert response.status_code == 200

#Parse Response content
response_json = json.loads(response.text)
updatedAt = jsonpath.jsonpath(response_json, 'updatedAt')
print(updatedAt[0])