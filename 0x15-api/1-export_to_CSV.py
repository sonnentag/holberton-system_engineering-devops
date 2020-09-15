#!/usr/bin/python3
""" write csv file with todo list info """

import sys
import requests
import csv


if __name__ == "__main__":
    ''' main '''
    try:
        eid = sys.argv[1]
        url = "https://jsonplaceholder.typicode.com/users/" + eid
        username = requests.get(url).json().get("username")
        todos = requests.get(url + "/todos/").json()

        with open(eid + ".csv", 'w') as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

            for todo in todos:
                writer.writerow([eid, username,
                                todo.get("completed"), todo.get("title")])

    except Exception as err:
        sys.stderr.write(str(err) + "\n")