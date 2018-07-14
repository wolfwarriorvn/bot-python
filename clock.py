from apscheduler.schedulers.blocking import BlockingScheduler
from app import *

sched = BlockingScheduler()

@sched.scheduled_job('interval', seconds=5)
def timed_job():
    print('This job is run every three seconds.')
    bot_test()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=7)
def scheduled_job():
    print('This job is run every day at 7am.')
    bot_run()

sched.start()