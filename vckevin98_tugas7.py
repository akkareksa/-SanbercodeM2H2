# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 19:41:05 2020

@author: Kevin
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

alamat = "https://kompas.com/"
html = urlopen(alamat)
data = BeautifulSoup(html, 'html.parser')

table = data.find_all("div", {"class":"most__wrap"})[0]
rows = table.find_all("h4")

populars = []
for row in rows:
    populars.append(row.get_text())    
    
df = pd.DataFrame({'title':populars})

print(df)