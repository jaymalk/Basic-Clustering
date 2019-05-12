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


class point_square(distributions):

    def __init__(self, size, points=10, max_sq_size=100):
        self.points = points
        self.max_sq_size = max_sq_size
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
            if abs(pnt.x()-self.list[i].x()) < self.max_sq_size//2 and abs(pnt.y()-self.list[i].y()) < self.max_sq_size//2:
                return True
        return False

    def _is_set_valid(self, pnt):
        for i in range(len(self.list)):
            if pnt.distance(self.list[i]) < self.max_sq_size:
                return False
        return True

class point_circle(distributions):

    def __init__(self, size, points=10, min_dist=100):
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

class concentric_circles(distributions):

    def __init__(self, size, points=10):
        self.points = points
        distributions.__init__(self, size)

    def _fill_list(self):
        for i in range(self.points):
            self.list += self._fill_circle(900*(1+i)/self.points)

    def _fill_circle(self, radius):
        dist = 300/self.points
        center = point(0, 0)
        point_list = []
        i = 0
        while i < self.size*(radius/90):
            temp_point = point(random.randint(-1000, 1000), random.randint(-1000, 1000))
            if temp_point.distance(center) <= radius+dist and temp_point.distance(center) >= radius-dist:
                point_list.append(temp_point)
                i += 1
        return point_list

def main():
    case = int(sys.argv[1])
    if case == 0:
        # UNIFORM
        uniform(int(sys.argv[2])).write_on_file("uniform_"+sys.argv[2]+".txt")
    elif case == 1:
        # Square Partitioning
        point_square((int(sys.argv[2])), int(sys.argv[3]), int(sys.argv[4])).write_on_file("point_square_"+sys.argv[2]+"_"+sys.argv[3]+"_"+sys.argv[4]+".txt")
    elif case == 2:
        # Point Clustering
        point_circle(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])).write_on_file("point_circle_"+sys.argv[2]+"_"+sys.argv[3]+"_"+sys.argv[4]+".txt")
    elif case == 3:
        # Point Clustering
        concentric_circles(int(sys.argv[2]), int(sys.argv[3])).write_on_file("concentric_circles_"+sys.argv[2]+"_"+sys.argv[3]+".txt")

    else:
        print("Illegal case.")

if __name__ == '__main__':
    main()
