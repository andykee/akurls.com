def _parser(name = 'display name',
        siteurl = 'http://www.url.com',
        feedurl = 'http://www.url.com/feed',
        limit = 10,
        tooltip = True):

    feed = []

    if tooltip is True:
        feed.append({'title':title, 'link':link, 'published':published, 'tooltip':tt})    
    else:
        feed.append({'title':title, 'link':link, 'published':published})

    return {'name':name, 'url':siteurl, 'feed':feed[0:limit]}
