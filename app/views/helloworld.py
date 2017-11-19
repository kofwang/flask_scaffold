#!/usr/bin/env python
#-*- coding: utf-8 -*-

from app import app
from app.models.demo import Demo
from flask import render_template

def www_index():
    return render_template('index.html')
