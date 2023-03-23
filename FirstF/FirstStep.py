from bs4 import BeautifulSoup as bs
import requests

url = "https://www.decathlon.com.dz/chaussures-randonnee-trek-homme/308131-53866-chaussures-de-randonnee-nh100-homme.html#/177-demodelsize-27239/11217-demodelcolor-8554624"

result = requests.get(url)
doc = bs(result.text, "html.parser")

#print(doc.prettify())
prices = doc.find_all(text="dzd")
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