from flask import Flask, render_template
import operator

app = Flask(__name__)
app.secret_key = 'This is really unique and secret'

mockdb = [
                {'type': 'story', 'title': "Sample Story", 'id': 1},
                {'type': 'story', 'title': "Another Story", 'id': 2},
                {'type': 'story', 'title': "Neverending Story", 'id': 3},
               ]

@app.route('/')
def index():
    title = "Home"
    return render_template("base.html", title=title)

@app.route('/library/')
def library():
    title = "Library"
    stories = []

    for item in mockdb:
        if item['type'] == 'story':
            stories.append(item)

    stories = sorted(stories, key=operator.itemgetter('title'))
    return render_template("base.html", title=title)


@app.route('/story/<int:storyid>')
def story(storyid):
    story = next((item for item in mockdb if item['id'] == storyid and item['type'] == 'story'), None)
    title = story['title']
    return render_template("base.html", title=title)