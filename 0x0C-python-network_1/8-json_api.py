#!/usr/bin/python3
"""8-json_api.py"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        d = {'q': ''}
    elif len(sys.argv) > 1:
        d = {'q': sys.argv[1]}

    try:
        r = requests.post('http://0.0.0.0:5000/search_user', d)
        if r.json():
            print('[{}] {}'.format(r.json().get('id'),
                                   r.json().get('name')))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
