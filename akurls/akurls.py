from __future__ import print_function

import socket
import boto3

from jinja2 import Environment, FileSystemLoader

from config import *
import parsers

def app(event,context):

    # Set global socket timeout
    socket.setdefaulttimeout(TIMEOUT)
    
    env = Environment(loader=FileSystemLoader('theme/templates'))
    template = env.get_template('base.html')
    
    content = {
        'gearpatrol' : parsers.gearpatrol(),
        'uncrate' : parsers.uncrate(),
        'acquire' : parsers.acquire(),
        'hackernews' : parsers.hackernews(),
        'reddit' : parsers.reddit('reddit','all',lim=30),
        'proggit' : parsers.reddit('proggit','programming'),
        'daringfireball' : parsers.daringfireball(),
        'eaterla' : parsers.eaterla(),
        'adventurejournal' : parsers.adventurejournal(),
        'pinkbike' : parsers.pinkbike(),
        'mgoblog' : parsers.mgoblog()
    }

    html = template.render(content)
    
    s3 = boto3.resource('s3')
    s3.Object(S3_BUCKET, 'index.html').put(Body=html,
                                           ACL='public-read',
                                           ContentType='text/html')


    return 'Donezo!'


