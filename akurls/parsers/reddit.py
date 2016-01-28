import re
import sys

import feedparser

def reddit(name,
        subreddit,
        limit = 10,
        tooltip = False):

    siteurl = 'http://www.reddit.com/r/' + subreddit
    feedurl = siteurl + '/.rss'

    feed = []

    try:
        d = feedparser.parse(feedurl)
        for entry in d['entries']:
            title = entry['title'].encode('ascii','xmlcharrefreplace')
            comments = entry['link'].encode('ascii','xmlcharrefreplace')
            ext_link = re.findall(r'href=[\'"]?([^\'" >]+)',entry['summary_detail']['value'])
            if ext_link[1]:
                link = ext_link[1].encode('ascii','xmlcharrefreplace')

            if tooltip is True:
                feed.append({'title':title, 'link':link, 'published':published, 'tooltip':tt})    
            else:
                feed.append({'title':title, 'link':link, 'comments':comments})

        return {'name':name, 'url':siteurl, 'feed':feed[0:limit]}

    except Exception as e:
        print(e)
        return {'name':name, 'url':siteurl, 'feed':feed}

