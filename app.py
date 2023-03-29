from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')  #empty router refers to home page
def home():
  return render_template('home.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
