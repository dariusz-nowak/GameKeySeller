from getInformation.ggDeals.ggDealsCheckGames import checkGames
from getInformation.steam.steamGetGameInfo import getGameInfo

# == GG.DEALS ==
# gamesList = checkGames()

# == STEAM ==
# for game in gamesList: 
#   if game[4] == 'Nowa pozycja': game.extend(getGameInfo(game[0]))

gamesList = [
    ['Sherlock Holmes Chapter One', 181.01, 44.26, '/pl/redirect/5270c1a5011a226191060f204d9366c397ef625f/?utm_source=deals%2Findex', 'Brak zmian', 'Opis produktu', [1,2,3,4,5]], 
    ['LEGO Star Wars: The Skywalker Saga', 206.13, 61.65, '/pl/redirect/b546b263ccb10776783f5734ce2babc3c2063091/?utm_source=deals%2Findex', 'Brak zmian', 'Opis produktu', [1,2,3,4,5]], 
    ["Marvel's Midnight Suns", 249.0, 85.66, '/pl/redirect/238b63541ffffb2cf46fecc62001159f2cc1a57a/?utm_source=deals%2Findex', 'Nowa pozycja', 'Opis produktu', [1,2,3,4,5]], 
    ['Heavenly Bodies', 74.74, 37.35, '/pl/redirect/d6057d3b12a1d0df34488eaeabe80c89383d26b5/?utm_source=deals%2Findex', 'Nowa pozycja', 'Opis produktu', [1,2,3,4,5]], 
    ['Sherlock Holmes The Awakened', 160.89, 88.47, '/pl/redirect/7ca3a810e7bec97b0dad242d3568ea665f5cab23/?utm_source=deals%2Findex', 'Wyższa cena', 'Opis produktu', [1,2,3,4,5]]
    ['Sherlock Holmes Chapter One', 181.01, 44.26, '/pl/redirect/5270c1a5011a226191060f204d9366c397ef625f/?utm_source=deals%2Findex', 'Wyższa cena', 'Opis produktu', [1,2,3,4,5]], 
    ['LEGO Star Wars: The Skywalker Saga', 206.13, 61.65, '/pl/redirect/b546b263ccb10776783f5734ce2babc3c2063091/?utm_source=deals%2Findex', 'Niższa cena', 'Opis produktu', [1,2,3,4,5]], 
    ["Marvel's Midnight Suns", 249.0, 85.66, '/pl/redirect/238b63541ffffb2cf46fecc62001159f2cc1a57a/?utm_source=deals%2Findex', 'Niższa cena', 'Opis produktu', [1,2,3,4,5]], 
    ['Heavenly Bodies', 74.74, 37.35, '/pl/redirect/d6057d3b12a1d0df34488eaeabe80c89383d26b5/?utm_source=deals%2Findex', 'Usunięta', 'Opis produktu', [1,2,3,4,5]], 
    ['Sherlock Holmes The Awakened', 160.89, 88.47, '/pl/redirect/7ca3a810e7bec97b0dad242d3568ea665f5cab23/?utm_source=deals%2Findex', 'Usunięta', 'Opis produktu', [1,2,3,4,5]]
]



# == OLX ==
# stworzyć ofertę dla nowego klucza
# # pobrać dane o grze (foto + info)
# edytować cenę względem istniejących oferty
# usunąć ofertę dla usuniętego klucza

# == SKLEPY Z KLUCZAMI ==
# automatyzacja zakupów na stronach