# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 09:51:39 2020

@author: DK
"""

import pickle
import numpy as np
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt

dirpath = 'F://Documents//MachineLearning//MLGame-master//games//arkanoid//log'
BallPosition = []
PlatformPosition = []
LRUP = []
last_ball_x = 0
last_ball_y = 0
files = listdir(dirpath)
log_number = 0
for k in range(0,4):
    for f in files:
      log_number = log_number + 1
      fullpath = join(dirpath, f)
      if isfile(fullpath):
        with open(fullpath , "rb") as f1:
            data_list1 = pickle.load(f1)
        for i in range(0 , len(data_list1)):
            BallPosition.append(data_list1[i].ball)
            PlatformPosition.append(data_list1[i].platform)
            if(i>=-1):
                if(last_ball_x - data_list1[i].ball[0] > 0):
                    LR = 1
                else:
                    LR = 0
                if(last_ball_y - data_list1[i].ball[1] > 0):
                    UP = 0
                else:
                    UP = 1
                LRUP.append(np.array((LR,UP)))
            last_ball_x = data_list1[i].ball[0]
            last_ball_y = data_list1[i].ball[1]


PlatX = np.array(PlatformPosition) [:,0][:,np.newaxis]
PlatX_next = PlatX[1:,:]
instrust = (PlatX_next-PlatX[0:len(PlatX_next),0][:,np.newaxis])/5

Ballarray = np.array(BallPosition[:-1])
LRUP = np.array((LRUP[:-1]))
# x = np.hstack((Ballarray,LRUP,PlatX[0:-1,0][:,np.newaxis]))
x = BallPosition
y = instrust 
np.set_printoptions(threshold=np.inf)
# Find which variable is the most in an array of variables
def most_found(array):
    list_of_words = []
    for i in range(len(array)):
        if array[i] not in list_of_words:
            list_of_words.append(array[i])

    most_counted = ''
    n_of_most_counted = None

    for i in range(len(list_of_words)):
        counted = array.count(list_of_words[i])
        if n_of_most_counted == None:
            most_counted = list_of_words[i]
            n_of_most_counted = counted
        elif n_of_most_counted < counted:
            most_counted = list_of_words[i]
            n_of_most_counted = counted
        elif n_of_most_counted == counted:
            most_counted = None

    return most_counted

def find_neighbors(point, data, labels, k=k):
    # How many dimentions do the space have?
    n_of_dimensions = len(point)
    # print("Lengh of point : {}".format(len(point)))

    #find nearest neighbors
    neighbors = []
    neighbor_labels = []

    for i in range(0, k):
        # To find it in data later, I get its order
        nearest_neighbor_id = None
        smallest_distance = None

        for i in range(0, len(data)):
            eucledian_dist = 0
            for d in range(0, n_of_dimensions):
                dist = abs(point[d] - data[i][d])
                eucledian_dist += dist

            eucledian_dist = np.sqrt(eucledian_dist)

            if smallest_distance == None:
                smallest_distance = eucledian_dist
                nearest_neighbor_id = i
            elif smallest_distance > eucledian_dist:
                smallest_distance = eucledian_dist
                nearest_neighbor_id = i

        neighbors.append(data[nearest_neighbor_id])
        neighbor_labels.append(labels[nearest_neighbor_id])

        data.remove(data[nearest_neighbor_id])
        labels.remove(labels[nearest_neighbor_id])
    return neighbor_labels

# point - the point to predict label
# data - data of other points
# labels - labels of data points
def k_nearest_neighbor(point, data, labels, k=k):

    # If two different labels are most found, continue to search for 1 more k
    while True:
        neighbor_labels = find_neighbors(point, data, labels, k=k)
        label = most_found(neighbor_labels)
        if label != None:
            break
        k += 1
        if k >= len(data):
            break
    print("Command : {}".format(label))
    return label
    
point = [181, 208]
k_nearest_neighbor(point, x, list(y), k=8)