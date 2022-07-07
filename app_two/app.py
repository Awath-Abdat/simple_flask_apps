from flask import Flask, redirect, url_for, request
import os

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
  return '<!doctype html> <html> <head> <title>Awath Hello, World</title> </head> <body> Welcome %s </body> </html>' % name

@app.route('/login', methods = ['POST', 'GET'])
def login():
  if request.method == 'POST':
    user = request.form['nm']
    return redirect(url_for('success', name = user))
  else:
    user = request.args.get('nm')
    return redirect(url_for('success', name = user))

@app.route('/', methods = ['POST', 'GET'])
def index():
  return '<!doctype html> <html> <head> <title>Awath\' Login App</title> </head> <body> <form action=\"/login\" method=\"GET\"> <p>Input your name below</p> <input type=\"text\" name=\"nm\" placeholder=\"Name\" /> <input type=\"submit\" value=\"Login\" /> </form> </body> </html>'

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(debug=False, host='0.0.0.0', port=port)