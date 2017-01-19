import requests
import sys
from time import sleep

import urllib
__author__ = "Hacknology"



urlist = open("url.txt", "r").readlines()
for url in urlist:
    url = url.strip()
    
    
    r = requests.get(url)
    if r.status_code == 200:
        yeni_url = r.url + "'"
        
        conn = requests.get(yeni_url)
        content = conn.text
        print(yeni_url, "taranıyor..")
        if "Warning" in content:
            print("[+] -->", url, "acik tespit edildi!")
            dosya = open("acikli.txt", "a")
            dosya.write(url + "\n")
        else:
            pass
            
                
    else:
        print("Şimdilik bişey bulamadım:")
        sleep(5)
        sys.exit()
