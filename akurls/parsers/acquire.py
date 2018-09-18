import feedparser

def acquire(name = 'acquire',
        siteurl = 'http://www.acquiremag.com',
        feedurl = 'http://feeds.feedburner.com/acquire',
        limit = 10,
        tooltip = True):

    d = feedparser.parse(feedurl)
    feed = []
    for entry in d['entries']:
        title = entry['title'].encode('ascii','xmlcharrefreplace').decode('utf8')
        link = entry['link']
        published = entry['published']  # can also get published_parsed

        if tooltip is True:
            text = entry['summary']
            img_src = entry['media_thumbnail'][0]['url']
            tt = {'img_src':img_src, 'text':text}
            feed.append({'title':title, 'link':link, 'published':published, 'tooltip':tt})
        else:
            feed.append({'title':title, 'link':link, 'published':published})

    return {'name':name, 'url':siteurl, 'feed':feed[0:limit]}
