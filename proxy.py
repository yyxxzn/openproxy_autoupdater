import requests
import json
import numpy as np

def update_proxies(proxy_type):

    url = requests.get('https://api.openproxy.space/lists/' + proxy_type) #requesting json file

    proxies = json.loads(url.content)
    proxies = proxies['data']
    proxies_data = np.array(proxies[0]['items'])

    #iterating in the JSON file to obtain all proxies
    for i in range (1, len(proxies)):
        proxies_data = np.concatenate((proxies_data, np.array(proxies[i]['items'])))
    
    #save CSV
    np.savetxt("proxies.csv", 
        proxies_data,
        delimiter =", ", 
        fmt ='% s')

update_proxies('http') #socks4, socks5, http