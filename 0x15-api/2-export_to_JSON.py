#!/usr/bin/python3
""" write csv file with todo list info """

import sys
import requests
import json


if __name__ == "__main__":
    ''' main '''
    try:
        eid = sys.argv[1]
        url = "https://jsonplaceholder.typicode.com/users/" + eid
        username = requests.get(url).json().get("username")
        if username:
            todos = requests.get(url + "/todos/").json()
            todo_list = []

            with open(eid + ".json", 'w') as jsonfile:
                for todo in todos:
                    todo_list.append(
                        {
                            "task": todo.get('title'),
                            "completed": todo.get('completed'),
                            "username": username
                        }
                    )
                jsonfile.write(json.dumps({eid: todo_list}))

    except:
        pass
