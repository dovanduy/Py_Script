# coding:utf-8

import requests

import json

url = "https://api.github.com"


def build_uri(endpoint):
    return '/'.join([url, endpoint])


def better_print(json_str):
    return json.dumps(json.loads(json_str), indent=4)


def request_get():
    url=build_uri('users/897308902')
    print url
    response = requests.get(url)
    print response.request.headers
    print better_print(response.text)


if __name__ == "__main__":
    request_get()
