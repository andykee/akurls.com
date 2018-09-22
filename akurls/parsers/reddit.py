import praw

def reddit(name,
        subreddit,
        lim = 10,
        tooltip = False):

    siteurl = 'http://www.reddit.com/r/' + subreddit

    feed = []
    r = praw.Reddit(client_id='G6UdDupuaiTG6A',
            client_secret='dLgMd9CImHUKr43qC1WLHj22zDo',
            user_agent='akurls')
    s = r.subreddit(subreddit)
    for submission in s.hot(limit = lim):
        title = submission.title.encode('ascii','xmlcharrefreplace').decode('utf8')
        link = submission.url
        comments = 'http://reddit.com' + submission.permalink
        feed.append({'title':title, 'link':link, 'comments':comments})

    return {'name':name, 'url':siteurl, 'feed':feed[0:lim]}
