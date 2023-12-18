#!/usr/bin/env python3
""" Python function that lists all documents in a collection"""


def list_all(mongo_collection):
    """ List all documents in Python """
    result = mongo_collection.find()
    return [i for i in result]
