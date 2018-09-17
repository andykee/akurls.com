import feedparser
from bs4 import BeautifulSoup

def daringfireball(name = 'daring fireball',
        siteurl = 'http://www.daringfireball.net',
        feedurl = 'http://feeds.feedburner.com/daringfireball',
        limit = 10,
        tooltip = False):

    d = feedparser.parse(feedurl)
    feed = []
    for entry in d['entries']:
        title = entry['title']
        link = entry['link']
        published = entry['published']  # can also get published_parsed

        if tooltip is True:
            #soup = BeautifulSoup(entry['content'][0]['value'],'html.parser')
            #img_src = soup.img['src'].encode('ascii','xmlcharrefreplace')
            #content = soup.get_text()
            #head, sep, tail = content.partition('...')
            #text = head + '...'.encode('ascii','xmlcharrefreplace')
            #text = text.encode('ascii','xmlcharrefreplace')
            #tt = {'img_src':img_src, 'text':text}
            #feed.append({'title':title, 'link':link, 'published':published, 'tooltip':tt})
            pass
        else:
            feed.append({'title':title, 'link':link, 'published':published})

    return {'name':name, 'url':siteurl, 'feed':feed[0:limit]}
