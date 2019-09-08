from models.station import Station


class Train:
    def __init__(self, data):
        self.data = data
        if(len(self.deservedStations) > 0 and 'stations' not in self.deservedStations[0]):
            for i in range(len(self.deservedStations)):
                self.deservedStations[i]['station'] = Station.find_station(self.deservedStations[i]['label'])

    def __getattr__(self, key):
        return self[key]

    def __setattr__(self, key, value):
        self[key] = value

    def __getitem__(self, key):
        if (key in self.data):
            return self.data[key]
        raise KeyError

    def __setitem__(self, key, value):
        self.station_data[key] = value
