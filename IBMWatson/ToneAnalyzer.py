import json
from watson_developer_cloud import ToneAnalyzerV3
import urllib
from bs4 import BeautifulSoup

url = "http://seekingalpha.com/news/3223984-j-and-j-arthritis-drug-mixed-results-incumbents"
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

print(json.dumps(tone_analyzer.tone(text.encode('utf-8')), indent=2))