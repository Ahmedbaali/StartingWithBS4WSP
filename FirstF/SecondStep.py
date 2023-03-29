from bs4 import BeautifulSoup as bs
import re

with open('Sindex.html', 'r') as f:
    doc = bs(f, 'html.parser')

tags = doc.find_all(text=re.compile("\$.*"))
for tag in tags:
    print(tag.strip())
tagss = list(map(lambda x: x.strip(), tags))
print(tagss)