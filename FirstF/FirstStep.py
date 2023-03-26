from bs4 import BeautifulSoup as bs
import requests

url = "https://technostationery.com/stylo-a-bille-focus-1-0-mm-techno.html"

result = requests.get(url)
doc = bs(result.text, "html.parser")

#print(doc.prettify())
prices = doc.find_all(text="DZD")
print(len(prices))

#-----------------------------------------------
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