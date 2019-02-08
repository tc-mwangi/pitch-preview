from flask import render_template, request, redirect, url_for
# from app import app
from . import main
# from ..requests import get_source, get_article


@main.route('/login')
def login():
    '''
    display login page and its data
    '''

    
    render_template('login.html')



@main.route('/landing')
def index():
    '''
    display landing page and its data
    '''


    render_template('index.html')



@main.route('/signup')
def signup():
    '''
    signup page and its data
    '''

    
    render_template('login.html')



@main.route('/view_category')
def view_category():
    '''
    view interview category and its data
    '''

    
    render_template('view-category.html')



@main.route('/view_profile')
def view_profile():
    '''
    specific user's profile page and its data
    '''

    
    render_template('view-profile.html')



@main.route('/my_pitches')
def my_pitches():
    '''
    specific user's pitches and its data
    '''

    
    render_template('my-pitches.html')



@main.route('/create_pitch')
def create_pitch():
    '''
    specific user's pitches and its data
    '''

    
    render_template('create-pitch.html')



