#!/usr/bin/python3
"""Given an Employee ID, returns information
about his/her TODO list progress.
"""
import requests
from sys import argv

if __name__ == '__main__':
    try:
        employee_id = int(argv[1])
    except ValueError:
        exit()

    api_url = 'https://jsonplaceholder.typicode.com'
    user_uri = '{api}/users/{id}'.format(api=api_url, id=employee_id)
    todo_uri = '{user_uri}/todos'.format(user_uri=user_uri)

    # User Response
    res = requests.get(user_uri).json()

    # Name of the employee in question
    name = res.get('name')

    # User TODO_LIST Response
    res = requests.get(todo_uri).json()

    # Total number of tasks ==> both completed and non-completed tasks
    total = len(res)

    # Number of non-completed tasks
    non_completed = sum([elem['completed'] is False for elem in res])

    # Number of completed tasks
    completed = total - non_completed

    # Formatting the expected output
    str = "Employee {name} is done with tasks({completed}/{total}):"
    print(str.format(name=name, completed=completed, total=total))

    # Printing completed tasks
    for elem in res:
        if elem.get('completed') is True:
            print("\t {}".format(elem.get('title')))
