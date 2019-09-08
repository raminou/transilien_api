from models.station import Station
import enum


class TrainType(enum.Enum):
    modeTransportEnum = "modeTransportEnum"
    lineTransportEnum = "lineTransportEnum"
    typeTrain = "typeTrain"
    codeMission = "codeMission"
    canceled = "canceled"
    delayed = "delayed"
    departureTime = "departureTime"
    arrivalTime = "arrivalTime"
    destinationMission = "destinationMission"
    platform = "platform"
    deservedStations = "deservedStations"
    hasTraficDisruption = "hasTraficDisruption"
    hasTravauxDisruption = "hasTravauxDisruption"
    disruptions = "disruptions"


class Train:
    def __init__(self, data):
        self.data = data
        if(len(self.deservedStations) > 0 and 'stations' not in self.deservedStations[0]):
            for i in range(len(self.deservedStations)):
                self.deservedStations[i]['station'] = Station.find_station(self.deservedStations[i]['label'])

    def __getattr__(self, key):
        if(key in TrainType.__members__):
            return self.data[key]
