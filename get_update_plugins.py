#%%
import requests

proxy = { 
            "http"  : "http://127.0.0.1:9001", 
            "https" : "http://127.0.0.1:9001"
        }

#proxies=proxy
url = 'https://archives.jenkins.io/updates/stable-2.19/update-center.json'
r = requests.get(url, allow_redirects=True, verify=True)
open('update-center.json', 'wb').write(r.content)
