#!/usr/bin/env python

import flask


app = flask.Flask(__name__)


@app.route('/')
def index():
    try:
        import dlib
    except ImportError as e:
        return 'Failed to import dlib! Error message: {}'.format(e)
    return 'Succeeded to import dlib! Its version is {}'.format(
        dlib.__version__)
