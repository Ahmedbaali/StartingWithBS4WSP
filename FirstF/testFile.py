from bs4 import BeautifulSoup as bs
import requests

url = "https://www.newegg.ca/grey-dowinx-ls-668903-chair-with-accessory/p/2T4-029X-00026?Item=9SIBC1THF56631"

result = requests.get(url)
doc = bs(result.text, "html.parser")

#print(doc.prettify())
prices = doc.find_all(text="$")
parent = prices[0].parent
strong = parent.find("strong")
print(strong.string)

#-------------------------------------------
"""with open("index.html", "r") as f:
    doc = bs(f, "html.parser")

#print(doc.prettify())

#    Ftag = doc.center
#    print(Ftag)
#    print(Ftag.string)
#    Stag = doc.title
#    Stag.string = "Title changed"
#    print(Stag)
#    print(doc)

Otags = doc.find_all("p")
for i in range(len(Otags)):
    print(Otags[i].find_all("b"))
    print("#"*10)"""