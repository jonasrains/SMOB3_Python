

def collision(hit_box1_points, hit_box2_points):
    bool_list1 = []
    collision_type = []
    for point in range(len(hit_box2_points)):
        point1 = hit_box2_points[point]
        if point == len(hit_box2_points) -1:
            point2 = hit_box2_points[0]
        else:
            point2 = hit_box2_points[point + 1]
        if point1[0] != point2[0]:
            m = (point2[1] - point1[1]) / (point2[0] - point1[0])
        else:
            m = 'undefined'
        if m != 'undefined':
            b = point1[1] - (m * point1[0])
        else:
            b = 'undefined'
        bool_list2 = []
        if m != 'undefined':
            if m != 0:
                for i in range(round(abs(point2[0] - point1[0]) / 2)):
                    x = point1[0] + (abs((point2[0] - point1[0])) / (point2[0] - point1[0])) * (i * 2)
                    y = m * x + b
                    bool_list2.append((hit_box1_points[0][0] < x < hit_box1_points[0][1]) and (hit_box1_points[1][0] < y < hit_box1_points[1][1]))
                    if(hit_box1_points[0][0] < x < hit_box1_points[0][1]) and (hit_box1_points[1][0] < y < hit_box1_points[1][1]):
                        if 1 not in collision_type:
                            collision_type += [1]
            if m == 0:
                bool_list2.append((point1[0] < hit_box1_points[0][0] < point2[0] or point1[0] < hit_box1_points[0][1] < point2[0]) and (hit_box1_points[1][0] < point1[1] < hit_box1_points[1][1]))
                if(point1[0] < hit_box1_points[0][0] < point2[0] or point1[0] < hit_box1_points[0][1] < point2[0]) and (hit_box1_points[1][0] < point1[1] < hit_box1_points[1][1]):
                    if 1 not in collision_type:
                        collision_type += [1]

        else:
            bool_list2.append(hit_box1_points[0][0] < point1[0] < hit_box1_points[0][1]
                             and (((point1[1] < hit_box1_points[1][0] < point2[1]) or (point1[1] < hit_box1_points[1][1] < point2[1]))
                                  or ((point1[1] > hit_box1_points[1][0] > point2[1]) or (point1[1] > hit_box1_points[1][1] > point2[1]))))
            if(hit_box1_points[0][0] < point1[0] < hit_box1_points[0][1]
                             and (((point1[1] < hit_box1_points[1][0] < point2[1]) or (point1[1] < hit_box1_points[1][1] < point2[1]))
                                  or ((point1[1] > hit_box1_points[1][0] > point2[1]) or (point1[1] > hit_box1_points[1][1] > point2[1])))):
                if 2 not in collision_type:
                    collision_type += [2]
        bool_list1.append(True in bool_list2)
    return [True in bool_list1, collision_type]
