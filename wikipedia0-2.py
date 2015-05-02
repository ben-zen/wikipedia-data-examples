"""A simple example/test of getting the English Wikipedia Main Page.

This sample provides a simple query to build off of and explore what the
MediaWiki API can do. Fetches my (Zen-ben's) user page and prints the first few
links found on it.
"""
# Copyright (C) 2015 Ben Lewis <benjf5+github@gmail.com>
# Licensed under the MIT license; freely share this code!

import requests

ENDPOINT = 'https://en.wikipedia.org/w/api.php'

parameters = { 'action' : 'query',
               'prop' : 'links',
               'titles' : 'User:Zen-ben|User:Benjamin Mako Hill',
               'continue' : '',
               'format' : 'json' }

page_links = {}

while True:
    wp_call = requests.get(ENDPOINT, params=parameters)
    response = wp_call.json()

    for page in response['query']['pages']:
        page_title = response['query']['pages'][page]['title']
        if page_title not in page_links:
            page_links[page_title] = []
        if 'links' in response['query']['pages'][page]:
            page_links[page_title].extend(response['query']['pages'][page]['links'])

    if 'continue' in response:
        parameters.update(response['continue'])
    else:
        break

for page in page_links:
    print(page)
    print(page_links[page])
