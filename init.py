from flask import Flask, jsonify, g

from db.DatabaseHelper import DatabaseHelper
from db.Repository import Repository


SQLITE = "Sqlite3"
#POSTGRESQL = "PostgreSQL"
DEFAULT_DB = SQLITE
repo = None

app = Flask(__name__)

def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = DatabaseHelper(DEFAULT_DB).db
    return g.link_db

@app.before_request
def before_request():
    try:
        global repo
        repo = Repository( get_db() )
    except Exception as e:
        print(e)


@app.route('/api/<topic>', methods=['GET'])
def one(topic):
	data = repo.random(topic)
	response = jsonify(data)
	response.headers['Cache-Control'] = 'no-store'
	return response


@app.route('/api/cheatsheet/<topic>', methods=['GET'])
def table(topic):
	data = repo.cheatsheet(topic)
	response = jsonify(data)
	response.headers['Cache-Control'] = 'no-store'
	return response	

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


if __name__ == '__main__':
	app.run(debug=True)