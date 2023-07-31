from bs4 import BeautifulSoup
from requests import get

link = 'https://gg.deals/deals/?sort=price'

soup = BeautifulSoup(get(link).content, 'html.parser')




x = [
    {
        'title': 'a',
        'old price': 11.22,
        'current price': 1.22,
        'store': 'link',
        'status': 'none'
    },
    {
        'title': 'b',
        'old price': 11.22,
        'current price': 1.22,
        'store': 'link',
        'status': 'none'
    },
]

string = 'asdf'

if string in ['as1df', 'asqw']: print('tak')

# Sprawdzić, czy pozycje są w bazie danych
# NIE: dodać ze zmienionym statusem na new
# TAK:
    # Sprawdzić, czy pozycje mają tę samą cenę
    # NIE: zmienić status na different price
    # TAK: nic nie zmieniać
# Pozostałe z wczytanych pozycji, które nie znalazły się na liście usunąć z bazy danych i wywołać usunięcie oferty z OLX