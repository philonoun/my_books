from flask import Flask, jsonify
from flask_cors import CORS

DEBUG = True

BOOKS = [
  {
    'title': 'From Darwin to Design',
    'author': 'Dr. C. L. Cagan with Robert Hymers',
    'read': False
  },
  {
    'title': 'Start-up Nation',
    'author': 'Dan Senor and Saul Singer',
    'read': False
  },
  {
    'title': 'Steve Jobs',
    'author': 'Walter Isaacson',
    'read': True
  },
]

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/books', methods=['GET'])
def all_books():
  return jsonify({
    'status': 'success',
    'books': BOOKS
  })

@app.route('/ping', methods=['GET'])
def ping_pong():
  return jsonify('pong!')


if __name__ == '__main__':
  app.run()
