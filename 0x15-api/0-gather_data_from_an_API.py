#!/usr/bin/python3
"""script that using REST API"""
import requests
from sys import argv


def api_show(argv):
    """ print to stdout"""
    id_user = str(argv[1])
    number_of_done_tasks = 0
    total_number_of_tasks = 0
    task_title = ""

    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id_user)
    user = requests.get(user_url).json()
    employee_name = user['name']

    task_url = 'https://jsonplaceholder.typicode.com/todos'
    tasks = requests.get(task_url).json()
    for task in tasks:
        if (task['userId'] == int(id_user)) and (task['completed'] is True):
            number_of_done_tasks += 1
            task_title += "\t {}\n".format(task['title'])
        elif task['userId'] == int(id_user):
            total_number_of_tasks += 1

    print("Employee {} is done with task({}/{}):"
        .format(employee_name, number_of_done_tasks, total_number_of_tasks))
    print('{}'.format(task_title), end='')

if __name__ == '__main__':
    api_show(argv)
