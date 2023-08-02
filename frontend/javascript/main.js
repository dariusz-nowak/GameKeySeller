data_container = document.querySelector('.content .container')

document.querySelectorAll('.prevent-default').forEach(e => e.preventDefault());

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

// loadPage('index')