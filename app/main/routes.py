from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app

from app.main import bp


@bp.route('/')
def index():
    return 'Hello Word'
