from urllib import urlencode
from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
from search import Searcher

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    searcher = Searcher()
    movies, tvs = searcher.default_display()
    return render_template("index.html", movie_videos=movies["videos"], tv_videos=tvs["videos"])

@app.route('/results', methods=['POST'])
def search(): 
    query = request.form['query']
    field = request.form['field']
    searcher = Searcher()
    result = searcher.search(query, field)
    return render_template("results.html", query=query, videos=result["videos"])

@app.route('/api/videos/search', methods=['GET'])
def api_search():
    query = request.args['query']
    field = request.args['field']
    searcher = Searcher()
    result = searcher.search(query, field)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0')