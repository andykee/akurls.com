#!/bin/bash

cd akurls
mkdir tmp
cp akurls.py tmp
cp config.py tmp
cp -r parsers tmp
cp -r theme tmp
cp -r $VIRTUAL_ENV/lib/python2.7/site-packages/. tmp

rm -r tmp/*.dist-info
rm -r tmp/_*
rm -r tmp/easy_install.*
rm -r tmp/pip
rm -r tmp/pkg_resources
rm -r tmp/setuptools

find tmp -name "*.pyc" -delete

cd tmp

zip -qr ../../akurls.zip *

cd ..

rm -r tmp

