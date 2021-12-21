from math import *
import matplotlib.pyplot as plt

# output data
x = []
y = []
speed = []
speed_x = []
speed_y = []
fuel_left = []

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
    up_flight_time = int(fuel_weight / burn_velocity)
    time_arr = [i for i in range(up_flight_time)]
    time_arr.insert(0, 0)
    rocket_up = False
    for second in range(up_flight_time):
        if second == 0:
            x.append(0)
            y.append(0)
            speed.append(0)
            speed_x.append(0)
            speed_y.append(0)
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
            speed_x.append(speed[-1] * cos(alpha))
            speed_y.append(speed[-1] * sin(alpha))
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
            time = time_arr[-1] + 1
            time_arr.append(time)
            new_y = last_y + last_speed * sin(alpha) * time - (calculate_g(y[-1], earth_weight) * time**2)/2
            new_x = last_x + last_speed * cos(alpha) * time
            new_speed = sqrt((last_speed * sin(alpha) - calculate_g(y[-1], earth_weight) * time)**2 + (last_speed * cos(alpha))**2)
            x.append(new_x)
            y.append(new_y)
            speed.append(new_speed)
            speed_x.append(new_speed * cos(alpha))
            speed_y.append(new_speed * sin(alpha))
            fuel_left.append(0)
    earth_x = [i for i in range(3 * 10**6)]
    earth_y = [0 for _ in range(3 * 10**6)]
    del time_arr[-1]
    print("Ракета летела", up_flight_time + time, "секунд.")
    plt.figure(figsize=(16, 10))
    plt.subplot(3, 3, 1)
    plt.title("Полёт ракеты:")
    plt.plot(earth_x, earth_y)
    plt.plot(x, y)
    plt.subplot(3, 3, 2)
    plt.title("Скорость ракеты по модулю:")
    plt.plot(time_arr, speed)
    plt.subplot(3, 3, 3)
    plt.title("Скорость ракеты по x:")
    plt.plot(time_arr, speed_x)
    plt.subplot(3, 3, 4)
    plt.title("Скорость ракеты по y:")
    plt.plot(time_arr, speed_y)
    plt.subplot(3, 3, 5)
    plt.title("Оставшееся топливо:")
    plt.plot(time_arr, fuel_left)
    plt.show()

