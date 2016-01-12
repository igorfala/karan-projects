"""
Project: Web Scraper for images and links
         To use it, import the module and
         call the : linkScraper(URL,DB) function.
         or imageScraper(URL, DB)
         
@author: Igor Fala

date: 01/12/2016
"""

from urllib import urlopen
from bs4 import BeautifulSoup
import sqlite3

def linkScraper(URL, DB):
    
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute('''
    DROP TABLE IF EXISTS Links''') 
    cur.execute('''
    CREATE TABLE Links (link TEXT)''')
    URL = urlopen(URL)
    html = URL.read()
    URL.close()
    soup = BeautifulSoup(html, 'html.parser')  
    tags = soup('a')
    for tag in tags:
        cur.execute("SELECT link FROM Links WHERE link= ?", (tag.get('href', None), ))
        try:
            data = cur.fetchone()[0] # Checking for duplicates
            print "Found in database ",data
            continue
        except:
            pass
        cur.execute('''INSERT INTO Links (link) 
            VALUES ( ? )''', ( tag.get('href', None), ) )
        conn.commit() # Committing changes
    cur.close()       # Closing the connection

def imageScraper(URL, DB):

    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute('''
    DROP TABLE IF EXISTS Images''')
    cur.execute('''
    CREATE TABLE Images (source TEXT)''')
    URL = urlopen(URL)
    html = URL.read()
    URL.close()
    soup = BeautifulSoup(html, 'html.parser')  
    imgs = soup('img')
    for img in imgs:
        cur.execute("SELECT source FROM Images WHERE source= ?", (img.get('src', None), ))
        try:
            data = cur.fetchone()[0]
            print "Found in database ",img
            continue
        except:
            pass
        cur.execute('''INSERT INTO Images (source) 
            VALUES ( ? )''', ( img.get('src', None), ) )
        conn.commit()
    cur.close()
    
if __name__ = '__main__': print __doc__
