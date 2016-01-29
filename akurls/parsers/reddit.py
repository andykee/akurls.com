import praw

def reddit(name,
        subreddit,
        lim = 10,
        tooltip = False):

    siteurl = 'http://www.reddit.com/r/' + subreddit

    feed = []
    r = praw.Reddit(user_agent = 'akurls.com')
    s = r.get_subreddit(subreddit)
    for submission in s.get_hot(limit = lim):
        title = submission.title.encode('ascii','xmlcharrefreplace')
        link = submission.url.encode('ascii','xmlcharrefreplace')
        comments = submission.permalink.encode('ascii','xmlcharrefreplace')
        feed.append({'title':title, 'link':link, 'comments':comments})

    return {'name':name, 'url':siteurl, 'feed':feed[0:lim]}
