#! /usr/bin/env python

from testflaskbower import app
import cProfile

app.jinja_env.cache = {}

if __name__ == "__main__":
    app.run(threaded=True)
