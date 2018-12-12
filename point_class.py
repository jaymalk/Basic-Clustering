#!/usr/bin/env python3
"A class of points on 2D"
from math import sqrt

class point:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return "("+str(self._x)+","+str(self._y)+")"

    def x(self):
        return self._x

    def y(self):
        return self._y

    def distance(self, other):
        return sqrt(pow(self._x-other.x(), 2)+pow(self._y-other.y(), 2))
