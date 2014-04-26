from flask import render_template
import operator
from neverlandlibrary import app


story_db = [{'title': "Sample Story", 'id': 1, 'author_id': 2},
            {'title': "Another Story", 'id': 2, 'author_id': 1},
            {'title': "Neverending Story", 'id': 3, 'author_id': 1},
            ]

chapter_db = [{'story': 3, 'id': 1, 'title': None,
               'text': """<p>This is a sample story text</p>
                          <p>It will be used for testing. This is chapter 1.</p>
                          <p>One more paragraph, for good measure.</p>"""},
              {'story': 3, 'id': 2, 'title': "A test title",
               'text': """<p>This is a sample story text</p>
                          <p>It will be used for testing. This is chapter 2.</p>
                          <p>One more paragraph, for good measure.</p>"""},
              {'story': 3, 'id': 3, 'title': "A different test title",
               'text': """<p>This is a sample story text.</p>
                          <p>It will be used for testing. This is chapter 3.</p>
                          <p>One more paragraph, for good measure.</p>"""},
              {'story': 1, 'id': 1, 'title': None,
               'text': """<p>This is a sample story text.</p>
                          <p>It will be used for testing. This is a oneshot.</p>
                          <p>One more paragraph, for good measure.</p>"""},
              {'story': 2, 'id': 1, 'title': None,
               'text': """<p>This is a sample story text.</p>
                          <p>It will be used for testing. This is chapter 1.</p>
                          <p>One more paragraph, for good measure.</p>"""},
              {'story': 2, 'id': 2, 'title': None,
               'text': """<p>This is a sample story text.</p>
                          <p>It will be used for testing. This is chapter 2.</p>
                          <p>One more paragraph, for good measure.</p>"""},
              ]

author_db = [{'id': 1, "handle": "Zoni"},
             {'id': 2, "handle": "adigitalmagician"}
             ]


@app.route('/')
def index():
    title = "Home"
    return render_template("base.html", title=title)


@app.route('/library/')
def library():
    title = "Library"
    stories = []

    for story in story_db:
        stories.append(story)

    stories = sorted(stories, key=operator.itemgetter('title'))
    return render_template("library.html", title=title, stories=stories)


@app.route('/story/<int:story_id>/')
@app.route('/story/<int:story_id>/<int:chapter_id>/')
def display_story(story_id, chapter_id=None):
    story = dict(next((i for i in story_db if i['id'] == story_id), None))
    title = story['title']

    if chapter_id is None or chapter_id == 0:
        return render_template("base.html", title=title)
    else:
        return chapter(story, chapter_id, title)


def chapter(s, i, t):
    s['author'] = dict(
        next((a for a in author_db if a['id'] == s['author_id']), None))
    s['chapter'] = dict(
        next(
            (c for c in chapter_db if c['story'] == s['id'] and c['id'] == i),
            None))
    next_i = i + 1
    prev_i = i - 1
    s['chapter']['next'] = next(
        (c for c in chapter_db if c['story'] == s['id'] and c['id'] == next_i),
        None)
    s['chapter']['previous'] = next(
        (c for c in chapter_db if c['story'] == s['id'] and c['id'] == prev_i),
        None)
    s['chapter']['next_id'] = next_i
    s['chapter']['previous_id'] = prev_i
    return render_template("chapter.html", story=s, title=t)
