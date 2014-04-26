from flask import Flask


app = Flask(__name__)
app.secret_key = 'This is really unique and secret'

import neverlandlibrary.views