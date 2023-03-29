from flask import Flask

app = Flask(__name__)


@app.route('/')  #empty router refers to home page
def home():
  return 'This is home'

if __name__ == "__main__":  
	app.run(host='0.0.0.0', debug = True)