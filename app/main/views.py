# step1
from flask import render_template, request, redirect, url_for
from . import main


@main.route('/')
def index():
    '''
    '''
    return 'pitch this'

