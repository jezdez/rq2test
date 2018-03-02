# app.py
import logging
import sys
from flask import Flask, has_app_context
from flask_rq2 import RQ


logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
logger = logging.getLogger(__name__)


app = Flask(__name__)
app.config['RQ_REDIS_URL'] = 'redis://127.0.0.1:6379/0'

rq = RQ(app)


@rq.job
def add(x, y):
    logger.info('Has app context: %s', has_app_context())
    return x + y


@app.route('/')
def index():
    add.queue(1, 3)
    return 'hello world!'
