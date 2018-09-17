import feedparser
from bs4 import BeautifulSoup

def hackernews(name = 'hackernews',
        siteurl = 'http://news.ycombinator.com',
        feedurl = 'http://news.ycombinator.com/rss',
        limit = 30,
        tooltip = False):

    d = feedparser.parse(feedurl)
    feed = []
    for entry in d['entries']:
        title = entry['title']
        link = entry['link']
        published = entry['published']  # can also get published_parsed
        comments = entry['comments']

        if tooltip is True:
            #soup = BeautifulSoup(entry['summary'],'html.parser')
            #img_src = soup.img['src'].encode('ascii','xmlcharrefreplace')
            #text = soup.get_text().encode('ascii','xmlcharrefreplace')
            #tt = {'img_src':img_src, 'text':text}
            #feed.append({'title':title, 'link':link, 'published':published, 'comments':comments, 'tooltip':tt})
            pass
        else:
            feed.append({'title':title, 'link':link, 'published':published, 'comments':comments})

    return {'name':name, 'url':siteurl, 'feed':feed[0:limit]}
