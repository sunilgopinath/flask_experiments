'''
Created on Mar 24, 2014

@author: sgopinath
'''
from functools import wraps
from flask import Flask, request, abort, make_response, redirect, current_app, Response

def require_apikey(fn):
    @wraps(fn)
    # the new, post-decoration function
    def decorated_function(*args, **kwargs):
        print request.view_args['api_key']
        if request.args.get('key'):
            print request.args.get('key')
        else:
            print 'no key found'
    return decorated_function

def jsonp(f):
    """Wraps JSONified output for JSONP
    wrapped function must return str or unicode."""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback')
        if callback:
            json_content = f(*args, **kwargs)
            js_expression = u'{0}({1})'.format(callback, json_content)
            return current_app.response_class(js_expression, mimetype='application/javascript; charset=utf-8')
        else:
            return Response(f(*args, **kwargs), mimetype='application/json; charset=utf-8')
    return decorated_function