#!/usr/bin/python3
"""10-my_github.py"""

import requests
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    pass = sys.argv[2]
    r = requests.get('https://api.github.com/user',
                       auth=(user, pass))
    print(r.json().get('id'))
