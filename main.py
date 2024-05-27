#!/usr/bin/env python
"""main app file"""
from app.v1 import app
from app.v1 import scheduler

scheduler.start()

if __name__ == '__main__':
    app.run()