from flask import Flask
app = Flask(__name__)

@app.route('/')
def root():
  return 'Hello Flask(Main.py)'
