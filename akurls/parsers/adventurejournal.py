import feedparser
from bs4 import BeautifulSoup

def adventurejournal(name = 'adventure journal',
        siteurl = 'http://www.adventure-journal.com',
        feedurl = 'http://feeds.feedburner.com/adventure-journal',
        limit = 10,
        tooltip = False):

    d = feedparser.parse(feedurl)
    feed = []
    for entry in d['entries']:
        title = entry['title'].encode('ascii','xmlcharrefreplace').decode('utf8')
        link = entry['link']
        published = entry['published']  # can also get published_parsed

        if tooltip is True:
            soup = BeautifulSoup(entry['summary_detail']['value'],'html.parser')
            img_src = soup.img['src']
            text = soup.get_text() + '...'
            tt = {'img_src':img_src, 'text':text}
            feed.append({'title':title, 'link':link, 'published':published, 'tooltip':tt})
        else:
            feed.append({'title':title, 'link':link, 'published':published})

    return {'name':name, 'url':siteurl, 'feed':feed[0:limit]}
