#!/usr/bin/env python
#-*- coding: utf-8 -*-
from app import app
import flask_restful
from flask_restful import fields, marshal_with

class HelloWorld(flask_restful.Resource):

    def get(self):
        return {'hello': 'world'}
