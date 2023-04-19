from bs4 import BeautifulSoup as bs
import requests

url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = bs(result, "html.parser")

print(doc.prettify())