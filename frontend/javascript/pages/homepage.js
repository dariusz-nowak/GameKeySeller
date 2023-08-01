function createHomepage() {

    let page = `
        <div class="sale-this-month">Sprzedaż aktualny miesiąc lub ostatnie 30 dni</div>       
        <div class="recently-sold">Ostatnio sprzedane (3-5) produkty</div>       
        <div class="most-popular-games">Najpopularniejsze (3-5) gry</div>       
        <div class="most-popular-pages">Najpopularniejsze (3-5) strony</div>
    `

    html = '<div class="homepage">'
    // Sprzedaż aktualny miesiąc lub ostatnie 30 dni
    html += '<div class="sale-this-month">'



    html += "</div>"
    
    // Ostatnio sprzedane (3-5) produkty
    html += '<div class="recently-sold">'



    html += "</div>"
    
    // Najpopularniejsze (3-5) gry
    html += '<div class="most-popular-games">'



    html += "</div>"
    
    // Najpopularniejsze (3-5) strony
    html += '<div class="most-popular-pages">'



    html += "</div>"
    html += '</div>'
    return html
}