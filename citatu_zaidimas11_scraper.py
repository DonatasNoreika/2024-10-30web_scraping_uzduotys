from copyreg import pickle

import requests
from bs4 import BeautifulSoup
import pickle

url = "https://quotes.toscrape.com/"

quotes = []

page = 1

while True:
    r = requests.get(f"{url}page/{page}/")
    soup = BeautifulSoup(r.text, 'html.parser')
    page += 1
    blocks = soup.find_all(class_="quote")
    if not blocks:
        break
    for block in blocks:
        quote = block.find(class_="text").get_text()
        author = block.find(class_="author").get_text()
        initials = " ".join(map(lambda zodis: f"{zodis[0]}." , author.split()))
        href = block.find(class_="author").find_next_sibling()['href']
        r_author = requests.get(f"{url}{href}")
        soup_author = BeautifulSoup(r_author.text, 'html.parser')
        born = soup_author.find(class_="author-born-location").parent.get_text()
        print(quote)
        print(author)
        print(initials)
        quote_dict = {
            "quote": quote,
            "author": author,
            "initials": initials,
            "born": born,
        }
        quotes.append(quote_dict)

with open("quotes.pkl", 'wb') as file:
    pickle.dump(quotes, file)