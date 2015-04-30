
# Import section.
from urllib.request import urlopen # Url library.
import xml.etree.ElementTree as ElementTree # XML parser.
import time # Time library.

# Channel RSS class.
class Channel :

    # Class constructor.
    def __init__ (self, rss) :
        self.rss = rss

    # Extract all news stored in RSS.
    def extractFeed (self) :
        # Read url and stored all the information in a var.
        content = urlopen (self.rss)
        xmlData = content.readall().decode('utf-8')
        content.close ()

        # Parse xml content.
        xml = ElementTree.fromstring (xmlData)

        itemsList = []
        for items in xml.getiterator("item"):
            feed = []
            categ = []
            for elem in items.getchildren():
                if ("title" in elem.tag):
                    feed.append (elem.text)
                if ("link" in elem.tag):
                    feed.append (elem.text)
                if ("description" in elem.tag):
                    feed.append (elem.text)
                if ("pubDate" in elem.tag):
                    feed.append (time.strptime (elem.text, "%a, %d %b %Y %H:%M:%S %Z"))
                if ("category" in elem.tag):
                    categ.append (elem.text)
            feed.append (categ)
            itemsList.append (feed)

        return itemsList
