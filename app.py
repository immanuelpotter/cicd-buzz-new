import os
import signal
from flask import Flask
from buzz import generator

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route("/")
def generate_buzz():
	page = '<!DOCTYPE html>'
	page += "<link rel='stylesheet' type = 'text/css' href='static/style.css'>"
	page += '<html><body><h1>'
	page += generator.generate_buzz()
	page += '</h1></body></h1>'
	return page

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=os.getenv('PORT')) #port 5000 is default
