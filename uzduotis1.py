import requests
from bs4 import BeautifulSoup
from random import shuffle

html = requests.get('http://delfi.lt').text
soup = BeautifulSoup(html, 'html.parser')

bad_words = ['COVID', 'mirt', 'NVSC', 'skiep', 'kar', "Ukrain"]

blocks = soup.find_all("article")
first_parts = []
second_parts = []

for block in blocks:
    try:
        title = block.find(class_="headline-title").a.get_text().strip()
        if ":" in title:
            if not any(word in title for word in bad_words):
                first_parts.append(title.split(":")[0])
                second_parts.append(title.split(":")[1])
    except: pass

shuffle(second_parts)

for i in range(len(first_parts)):
    print(f"{i+1}. {first_parts[i]}:{second_parts[i]}")