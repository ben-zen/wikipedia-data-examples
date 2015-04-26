import requests

# http://en.wikipedia.org/w/api.php?
# action=query&
# list=users&
# ususers=Benjamin_Mako_Hill|Jtmorgan|Sj|Koavf&
# usprop=editcount
# &format=json

# QUERY API: https://www.mediawiki.org/wiki/API:Query

ENDPOINT = 'https://en.wikipedia.org/w/api.php'

parameters = {'action' : 'query',
              'list' : 'users',
              'ususers' : 'Benjamin_Mako_Hill|Jtmorgan|Sj|Koavf',
              'usprop' : 'editcount',
              'format' : 'json'}

user_lookup = requests.get(ENDPOINT, params=parameters)
response = user_lookup.json()

for user in response['query']['users']:
    print("{0} has made {1} edits to Wikipedia.".format(user['name'], user['editcount']))
