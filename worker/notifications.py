"""
"""

import os

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate('service-account-key.json')
app = firebase_admin.initialize_app(cred, {'databaseURL' : os.environ['DATABASE_URL']})
root = db.reference()


def _get_value(key):
    return root.child(key).get()


def _set_value(key, value):
    return root.child(key).set(value)


def get_police_nofication():
    return _get_value('policeNotification')


def set_police_nofication(notification):
    return _set_value('policeNotification', notification)


def _push_notification(child, notification):
    return root.child(child).push().set(notification)


def push_police_notification(notification):
    return _push_notification('policeNotification', notification)
