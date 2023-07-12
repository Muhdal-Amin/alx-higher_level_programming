#!/usr/bin/python3
"""a function that create an object from a JSON file"""
import json


def load_from_json_file(filename):
    """creates an Object from JSON """
    with open(filename, encoding="utf-8") as f:
        return json.load(f) 
