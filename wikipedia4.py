import requests

parameters = { 'action' : 'query',
               'prop' : 'revisions',
               'titles' : 'Python (programming language)',
               'rvlimit' : 100,
               'rvprop' : 'timestamp|user',
               'format' : 'json',
               'continue' : '' }

anon_editors = {}
logged_in_editors = {}

while True:
    wp_call = requests.get('https://en.wikipedia.org/w/api.php',
                           params=parameters)
    response = wp_call.json()
    for page_id in response['query']['pages']:
        revisions = response['query']['pages'][page_id]['revisions']
        for rev in revisions:
            if 'anon' in rev:
                if rev['user'] in anon_editors:
                    anon_editors[rev['user']] += 1
                else:
                    anon_editors[rev['user']] = 1
            else:
                if rev['user'] in logged_in_editors:
                    logged_in_editors[rev['user']] += 1
                else:
                    logged_in_editors[rev['user']] = 1

    if 'continue' in response:
        parameters.update(response['continue'])
        # Replaces what was in parameters['continue'] with what's in
        # response['continue']
    else:
        break

anon_edit_count = 0
logged_in_edit_count = 0
for editor in anon_editors:
    anon_edit_count += anon_editors[editor]
for editor in logged_in_editors:
    logged_in_edit_count += logged_in_editors[editor]

print_params = { 'anon_edits' : anon_edit_count,
                 'logged_in_edits' : logged_in_edit_count,
                 'total_edits' : anon_edit_count + logged_in_edit_count }
print( print_params)
