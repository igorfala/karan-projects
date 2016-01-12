# -*- coding : utf-8 -*-

"""
Project: Fetch Current Weather
         To use it, import the module and
         call the : weather() function.
         It can be called with weather('Location name')
         or weather('zip code') # note that zip code 
         needs to be string. If weather() is called with no 
         arguments, it determines your location automatically.
         
@author: Igor Fala

date: 03/17/2015
"""

import urllib
import re 
from sgmllib import SGMLParser
import htmlentitydefs

class IPinfo(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.data = []
        self.starts = []
        self.newline = False
        self.GeoTag = False
        self.title = ""
        self.isTitle = False

    def handle_entityref(self, ref):
        # called for each entity reference, e.g. for "&copy", ref will be "copy"
        # Reconstruct the original entity reference.
        entities = [('nbsp', ''), ('deg', u"\u00B0"), 
                    ('prime', u"\u2032"),('Prime', u"\u2032")]
        for fr, to in entities:
            ref = ref.replace(fr, to) 
        #if self.data[-1] == '|':
        #    self.data.pop()
        self.data.append("%(ref)s" % locals())
        # standard HTML entities are enclosed with a semicolon; other entities are not
        self.newline = False 
    
    def unknown_starttag(self, tag, attrs):
        # called for each start tag
        # attrs is a list of (attr, value) tuples
        # e.g. for <pre class="screen">, tag="pre", attrs= [("class", "screen")]
        # Ideally we would like to reconstruct original tag attributes, but 
        # we may end up quoting attribute values that weren't quoted in the source
        # document, or we may change the type of quotes around the attribute value
        # (single to double quotes).
        # Note that improperly embedded non-HTML code (like client-side Javascript)
        # may be parsed incorrectly by the ancestor, causing runtime script errors.
        # All non-HTML code must be enclosed in HTML comment tags (!-- code -->)
        # to ensure that it will pass this parser unaltered (in handle comment).
        strattrs = "".join([' %s="%s"' %(key, value) for key, value\
                             in attrs if value == 'GeoTableHeader'])
        if strattrs or tag == 'th' or tag == 'td':
            self.GeoTag = True
            self.starts.append("<%(tag)s>" % locals())
        if tag == "title": self.isTitle = True
    
    def handle_data(self, text):
        # called for each block of plain text, i.e. outside of any tag
        # not containing any character or entity references
        # Store the original text verbatim.
        #text.replace("&deg", u"\u00B0") 
        if self.newline:
            self.data.append('|')
            self.newline = False 
        if self.GeoTag:
            self.data.append(text)
        if self.isTitle: self.title += text
        
    def unknown_endtag(self, tag):
            #called for each end tag, e.g. for </pre>, tag will be "pre"
            #Reconstruct the original end tag.
            if "<%s>" % tag in self.starts:
                self.GeoTag = False
                if tag == 'td':
                    self.newline = True
            if tag == "title": self.isTitle = False
    def output(self):
        print self.title
        print
        for i in range(len(self.data)):
            self.data[i]=self.data[i].replace("\n", "")
        print"\n".join([i for i in("".join(self.data)).split("|")])
        

class Weather(SGMLParser):
    def reset(self):
         SGMLParser.reset(self)
         self.starts = []
         self.weatherTag = False
         self.reference = False
         self.isTitle = False
         self.isData = False
         self.data = []
         self.title = ""
         self.day = []
         self.isDay = False
    def unknown_starttag(self, tag, attrs):
        strattrs = "".join(['%s="%s"' %(key, value) for key, value in attrs ])
        if tag == "title": 
            self.isTitle = True
            self.starts.append("%(tag)s" % locals())
        if tag == 'span':
            self.weatherTag = True
            if strattrs == 'class="Title"':
                self.isDay = True
            elif strattrs == \
                    'style="font-size: 16px;  font-weight: normal; color: #000000;"':
                self.isData = True
            self.starts.append("%(tag)s" % locals())
        if tag == "script":
            self.weatherTag ==  False
    
    def handle_entityref(self, ref):
        # called for each entity reference, e.g. for "&copy", ref will be "copy"
        # Reconstruct the original entity reference.
        entities = [('nbsp', ''), ('deg', u"\u00B0"), ('deg;', u"\u00B0"), 
                    ('prime', u"\u2032"),('Prime', u"\u2032"),
                    (u'',''), (u'amp',''),(u'copy',''),(u'\xb0','')]
        for fr, to in entities:
            ref = ref.replace(fr, to) 
        #if self.data[-1] == '|':
        #    self.data.pop()
        try:
            self.data[-1] = self.data[-1] + ("%(ref)s" % locals())
        except IndexError:
            pass
        # standard HTML entities are enclosed with a semicolon; other entities are not
        self.reference = True 
            
    def handle_data(self, text):
        # called for each block of plain text, i.e. outside of any tag
        # not containing any character or entity references
        # Store the original text verbatim. 
        if self.isTitle: self.title += text
        if self.weatherTag:
            if self.isData:
                
                if self.reference and len(self.data):
                    try:
                        if "Night" in text: self.data[-1] = self.data[-1] + "\n> "
                        self.data[-1] = self.data[-1] + text
                        self.reference = True
                        
                    except IndexError:
                        pass
                        
                else:
                    self.data.append(text)
            elif self.isDay:
                self.day.append(text+"\n") 
                self.reference = False
    def unknown_endtag(self, tag):
            #called for each end tag, e.g. for </pre>, tag will be "pre"
            #Reconstruct the original end tag.
            if tag in self.starts:
                self.weatherTag = False
                self.isDay = False
                self.isData = False
                self.isTitle = False
            if tag == "script":
                self.weatherTag == True
    def output(self):
        weather =  "\n\n".join(["%s\n> %s" % (key, value) for key, value\
                            in zip(self.day, self.data)])
        return "%s\n\n%s" % (self.title, weather)

def ipToZip(ip=None):

    if ip == None:
        ip = re.search('"([0-9.]*)"',urllib.urlopen("http://ip.jsontest.com/").read()).group(1)
        if not ip:
            ip = re.search('"([0-9.]*)"',urllib.urlopen("http://httpbin.org/ip").read()).group(1)

    url = urllib.urlopen('http://whatismyipaddress.com/ip/%s'% ip)
    usock= url.read()
    url.close()

    parser = IPinfo()
    parser.feed(usock)
    parser.close()
    parser.output()
    print
    print parser.data
    try:
        zipcode = [i.split(':')[1] for i in("".join(parser.data)).split("|")\
                    if i.split(':')[0] == "Postal Code" ][0]
        return zipcode
    except IndexError:
        print "Sorry, could'nt obtain the zipcode. The city name is returned instead!"
        print
        
        city = [i.split(':')[1] for i in("".join(parser.data)).split("|")\
                    if i.split(':')[0] == "City" ][0]
        print city
        return city

def weather(location = None):
    '''Getting weather by scrapping http://weatherforyou.com/'''
    address = location and str(location).replace(' ', '+') # Spaces are replaced with '+', to fit URL style 
    if not address: address = ipToZip()
    fsock = urllib.urlopen('http://www.weatherforyou.com/reports/index.php?forecast=zandh&pands=%s&Submit=Get+Weather'% address)
    usock = fsock.read()
    fsock.close()
    parser = Weather()
    parser.feed(usock)
    parser.close()
    
    x = int(raw_input("\n   To show weather: press 1.\n\
   To write it on  text document, press 2.\n\
   To write email, press 3.\n\
   To exit, press 4.\n   >>>   "))
    if x == 1:
        print parser.output()
    if x == 2:
        import datetime
        delimiter = ',' in parser.title and ',' or 'Local' 
        city = parser.title.split(delimiter)[0]
        outfile = "%s Weather %s.txt" % (city, datetime.date.today())
        fsock = open(outfile, "wb")
        try:
            fsock.write(parser.output())
            print "Succesfully saved to: %s" % outfile
        except:
            print "A problem occured, file not saved"
        fsock.close()
    if x == 3:
        receiver = str(raw_input("Please enter the receiver's email address > "))
        subject = 'Weather %s' % (parser.title.encode('utf-8'))
        myemail(receiver, subject, parser.output())
    if x == 4: exit()
    
if __name__ =="__main__":

    print __doc__
