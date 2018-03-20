import json

def greet_user():
    '''Greet the user by name'''
    
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
