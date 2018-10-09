import math
import requests





def calc_dist(lat1, lon1, lat2, lon2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    h = math.sin((lat2 - lat1) / 2) ** 2 + \
      math.cos(lat1) * \
      math.cos(lat2) * \
      math.sin((lon2 - lon1) / 2) ** 2

    return 6372.8 * 2 * math.asin(math.sqrt(h))


def getMeteorCoordinates(meteor):
    latitude = meteor.get('reclat')
    longtitude = meteor.get('reclong')
    coordinates = (latitude, longtitude)
    return coordinates


def calculateAndAddDistancesOfMeteors():
    global meteor_data
    for meteor in meteor_data:
        if 'reclat' not in meteor or 'reclong' not in meteor:
            continue
        meteor['distance'] = calc_dist(houseCoordinates[0], houseCoordinates[1],
                                       float(getMeteorCoordinates(meteor)[0]), float(getMeteorCoordinates(meteor)[1]))


def get_distance(meteor):
    return meteor.get('distance', math.inf)


if __name__ == '__main__':
    houseCoordinates = (52.08673121780718, 5.049856391142839)

    nasaResponse = requests.get('https://data.nasa.gov/resource/y77d-th95.json')
    meteor_data = nasaResponse.json()
    calculateAndAddDistancesOfMeteors()

    meteor_data.sort(key=get_distance)
    
    print(meteor_data[:10])





