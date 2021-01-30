# Simple API application
# Python with Flask
# By farinap5

country = [
    {"id":0,"name":"Brazil"},
    {"id":2,"name":"Germany"},
    {"id":3,"name":"Australia"}
]


from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "<h1>First Page!</h1>"

@app.route('/country/', methods=['GET'])
def api():
    return jsonify(country)

@app.route('/country/<id>', methods=['GET'])
def api_by_id(id):
    try:
        return jsonify(country[int(id)])
    except:
        return '{"error":"not found!"}'
app.run(debug=True, port=8008)
