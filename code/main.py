# _*_ coding: UTF-8 _*_
import json
from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)


def check_mysql_connect():
    db_con = mysql.connector.connect(
        host=os.environ.get("MYSQL_HOST", "127.0.0.1"),
        port=os.environ.get("MYSQL_PORT"),
        user=os.environ.get("MYSQL_USER"),
        passwd=os.environ.get("MYSQL_PASSWORD"),
        database=os.environ.get("MYSQL_DATABASE"),
    )
    return db_con.is_connected()


@app.route("/")
def index():
    if check_mysql_connect():
        return f"Connected Mysql!!"
    else:
        return f"Cannot connect Mysql!!"
