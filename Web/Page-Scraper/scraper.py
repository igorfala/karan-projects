"""
Project: Web Scraper for images and links
         To use it, import the module and
         call the : linkScraper(URL,DB) function.
         or imageScraper(URL, DB)
         To download all the images saved in the DB, 
         simply call imageDownload(DB), only after 
         imageScraper() was called
         
@author: Igor Fala

date: 01/12/2016
"""

from urllib import urlopen
from bs4 import BeautifulSoup
import sqlite3, os

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
    
def download(src, fileName): # src is the image link, fileName is the name of
    fsock = urlopen(src)     # the file it will be saved under
    fObj = open(fileName, 'wb')
    fObj.write(fsock.read())
    fsock.close()
    fObj.close()

def imageDownload(DB):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    try:              # Verify if the DB with src was created
        sources = cur.execute('''SELECT source FROM Images''')
    except sqlite3.OperationalError:
        print "Please call imageScraper() first, to create a database with image sources."
        return
    count = 0
    if not os.path.exists('IMAGES'):      # Create the 'Images' directory if it 
        os.makedirs('IMAGES')             # does not exist.
    os.chdir(os.getcwd()+'/IMAGES')       # Change to 'Images' to save files there.

    if os.listdir(os.getcwd()) != []:
        print "Directory not empty, removing all contents before proceding"
        inp = raw_input('To continue pres "Y", to abort press "N":\t')
        if inp in ("Y", 'y'):
            print "Deleting all files, to place new images."
            for f in os.listdir(os.getcwd()):
                os.remove(f)
        else:
            print "Aborted"
            os.chdir(os.path.dirname(os.getcwd())) # Changing back to parent directory
            return
    print 'Downloading...'
    for source in sources:
        src = source[0]                   # Get the actual text (source is a tuple).
        try:
            name = src.split('/')[-1]
            download(src, name)
        except:
            print " Couldn't save: %s" % src
            pass
    print 'Finished, check IMAGES'
    os.chdir(os.path.dirname(os.getcwd())) # Changing back to parent directory

if __name__ == '__main__': print __doc__
