
# Import section.
from RSS.Channel import Channel

europaTech = Channel ("http://www.europapress.es/rss/rss.aspx?ch=445")
list = europaTech.extractFeed ()

for i in range (0,len(list)):
    print (list[i][0])
