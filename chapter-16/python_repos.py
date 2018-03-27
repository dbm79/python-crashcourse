import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status Code: ', r.status_code)

#Store API response in a dictionary
response_dict = r.json()
print('Total Repositories: ', response_dict['total_count'])

#Explore information about the repositories
repo_dicts = response_dict['items']
print('Repositories returned:', len(repo_dicts))

#Examine the first repo.
repo_dict = repo_dicts[0]
print('\nKeys:', len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)

#Explore select info for first repo
print('\nSelect information about the first repo.')
print('Name: ', repo_dict['name'])
print('Owner: ', repo_dict['owner']['login'])
