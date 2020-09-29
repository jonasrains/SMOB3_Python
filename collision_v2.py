def collision():
    # [left, right, top, bottom]
    col_type = [False, False, False, False]
    # hb2 must be split into multiple parts that get loaded at different times to decrease running speed
    # first entry in each area is the start x and end x. used to determine which areas need to be loaded
    hb2 = [[[0, 704], [0, 0], [0, 339], [704, 339], [704, 243]], [[704, 1246], [704, 243], [768, 243], [768, 339],[1246, 339]], [[1246, 2048], [1246, 307], [2048, 307], [2048, 0], [2048, 500], [0, 500]]]
    # hb1 is in [[start x, end x], [start y, end y], [center x, center y]]
    hb1 = [[0, 32], [0, 64], [16, 32]]
    # go through hb2, find out which area to test for then go through all the lines in that area
    i = 0
    for area in hb2:
        # tests if line goes through the hit-box area
        if area[0][0] - 5 <= hb1[2][0] <= area[0][1]:
            ii = 0
            for point in area:
                next_point = area[i+1]
                # the first point in each area is the min and max x, so it gets skipped here
                if i == 0:
                    continue
                # tests if any lines are with in the range of the hit-box, and sets the corresponding index in col_type to true if it is
                if point[0]-5 <= hb1[0][0] <= next_point[0]+5 and point[0]-5 <= hb1[2][0] <= next_point[0]+5:
                    col_type[0] = True
                if point[0]-5 <= hb1[0][1] <= next_point[0]+5 and point[0]-5 <= hb1[2][0] <= next_point[0]+5:
                    col_type[1] = True
                if point[1]-5 <= hb1[1][0] <= next_point[1]+5 and point[0]-5 <= hb1[2][1] <= next_point[0]+5:
                    col_type[2] = True
                if point[1]-5 <= hb1[1][1] <= next_point[1]+5 and point[0]-5 <= hb1[2][1] <= next_point[0]+5:
                    col_type[3] = True
                ii += 1
        # continues if player is not in the area's range
        else:
            continue
        i += 1
    # return value of col_type
    return col_type
    # collisions: if both sides and/or the bottom are colliding with something, it is solid ground, if one side and bottom collide then it is a slope. both sides and top are colliding then it is a ceiling hit
