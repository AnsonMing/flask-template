# _*_ coding: UTF-8 _*_
import json
from flask import Flask, request, jsonify
import mysql.connector
import os
import redis

app = Flask(__name__)


def check_mysql_connect():
    db_con = mysql.connector.connect(
        host=os.environ.get("MYSQL_HOST", "127.0.0.1"),
        port=os.environ.get("MYSQL_PORT"),
        user=os.environ.get("MYSQL_USER", "root"),
        passwd=os.environ.get("MYSQL_ROOT_PASSWORD"),
        database=os.environ.get("MYSQL_DATABASE"),
    )
    return db_con.is_connected()


def check_redis_connect():
    r = redis.StrictRedis(host=os.environ.get("REDIS_HOST"))
    return r.set("foo", "bar")


@app.route("/")
def index():
    result = ""
    if check_mysql_connect():
        result += "mysql connected\n"

    if check_redis_connect():
        result += "redis connected"

    return result
