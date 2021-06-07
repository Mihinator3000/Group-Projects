import math
import matplotlib.pyplot as plt
import numpy as np

class Point:
    def __init__(self, x_, y_, v_):
        self.x = x_
        self.y = y_
        self.v = v_

    def __str__(self):
        return str([self.x, self.y, self.v])


def calculate_e_by_x(fPoint, sPoint):
    return -(sPoint.v - fPoint.v) / (sPoint.x - fPoint.x)


def calculate_e_by_y(fPoint, sPoint):
    return -(sPoint.v - fPoint.v) / (sPoint.y - fPoint.y)


for i in range(18):
    file_name = "{}.txt".format(i+1)
# file_name = "18.txt"
    with open(file_name, 'r') as fin:
        arr_x, arr_y, arr_e = [], [], []
        arr_red_x, arr_red_y = [], []
        arr_blue_x, arr_blue_y = [], []
        array_of_points = []
        for line in fin:
            if line[0] != "%":
                x, y, str_v = line.split()
                x, y = float(x), float(y)
                v = ""
                for char in str_v:
                    if char == "-" or char == "+":
                        break
                    v += char
                v = float(v)
                array_of_points.append(Point(x, y, v))

        for point in array_of_points:
            border_over_cur_x, border_below_cur_x = 1e9, -1e9
            border_over_cur_y, border_below_cur_y = 1e9, -1e9
            for other_point in array_of_points:
                if border_over_cur_x > other_point.x > point.x:
                    border_over_cur_x = other_point.x
                    v_over_x = other_point.v
                if border_below_cur_x < other_point.x < point.x:
                    border_below_cur_x = other_point.x
                    v_below_x = other_point.v
                if border_over_cur_y > other_point.y > point.y:
                    border_over_cur_y = other_point.y
                    v_over_y = other_point.v
                if border_below_cur_y < other_point.y < point.y:
                    border_below_cur_y = other_point.y
                    v_below_y = other_point.v

            if border_over_cur_x == 1e9:
                border_over_cur_x = point.x
                v_over_x = point.v
            if border_below_cur_x == -1e9:
                border_below_cur_x = point.x
                v_below_x = point.v
            if border_over_cur_y == 1e9:
                border_over_cur_y = point.y
                v_over_y = point.v
            if border_below_cur_y == -1e9:
                border_below_cur_y = point.y
                v_below_y = point.v

            point_over_x = Point(border_over_cur_x, 0, v_over_x)
            point_below_x = Point(border_below_cur_x, 0, v_below_x)
            point_over_y = Point(0, border_over_cur_y, v_over_y)
            point_below_y = Point(0, border_below_cur_y, v_below_y)

            e_x = calculate_e_by_x(point_below_x, point_over_x)
            e_y = calculate_e_by_y(point_below_y, point_over_y)
            cur_e = math.sqrt(e_x ** 2 + e_y ** 2)
            arr_x.append(point.x)
            arr_y.append(point.y)
            arr_e.append(cur_e)

        for j in range(len(arr_e)):
            if arr_e[j] >= 1300:
                arr_red_x.append(arr_x[j])
                arr_red_y.append(arr_y[j])
            arr_blue_x.append(arr_x[j])
            arr_blue_y.append(arr_y[j])

        print(np.mean(arr_e))

    # plt.figure(figsize=(18, 16))
    # plt.scatter(arr_blue_x, arr_blue_y, s=15, c="#1f77b4", marker="s")
    # plt.scatter(arr_red_x, arr_red_y, s=15, c="#d62728", marker="s")
    # plt.xlim(-6, 6)
    # plt.ylim(-3, 3)
    # plt.show()
