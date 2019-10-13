# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 23:25:59 2019

@author: Ettore
"""

import telegram
import configparser
import redis

from telegram.ext import Updater

# Configuring bot
config = configparser.ConfigParser()
config.read_file(open('config.ini'))

# Connecting to Telegram API
# Updater retrieves information and dispatcher connects commands
updater = Updater(token=config['DEFAULT']['token'])
dispatcher = updater.dispatcher

# Connecting to Redis db
db = redis.StrictRedis(host=config['DB']['host'],
                       port=config['DB']['port'],
                       db=config['DB']['db'])