#!/usr/bin/python3
"""Given an Employee ID, returns information
about his/her TODO list progress.
"""
import requests
from sys import argv

if __name__ == "__main__":

    
    emp_id = argv[1]

    API_domain = "jsonplaceholder.typicode.com"

    response = requests.get(f"https://{API_domain}/users/{emp_id}")

    employee_name = response.json()["name"]

    response = requests.get(f"https://{API_domain}/users/{emp_id}/todos")

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
