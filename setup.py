import os
from setuptools import setup

setup(
        name='akurls.com',
        version='1.0.0',
        author='Andy Kee',
        author_email='andykee@gmail.com',
        packages=['akurls'],
        install_requires=[
            'BeautifulSoup >= 4.4.1', 
            'feedparser >= 5.2.1',
            'Jinja >= 2.8',
            'MarkupSafe >= 0.23',
            'wheel >= 0.24.0',
            'praw >= 3.6.1'],
        python_requires='>=3',
        )
