from math import *
import matplotlib.pyplot as plt

x = []
y = []

speed = []
fuel_left = []

earth_x = [i for i in range(10 ** 6)]
earth_y = [0 for i in range(10 ** 6)]

#  CONST
earth_radius = 6.37 * 10 ** 6
G = 6.67 * 10 ** (-11)


def calculate_g(prev_y, earth_weight):
    return G * earth_weight / (earth_radius + prev_y) ** 2


def calculate_speed(ax, ay, t):
    return sqrt((ax*t)**2 + (ay*t)**2)


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
    time = 0
    ax = 0
    ay = 0

    up_flight_time = int(fuel_weight / burn_velocity)
    rocket_up = False
    for second in range(up_flight_time):
        if second == 0:
            x.append(0)
            y.append(0)
            speed.append(0)
            fuel_left.append(fuel_weight)
        else:
            cur_rocket_weight = rocket_weight + fuel_left[second - 1]
            ax = calculate_acceleration_x(cur_rocket_weight, gas_velocity, burn_velocity, alpha)
            ay = calculate_acceleration_y(cur_rocket_weight, y[second - 1], gas_velocity, burn_velocity, earth_weight,
                                          alpha)
            if calculate_y(ay, second) >= 0:
                rocket_up = True
                x.append(calculate_x(ax, second))
                y.append(calculate_y(ay, second))
            else:
                if rocket_up:
                    print("Ракета завершила полёт на %i секунде!" % second)
                    break
                x.append(0)
                y.append(0)
            speed.append(calculate_speed(ax, ay, second))
            fuel_left.append(calculate_left_fuel(second, fuel_weight, burn_velocity))
    if not rocket_up:
        print("Ракета не взлетела :(")

    if calculate_g(y[-1], earth_weight) <= 10**-3:
        print("Ракета осталась в космосе по завершении своего полёта!")
    else:
        last_x = x[-1]
        last_y = y[-1]
        last_speed = speed[-1]
        while y[-1] > 10**-3:
            if calculate_g(y[-1], earth_weight) <= 10**-3:
                print("Ракета осталась в космосе по завершении своего полёта!")
                break
            time += 1
            new_y = last_y + last_speed * sin(alpha) * time - (calculate_g(y[-1], earth_weight) * time**2)/2
            new_x = last_x + last_speed * cos(alpha) * time
            new_speed = sqrt((last_speed * sin(alpha) - calculate_g(y[-1], earth_weight) * time)**2 + (last_speed * cos(alpha))**2)
            y.append(new_y)
            x.append(new_x)
            speed.append(new_speed)
            fuel_left.append(0)
            # print(new_x, new_y, new_speed, calculate_g(y[-1], earth_weight))

    earth_x = [i for i in range(int(max(x)) + 10 ** 3)]
    earth_y = [0 for _ in range(int(max(x)) + 10 ** 3)]
    plt.plot(earth_x, earth_y)
    plt.plot(x, y)
    print("Ракета летела", up_flight_time + time, "секунд.")
    plt.show()

