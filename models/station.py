import requests
import json
import utils

stations_manager = [], False


class Station:
    def __init__(self, station_data, loaded=False):
        self.station_data = station_data

    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, key, value):
        self[key] = value

    def __getitem__(self, key):
        if (key in self.station_data):
            return self.station_data[key]
        raise KeyError

    def __setitem__(self, key, value):
        self.station_data[key] = value

    def __eq__(self, other):
        return isinstance(other, Station) and self.label == other.label

    @staticmethod
    def get_stations(force=False):
        global stations_manager
        stations, loaded = stations_manager
        if(force or not(loaded)):
            try:
                r = requests.get("https://www.transilien.com/aidesaisie/autocompletion/stopareas")
                data = json.loads(r.text)
                stations_manager = {station['label']: Station(station, True) for station in data['content']}, True
            except:
                return None
        return stations_manager[0]

    @staticmethod
    def find_station(name):
        # Load stations
        stations = Station.get_stations()

        # Sanitize name
        name = utils.sanitize_name(name)

        if(name in stations):
            return stations[name]
        else:
            for station in stations.values():
                for keyword in station.keywords:
                    if(keyword == name):
                        return station
            return None
