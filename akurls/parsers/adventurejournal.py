import feedparser
from bs4 import BeautifulSoup

def adventurejournal(name = 'adventure journal',
        siteurl = 'http://www.adventure-journal.com',
        feedurl = 'http://feeds.feedburner.com/adventure-journal',
        limit = 10,
        tooltip = True):

    d = feedparser.parse(feedurl)
    feed = []
    for entry in d['entries']:
        title = entry['title'].encode('ascii','xmlcharrefreplace')
        link = entry['link'].encode('ascii','xmlcharrefreplace')
        published = entry['published']  # can also get published_parsed

        if tooltip is True:
            soup = BeautifulSoup(entry['summary_detail']['value'],'parser.html')
            img_src = soup.img['src'].encode('ascii','xmlcharrefreplace')
            text = soup.get_text() + '...'
            text = text.encode('ascii','xmlcharrefreplace')
            tt = {'img_src':img_src, 'text':text}
            feed.append({'title':title, 'link':link, 'published':published, 'tooltip':tt})
        else:
            feed.append({'title':title, 'link':link, 'published':published})

    return {'name':name, 'url':siteurl, 'feed':feed[0:limit]}