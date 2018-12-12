#!/usr/bin/env python3

import random
from point_class import point

class distributions:

    def __init__(self, size=0):
        self.list = []
        self.size = size

    def get_list(self):
        return self.list

    def reset(self):
        pass

class uniform(distributions):

    def __init__(self, size):
        distributions.__init__(self, size)
        self._fill_list()

    def _fill_list(self):
        for _ in range(self.size):
            self.list.append(point(random.randint(-1000, 1000), random.randint(-1000, 1000)))

    def reset(self):
        self.list = []
        self._fill_list()

class two_way_partitioned(distributions):

    def __init__(self, size):
        distributions.__init__(self, size)
        self._fill_list()

    def _fill_list(self):
        for _ in range(self.size/2):
            self.list.append(point(500+random.randint(-500, 500), 500+random.randint(-500, 500)))
            self.list.append(point(-500+random.randint(-500, 500), -500+random.randint(-500, 500)))

    def reset(self):
        self.list = []
        self._fill_list()
