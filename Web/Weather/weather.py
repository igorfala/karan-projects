"""
Project: Fetch Current Weather
         To use it, import the module and
         call the : weather() function.
         It can be called with weather('Location name')
         or weather('zip code') # note that zip code 
         needs to be string. If weather() is called with no 
         arguments, it determines your location automatically.
         
author: Igor Fala

date: 01/08/2016
"""
import urllib, json
from bs4 import BeautifulSoup
from myemail import myemail

def ipInfo():
    """Determines the host ip address and returns it"""
    url = "https://api.ipify.org?"
    url = url+urllib.urlencode({'format': 'json'})
    fsock = urllib.urlopen(url)
    data = json.load(fsock)
    fsock.close()
    return data['ip']

def ipToZip(ip=ipInfo()):
    '''Takes the ip address as argument, and returns the Internet Provider zipcode'''
    url ="http://freegeoip.net/json/%s" % ip
    fsock= urllib.urlopen(url)
    data = json.load(fsock)
    return data['zip_code']

def weather(location = None):
    '''Getting weather by scrapping http://weatherforyou.com/'''
    address = location and str(location).replace(' ', '+') # Spaces are replaced with '+', to fit URL style 
    if not address: address = ipToZip()
    fsock = urllib.urlopen('http://www.weatherforyou.com/reports/index.php?forecast=zandh&pands=%s&Submit=Get+Weather'% address)
    html = fsock.read()
    fsock.close()
    soup = BeautifulSoup(html, "html.parser")
    title = None
    title = soup.findAll("span", {"class" : "headerText"})[0].string
    if title is None: # If the title is not found, the data was not fetched
        print "Can't find the location you're looking for, please be more specific!"
        exit()

    weatherTags = soup('span') # Getting all the span tags (the weather info is held in them)
    days, data, isData = [], [], False

    for i in range(len(weatherTags)):
        if isData:                                     # Determining if it's weather info
            info = weatherTags[i].string
            try:                                           # In case it's the last statement
                if 'Night:' in weatherTags[i+1].string:    # If the Night part exists, 
                    info += '\n'+ weatherTags[i+1].string  # it's added to the info
                data.append(info)              # data is a list with weather info for all days
                isData = False                 # isData flag is turned off
            except IndexError:                 # Catch the IndexError
                pass
        if weatherTags[i].has_attr('class') and weatherTags[i].attrs['class'][0]=='Title':
            days.append(weatherTags[i].string)   # days holds all the day names
            isData = True                        # isData flag is turned on


    x = raw_input("\n    To show weather: press 1.\n\
    To write it on a text document, press 2.\n\
    To write email, press 3.\n\
    To exit, press 4.\n   >>>   ")
    try: 
        x = int(x)
    except:
        print "Invalid numeral. Please enter a number between 1 and 4\n"

    weatherInfo = "\n".join(["\n>>%s:\n\n%s" %(i, j) for i,j in zip(days, data)])

    if x == 1:
        print type(title), type(weatherInfo)
        print title+'\n'+weatherInfo

    if x == 2:
        import datetime 
        city = title.split()[0]
        outfile = "%s Weather %s.txt" % (city, datetime.date.today())
        fsock = open(outfile, "wb")
        try:
            fsock.write(weatherInfo.encode('utf-8'))
            print "Succesfully saved to: %s" % outfile
        except:
            print "A problem occured, file not saved"
        fsock.close()

    if x == 3:
        receiver = str(raw_input("Please enter the receiver's email address > "))
        subject = 'Weather %s' % (title.encode('utf-8'))
        myemail(receiver, subject, weatherInfo)

    if x >= 4: exit()
    
if __name__ =="__main__":
    print __doc__

