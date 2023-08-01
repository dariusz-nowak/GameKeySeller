data_section = document.querySelector('.content .data')

async function fetchData(){
    const res = await fetch("frontend/javascript/data.json");
    const json = await res.json();
    console.log(json);
}

function loadXMLDoc() {
    var xmlhttp = new XMLHttpRequest();

    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState == XMLHttpRequest.DONE) {
           if (xmlhttp.status == 200) {
               document.getElementById("myDiv").innerHTML = xmlhttp.responseText;
           }
           else if (xmlhttp.status == 400) {
              alert('There was an error 400');
           }
           else {
               alert('something else other than 200 was returned');
           }
        }
    };

    xmlhttp.open("GET", "ajax_info.txt", true);
    xmlhttp.send();
}

function loadPage(page) {

    data = {'page': page}
    $.ajax({
        type : 'GET',
        url : 'ajaxurl',
        data : data
    })

    // Stworzyć dane z wykorzystanie AJAX i GET
    // Zapisać dane w pliku JSON lub zwrócić w tej postaci
    // Wczytać dane do kreatora treści strony

    if (page == 'index') data_section.innerHTML = createHomepage()
    else if (page == '') data_section.innerHTML = createHomepage()
}

loadPage('index');