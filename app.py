import os
import signal
from flask import Flask
from buzz import generator

app = Flask(__name__)

signal.signal(signal.SIGINT, lambda s, f: os._exit(0))

@app.route("/")
def generate_buzz():
	page = '<html><head>DevOps Buzz Generator</head>'
	page += '<style>body{background-color: #c43f11}</style><body><h1>'
	page += generator.generate_buzz()
	page += '</h1></body></html>'
	return page

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=os.getenv('PORT')) #port 5000 is default
