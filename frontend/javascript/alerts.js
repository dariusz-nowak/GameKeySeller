function getAlert(alert) {
    alert = JSON.parse(alert.replace(/\\n/g, '').replace('[', '{').replace(']', '}'))
    
    if (alert['code'] == '001') {
        return `
        <h1> odhujaj się </h1>
        `
    }
}