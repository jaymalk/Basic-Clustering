#!/usr/bin/env python3

import random
from point_class import point
import sys

class distributions:

    def __init__(self, size=0):
        self.list = []
        self.size = size
        self._fill_list()

    def get_list(self):
        return self.list

    def _fill_list(self):
        pass

    def reset(self):
        self.list = []
        self._fill_list()

    def write_on_file(self, path):
        _f = open("../Distributions/"+path, "w+")
        _s = ""
        for pnt in self.list:
            _s = _s+str(pnt.x())+" "+str(pnt.y())+"\n"
        _f.write("Total Points: "+str(self.size)+"\n\n")
        _f.write(_s+"\n")
        _f.close()

class uniform(distributions):

    def _fill_list(self):
        for _ in range(self.size):
            self.list.append(point(random.randint(-1000, 1000), random.randint(-1000, 1000)))


class two_square_partitioned(distributions):

    def _fill_list(self):
        p_1 = random.choice([501, -501])
        p_2 = random.choice([501, -501])
        p_3 = random.choice([501, -501])
        p_4 = random.choice([501, -501])
        for _ in range(self.size//2):
            self.list.append(point(p_1+random.randint(-500, 500), p_2+random.randint(-500, 500)))
            self.list.append(point(p_3+random.randint(-500, 500), p_4+random.randint(-500, 500)))
        if self.size%2 == 1:
            self.list.append(point(0, 0))

class point_centered(distributions):

    def __init__(self, size, points=None, min_dist=None):
        self.points = points
        self.min_dist = min_dist
        distributions.__init__(self, size)

    def _fill_list(self):
        self.list.append(point(random.randint(-1000, 1000), random.randint(-1000, 1000)))
        set_points = 1
        while set_points != self.points:
            temp_point = point(random.randint(-1000, 1000), random.randint(-1000, 1000))
            if self._is_set_valid(temp_point):
                set_points += 1
                self.list.append(temp_point)
        total = self.points+1
        while total != self.size:
            temp_point = point(random.randint(-1000, 1000), random.randint(-1000, 1000))
            if self._is_valid(temp_point):
                self.list.append(temp_point)
                total += 1


    def _is_valid(self, pnt):
        for i in range(self.points):
            if pnt.distance(self.list[i]) < self.min_dist:
                return True
        return False

    def _is_set_valid(self, pnt):
        for i in range(len(self.list)):
            if pnt.distance(self.list[i]) < 2*self.min_dist:
                return False
        return True

def main():
    case = int(sys.argv[1])
    if case == 0:
        # UNIFORM
        uniform(int(sys.argv[2])).write_on_file("uniform_"+sys.argv[2]+".txt")
    elif case == 1:
        # Square Partitioning
        two_square_partitioned(int(sys.argv[2])).write_on_file("partitioned_"+sys.argv[2]+".txt")
    elif case == 2:
        # Point Clustering
        point_centered(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])).write_on_file("point_centered_"+sys.argv[2]+"_"+sys.argv[3]+"_"+sys.argv[4]+".txt")

    else:
        print("Illegal case.")

if __name__ == '__main__':
    main()
