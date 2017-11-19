#!/usr/bin/env python
#-*- coding: utf-8 -*-
from flask import Flask
import flask_restful
import os
from app.url import init_view_url, init_api_url

app = Flask(__name__)
app.config.from_object('config.default')
if os.environ.get('APP_CONFIG_FILE'):
    app.config.from_envvar('APP_CONFIG_FILE')

api = flask_restful.Api(app)

init_view_url(app)
init_api_url(api)
