from flask import Flask, request, jsonify
from flask import Response

app = Flask(__name__)

# Завдання 2: Простий GET-запит
@app.route("/")
def hello_world():
    return "Hello, World!"

# Завдання 3: GET-запит зі шляхом і параметром
@app.route("/currency")
def get_currency():
    today = request.args.get('today')
    if today:
        return "USD - 41.5"
    return "Invalid request. Use ?today parameter."

# Завдання 4: Обробка заголовків запиту
@app.route("/header-check")
def header_check():
    content_type = request.headers.get('Content-Type')
    if content_type == "application/json":
        return jsonify({"currency": "USD", "value": 41.5})
    elif content_type == "application/xml":
        return Response("<currency><name>USD</name><value>41.5</value></currency>", mimetype="application/xml")
    else:
        return "Plain text response: USD - 41.5"

if __name__ == '__main__':
    app.run(port=8000)
