#!/usr/bin/env python
#-*- coding: utf-8 -*-
from flask import Flask
import flask_restful
import os

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.default')
app.config.from_pyfile('config.py') # import config from instance
if os.environ.get('APP_CONFIG_FILE'):
    app.config.from_envvar('APP_CONFIG_FILE')

api = flask_restful.Api(app)

## Setup the url resource routing here

## Setup the Api resource routing here
from app.api_views.helloworld import HelloWorld
api.add_resource(HelloWorld, '/helloworld')
