import feedparser

def eaterla(name = 'eater la',
        siteurl = 'http://www.la.eater.com',
        feedurl = 'http://www.la.eater.com/rss/index.xml',
        limit = 10,
        tooltip = False):

    d = feedparser.parse(feedurl)
    feed = []
    
    for entry in d['entries']:
        title = entry['title'].encode('ascii','xmlcharrefreplace')
        link = entry['link'].encode('ascii','xmlcharrefreplace')
        published = entry['published'].encode('ascii','xmlcharrefreplace')
    
        if tooltip is True:
            feed.append({'title':title, 'link':link, 'published':published, 'tooltip':tt})    
        else:
            feed.append({'title':title, 'link':link, 'published':published})

    return {'name':name, 'url':siteurl, 'feed':feed[0:limit]}
