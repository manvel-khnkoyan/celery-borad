from __future__ import absolute_import, unicode_literals

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
