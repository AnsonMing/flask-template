from flask import Blueprint, render_template, redirect, request, Flask


main = Blueprint("main", __name__)


def index():
    return "hi"
