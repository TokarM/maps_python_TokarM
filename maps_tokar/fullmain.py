import json
import falcon
import googlemaps
from wsgiref import simple_server
from math import sin, cos, sqrt, atan2, radians

api = falcon.API()

class GasStation(object):

    def on_get(self, req, resp):
        # Insert personal API key
        gmaps = googlemaps.Client(key='Your API key here')
        input = req.params

        # Get geo location of your device
        #mylocation = gmaps.geolocate()
        #mylocation = mylocation['location']
        try:
            lat = float(input['lat'])
            lng = float(input['lng'])
            mylocation = {'lat': lat, 'lng': lng,}
        except:
            raise falcon.HTTPBadRequest( "Incorrect parameters",
            "Provide correct parameters")

        if input['destination'] == 'gas_station':
            output = Distance().find_address(gmaps,mylocation,"gas station")
        elif input['destination'] == 'starbucks':
            output = Distance().find_address(gmaps,mylocation,"starbucks")
        elif input['destination'] == 'dunkin':
            output = Distance().find_address(gmaps,mylocation,"dunkin donats")
        elif req.content_length == 0:
            raise falcon.HTTPBadRequest("Incorrect parameters",
            "Provide correct parameters")

        # Get provided parameters
        resp.body = json.dumps(output)

        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):

        output = {'request': 'Incorrect'}

        resp.body = json.dumps(output)

        resp.status = falcon.HTTP_200


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

        return round(distance_,2)

    """ Input: Dictance between two points
        Output: Address of destination """
    def find_address(self, _gmaps, _from, _to):
        # Find closest building that you are looking for
        search_for_place = _gmaps.places(query=_to, location=_from, )
        results = search_for_place['results']

        # Find distance in miles between you and destination point
        dist = Distance()
        distance_ = dist.find_distance(_from, results[0]['geometry']['location'])

        # Data preparation for output as a JSON file
        output = {'address': results[0]['formatted_address'],
                  'distance': distance_,
                  'name': results[0]['name']}
        return output


gas_station = GasStation()

#api.add_route('/gas_station', gas_station)
api.add_route('/key', gas_station)

if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, api)
    httpd.serve_forever()
