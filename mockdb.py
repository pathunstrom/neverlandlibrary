__author__ = 'Patrick'

story_table = [{'title': "Sample Story", 'id': 1, 'author_id': 2},
            {'title': "Another Story", 'id': 2, 'author_id': 1},
            {'title': "Neverending Story", 'id': 3, 'author_id': 1},
            ]

chapter_table = [{'story': 3, 'id': 1, 'title': None,
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

author_table = [{'id': 1, "handle": "Zoni"},
             {'id': 2, "handle": "adigitalmagician"}
             ]