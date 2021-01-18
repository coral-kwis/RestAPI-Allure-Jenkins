import requests
import json
import jsonpath
import pprint

url = 'https://reqres.in/api/users?page=2'

response = requests.get(url)
print(response)
pprint.pprint(f'body: {response.json()}')
pprint.pprint(f'content: {response.content}')
rs_json = json.loads(response.text)
pprint.pprint(f'json  body: {rs_json}')
first_name = jsonpath.jsonpath(rs_json,'data[1].first_name')
pprint.pprint(first_name[0])