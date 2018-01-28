"""
"""

import logging

from apscheduler.schedulers.blocking import BlockingScheduler
import redis


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

r = redis.Redis(host='redis', decode_responses=True)


def check_new_files():
    while True:
        next_file = r.lpop('files')
        if not next_file:
            return
        logger.info(f'processing {next_file}')


scheduler = BlockingScheduler()
scheduler.add_job(check_new_files, 'interval', seconds=5)
scheduler.start()
