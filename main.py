#!/usr/bin/env python
"""main app file"""
from application.v1 import app
from application.v1 import scheduler
import application.v1.ressources  
from application.v1.utils.fetch_and_process import default_fetch_and_analyse


@scheduler.task('interval', id='do_job_1', seconds=130, misfire_grace_time=900)
def job1():
    """Collet the latest news
       Analyse sentiment
       Insert to DB
    """
    default_fetch_and_analyse()


if __name__ == '__main__':
    scheduler.start()
    app.run()
