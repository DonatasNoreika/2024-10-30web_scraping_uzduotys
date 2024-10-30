import requests
from bs4 import BeautifulSoup
from random import randint

url = "https://quotes.toscrape.com/"

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

number = randint(1, 10)
block = soup.find_all(class_="quote")[number]

quote = block.find(class_="text").get_text()
author = block.find(class_="author").get_text()
print(quote)
spejimas = input("Kas yra šios citatos autorius?")
if author == spejimas:
    print("Teisingai!")
else:
    print(f"Autoriaus inicialai: {" ".join(map(lambda zodis: f"{zodis[0]}." , author.split()))}")
    spejimas = input("Kas yra šios citatos autorius?")
    if author == spejimas:
        print("Teisingai!")
    else:
        href = block.find(class_="author").find_next_sibling()['href']
        r_author = requests.get(f"{url}{href}")
        soup_author = BeautifulSoup(r_author.text, 'html.parser')
        print(soup_author.find(class_="author-born-location").parent.get_text())
        spejimas = input("Kas yra šios citatos autorius?")
        if author == spejimas:
            print("Teisingai!")
        else:
            print(f"Neatspėjote, citatos autorius - {author}")
