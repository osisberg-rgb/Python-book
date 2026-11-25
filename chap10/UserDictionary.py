from pathlib import Path
import json

path = Path('User_dictionary.json')


def make_User():
    dic1 = input("What is your name\n")
    dic2 = input("What is your age")

    dict = {
        "name": dic1,
        "age": dic2
    }

    content = json.dumps(dict)
    path.write_text(content)

def load_User():
    loadContent = path.read_text()
    load = json.loads(loadContent)
    print(f"Hey {load['name']}, welcome back. You are {load['age']} years old")

