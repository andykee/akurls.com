import os
from setuptools import setup

setup(
        name='akurls.com',
        version='1.0.0',
        author='Andy Kee',
        author_email='andykee@gmail.com',
        packages=['akurls'],
        package_data={'akurls': ['parsers/*','theme/*']},
        install_requires=[
            'BeautifulSoup4 >= 4.4.1', 
            'feedparser >= 5.2.1',
            'Jinja2 >= 2.8',
            'MarkupSafe >= 0.23',
            'wheel >= 0.24.0',
            'praw >= 3.6.1',
            'boto3'],
        python_requires='>=3',
        )
