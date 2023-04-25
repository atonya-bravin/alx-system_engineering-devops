#!/usr/bin/python3
"""fetching json data from an api"""

import requests
from sys import argv

if __name__ == "__main__":

    """get the user id from the shell"""
    employee_id = argv[1]

    """ user route """
    response = requests.get(f
        "https://jsonplaceholder.typicode.com/users/{employee_id}")

    """ get name from dict """
    employee_name = response.json()["name"]

    """ todo route """
    response = requests.get(f"https://jsonplaceholder.typicode.com/
        users/{employee_id}/todos")

    total_number_of_tasks = len(response.json())
    number_of_done_tasks = 0

    print(f"Employee {employee_name} is done with tasks(", end="")
    for todo in response.json():
        if todo["completed"]:
            number_of_done_tasks += 1

    print(f"{number_of_done_tasks}/{total_number_of_tasks}):")

    for todo in response.json():
        if todo["completed"]:
            print("\t ", todo["title"])
