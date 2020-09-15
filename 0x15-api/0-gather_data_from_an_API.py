#!/usr/bin/python3
""" return formatted todo list info """

import requests
import sys


if __name__ == "__main__":
    ''' main '''
    try:
        eid = sys.argv[1]
        url = "https://jsonplaceholder.typicode.com/users/" + eid
        name = requests.get(url).json().get("name")
        if name:
            num_todos = len(requests.get(url + "/todos/").json())
            completed = requests.get(url + "/todos/",
                                     params={"completed": 'true'}).json()

            print("Employee {} is done with tasks({}/{}):"
                  .format(name, len(completed), num_todos))
            for todo in completed:
                title = todo.get("title")
                print("     {}".format(title))
    except:
        pass
