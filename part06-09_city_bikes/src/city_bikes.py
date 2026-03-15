import math # bach mnb9awch n3ayto 3la liberary kola mara 
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
    

    longitude1 = stations[station1][0]
    longitude2 = stations[station2][0]
    latitude1 = stations[station1][1]
    latitude2 = stations[station2][1]

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations: dict):
    greatest_distance = -1
    station_names = list(stations.keys()) # give us just keys in our dic it's the name of station
    best_pair = ("", "") 

    for i in range(len(station_names)):
        # loop don't repeat the same calculation of 2 station start from i + 1
        for j in range(i+1, len(station_names)):
            s1 = station_names[i]
            s2 = station_names[j]
            d = distance(stations, s1, s2)
            if d > greatest_distance:
                greatest_distance = d
                best_pair = (s1, s2)
    return (best_pair[0], best_pair[1], greatest_distance)







if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)
