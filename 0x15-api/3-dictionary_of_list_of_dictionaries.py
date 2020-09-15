#!/usr/bin/python3
""" write json file all users todo list info """

import json
import requests


if __name__ == "__main__":
    ''' main '''
    eid = 1
    url = "https://jsonplaceholder.typicode.com/users/"
    todict = {}

    try:
        max_id = len(requests.get(url).json())
        while eid <= max_id:
            username = requests.get(
                "{}{}".format(url, eid)).json().get("username")
            if username:
                todos = requests.get(
                    "{}{}/todos/".format(url, eid)).json()
                todo_list = []

                for todo in todos:
                    todo_list.append(
                        {
                            "username": username,
                            "task": todo.get('title'),
                            "completed": todo.get('completed')
                        }
                    )
                todict[eid] = todo_list

                with open("todo_all_employees.json", 'w') as jsonfile:
                    json.dump(todict, jsonfile)

            eid += 1

    except:
        pass
