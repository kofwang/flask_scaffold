#!/usr/bin/env python
#-*- coding: utf-8 -*-
from app import app
import flask_restful
from flask_restful import fields, marshal_with
from app.models.demo import Demo

class HelloWorld(flask_restful.Resource):

    def get(self):
        ret = Demo.sayhi()
        return {'hello': 'world', 'model': ret}
