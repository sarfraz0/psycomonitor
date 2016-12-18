# -_- coding: utf-8 -_-
# Author : Sarfraz Kapasi
# Date   : 14/12/2016
""" Filesystem monitoring celery tasks """

# standard
import logging
# installed
# from celery.schedules import crontab
# custom
from .celery import app

# Globals
###############################################################################

logger = logging.getLogger(__name__)

# Functions and Classes
###############################################################################


@app.task
def testa():
    print('lol')


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls testa() every 10 seconds.
    sender.add_periodic_task(10.0, testa.s(), name='add every 10')

###############################################################################
#
