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
rm -r tmp/pyasn1
rm -r tmp/rsa
rm -r tmp/jmespath
rm -r tmp/six
rm -r tmp/python-dateutil
rm -r tmp/docutils
rm -r tmp/botocore
rm -r tmp/colorama
rm -r tmp/awscli

find tmp -name "*.pyc" -delete

cd tmp

zip -qr ../../akurls.zip *

cd ..

rm -r tmp

