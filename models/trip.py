import requests
from models.station import Station
from models.train import Train

import enum
import json


class TripKey(enum.Enum):
    plateformAvailable = "plateformAvailable"
    disruptionsAvailable = "disruptionsAvailable"
    arrivalTimeAvailable = "arrivalTimeAvailable"
    nextTrainsList = "nextTrainsList"
    departureStopArea = "departureStopArea"
    arrivalStopArea = "arrivalStopArea"


class Trip:
    def __init__(self, departure_station, arrival_station=None, data=None):
        self.departure_station = departure_station
        self.arrival_station = arrival_station

        if(data is None):
            self.data = {}
        else:
            self.data = data

        if(len(self.nextTrainsList) > 0 and not isinstance(self.nextTrainsList[0], Train)):
            self.data['nextTrainsList'] = [Train(train_data) for train_data in self.data['nextTrainsList']]

    def __getattr__(self, key):
        if(key in TripKey.__members__):
            return self.data[key]
        raise KeyError

    @staticmethod
    def next_trains(departure_station, arrival_station=None, pmr=False):
        if(isinstance(departure_station, str)):
            departure_station = Station.find_station(departure_station)
            print(departure_station)

        if(departure_station is None):
            raise TypeError("departure_station can't be None")

        if (arrival_station == ""):
            arrival_station = None

        if (isinstance(arrival_station, str)):
            arrival_station = Station.find_station(arrival_station)

            # Prepare Body
        data = {"departure": departure_station.label, "pmr": pmr}
        if (arrival_station is not None):
            data["uicArrival"] = arrival_station.uic

        # Prepare headers
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        r = requests.post("https://www.transilien.com/api/nextDeparture/search", data=json.dumps(data),
                          headers=headers)
        data = json.loads(r.text)
        t = Trip(departure_station, arrival_station, data)
        return t
