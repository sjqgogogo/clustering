from collections import defaultdict
from math import inf
import random
import csv


def point_avg(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    element_number = len(points)
    dimension_number = len(points[0])
    center = []

    for i in range(dimension_number):
        center.append(0)

    for i in range(element_number):
        for j in range(dimension_number):
            center[j] = center[j] + points[i][j]

    for i in range(dimension_number):
        center[i] = center[i]/element_number

    # raise NotImplementedError()

    return center


def update_centers(data_set, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the center for each of the assigned groups.
    Return `k` centers in a list
    """
    # print("assignments are ",assignments)
    element_number = len(data_set)

    # get k
    max = 0
    for item in assignments:
        if(item>max):
            max = item
    k=max+1
    # print("k is ",k)

    # raise NotImplementedError()

    # get new_cneter_i for label i
    centers = []
    for label in range(k):
        points = []
        for i in range(element_number):
            if(assignments[i]==label):
                points.append(data_set[i])
        centers.append(point_avg(points))

    return centers

def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    """
    Returns the Euclidean distance between a and b
    """

    dimension_number = len(a)
    dis = 0
    for i in range(dimension_number):
        dis = dis+(a[i]-b[i])*(a[i]-b[i])

    # raise NotImplementedError()

    return dis

def generate_k(data_set, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """

    # generate k different random number
    element_number = len(data_set)
    random_index = []
    if(k>element_number-1):
        print("k=",k," n=",element_number)
        raise ValueError("k should be less than n")
    for i in range(k):
        while(True):
            temp = random.randint(0,element_number-1)
            if temp not in random_index:
                random_index.append(temp)
                break

    # set these k points as centers
    k_center = []
    for item in random_index:
        k_center.append(data_set[item])


    #raise NotImplementedError()

    return k_center


def get_list_from_dataset_file(dataset_file):
    # (x,y)

    csvFile = open(dataset_file, "r")

    dataset = []

    reader = csv.reader(csvFile)

    for item in reader:
        temp = []
        temp.append(float(item[0]))
        temp.append(float(item[1]))
        dataset.append(temp)


    #raise NotImplementedError()
    return dataset


def cost_function(clustering):

    # clustering is a dict
    # key: label    value: points

    cost = 0
    centers = []
    for label in clustering:
        points = []
        for point in clustering[label]:
            points.append(point)
        center = point_avg(points)
        for point in clustering[label]:
            cost = cost+distance(center,point)

    # raise NotImplementedError()
    return cost


def k_means(dataset_file, k):
    dataset = get_list_from_dataset_file(dataset_file)
    k_points = generate_k(dataset, k)
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = update_centers(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering


# k_means("C://Users//sjqgo//Desktop//CS506//extra_credit//clustering//tests//test_files//dataset_1.csv",5)