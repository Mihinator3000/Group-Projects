from math import *
import matplotlib.pyplot as plt

x_up = []
y_up = []

x_down = []
y_down = []

speed = []
fuel_left = []

earth_x = [i for i in range(10 ** 6)]
earth_y = [0 for i in range(10 ** 6)]

#  CONST
earth_radius = 6.37 * 10 ** 6
G = 6.67 * 10 ** (-11)


def calculate_g(prev_y, earth_weight):
    return G * earth_weight / (earth_radius + prev_y) ** 2


def calculate_speed(cur_rocket_weight, gas_velocity, rocket_weight):
    return gas_velocity * log1p(cur_rocket_weight / rocket_weight)


def calculate_acceleration_x(full_rocket_weight, gas_velocity, burn_velocity, alpha):
    return (gas_velocity * burn_velocity * cos(alpha)) / full_rocket_weight


def calculate_acceleration_y(full_rocket_weight, prev_y, gas_velocity, burn_velocity, earth_weight, alpha):
    return (gas_velocity * burn_velocity * sin(alpha)) / full_rocket_weight - calculate_g(prev_y, earth_weight)


def calculate_left_fuel(cur_time, fuel_weight, burn_velocity):
    return fuel_weight - cur_time * burn_velocity


def calculate_x(cur_acceleration_x, cur_time):
    return (cur_acceleration_x * cur_time ** 2) / 2


def calculate_y(cur_acceleration_y, cur_time):
    return (cur_acceleration_y * cur_time ** 2) / 2


def graph(alpha, rocket_weight, fuel_weight, gas_velocity, burn_velocity, earth_weight):
    i = 0
    ax = 0
    ay = 0
    plt.plot(earth_x, earth_y)
    up_flight_time = int(fuel_weight / burn_velocity)
    rocket_up = False
    for second in range(up_flight_time):
        if second == 0:
            x_up.append(0)
            y_up.append(0)
            speed.append(0)
            fuel_left.append(fuel_weight)
        else:
            cur_rocket_weight = rocket_weight + fuel_left[second - 1]
            ax = calculate_acceleration_x(cur_rocket_weight, gas_velocity, burn_velocity, alpha)
            ay = calculate_acceleration_y(cur_rocket_weight, y_up[second - 1], gas_velocity, burn_velocity, earth_weight,
                                          alpha)
            if calculate_y(ay, second) >= 0:
                rocket_up = True
                x_up.append(calculate_x(ax, second))
                y_up.append(calculate_y(ay, second))
            else:
                if rocket_up:
                    print("Ракета завершила полёт на %i секунде!" % second)
                    break
                x_up.append(0)
                y_up.append(0)
            speed.append(calculate_speed(cur_rocket_weight, gas_velocity, rocket_weight))
            fuel_left.append(calculate_left_fuel(second, fuel_weight, burn_velocity))
    if not rocket_up:
        print("Ракета не взлетела :(")
    # print(len(x_up), len(y_up))
    plt.plot(x_up, y_up)
    # plt.show()
    if calculate_g(y_up[-1], earth_weight) <= 10**-3:
        print(calculate_g(y_up[-1], earth_weight), ay)
        print("Ракета осталась в космосе по завершении своего полёта!")
    else:
        y_down.append(y_up[-1])
        x_down.append(x_up[-1])
        while y_down[-1] > 0:
            i += 1
            y_down.append(y_down[-1] - (calculate_g(y_down[-1], earth_weight)) * i)
            x_down.append(x_down[-1] + i * ax)
        plt.plot(x_down, y_down)
    print("Ракета летела", up_flight_time + i, "секунд.")
    plt.show()

