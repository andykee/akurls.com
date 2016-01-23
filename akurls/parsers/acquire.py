import feedparser

def acquire(name = 'acquire',
        siteurl = 'http://www.acquiremag.com',
        feedurl = 'http://feeds.feedburner.com/acquire',
        limit = 10,
        tooltip = True):

    d = feedparser.parse(feedurl)
    feed = []
    for entry in d['entries']:
        title = entry['title'].encode('ascii','xmlcharrefreplace')
        link = entry['link'].encode('ascii','xmlcharrefreplace')
        published = entry['published']  # can also get published_parsed

        if tooltip is True:
            text = entry['summary'].encode('ascii','xmlcharrefreplace')
            img_src = entry['media_thumbnail'][0]['url'].encode('ascii','xmlcharrefreplace')
            tt = {'img_src':img_src, 'text':text}
            feed.append({'title':title, 'link':link, 'published':published, 'tooltip':tt})
        else:
            feed.append({'title':title, 'link':link, 'published':published})

    return {'name':name, 'url':siteurl, 'feed':feed[0:limit]}
