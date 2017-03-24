import feedparser
from bs4 import BeautifulSoup

def gearpatrol(name = 'gear patrol',
        siteurl = 'http://www.gearpatrol.com',
        feedurl = 'http://feeds.feedburner.com/gearpatrol',
        limit = 10,
        tooltip = True):

    d = feedparser.parse(feedurl)
    feed = []
    for entry in d['entries']:
        title = entry['title'].encode('ascii','xmlcharrefreplace')
        link = entry['link'].encode('ascii','xmlcharrefreplace')
        published = entry['published']  # can also get published_parsed

        if tooltip is True:
            head, sep, tail = entry['summary'].partition('...')
            soup = BeautifulSoup(head, 'html.parser')
            img_src = entry['media_content'][0]['url']
            text = soup.p.text.encode('ascii','xmlcharrefreplace')
            tt = {'img_src':img_src, 'text':text}
            feed.append({'title':title, 'link':link, 'published':published, 'tooltip':tt})
        else:
            feed.append({'title':title, 'link':link, 'published':published})

    return {'name':name, 'url':siteurl, 'feed':feed[0:limit]}
