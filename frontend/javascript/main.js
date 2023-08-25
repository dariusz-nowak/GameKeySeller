data_container = document.querySelector('.content .container')

async function loadPageHTML(page) {
    try {
        const response = await fetch('/api/' + page);
        const result = await response.text();
        return result;
    } catch (error) {
        console.error('Wystąpił błąd:', error);
        return null; // lub możesz zwrócić inny odpowiedni komunikat błędu
    }
}
    
async function loadPage(page) {
    try {
        const result = await loadPageHTML(page);
        data_container.innerHTML = result
    } catch (error) {
        console.error('Wystąpił błąd:', error);
    }
}

// Sprawdzenie wystąpienia alertu
const urlParams = new URLSearchParams(window.location.search);
const alertMessage = urlParams.get('alert');
if (alertMessage) data_container.innerHTML = getAlert(alertMessage.slice(2, -1))

// Sprawdzenie polskich znaków w formularzu
function checkForm() {
    var title = document.getElementById("title").value;
    var platform = document.getElementById("platform").value;
    var polishCharactersPattern = /[ąćęłńóśźżĄĆĘŁŃÓŚŹŻ]/;

    if (polishCharactersPattern.test(title) || polishCharactersPattern.test(platform)) {
        alert("Pola zawierają polskie znaki. Proszę poprawić dane przed wysłaniem formularza.");
        return false;
    }
    return true;
}

function loadFiltersForm() {
    document.querySelector('.sales-raport form').classList.toggle('hide')
}

function loadPopularPagesFilterForm() {
    document.querySelector('.popular-pages-raport form').classList.toggle('hide')
}

function loadPopularGamesFilterForm() {
    document.querySelector('.popular-games-raport form').classList.toggle('hide')
}

function loadAdvertsFilterForm() {
    document.querySelector('.adverts-raport form').classList.toggle('hide')
}
function loadAdvertsFilterForm() {
    
}

function tableExporter() {
    const table = document.querySelector('table.list')
    const tableRows = table.querySelectorAll('tbody tr')
    const tableHeaderRow = table.querySelector('thead tr')

    let data = []
    let footerData = []
    let tableColumnHeaders = []

    tableHeaderRow.querySelectorAll('th').forEach(headerCell => {
        tableColumnHeaders.push(headerCell.innerText)
    })

    if (table.querySelector('tfoot tr')) {
        const tableFooterRow = table.querySelector('tfoot tr')
        tableFooterRow.querySelectorAll('td').forEach(cell => {
            footerData.push(cell.innerText);
        });
    } else tableFooterRow = ""

    tableRows.forEach(row => {
        const rowData = []
        row.querySelectorAll('td').forEach(cell => {
            rowData.push(cell.innerText)
        })
        data.push(rowData);
    });

    const doc = new jspdf.jsPDF({
        orientation: 'l'
    })
    
    header = document.querySelector('.window h1').innerText + " "
    if (document.querySelector('.window input#from-date').value + " - ") {
        fromDate = document.querySelector('.window input#from-date').value + " - "
    } else fromDate = "nieokreślono" + " - "
    if (document.querySelector('.window input#to-date').value) {
        toDate = document.querySelector('.window input#to-date').value
    } else toDate = "nieokreślono"

    doc.autoTable({
        head: [tableColumnHeaders],
        body: data,
        startY: 22,
        headStyles: { fillColor: [100, 100, 100] },
        foot: [footerData],
        footStyles: { fillColor: [200, 200, 200] },
        styles: {
            font: "roboto",
            fontSize: 8,
            halign: 'center'
        },
        didDrawPage: function(data) {
            function centerTextOnPage(doc, text, yPosition) {
                const textWidth = doc.getStringUnitWidth(text) * doc.internal.getFontSize() / doc.internal.scaleFactor
                const pageWidth = doc.internal.pageSize.width
                const centerX = (pageWidth - textWidth) / 2
                doc.text(text, centerX, yPosition)
            }
            
            doc.setFont("roboto");
            doc.setFontSize(12)
            doc.setTextColor(100)
            
            centerTextOnPage(doc, header, 10)
            centerTextOnPage(doc, fromDate + toDate, 16)
        }
    })

    doc.save(header + fromDate + toDate + '.pdf');
}
// loadPage('index')