#!/bin/bash

cd akurls
mkdir tmp
cp akurls.py tmp
cp config.py tmp
cp -r parsers tmp
cp -r theme tmp
cp -r $VIRTUAL_ENV/lib/python2.7/site-packages/bs4 tmp
cp -r $VIRTUAL_ENV/lib/python2.7/site-packages/feedparser.py tmp
cp -r $VIRTUAL_ENV/lib/python2.7/site-packages/jinja2 tmp
cp -r $VIRTUAL_ENV/lib/python2.7/site-packages/markupsafe tmp
cp -r $VIRTUAL_ENV/lib/python2.7/site-packages/wheel tmp
cp -r $VIRTUAL_ENV/lib/python2.7/site-packages/praw tmp 
cp -r $VIRTUAL_ENV/lib/python2.7/site-packages/requests tmp
cp -r $VIRTUAL_ENV/lib/python2.7/site-packages/update_checker.py tmp
cp -r $VIRTUAL_ENV/lib/python2.7/site-packages/decorator.py tmp


find tmp -name "*.pyc" -delete

cd tmp

zip -qr ../../akurls.zip *

cd ..

rm -r tmp

