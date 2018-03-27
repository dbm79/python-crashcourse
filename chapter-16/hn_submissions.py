import requests
from operator import itemgetter

#Make API call and store results
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print('Request Response: ', r.status_code)
