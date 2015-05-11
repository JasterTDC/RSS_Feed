
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
    def insertTechReport (self, report):
        self.app.tech.insert_one ({
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

    # Search into database, news with this title.
    def findNationalReportByTitle (self, report):
        return self.app.nat.find({ "title" : report.getTitle() }).count()

    # Search into database, news with the same title.
    def findInternationalReportByTitle (self, report):
        return self.app.inter.find({ "title" : report.getTitle() }).count()

    # Search into database, news with the same title.
    def findTechReportByTitle (self, report):
        return self.app.tech.find({ "title" : report.getTitle() }).count()
