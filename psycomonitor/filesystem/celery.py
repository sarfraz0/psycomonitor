# -_- coding: utf-8 -_-
# Author : Sarfraz Kapasi
# Date   : 14/12/2016
""" Filesystem monitoring celery application """

# standard
import os
import logging
# installed
from celery import Celery
# custom
from ..common.constants import PARIS_TIMEZONE

# Globals
###############################################################################

logger = logging.getLogger(__name__)

app = Celery(broker=os.environ['CELERY_BROKER'],
             backend=os.environ['CELERY_BACKEND'],
             include=['psycomonitor.filesystem.tasks'])

app.conf.update(
    timezone=PARIS_TIMEZONE
)

###############################################################################

if __name__ == '__main__':
    app.start()

#
