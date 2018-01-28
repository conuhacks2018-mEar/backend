"""
"""

import logging
import os

from apscheduler.schedulers.blocking import BlockingScheduler
import redis

import label_wav
import notifications

LABEL_PROB_THRESHOLD = float(os.environ['LABEL_PROB_THRESHOLD'])
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

r = redis.Redis(host='redis', decode_responses=True)


def check_new_files():
    while True:
        next_wav_id = r.lpop('wav_id')
        if not next_wav_id:
            return
        next_file = f'/data/{next_wav_id}.wav'
        logger.info(f'processing {next_file}')
        result, error = None, None
        try:
            result = label_wav.label_wav(next_file)
            logger.info('result from label_wav: ' + str(result))
        except Exception as e:
            error = e
            logger.info('error from label_wav: ' + str(error))
            continue
        for k, v in result.items():
            label = k
            label_prob = v
        if label_prob > LABEL_PROB_THRESHOLD:
            notifications.push_police_notification({
                'wav_id': next_wav_id,
                'label': label,
                'label_prob': str(label_prob),
            })


scheduler = BlockingScheduler()
scheduler.add_job(check_new_files, 'interval', seconds=5)
scheduler.start()
