

def collision(hitbox1_points, hitbox2_points):
    boollist1 = []
    collision_type = []
    for point in range(len(hitbox2_points)):
        point1 = hitbox2_points[point]
        if point == len(hitbox2_points) -1:
            point2 = hitbox2_points[0]
        else:
            point2 = hitbox2_points[point + 1]
        if (((point1[0] > sum(hitbox1_points[0]) / 2 - 768) and (point1[0] < sum(hitbox1_points[0]) / 2 + 768)) or (point2[0] > sum(hitbox1_points[0]) / 2 - 768) and (point2[0] < sum(hitbox1_points[0]) / 2 + 768)) and (((point1[1] > sum(hitbox1_points[1]) / 2 - 720) and (point1[1] < sum(hitbox1_points[1]) / 2 + 720)) or ((point2[1] > sum(hitbox1_points[1]) / 2 - 720) and (point2[1] < sum(hitbox1_points[1]) / 2 + 720))):
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
                if m != 0:
                    if (point1[0] < hitbox1_points[0][0] < point2[0] or point1[0] < hitbox1_points[0][1] < point2[0]) and (point1[1] > hitbox1_points[1][0] > point2[1] or point1[1] > hitbox1_points[1][1] > point2[1]):
                        for i in range(round(abs(point2[0] - point1[0]))):
                            x = point1[0] + (abs((point2[0] - point1[0])) / (point2[0] - point1[0])) * i
                            y = m * x + b
                            boollist2.append((hitbox1_points[0][0] < x < hitbox1_points[0][1]) and (hitbox1_points[1][0] < y < hitbox1_points[1][1]))
                            if(hitbox1_points[0][0] < x < hitbox1_points[0][1]) and (hitbox1_points[1][0] < y < hitbox1_points[1][1]):
                                if 1 not in collision_type:
                                    collision_type += [1]
                if m == 0:
                    boollist2.append((point1[0] < hitbox1_points[0][0] < point2[0] or point1[0] < hitbox1_points[0][1] < point2[0]) and (hitbox1_points[1][0] < point1[1] < hitbox1_points[1][1]))
                    if(point1[0] < hitbox1_points[0][0] < point2[0] or point1[0] < hitbox1_points[0][1] < point2[0]) and (hitbox1_points[1][0] < point1[1] < hitbox1_points[1][1]):
                        if 1 not in collision_type:
                            collision_type += [1]

            else:
                boollist2.append(hitbox1_points[0][0] < point1[0] < hitbox1_points[0][1]
                                 and (((point1[1] < hitbox1_points[1][0] < point2[1]) or (point1[1] < hitbox1_points[1][1] < point2[1]))
                                      or ((point1[1] > hitbox1_points[1][0] > point2[1]) or (point1[1] > hitbox1_points[1][1] > point2[1]))))
                if(hitbox1_points[0][0] < point1[0] < hitbox1_points[0][1]
                                 and (((point1[1] < hitbox1_points[1][0] < point2[1]) or (point1[1] < hitbox1_points[1][1] < point2[1]))
                                      or ((point1[1] > hitbox1_points[1][0] > point2[1]) or (point1[1] > hitbox1_points[1][1] > point2[1])))):
                    if 2 not in collision_type:
                        collision_type += [2]
            boollist1.append(True in boollist2)
    return [True in boollist1, collision_type]
