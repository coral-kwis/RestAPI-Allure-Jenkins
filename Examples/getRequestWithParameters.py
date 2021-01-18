import requests

url = 'https://httpbin.org/get'
params = {'name': 'coral', 'email': 'coral@coral.com', 'number': '3432-432-2345'}

response = requests.get(url, params=params)

print(response.text)

#  "url": "https://httpbin.org/get?name=coral&email=coral%40coral.com&number=3432-432-2345"
