from bs4 import BeautifulSoup as bs
import re

with open('Sindex.html', 'r') as f:
    doc = bs(f, 'html.parser')

tags = doc.find_all(text=re.compile("\$.*"))
for tag in tags:
    print(tag.strip())
tagss = list(map(lambda x: x.strip(), tags))
print(tagss)

# saving a new html file

tags2 = doc.find_all("input", type="text", limit=2)
for t in tags2:
    t['placeholder'] = "it is changed!!"

with open("changed.html", "w") as file:
    file.write(str(doc))
print("done!!!!!!")