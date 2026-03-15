def get_station_data(filename: str):
    distance_dic = {}
    with open(filename) as f:
        for line in f:
            parts = line.strip().split(";")
            if parts[0] == "Longitude":
                continue
            distance_dic[parts[3]] = (float(parts[0]), float(parts[1]))
        return distance_dic

def distance(stations: dict, station1: str, station2: str):
    import math

    longitude1 = stations[station1][0]
    longitude2 = stations[station2][0]
    latitude1 = stations[station1][1]
    latitude2 = stations[station2][1]

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations: dict):
    greatest_distance = 0
    station_1 = ""
    station_2 = ""

    for station1 in stations:
        for station2 in stations:
            distance_km = distance(stations, station1, station2)
            if distance_km > greatest_distance:
                greatest_distance = distance_km
                station_1 = station1
                station_2 = station2
    return (station_1, station_2, greatest_distance)





if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)
