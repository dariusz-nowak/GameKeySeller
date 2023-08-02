def redirect(data):
    url = f"{data['page']}?alert={str(data['alert']).encode('latin-1')}"
    data['self'].send_response(302)
    data['self'].send_header('Content-type', 'text/html')
    data['self'].send_header('Location', url)
    data['self'].end_headers()
