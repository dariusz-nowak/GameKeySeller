import sys, os
sys.path.append(f"{os.getcwd()}")
from backend.database.databaseActions import loadMonthSales

from calendar import monthrange
from datetime import datetime

def daysInMonthCounter(year, month):
    return monthrange(year, month)[1]

def loadIndex():

    page = """
        <div class="sale-this-month">Sprzedaż aktualny miesiąc lub ostatnie 30 dni</div>       
        <div class="recently-sold">Ostatnio sprzedane (3-5) produkty</div>       
        <div class="most-popular-games">Najpopularniejsze (3-5) gry</div>       
        <div class="most-popular-pages">Najpopularniejsze (3-5) strony</div>
    """

    html = '<div class="homepage">'

    # Sprzedaż aktualny miesiąc lub ostatnie 30 dni
    days = {}
    currentMonth = datetime.now().month
    currentYear = datetime.now().year
    for key, _ in enumerate(range(daysInMonthCounter(currentYear, currentMonth))): days[f'{key + 1}'] = 0

    bestSale = 0
    monthSale = 0
    sales = loadMonthSales()
    for sale in sales: 
        days[str(sale['day'])] += sale['sell price']
        monthSale += sale['sell price']
        if bestSale < sale['sell price']: bestSale = sale['sell price']
        
    html += f'<div class="sale-this-month"><h1>Sprzedaż w miesiącu: {monthSale} zł</h1><div class="days">'
    for day in days:
        html += """
            <div class="day">
                <span class="date">{}.{}</span>
                <span class="grapf" style="width: {}px"></span>
                <span class="value">{}</span>
            </div>
        """.format(day, currentMonth, (days[str(day)] / bestSale) * 100, f'{days[str(day)]} zł' if days[str(day)] > 0 else '')
    html += "</div></div>"
    
    # Ostatnio sprzedane (3-5) produkty
    html += '<div class="recently-sold">'
    # -----------------------------------------------------------------

    # KOD...

    # -----------------------------------------------------------------
    html += "</div>"
    
    # Najpopularniejsze (3-5) gry
    html += '<div class="most-popular-games">'
    # -----------------------------------------------------------------

    # KOD...

    # -----------------------------------------------------------------
    html += "</div>"
    
    # Najpopularniejsze (3-5) strony
    html += '<div class="most-popular-pages">'
    # -----------------------------------------------------------------

    # KOD...

    # -----------------------------------------------------------------
    html += "</div>"
    html += '</div>'
    return html