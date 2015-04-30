
# Include datetime library.
import datetime

# Technology class.
class Report:

    # Title setter.
    def setTitle (self, title):
        self.title = title

    # Description setter.
    def setDescription (self, desc):
        self.description = desc

    # Date setter.
    def setDate (self, date):
        self.date = date

    # Link setter.
    def setLink (self, link):
        self.link = link

    # Category setter.
    def setCategory (self, categ):
        self.category = categ

    # Title getter.
    def getTitle (self) :
        return self.title

    # Description getter.
    def getDescription (self) :
        return self.description

    # Date getter.
    def getDate (self) :
        return self.date

    # Link getter.
    def getLink (self) :
        return self.link

    # Category list getter.
    def getCategory (self) :
        return self.category
