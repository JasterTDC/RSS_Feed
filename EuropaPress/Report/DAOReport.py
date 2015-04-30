
# Import section.
from .ReportData import Report
from pymongo import MongoClient # Import mongodb driver.

# DAOReport class.
class DAOReport :

    # Class constructor.
    def __init__(self):
        self.client = MongoClient () # MongoDB connection.
        self.app = self.client.app # Select database.

    # Class modifier that insert a report into a mongodb.
    def insertFeedReport (self, report):
        self.app.feed.insert_one ({
            "title" : report.getTitle(),
            "description" : report.getDescription(),
            "link" : report.getLink(),
            "date" : report.getDate(),
            "category" : report.getCategory()
        })

    # Class modifier that insert a report into a mongodb.
    def insertInternationalReport (self, report):
        self.app.inter.insert_one ({
            "title" : report.getTitle(),
            "description" : report.getDescription(),
            "link" : report.getLink(),
            "date" : report.getDate(),
            "category" : report.getCategory()
        })

    # Class modifier that insert a report into a mongodb.
    def insertNationalReport (self, report):
        self.app.nat.insert_one ({
            "title" : report.getTitle(),
            "description" : report.getDescription(),
            "link" : report.getLink(),
            "date" : report.getDate(),
            "category" : report.getCategory()
        })
