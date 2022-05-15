import requests
from bs4 import BeautifulSoup

html_doc = requests.get('https://www.detik.com/terpopuler')


soup = BeautifulSoup(html_doc.text, 'html.parser' )

populer = soup.find(attrs={'class':'grid-row list-content'})

judul = soup.findAll(attrs={'class': 'media__title'})
print(judul)