from flask import Flask, render_template
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


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
