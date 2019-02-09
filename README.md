# akurls.com
akurls is a link aggregator that is specifically designed to cut down on the consumption of web content. You are forced to choose between seeing the most recent 10 or 30 articles from a site. Once it't no longer in the top 10 (or 30), it's gone. akurls runs on AWS Lambda and S3

1. Make sure Python 3.x is installed:

   which python3
   
2. Install pip3:

   sudo apt-get update
   sudo apt-get install pip3
   
3. Install akurls.com

   pip install git+http://github.com/andykee/akurls.com --user

4. Copy over .aws/credentials

5. Set up a cronjob by running crontab -e in the terminal
