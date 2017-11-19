#!/usr/bin/env python
#-*- coding: utf-8 -*-

def init_view_url(app):
    """
    Place your www router here
    """
    from .views.helloworld import www_index
    app.add_url_rule('/', 'www_index', www_index)
    app.add_url_rule('/test/', 'www_index', www_index)

def init_api_url(api):
    """
    Place your api router here
    """
    from .api_views.helloworld import HelloWorld
    api.add_resource(HelloWorld, '/helloworld')
