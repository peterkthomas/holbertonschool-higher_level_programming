#!/usr/bin/python3
"""2-post_email.py"""
import urllib.request
import sys

if __name__ == "__main__":
    email = sys.argv[2]
    p_data = urllib.parse.urlencode({"email": email}).encode('ascii')
    with urllib.request.urlopen(sys.argv[1], p_data) as url:
        s = url.read()
        print(s.decode('utf-8'))
