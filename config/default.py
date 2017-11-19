#!/usr/bin/env python
#-*- coding: utf-8 -*-

DEBUG = False
SECRET_KEY = 'HKup5cuW7dce5@TrwN'
SESSION_TYPE = 'filesystem'

# Database configuration
DB_USER = 'test'
DB_PASSWORD = 'test'
DB_HOST = 'test'
DB_PORT = 'test'
DB_NAME = 'test'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{0}:{1}@{2}:{3}/{4}'.format(
        DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME)
SQLALCHEMY_TRACK_MODIFICATIONS = False
