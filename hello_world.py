import mysql.connector
import json
from flask import Flask

app = Flask(__name__)

@app.route('/saludomundo')
def hello_world():
  return 'hola mundo  '