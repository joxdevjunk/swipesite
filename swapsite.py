# coding: utf8 
# swapper les information d'un site 
import os
from bs4 import BeautifulSoup
import urllib.request
import requests 

class scwap:
    def __init__(self, req):
        self.online = True
        try:        # gere http & https...
            self.request = requests.Session()
            self.soup = BeautifulSoup(self.request.get(req).text, "html.parser")
        except:  # gere le cas d'utilité en fichier local
           with open(req,'r') as f:
               req = f.read()
               self.soup = BeautifulSoup(req, "html.parser")
               self.online = False
        
    def allby(self,sel):
        return self.soup.findAll(sel)
    
    def getext(self):
        return self.soup.get_text().split()
     
url = "https://www.alwaysdata.com/fr/"
t = scwap('Accueil.html')
b = scwap(f'{url}')


# 2020 by guitarPgm // Yayou Corp 



