#!/usr/bin/python3
import json
import cgi
import os

if __name__ == '__main__':
    # Output results
    print('Content-Type: application/json\n')
    #print('{"Result": "Hi!"}')
    user = os.environ['REMOTE_USER']
    path = os.environ['SCRIPT_URL']
    fields = cgi.FieldStorage()
    field_dict = {k: fields.getlist(k) for k in fields.keys()}
    print(json.dumps({'user': user, 'path': path, 'args': field_dict}))
