#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
from slogging import logger
while True:
    logger.info('test')
    logger.info(u'中文')
    time.sleep(2)
