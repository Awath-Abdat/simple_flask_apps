from flask import Flask
import os

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def hello_world():
  return '<!doctype html> <html> <head> <title>Awath Hello, World</title> </head> <body> Hello World </body> </html>'

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(debug=False, host='0.0.0.0', port=port)