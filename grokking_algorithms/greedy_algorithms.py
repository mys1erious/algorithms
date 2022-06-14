import time


def imitate_stations_problem():
    states_needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}

    stations = {
        'kone': {'id', 'nv', 'ut'},
        'ktwo': {'wa', 'id', 'mt'},
        'kthree': {'or', 'nv', 'ca'},
        'kfour': {'nv', 'ut'},
        'kfive': {'ca', 'az'}
    }



    return states_needed, stations


def approx_min_stations(states_needed: set, stations: dict):
    final_stations = set()
    cur_set_of_states = set()

    for i in range(len(stations)):
        if cur_set_of_states == states_needed:
            return final_stations

        station_to_add = None
        states_to_add = set()
        for station, states in stations.items():
            unique_states = states - states_to_add - cur_set_of_states  # states_needed & states
            if unique_states > states_to_add:
                station_to_add = station
                states_to_add = unique_states

        if station_to_add is not None:
            final_stations.add(station_to_add)
            cur_set_of_states.update(states_to_add)
            stations.pop(station_to_add)

    return -1


def ams_book(states_needed, stations):
    final_stations = set()

    while states_needed:
        best_station = None
        states_covered = set()
        for station, states in stations.items():
            covered = states_needed & states
            if len(covered) > len(states_covered):
                best_station = station
                states_covered = covered

        states_needed -= states_covered
        final_stations.add(best_station)

    return final_stations


if __name__ == '__main__':
    states_needed, stations = imitate_stations_problem()
    s1 = time.time()
    print(approx_min_stations(states_needed, stations))
    s2 = time.time() - s1

    states_needed, stations = imitate_stations_problem()
    s3 = time.time()
    print(ams_book(states_needed, stations))
    s4 = time.time() - s3

    print("Time1:", s2)
    print("Time2:", s4)
