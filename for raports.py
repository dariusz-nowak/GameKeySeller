from xlsxwriter import Workbook 

def createXLSXfile(games):
    workbook = Workbook('docs/Games to check.xlsx')
    allGamesWorksheet = workbook.add_worksheet('Wszystkie')
    newGamesWorksheet = workbook.add_worksheet('Nowe pozycje')
    higherPriceGamesWorksheet = workbook.add_worksheet('Droższe')
    lowerPriceGamesWorksheet = workbook.add_worksheet('Tańsze')
    deletedGamesWorksheet = workbook.add_worksheet('Usunięte')
    allGamesRow, newGamesRow, higherPriceGamesRow, lowerPriceGamesRow, deletedGamesRow, col = 1, 1, 1, 1, 1, 0

    worksheets = [
        [allGamesWorksheet, allGamesRow],
        [newGamesWorksheet, newGamesRow],
        [higherPriceGamesWorksheet, higherPriceGamesRow],
        [lowerPriceGamesWorksheet, lowerPriceGamesRow],
        [deletedGamesWorksheet, deletedGamesRow],
    ]

    def saveGameDataInWorksheet(worksheet):
        worksheet[0].write(worksheet[1], col,     title)
        worksheet[0].write(worksheet[1], col + 1, oldPrice)
        worksheet[0].write(worksheet[1], col + 2, newPrice)
        worksheet[0].write(worksheet[1], col + 3, shopLink)
        worksheet[0].write(worksheet[1], col + 4, status)
        worksheet[1] += 1

    def fitWorksheetAndCreateTable(worksheet):
        worksheet[0].autofit()
        worksheet[0].add_table(f'A1:D{worksheet[1]}',
            {
                'style': 'Table Style Light 1',
                'columns': [
                    {'header':'Nazwa gry'},
                    {'header':'Stara cena'},
                    {'header':'Nowa cena'},
                    {'header':'Link'},
                ],
            })

    for title, oldPrice, newPrice, shopLink, status in games:
        saveGameDataInWorksheet(worksheets[0])
        if status == 'Nowa pozycja': saveGameDataInWorksheet(worksheets[1])
        elif status == 'Wyższa cena': saveGameDataInWorksheet(worksheets[2])
        elif status == 'Niższa cena': saveGameDataInWorksheet(worksheets[3])
        elif status == 'Usunięta': saveGameDataInWorksheet(worksheets[4])

    for worksheet in worksheets: 
        if worksheet[1] > 1: fitWorksheetAndCreateTable(worksheet)

    workbook.close()