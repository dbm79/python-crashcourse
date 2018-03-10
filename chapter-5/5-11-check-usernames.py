current_users = ['gerry', 'mike', 'stan', 'toby', 'admin', 'dwight']
new_users = ['Kathy', 'MIKE', 'Jim', 'Pam', 'Stan', 'creed']

for user in new_users:
    if user.lower() in current_users:
        print('Sorry, user ' + user.title() + ' is already taken.')
    else:
        print(user.title() + ' is available.')
