#!/usr/bin/env python
#-*- coding: utf-8 -*-

from app import app
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

# Place your model here

class Demo(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    @staticmethod
    def sayhi():
        return "hello world"
