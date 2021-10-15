#!/usr/bin/python3
"""
    File: 6-load_from_json_file.py
"""
import json


def load_from_json_file(filename):
    """ load_from_json_file(filename) """
    with open(filename, 'r', encoding='utf-8') as fd:
        return(json.load(fd))
