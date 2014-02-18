# utility functions 


import math


def distance(x1, x2):
    return math.sqrt(((x2[0] - x1[0])*(x2[0] - x1[0])) + ((x2[1] - x1[1])*(x2[1] - x1[1])))


def sort_goals(door_coord, goal_coords):
    temp_goals = list(goal_coords)
    for i in range(len(goal_coords)):
        for j in range(i + 1, len(goal_coords)):
            g1 = temp_goals[i][0]['min']
            g2 = temp_goals[j][0]['min']
            if distance(door_coord, g2) < distance(door_coord, g1):
                temp = temp_goals[i]
                temp_goals[i] = temp_goals[j]
                temp_goals[j] = temp
    return temp_goals
