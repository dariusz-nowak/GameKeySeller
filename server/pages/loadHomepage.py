import sys, os
sys.path.append(f"{os.getcwd()}")
from backend.database.databaseActions import loadMonthSales, loadPopularSales

from datetime import datetime, timedelta

def loadHomepage():
    html = '<div class="homepage">'
    
    # Sprzedaż aktualny miesiąc lub ostatnie 30 dni
    dates = {}
    sales = loadMonthSales()
    current_date = datetime.now().date()
    for _ in range(31):
        dates[current_date.strftime('%d-%m')] = 0
        current_date -= timedelta(days=1)
        
    bestSale = 0
    monthSale = 0
    last5Sales = []
    for sale in sales:
        dates[f"{sale['day']}-{sale['month']}"] += sale['profit']
        monthSale += sale['profit']
        if len(last5Sales) < 5: last5Sales.append({'title': sale['title'], 'profit': sale['profit'], 'platform': sale['platform']})

    for date in dates: 
        if bestSale < dates[str(date)]: bestSale = dates[str(date)]

    html += f'<div class="sale-this-month window"><h1>Zysk w miesiącu: {monthSale:.2f} zł</h1><div class="days list">'
    for date in dates:
        html += """
            <div class="day">
                <span class="date">{day}.{month}</span>
                <span class="grapf" style="width: {width}"></span>
                <span class="value">{value}</span>
            </div>
        """.format(day = date[0:2], 
                   month = date[3:5], 
                   width = f"{(dates[str(date)] / bestSale) * 100}%",
                   value = f'{dates[str(date)]:.2f} zł' if dates[str(date)] > 0 else '')
    html += "</div></div>"
    
    # Ostatnio sprzedane 5 gier
    html += '<div class="last-and-popular">'
    html += '<div class="recently-sold window">'
    html += '<h1>Ostatnio sprzedane</h1>'
    html += '<div class="sales list">'
    for sale in last5Sales:
        html += """
            <div class="sale">
                <span class="title">{title}</span>
                <span class="price">{price} zł</span>
                <span class="platform">{platform}</span>
            </div>
        """.format(title = sale['title'], 
                   price = f"{sale['profit']:.2f}", 
                   platform = sale['platform'])
    html += '</div></div>'
    
    # Najpopularniejsze 5 gier
    popularTitles = loadPopularSales("title")
    html += '<div class="most-popular-games window">'
    html += '<h1>Najpopularniejsze gry</h1>'
    html += '<div class="titles list">'

    for title in popularTitles:
        html += """
            <div class="title">
                <span class="title">{title}</span>
                <span class="count">Sprzedaż: {count} szt.</span>
            </div>
        """.format(title = title['title'], 
                   count = title['count'])
    html += "</div></div>"
    
    # Najpopularniejsze 5 stron
    popularPlatforms = loadPopularSales("buy_platform")
    html += '<div class="most-popular-pages window">'
    html += '<h1>Najpopularniejsze strony</h1>'
    html += '<div class="platforms list">'
    for platform in popularPlatforms:
        html += """
            <div class="platform">
                <span class="platform">{platform}</span>
                <span class="count">Zakup: {count} szt.</span>
            </div>
        """.format(platform = platform['title'], 
                   count = platform['count'])
    html += "</div></div></div></div></div></div>"
    return html


loadHomepage()