"""
"""

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate('service-account-key.json')
app = firebase_admin.initialize_app(cred, {'databaseURL' : 'https://conuhacks2018-mear.firebaseio.com'})
root = db.reference()


def _get_value(key):
    return root.child(key).get()


def _set_value(key, value):
    return root.child(key).set(value)


def get_police_token():
    return _get_value('police')


def set_police_nofication(notification):
    return _set_value('policeNotification', notification)
