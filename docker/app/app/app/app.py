# coding=utf-8

from flask import Flask


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
	return '<h1>Index</h1>'


@app.route('/hello', methods=['GET'])
def hello():
	return '<h1>Hello</h1>'


if __name__ == '__main__':
	app.run()
