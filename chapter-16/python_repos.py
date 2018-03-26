import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status Code: ', r.status_code)

#Store API response in a dictionary
response_dict = r.json()

#Process the results
print(response_dict.keys())
