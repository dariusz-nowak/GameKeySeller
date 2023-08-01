data_section = document.querySelector('.content .data')

function runPythonScript() {
    // Wywołanie skryptu Pythona na serwerze przy użyciu Fetch API
    fetch('/backend/server/server_script')
        .then(response => response.text())
        .then(result => {
            console.log(result); // Wyświetlenie wyniku działania skryptu Pythona w alert'cie
        })
        .catch(error => {
            console.error('Wystąpił błąd:', error);
        });
}

runPythonScript()

function loadPage(page) {

    runPythonScript()

    // Stworzyć dane z wykorzystanie AJAX i GET
    // Zapisać dane w pliku JSON lub zwrócić w tej postaci
    // Wczytać dane do kreatora treści strony

    // if (page == 'index') data_section.innerHTML = createHomepage()
    // else if (page == '') data_section.innerHTML = createHomepage()
}