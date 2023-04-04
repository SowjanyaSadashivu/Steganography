from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from database import add_user, engine
from flask_login import logout_user
import re
import os
#from hashlib import md5
from sqlalchemy import text
#from database import load_values_from_db
#import above if we are using any function in the page

UPLOAD_FOLDER = ('static/uploads')
# # Define allowed files
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg'}

app = Flask(__name__)


@app.route('/')  #empty router refers to home page
def home():
  return render_template('home.html')


@app.route('/register/', methods=['GET', 'POST'])
def register():
  msg = ''
  if request.method == 'POST' and 'name' in request.form and 'username' in request.form and 'password' in request.form and 'email' in request.form and 'con_password' in request.form:
    #data = request.form
    name = request.form['full_name']
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    confirm_password = request.form['con_password']
    with engine.connect() as conn:
      data = {"email": email, "password": password}
      query = text(
        'SELECT * FROM register WHERE email = :email AND password = :password')
      result = conn.execute(query, data)
      account = result.all()
      if account:
        msg = 'Account already exists!'
      elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        msg = 'Invalid email address!'
      elif not re.match(r'[A-Za-z0-9]+', username):
        msg = 'Username must contain only characters and numbers!'
      elif not username or not password or not email or not name:
        msg = 'Please fill out the form!'
      elif password != confirm_password:
        msg = 'Password and confirm Password does not match!!'
      else:
        add_user(name, username, password, email)
        msg = 'Login to continue'
        return render_template('login.html', msg=msg)
  return render_template('register.html', msg=msg)


@app.route('/login/', methods=['GET', 'POST'])
def login():
  msg = ''
  if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
    email = request.form['email']
    password = request.form['password']
    with engine.connect() as conn:
      data = {"email": email, "password": password}
      query = text(
        'SELECT * FROM register WHERE email = :email AND password = :password')
      result = conn.execute(query, data)
    account = result.all()
    if account:
      #session['loggedin'] = True
      #session['id'] = account['id']
      #session['email'] = account['email']
      return redirect('home_encodedecode')
    else:
      msg = "Incorrect email/password!"
  return render_template('login.html', msg=msg)


@app.route('/login/logout')
def logout():
  # Remove session data, this will log the user out
  logout_user()
  # Redirect to login page
  return redirect(url_for('login'))


@app.route('/login/home_encodedecode/')
def encodedecode():
  return render_template('home_encodedecode.html')


@app.route('/imageencode/')
def imageencode():
  return render_template('imageencode.html')


@app.route('/textencode/')
def textencode():
  return render_template('textencode.html')


@app.route('/textencode/', methods=("POST", "GET"))
def uploadFile():
  if request.method == 'POST':
    # Upload file flask
    uploaded_img = request.files['baseFile']
    # Extracting uploaded data file name
    img_filename = secure_filename(uploaded_img.filename)
    # Upload file to database (defined uploaded folder in static path)
    uploaded_img.save(os.path.join(app.config['UPLOAD_FOLDER'], img_filename))
  return render_template('textencode.html')


if __name__ == '__main__':
  app.run(debug=True)


@app.route('/audioencode/')
def audioencode():
  return render_template('audioencode.html')


@app.route('/videoencode/')
def videoencode():
  return render_template('videoencode.html')


@app.route('/imagedecode/')
def imagedecode():
  return render_template('imagedecode.html')


@app.route('/textdecode/')
def textdecode():
  return render_template('textdecode.html')


@app.route('/audiodecode/')
def audiodecode():
  return render_template('audiodecode.html')


@app.route('/videodecode/')
def videodecode():
  return render_template('videodecode.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
