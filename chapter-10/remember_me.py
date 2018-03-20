import json

def greet_user():
    # load the username if it has been sotred previously
    # otherwise, prompt for the username and store it
    filename  = 'username.json'

    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("What is your username? ")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print('We will remember you next tume ' + username + '.')
    else:
        print('Welcome back ' + username + '.')

greet_user()
