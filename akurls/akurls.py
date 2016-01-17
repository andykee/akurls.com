from __future__ import print_function

from jinja2 import Environment, FileSystemLoader

from config import *
import parsers

env = Environment(loader=FileSystemLoader('theme/templates'))
template = env.get_template('base.html')




gp = parsers.gearpatrol()

print(gp)
