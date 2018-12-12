#!/usr/bin/env python3
"A program to generate a set of random points and use the for clustering."

import sys                              # Taking arguments from command line
from random import randint, choice      # Randomly selecting points
from point_class import point           # Points class self-created for workign with the points
from distributions import uniform

def all_true(bool_list):
    answer = True
    for case in bool_list:
        answer = answer and case
    return answer

def closest(pnt, cluster_pivots):
    min_dist_point = len(cluster_pivots)-1
    min_dist = pnt.distance(cluster_pivots[min_dist_point])
    i = 0
    while i < len(cluster_pivots)-1:
        if pnt.distance(cluster_pivots[i]) < min_dist:
            min_dist_point = i
            min_dist = pnt.distance(cluster_pivots[i])
        i += 1
    return min_dist_point

def get_mean(point_list):
    total_x = 0
    total_y = 0
    for pnt in point_list:
        total_x += pnt.x()
        total_y += pnt.y()
    return point(total_x/len(point_list), total_y/len(point_list))

def list_string(point_list):
    _s = "["
    for pnt in point_list:
        _s = _s + str(pnt)+", "
    _s = _s.rstrip(", ")
    _s = _s + "]"
    return _s

def write_list_string(point_list):
    _s = ""
    for pnt in point_list:
        _s = _s+str(pnt.x())+" "+str(pnt.y())+"\n"
    return _s

def main():
    "Main function for running everything."
    total_points = int(sys.argv[1])
    threshold_distance = pow(10, -int(sys.argv[2]))
    total_clusters = int(sys.argv[3])
    points = uniform(total_points).get_list()
    _f = open("./data_"+str(total_points)+"_"+str(total_clusters)+".txt", "w+")
    _f.write("Total Points: "+str(total_points)+"\nTotal Clusters: "+str(total_clusters)+"\n\n")
    _f.write("Total Points\n"+write_list_string(points)+"\n\n")
    clusters = [[] for _ in range(total_clusters)]
    cluster_pivots = []
    cluster_complete = [False]*total_clusters
    for _ in range(total_clusters):
        while True:
            temp_point = choice(points)
            if cluster_pivots.count(temp_point) == 0:
                cluster_pivots.append(temp_point)
                break
    passes = 0
    while not all_true(cluster_complete):
        passes += 1
        _f.write("Pass no. "+str(passes)+"\n\n")
        for pnt in points:
            clusters[closest(pnt, cluster_pivots)].append(pnt)
        for i in range(len(clusters)):
            _f.write("Cluster No. "+str(i+1)+"\n")
            _f.write("Pivot: "+str(cluster_pivots[i].x())+" "+str(cluster_pivots[i].y())+"\n")
            _f.write("Mean: "+str(get_mean(clusters[i]))+"\n")
            _f.write(write_list_string(clusters[i])+"\n")
        for i in range(total_clusters):
            if not cluster_complete[i]:
                mean_point = get_mean(clusters[i])
                if mean_point.distance(cluster_pivots[i]) <= threshold_distance:
                    cluster_complete[i] = True
                cluster_pivots[i] = mean_point
        if all_true(cluster_complete):
            _f.write("Total passes: "+str(passes)+"\nFinal Clustering\n\n")
            for i in range(len(clusters)):
                _f.write("Cluster No. "+str(i+1)+"\n")
                _f.write("Pivot: "+str(cluster_pivots[i].x())+" "+str(cluster_pivots[i].y())+"\n")
                _f.write("Mean: "+str(get_mean(clusters[i]))+"\n")
                _f.write(write_list_string(clusters[i])+"\n")
        clusters = [[] for _ in range(total_clusters)]

if __name__ == '__main__':
    main()
