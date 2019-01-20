

def collision(hitbox1_points, hitbox2_points):
    '''this function will determine if 2 objects are touching (only returns true if they have intersecting lines)

    :param hitbox1_points: the min and max x and y values of a rect, should be entered like [[0,5],[0,5]]
    :param hitbox2_points: the points of the object, last point connects with first point, should be entered like [[0,0],[0,5],[5,5],[5,0]]
    :return: returns True if hitbox1_points are inside of hitbox2_points
    '''
    boollist1 = []
    for point in range(len(hitbox2_points)):
        point1 = hitbox2_points[point]
        if point == len(hitbox2_points) -1:
            point2 = hitbox2_points[0]
        else:
            point2 = hitbox2_points[point + 1]
        if point1[0] != point2[0]:
            m = (point2[1] - point1[1]) / (point2[0] - point1[0])
        else:
            m = 'undefined'
        if m != 'undefined':
            b = point1[1] - (m * point1[0])
        else:
            b = 'undefined'
        boollist2 = []
        if m != 'undefined':
            for i in range(abs(point2[0] - point1[0]) * 5):
                x = point1[0] + (abs((point2[0] - point1[0])) / (point2[0] - point1[0])) * (i/5)
                y = m * x + b
                boollist2.append((hitbox1_points[0][0] < x < hitbox1_points[0][1]) and (hitbox1_points[1][0] < y < hitbox1_points[1][1]))
        else:
            boollist2.append((hitbox1_points[0][0] < point1[0] < hitbox1_points[0][1]) and (hitbox1_points[1][0] < point1[1] < hitbox1_points[1][1]))
        boollist1.append(True in boollist2)
    return True in boollist1

