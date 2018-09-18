import feedparser
from bs4 import BeautifulSoup

def seriouseats(name = 'seriouseats',
        siteurl = 'http://www.seriouseats.com',
        feedurl = 'http://feeds.feedburner.com/seriouseatsfeaturesvideos',
        limit = 10,
        tooltip = True):

    d = feedparser.parse(feedurl)
    feed = []
    for entry in d['entries']:
        title = entry['title'].encode('ascii','xmlcharrefreplace').decode('utf8')
        link = entry['link']
        published = entry['published']  # can also get published_parsed

        if tooltip is True:
            soup = BeautifulSoup(entry['content'][0]['value'],'html.parser')
            img_src = soup.img['src']
            content = soup.get_text()
            text = soup.get_text()
            tt = {'img_src':img_src, 'text':text}
            feed.append({'title':title, 'link':link, 'published':published, 'tooltip':tt})
        else:
            feed.append({'title':title, 'link':link, 'published':published})

    return {'name':name, 'url':siteurl, 'feed':feed[0:limit]}
