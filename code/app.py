# _*_ coding: UTF-8 _*_
import json
from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)


def check_mysql_connect():
    db_con = mysql.connector.connect(
        host=os.environ.get("MYSQL_HOST", "127.0.0.1"),
        port=os.environ.get("PORT"),
        user=os.environ.get("USER"),
        passwd=os.environ.get("PASSWORD"),
        database=os.environ.get("DATABASE"),
    )
    return db_con.is_connected()


@app.route("/")
def index():
    return f"{check_mysql_connect()}"
