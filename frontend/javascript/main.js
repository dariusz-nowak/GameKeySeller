
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