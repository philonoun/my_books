from flask import Flask, jsonify, request
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

@app.route('/books', methods=['GET', 'POST'])
def all_books():
  response_object = {'status': 'success'}
  if request.method == 'POST':
    post_data = request.get_json()
    BOOKS.append({
      'title': post_data.get('title'),
      'author': post_data.get('author'),
      'read': post_data.get('read')
    })
    response_object['message'] = 'Book added!'
  else:
    response_object['books'] = BOOKS
  return jsonify(response_object)

@app.route('/ping', methods=['GET'])
def ping_pong():
  return jsonify('pong!')


if __name__ == '__main__':
  app.run()
