#!/usr/bin/env python
"""Jobs module"""
from app.v1 import scheduler
from utils.fetch_and_process import fetch_and_analyse

@scheduler.task('interval', id='do_job_1', seconds=60, misfire_grace_time=900)
def job1():
    """Collet the latest news
       Analyse sentiment
       Insert to DB
    """
    fetch_and_analyse()
