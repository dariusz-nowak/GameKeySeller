from ggDealsCheckGames import checkGames
from steamGetGameInfo import getGameInfo

# == GG.DEALS ==
# gamesList = checkGames()

# == STEAM ==
# for game in gamesList: 
#   if game[4] == 'Nowa pozycja': game.extend(getGameInfo(game[0]))

gamesList = [
    ['Sherlock Holmes Chapter One', 180.45, 44.12, '/pl/redirect/5270c1a5011a226191060f204d9366c397ef625f/?utm_source=deals%2Findex', 'Brak zmian', 'opis', [1,2,3,4,5]],
    ['Sherlock Holmes Chapter One', 180.45, 44.12, '/pl/redirect/5270c1a5011a226191060f204d9366c397ef625f/?utm_source=deals%2Findex', 'Brak zmian', 'opis', [1,2,3,4,5]],
    ['Sherlock Holmes Chapter One', 180.45, 44.12, '/pl/redirect/5270c1a5011a226191060f204d9366c397ef625f/?utm_source=deals%2Findex', 'Nowa pozycja', 'opis', [1,2,3,4,5]],
    ['Sherlock Holmes Chapter One', 180.45, 44.12, '/pl/redirect/5270c1a5011a226191060f204d9366c397ef625f/?utm_source=deals%2Findex', 'Nowa pozycja', 'opis', [1,2,3,4,5]],
    ['Sherlock Holmes Chapter One', 180.45, 44.12, '/pl/redirect/5270c1a5011a226191060f204d9366c397ef625f/?utm_source=deals%2Findex', 'Wyższa cena', 'opis', [1,2,3,4,5]],
    ['Sherlock Holmes Chapter One', 180.45, 44.12, '/pl/redirect/5270c1a5011a226191060f204d9366c397ef625f/?utm_source=deals%2Findex', 'Wyższa cena', 'opis', [1,2,3,4,5]],
    ['Sherlock Holmes Chapter One', 180.45, 44.12, '/pl/redirect/5270c1a5011a226191060f204d9366c397ef625f/?utm_source=deals%2Findex', 'Niższa cena', 'opis', [1,2,3,4,5]],
    ['Sherlock Holmes Chapter One', 180.45, 44.12, '/pl/redirect/5270c1a5011a226191060f204d9366c397ef625f/?utm_source=deals%2Findex', 'Niższa cena', 'opis', [1,2,3,4,5]],
    ['Sherlock Holmes Chapter One', 180.45, 44.12, '/pl/redirect/5270c1a5011a226191060f204d9366c397ef625f/?utm_source=deals%2Findex', 'Usunięta', 'opis', [1,2,3,4,5]],
    ['Sherlock Holmes Chapter One', 180.45, 44.12, '/pl/redirect/5270c1a5011a226191060f204d9366c397ef625f/?utm_source=deals%2Findex', 'Usunięta', 'opis', [1,2,3,4,5]],
]

# == OLX ==
# stworzyć ofertę dla nowego klucza
# # pobrać dane o grze (foto + info)
# edytować cenę względem istniejących oferty
# usunąć ofertę dla usuniętego klucza

# == SKLEPY Z KLUCZAMI ==
# automatyzacja zakupów na stronach