function getAlert(alert) {
    alert = JSON.parse(alert.replace(/\\n/g, '').replace('[', '{').replace(']', '}'))
    
    if (alert['name'] == 'add sale') {
        return `
        <h1> odhujaj się </h1>
        `
    }
    if (alert['name'] == 'add platform') {
        return `
        <h1> odhujaj się 2 </h1>
        `
    }
}