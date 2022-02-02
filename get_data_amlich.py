#!/usr/bin/python
# -*- coding: utf-8 -*-

# read html at http://www.informatik.uni-leipzig.de/~duc/amlich/DuLieu/
# save in table 1800-99.html, etc..

from urllib.request import urlopen, Request
import requests
import re

def Open_Url(url):
    req = Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
    response = ''
    link = ''
    try:
        response = urlopen(req)
        link=response.read()
        if debug: print('OK reading url')
        response.close()
    except: pass
    if link != '':
        return link
    else:
        link = 'Opened'
        return link

def page(c, p):
    url_to_open = 'http://www.informatik.uni-leipzig.de/~duc/amlich/DuLieu/Sun-Moon-' + c + p + '.html'
    text = Open_Url(url_to_open)

    #print(text)
    # get table tag
    text=text.decode('utf8').replace('<table>\r\n</body>','</table>\r\n</body>')
    #print(text)
    match2 = re.compile('<table border=1>(.+?)</table>.+?',re.DOTALL).findall(str(text))

    #print(match2)

    for k in range(len(match2)):
        #print(match2[k])
        match2[k]=match2[k].replace('\\r\\n','')
        match2[k]=match2[k].replace('\\n','')
        match2[k]=match2[k].replace('colspan=2','colspan=3')
        match2[k]=match2[k].replace(' c&#225;c ','</td><td><b>')
        match2[k]=match2[k].replace(' - ','</td><td>')
        match2[k]=match2[k].replace('<tr><td>&nbsp;</td>','<tr><td>&nbsp;&nbsp;</td>') #première colonne vide
        # split 2ème colonne vide
        match2[k]=match2[k].replace('<td>&nbsp;</td>','<td>-</td>')
        match2[k]=match2[k].replace('-','</td><td>')     
    return match2


tab = '<table border=1>'
r = ''
century='18'

for p in ['00','20','40','60','80']:
    match = page(century, p)
    r += ''.join(match)
    
tab += r + '</table>'
#print(tab)

with open(century+'00-99.html','w') as f:
    f.write(tab)
