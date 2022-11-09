from urllib.parse import urlparse
from http import client

def extract_short_link(url):
    host = urlparse(url).netloc
    path = urlparse(url).path
    c = client.HTTPSConnection(host)
    c.request("GET", path)

    r = c.getresponse()
    c.close()
    if(r.status == 301 or r.status == 302):
        return extract_short_link(r.headers["Location"])
    else:
        return url
