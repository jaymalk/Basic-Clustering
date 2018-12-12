#!/usr/bin/env python3

import sys
from matplotlib import pyplot as plt
import random

def main():
    total_points = int(sys.argv[1])
    total_clusters = int(sys.argv[2])
    r = lambda: random.randint(0,255)
    colors = []
    for _ in range(total_clusters):
        colors.append('#%02X%02X%02X' % (r(),r(),r()))
    _f = open("./data_"+str(total_points)+"_"+str(total_clusters)+".txt", "r+")
    while True:
        line = _f.readline()
        if line.startswith("Final"):
            break
    _f.readline()
    for _ in range(total_clusters):
        _f.readline()
        _f.readline()
        _f.readline()
        _x = []
        _y = []
        while True:
            line = _f.readline()
            if line == '\n':
                break
            [x, y] = list(map(float, line.split()))
            _x.append(x)
            _y.append(y)
        plt.plot(_x, _y, 'o',  markersize = 2.5, color = colors.pop())
    plt.show()


if __name__ == '__main__':
    main()
