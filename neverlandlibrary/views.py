from flask import render_template
import operator
from neverlandlibrary import app
from mockdb import *


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/library/')
def library():
    title = "Library"
    stories = []

    for story in story_table:
        stories.append(story)

    stories = sorted(stories, key=operator.itemgetter('title'))
    return render_template("library.html", title=title, stories=stories)


@app.route('/story/<int:story_id>/')
@app.route('/story/<int:story_id>/<int:chapter_id>/')
def display(story_id, chapter_id=0):
    story = dict(next((i for i in story_table if i['id'] == story_id), None))
    title = story['title']
    story['author'] = dict(
        next((a for a in author_table if a['id'] == story['author_id']), None))
    story['chapters'] = sorted(
        list(
            (c for c in chapter_table if c['story'] == story['id'])),
        key=operator.itemgetter('id'))
    if chapter_id:
        story['chapter'] = story['chapters'][chapter_id - 1]
        next_id = chapter_id + 1
        prev_id = chapter_id - 1

        try:
            if next_id - 1 < len(story['chapters']):
                story['chapter']['next'] = True
        except IndexError:
            story['chapter']['next'] = False

        if prev_id > 0:
            story['chapter']['previous'] = True
        else:
            story['chapter']['previous'] = False

        story['chapter']['next_id'] = next_id
        story['chapter']['previous_id'] = prev_id
        return render_template("chapter.html", story=story, title=title)
    else:
        return render_template("story.html", story=story, title=title)