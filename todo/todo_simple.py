'''
Created on Mar 24, 2014

@author: sgopinath
'''
from flask import Flask, request
from flask.ext.restful import Resource

todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

        