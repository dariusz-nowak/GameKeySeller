import sys, os
sys.path.append(f"{os.getcwd()}")
from backend.database.databaseActions import loadMonthSales, loadPopularSales

from calendar import monthrange
from datetime import datetime

def daysInMonthCounter(year, month):
    return monthrange(year, month)[1]

def loadIndex():
    html = '<div class="homepage">'

    sales = loadMonthSales()

    # Sprzedaż aktualny miesiąc lub ostatnie 30 dni
    days = {}
    currentDay = datetime.now().day
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    for key, _ in enumerate(range(daysInMonthCounter(currentYear, currentMonth))): days[f'{key + 1}'] = 0

    bestSale = 0
    monthSale = 0
    last5Sales = []
    for sale in sales:
        days[str(sale['day'])] += sale['sell price']
        monthSale += sale['sell price']
        if len(last5Sales) < 5: last5Sales.append({'title': sale['title'], 'sell price': sale['sell price'], 'platform': sale['platform']})

    for day in days: 
        if bestSale < days[str(day)]: bestSale = days[str(day)]
        
    html += f'<div class="sale-this-month"><h1>Sprzedaż w miesiącu: {monthSale:.2f} zł</h1><div class="days">'
    for day in days:
        html += """
            <div class="day">
                <span class="date">{}.{}</span>
                <span class="grapf" style="width: {}px{}"></span>
                <span class="value">{}</span>
            </div>
        """.format(day if len(str(day)) == 2 else f"0{day}", 
                   day if len(str(currentMonth)) == 2 else f"0{currentMonth}", 
                   (days[str(day)] / bestSale) * 600, 
                   '; background-color: darkolivegreen' if int(currentDay) == int(day) else '', 
                   f'{days[str(day)]:.2f} zł' if days[str(day)] > 0 else '')
    html += "</div></div>"
    
    # Ostatnio sprzedane (3-5) produkty
    html += '<div class="last-and-popular">'
    html += '<div class="recently-sold">'
    html += '<h1>5 ostatnich sprzedaży</h1>'
    html += '<div class="sales">'
    for sale in last5Sales:
        html += """
            <div class="sale">
                <span class="title">{}</span>
                <span class="price">{} zł</span>
                <span class="platform">{}</span>
            </div>
        """.format(sale['title'], 
                   f"{sale['sell price']:.2f}", 
                   sale['platform'])
    html += '</div></div>'
    
    # Najpopularniejsze (3-5) gry
    popularTitles = loadPopularSales("title")
    html += '<div class="most-popular-games">'
    html += '<h1>Najpopularniejsze gry</h1>'
    html += '<div class="titles">'

    for title in popularTitles:
        html += """
            <div class="title">
                <span class="title">{}</span>
                <span class="count">Sprzedaż: {} szt.</span>
            </div>
        """.format(title['title'], 
                   title['count'])
    html += "</div></div>"
    
    # Najpopularniejsze (3-5) strony
    popularPlatforms = loadPopularSales("platform")
    html += '<div class="most-popular-pages">'
    html += '<h1>Najpopularniejsze strony</h1>'
    html += '<div class="platforms">'
    for platform in popularPlatforms:
        html += """
            <div class="platform">
                <span class="platform">{}</span>
                <span class="count">Zakup: {} szt.</span>
            </div>
        """.format(platform['title'], 
                   platform['count'])
    html += "</div></div>"
    html += "</div></div></div></div>"
    return html