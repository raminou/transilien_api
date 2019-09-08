import requests
import json
import enum
import utils

stations_manager = [], False


class StationKey(enum.Enum):
    label = "label"
    value = "value"
    coordonneeX = "coordonneeX"
    coordonneeY = "coordonneeY"
    name = "name"
    typeRue = "typeRue"
    city = "city"
    coordLambertX = "coordLambertX"
    coordLambertY = "coordLambertY"
    uic = "uic"
    train = "train"
    rer = "rer"
    tramway = "tramway"
    metro = "metro"
    bateau = "bateau"
    navette = "navette"
    bus = "bus"
    stopPoint = "stopPoint"
    ratp = "ratp"
    sncf = "sncf"
    keywords = "keywords"
    tempsReel = "tempsReel"
    lignes = "lignes"
    entryPointType = "entryPointType"


class PlaceType(enum.Enum):
    no_filter = ""
    train = "train"
    metro = "metro"
    rer = "rer"
    bus = "bus"
    navette = "navette"
    tramway = "tramway"


class Station:
    def __init__(self, station_data, loaded=False):
        self.station_data = station_data

    def __getattr__(self, key):
        if(key in StationKey.__members__):
            return self.station_data[key]
        raise KeyError

    """
    def __setattr__(self, key, value):
        self.station_data[key] = value
    """

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
                test = [Station(station) for station in data['content']]
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

    @staticmethod
    def search_list_places(name, filter_item=PlaceType.no_filter):
        if(not isinstance(filter_item, PlaceType)):
            raise TypeError("filter_item must have the type PlaceType")
        r = requests.get("https://www.transilien.com/api/places", params={"search": name})
        data = json.loads(r.text)
        if(filter_item != PlaceType.no_filter):
            return [place for place in data['places'] if place[filter_item.value]]
        else:
            return data['places']
