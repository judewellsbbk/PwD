initial_road_map = [('Massachusetts', 'Boston', 42.2352, -71.0275),
                    ('North Carolina', 'Raleigh', 35.771, -78.638),
                    ('Virginia', 'Richmond', 37.54, -77.46),
                    ('Washington', 'Olympia', 47.042418, -122.893077),
                    ('New York', 'Albany', 42.659829, -73.781339),
                    ]

from math import *
import random
from copy import deepcopy

def distance(lat1degrees, long1degrees, lat2degrees, long2degrees):
    earth_radius = 3956  # miles
    lat1 = radians(lat1degrees)
    long1 = radians(long1degrees)
    lat2 = radians(lat2degrees)
    long2 = radians(long2degrees)
    lat_difference = lat2 - lat1
    long_difference = long2 - long1
    sin_half_lat = sin(lat_difference / 2)
    sin_half_long = sin(long_difference / 2)
    a = sin_half_lat ** 2 + cos(lat1) * cos(lat2) * sin_half_long ** 2
    c = 2 * atan2(sqrt(a), sqrt(1.0 - a))
    return earth_radius * c

def compute_total_distance(road_map):
    """
    Returns, as a floating point number, the sum of the distances of all
    the connections in the `road_map`. Remember that it's a cycle, so that
    (for example) in the initial `road_map`, Wyoming connects to Alabama...
    """
    def distance(lat1degrees, long1degrees, lat2degrees, long2degrees):
        earth_radius = 3956  # miles
        lat1 = radians(lat1degrees)
        long1 = radians(long1degrees)
        lat2 = radians(lat2degrees)
        long2 = radians(long2degrees)
        lat_difference = lat2 - lat1
        long_difference = long2 - long1
        sin_half_lat = sin(lat_difference / 2)
        sin_half_long = sin(long_difference / 2)
        a = sin_half_lat ** 2 + cos(lat1) * cos(lat2) * sin_half_long ** 2
        c = 2 * atan2(sqrt(a), sqrt(1.0 - a))
        return earth_radius * c
    total_distance = 0
    number_of_cities = len(road_map)
    for i in range (number_of_cities):
        next_city_index = (i + 1) % number_of_cities
        total_distance += (distance(road_map[i][2], road_map[i][3], road_map[next_city_index][2], road_map[next_city_index][3]))
    return (total_distance)


def swap_cities(road_map, index1, index2):

    new_road_map = deepcopy(road_map)

    # Logic for when "road_map" contains single city
    if len(new_road_map) <= 1:
        return (new_road_map, 0)
    # Logic for same location swap
    elif index1 == index2:
        new_total_distance = compute_total_distance(new_road_map)
        return (new_road_map, new_total_distance)
    else:
        # Logic for location swop in "road_map"
        first_position = new_road_map[index1]
        second_position = new_road_map[index2]
        new_road_map[index1] = second_position
        new_road_map[index2] = first_position
        new_total_distance = compute_total_distance(new_road_map)
        return (new_road_map, new_total_distance)


def find_best_cycle(road_map):
    swap_return_tuple = ()
    numb_of_cities = len(road_map)
    previous_total_distance = compute_total_distance(road_map)

    i = 0

    while i < 10:
        # If even: swap_cities; if odd: swap_adjacent_cities
        swap_type = 4 #int(10 * random.random())

        print("Starting distance ")
        print(compute_total_distance(road_map))

        if swap_type % 2 == 0:
            city1 = int(numb_of_cities * random.random())
            city2 = int(numb_of_cities * random.random())
            print(city1)
            print(city2)

            swap_return_tuple = swap_cities(road_map, city1, city2)

            print("swap return distance ")
            print(swap_return_tuple[1])

            # If swapped-city total distance < previous total distance, update "road_map"
            swap_total_distance = swap_return_tuple[1]

            if swap_total_distance < previous_total_distance:
                print("less")
                # print(swap_total_distance)
                road_map = swap_return_tuple[0]
                # print(compute_total_distance(road_map))
                previous_total_distance = swap_total_distance
                i += 1
            else:
                print("greater")
                i += 1
        else:
            i += 1


find_best_cycle(initial_road_map)
