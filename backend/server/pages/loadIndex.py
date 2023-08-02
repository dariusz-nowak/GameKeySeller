def loadIndex():

    page = """
        <div class="sale-this-month">Sprzedaż aktualny miesiąc lub ostatnie 30 dni</div>       
        <div class="recently-sold">Ostatnio sprzedane (3-5) produkty</div>       
        <div class="most-popular-games">Najpopularniejsze (3-5) gry</div>       
        <div class="most-popular-pages">Najpopularniejsze (3-5) strony</div>
    """

    html = '<div class="homepage">index'


    # Sprzedaż aktualny miesiąc lub ostatnie 30 dni
    html += '<div class="sale-this-month">'
    # -----

    html += """
    
    """

    # -----
    html += "</div>"
    
    # Ostatnio sprzedane (3-5) produkty
    html += '<div class="recently-sold">'
    # -----



    # -----
    html += "</div>"
    
    # Najpopularniejsze (3-5) gry
    html += '<div class="most-popular-games">'
    # -----



    # -----
    html += "</div>"
    
    # Najpopularniejsze (3-5) strony
    html += '<div class="most-popular-pages">'
    # -----



    # -----
    html += "</div>"
    html += '</div>'
    return html

a = """
    <div class="sale-this-month">
        <div class="homepage"><div class="sale-this-month">
            <div class="data">
                <div class="days">
                    <div class="day">
                        <span class="number">1</span>
                        <span class="grapf"></span>
                        <span class="value">5</span>
                    </div>
                    <div class="day">
                        <span class="number">2</span>
                        <span class="grapf"></span>
                        <span class="value">10</span>
                    </div>
                    <div class="day">
                        <span class="number">3</span>
                        <span class="grapf"></span>
                        <span class="value">7</span>
                    </div>
                </div>
            </div>
            <!-- <h1>Sprzedaż w miesiąc</h1> -->
        </div>
    </div>
    <div class="recently-sold">

    </div>
    <div class="most-popular-games">

    </div>
    <div class="most-popular-pages">
        
    </div>
"""