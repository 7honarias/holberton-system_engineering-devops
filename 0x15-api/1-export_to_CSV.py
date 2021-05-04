#!/usr/bin/python3
"""script that using REST API"""
import csv
import requests
from sys import argv


if __name__ == '__main__':
    userId = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(userId), verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(userId), verify=False).json()
    file_csv = argv[1] + '.csv'
    with open(file_csv, 'w') as csvfile:
        txt = csv.writer(csvfile)
        for task in todo:
            txt.writerow([str(argv[1]),
                          user.get('username'),
                          task.get('completed'),
                          task.get('title')])
