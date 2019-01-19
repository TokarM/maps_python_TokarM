from math import sin, cos, sqrt, atan2, radians

# Approximate radius of earth in km
R = 6373.0
MILES_IN_KM: float = 0.621371

class Distance(object):

    """ Input: Dict with geolocation point
        Output: Distance between two points """
    def find_distance(self, from_, to_):

        # Retrieve values from dictionary to variables
        lat1 = from_['lat']
        lon1 = from_['lng']
        lat2 = to_['lat']
        lon2 = to_['lng']

        # Calculate distance using geolocation of two points
        dlon = radians(lon2 - lon1)
        dlat = radians(lat2 - lat1)

        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance_ = (R * c) * MILES_IN_KM

        return distance_




