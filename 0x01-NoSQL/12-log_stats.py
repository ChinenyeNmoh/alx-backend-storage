#!/usr/bin/env python3
"""Python script that
provides some stats about
Nginx logs stored in MongoDB"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx
    counter = nginx.count_documents({})
    get = nginx.count_documents({"method": "GET"})
    post = nginx.count_documents({"method": "POST"})
    put = nginx.count_documents({"method": "PUT"})
    patch = nginx.count_documents({"method": "PATCH"})
    delete = nginx.count_documents({"method": "DELETE"})
    path_stat = nginx.count_documents({"method": "GET", "path": "/status"})

    print(f"{counter} logs")
    print('Methods:')
    print(f'\tmethod GET: {get}')
    print(f'\tmethod POST: {post}')
    print(f'\tmethod PUT: {put}')
    print(f'\tmethod PATCH: {patch}')
    print(f'\tmethod DELETE: {delete}')
    print(f'{path_stat} status check')
