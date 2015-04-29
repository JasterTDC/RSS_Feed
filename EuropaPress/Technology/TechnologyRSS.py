
# Import Tecnology class.
from Technology import Technology

# Include xml parser.
import xml.etree.ElementTree as ElementTree

# Include url library.
from urllib.request import urlopen

# Include datetime library.
import time

# RSS url.
rss = "http://www.europapress.es/rss/rss.aspx?ch=445"

# Read the url content.
content = urlopen (rss)
xmlData = content.readall().decode('utf-8')
content.close()

# Parse the content of the url.
xml = ElementTree.fromstring (xmlData)

# Latests news.
latest = []

# Extract all the information about one new.
for item in xml.getiterator ("item"):
    # Initialize vars.
    tech = Technology ()
    categ = []
    for elem in item.getchildren() :
        if ("title" in elem.tag) :
            tech.setTitle (elem.text)
        if ("link" in elem.tag) :
            tech.setLink (elem.text)
        if ("description" in elem.tag) :
            tech.setDescription (elem.text)
        if ("pubDate" in elem.tag) :
            tech.setDate (time.strptime (elem.text, "%a, %d %b %Y %H:%M:%S %Z"))
        if ("category" in elem.tag) :
            categ.append (elem.text)
    tech.setCategory (categ)

    # Add tech news to the list.
    latest.append (tech)
