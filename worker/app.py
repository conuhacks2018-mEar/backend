"""
"""

import logging

from apscheduler.schedulers.blocking import BlockingScheduler
import redis

import label_wav
import notifications


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

r = redis.Redis(host='redis', decode_responses=True)


def check_new_files():
    while True:
        next_file = r.lpop('files')
        if not next_file:
            return
        logger.info(f'processing {next_file}')
        result, error = None, None
        try:
            result = label_wav.label_wav(next_file)
        except Exception as e:
            error = e
        logger.info('result from label_wav: ' + str(result))
        logger.info('error from label_wav: ' + str(error))
        # logger.info('error from label_wav: ' + 'testing')
        # do something with result
        for key in result:
            result[key] = str(result[key])
        if not error:
            notifications.push_police_notification({
                'filename': next_file,
                'notification': 'something',
                'label_wav_result': result,
            })


scheduler = BlockingScheduler()
scheduler.add_job(check_new_files, 'interval', seconds=5)
scheduler.start()
