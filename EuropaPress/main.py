
# Import section.
from RSS.Channel import Channel
from Report.DAOReport import DAOReport
from Report.ReportData import Report
from time import strftime
import datetime

europaTech = Channel ("http://www.europapress.es/rss/rss.aspx?ch=445")
europaInter = Channel ("http://www.europapress.es/rss/rss.aspx?ch=69")
europaNat = Channel ("http://www.europapress.es/rss/rss.aspx?ch=66")

list = europaNat.extractFeed ()

reportDB = DAOReport ()

for i in range (0, len (list)):
    rep = Report ()

    for elem in range (0, len(list[i])):
        if (elem == 0):
            rep.setTitle (list[i][elem])
        if (elem == 1):
            rep.setLink (list[i][elem])
        if (elem == 2):
            rep.setDescription (list[i][elem])
        if (elem == 3):
            rep.setDate (strftime("%a, %d %b %Y %H:%M:%S %Z", list[i][elem]))
        if (elem == 4):
            rep.setCategory (list[i][elem])

    reportDB.insertNationalReport (rep)
