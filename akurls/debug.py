from __future__ import print_function

import socket

from jinja2 import Environment, FileSystemLoader

from config import *
import parsers

env = Environment(loader=FileSystemLoader('theme/templates'))
template = env.get_template('base.html')
    
content = {
        'gearpatrol' : parsers.gearpatrol(),
        'uncrate' : parsers.uncrate(),
        'acquire' : parsers.acquire(),
        'hackernews' : parsers.hackernews(),
        'proggit' : parsers.reddit('proggit','programming'),
        'daringfireball' : parsers.daringfireball(),
        'eaterla' : parsers.eaterla(),
        'adventurejournal' : parsers.adventurejournal(),
        'pinkbike' : parsers.pinkbike(),
        'mgoblog' : parsers.mgoblog()
}

html = template.render(content)
print(html)
