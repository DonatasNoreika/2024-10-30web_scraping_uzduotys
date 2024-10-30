from random import choice
import pickle

with open('quotes.pkl', 'rb') as file:
    quotes = pickle.load(file)

url = "https://quotes.toscrape.com/"

quote = choice(quotes)
print(quote['quote'])
spejimas = input("Kas yra šios citatos autorius?")
if quote['author'] == spejimas:
    print("Teisingai!")
else:
    print(quote['initials'])
    spejimas = input("Kas yra šios citatos autorius?")
    if quote['author'] == spejimas:
        print("Teisingai!")
    else:
        print(quote['born'])
        spejimas = input("Kas yra šios citatos autorius?")
        if quote['author'] == spejimas:
            print("Teisingai!")
        else:
            print(f"Neatspėjote, citatos autorius - {quote['author']}")
