users = ['gerry', 'mike', 'stan', 'toby', 'admin', 'dwight']

for user in users:
    if user == 'admin':
        print('Hello ' + user.title() + ' would you like a report?')
    else:
        print('Hello ' + user.title())
