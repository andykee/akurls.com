import feedparser
from bs4 import BeautifulSoup

def mgoblog(name = 'mgoblog',
        siteurl = 'http://www.mgoblog.com',
        feedurl = 'http://feeds.feedburner.com/mgoblog',
        limit = 10,
        tooltip = False):

    d = feedparser.parse(feedurl)
    feed = []
    for entry in d['entries']:
        title = entry['title'].encode('ascii','xmlcharrefreplace')
        link = entry['link'].encode('ascii','xmlcharrefreplace')
        published = entry['published']  # can also get published_parsed

        if tooltip is True:
            pass
            #soup = BeautifulSoup(entry['content'][0]['value'],'parser.html')
            #img_src = soup.img['src'].encode('ascii','xmlcharrefreplace')
            #content = soup.get_text()
            #head, sep, tail = content.partition('...')
            #text = head + '...'.encode('ascii','xmlcharrefreplace')
            #text = text.encode('ascii','xmlcharrefreplace')
            #tt = {'img_src':img_src, 'text':text}
            #feed.append({'title':title, 'link':link, 'published':published, 'tooltip':tt})
        else:
            feed.append({'title':title, 'link':link, 'published':published})

    return {'name':name, 'url':siteurl, 'feed':feed[0:limit]}
