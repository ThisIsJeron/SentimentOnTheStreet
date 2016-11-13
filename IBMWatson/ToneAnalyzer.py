import json
from watson_developer_cloud import ToneAnalyzerV3
import urllib
from bs4 import BeautifulSoup
from operator import itemgetter

url = "http://seekingalpha.com/news/3223481-downdraft-hits-tech-post-election"
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

tone_analyzer = ToneAnalyzerV3(
   username='1b6c7837-9fd0-40b5-b4e4-86963d2dba61',
   password='4CVOwMTL1JIq',
   version='2016-05-19 ')

with open('aapl5.json', 'w') as outfile:
    json.dump(tone_analyzer.tone(text.encode('utf-8')), outfile)

with open('aapl5.json') as f:
    items = json.load(f)
    #print items
    banana = max(items["document_tone"]["tone_categories"][0]["tones"], key=lambda ev: ev["score"])
    print banana
    print banana["tone_name"]
    print banana["score"]
