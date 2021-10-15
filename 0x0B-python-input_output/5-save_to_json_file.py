#!/usr/bin/python3
"""File: 5-save_to_json_file.py"""
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file"""
    with open(filename, 'w', encoding='utf-8') as fd:
        return(json.dump(my_obj, fd))
