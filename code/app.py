# _*_ coding: UTF-8 _*_

# add lib
from flask import Flask, Blueprint

# add views
from views.main import *


# app config
app = Flask(__name__)

# add blueprint
# app.register_blueprint(main)


# add url
app.add_url_rule("/", "index", index)


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, True)
