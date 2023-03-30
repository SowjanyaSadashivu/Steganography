from flask import Flask, render_template, request
from database import add_user
#from database import load_values_from_db
#import above if we are using any function in the page

app = Flask(__name__)


@app.route('/')  #empty router refers to home page
def home():
  return render_template('home.html')


@app.route('/register')
def register():
  return render_template('register.html', name='register')


@app.route('/login')
def login():
  return render_template('login.html', name='login')


@app.route('/register/', methods=['post'])
def create_user():
  if request.method == 'POST':
    data = request.form
    name = request.form['full_name']
    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['con_password']
    if password != confirm_password:
      return render_template('register.html', name='register')
    else:
      #store the data into DB
      add_user(data)
  return render_template('home_encodedecode.html', user=name)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
