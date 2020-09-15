#!/usr/bin/python3
""" write json file all users todo list info """

import requests
import json


if __name__ == "__main__":
    ''' main '''
    url = "https://jsonplaceholder.typicode.com/users/"
    todict = {}
    todo_list = []
    try:
        users = requests.get(url).json()
        for user in users:
            eid = user.get('id')
            username = user.get('username')
            todos = requests.get(
                "{}{}/todos/".format(url, eid)).json()

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

    except:
        pass
