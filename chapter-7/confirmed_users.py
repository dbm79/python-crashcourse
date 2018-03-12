#start with a list of users that need confirmed
#and an empty list to hold confirmed users
confirmed_users = []
unconfirmed_users = ['bryan', 'lucas', 'melissa', 'devin']

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print('Verifying user: ' + current_user.title())
    confirmed_users.append(current_user)

print('\nThe folowing users have been confirmed:')
for user in confirmed_users:
    print(user.title())
