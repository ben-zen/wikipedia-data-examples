import time
import simplejson as json
from urllib2 import urlopen

url_base = 'https://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles=%s&rvlimit=100&rvprop=timestamp|user&format=json'

pages = ["Benjamin_Mako_Hill", "Python", "Data_science"]

for page_title in pages:
    
    wp_call = urlopen(url_base % page_title)
    response = json.loads(wp_call.read())

    for page_id in response["query"]["pages"].keys():
        page_title = response["query"]["pages"][page_id]["title"]
        revisions = response["query"]["pages"][page_id]["revisions"]

        for rev in revisions:
            print page_title + "\t" + rev["user"] + "\t" + rev["timestamp"]


    time.sleep(3)
