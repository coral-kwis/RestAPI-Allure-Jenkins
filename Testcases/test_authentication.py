import requests
import jsonpath
from requests.auth import HTTPBasicAuth


def test_basic_oauth_with_credentials():
    """This is comment"""
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=HTTPBasicAuth('user', 'pass'))
    print(response.json())


def test_oauth():
    token_url = 'http://thetestingworldapi.com/Token'
    data = {'grant_type': 'password', 'username': 'admin', 'password': 'adminpass'}
    response = requests.post(token_url, data)
    token = jsonpath.jsonpath(response.json(), 'access_token')

    auth = {'Authorization': 'Bearer ' + token[0]}
    API_URL = 'http://thetestingworldapi.com/api/StDetails/1104'
    response = requests.get(API_URL, headers=auth)
    print(response.text)
