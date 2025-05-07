'''
The location for the Flask app interface for the project.
'''
from flask import Flask, abort

from ProductionCode.most_banned import (
    most_banned_districts,
    most_banned_authors,
    most_banned_states,
    most_banned_titles)

app = Flask(__name__)

most_banned_map = {
    "states": most_banned_states,
    "districts": most_banned_districts,
    "authors": most_banned_authors,
    "titles": most_banned_titles
}

@app.route('/')
def home_page():
    '''
    The home page of the Flask app
    '''
    return(
        "<h1>The Forbidden Library</h1>"
        "<p>Use the following endpoints:</p>"
        "<ul>"
        "<li>/most-banned/districts/limit</li>"
        "<li>/most-banned/authors/limit</li>"
        "<li>/most-banned/states/limit</li>"
        "<li>/most-banned/titles/limit</li>"
        "</ul>"
    )

@app.route('/most-banned/<field>/<limit>', strict_slashes=False)
def most_banned(field, limit):
    '''
    The endpoint for the most banned titles
    '''
    if not limit.isdigit() or field not in most_banned_map:
        abort(500)
    function = most_banned_map[field]
    return function(int(limit))

@app.errorhandler(500)
def python_bug(_error):
    '''
    The endpoint for the most banned titles
    '''
    return "500: Bad Request", 500

if __name__ == "__main__":
    app.run()
