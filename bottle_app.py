from bottle import route, run, request, response

# Завдання 2: Простий GET-запит
@route("/")
def hello():
    return "Hello, World!"

# Завдання 3: GET-запит зі шляхом і параметром
@route("/currency")
def get_currency():
    today = request.query.today
    if today:
        return "USD - 41.5"
    return "Invalid request. Use ?today parameter."

# Завдання 4: Обробка заголовків запиту
@route("/header-check")
def header_check():
    content_type = request.get_header('Content-Type')
    if content_type == "application/json":
        response.content_type = "application/json"
        return {"currency": "USD", "value": 41.5}
    elif content_type == "application/xml":
        response.content_type = "application/xml"
        return "<currency><name>USD</name><value>41.5</value></currency>"
    else:
        return "Plain text response: USD - 41.5"

if __name__ == '__main__':
    run(host='localhost', port=8000)

