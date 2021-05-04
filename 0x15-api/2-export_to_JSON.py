#!/usr/bin/python3
"""script that using REST API"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    userId = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(userId), verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(userId), verify=False).json()
    file_json = argv[1] + '.json'
    list_task = []
    dir_task = {}
    for task in todo:
        dir_task['task'] = task.get('title')
        dir_task['completed'] = task.get('completed')
        dir_task['username'] = task.get('username')
        list_task.append(dir_task)
    jsonobj = {}
    jsonobj[userId] = list_tasks
    with open(file_json, 'w') as jsonfile:
        json.dump(jsonobj, jsonfile)
