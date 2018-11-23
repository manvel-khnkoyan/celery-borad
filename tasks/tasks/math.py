from __future__ import absolute_import, unicode_literals

from time import sleep
from settings import app
from trebel.system.math import *


@app.task
def system_math_add(x, y):
    return add(x,y)


@app.task
def system_math_mul(x, y):
    return mul(x,y)


@app.task
def system_math_xsum(numbers):
    return xsum(numbers)


@app.task
def system_add_log(str):
    sleep(50)
    f = open("/tmp/celery.txt", "a")
    f.write(str)
    return str
