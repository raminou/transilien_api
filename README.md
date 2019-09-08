# Transilien API

Unofficial Python API using by [transilien.com](http://transilien.com)

 ## Usage

Install the environment
```shell script
pip install -r requirements.txt
```

### Next trains

Look for the next trains at a station
```python
from models.trip import Trip

trip = Trip.next_trains("GARE DE PARIS AUSTERLITZ")
```

Trip object attributes are:

 - `trip.platformAvailable` *(boolean)*: ?
 - `trip.disruptionsAvailable` *(boolean)*: ?
 - `trip.arrivalTimeAvailable` *(boolean)*: ?
 - `trip.nextTrainsList` *(list[[Train](train)])*: List of the next trains
 - `trip.departureStopArea` *(dict})*: Details about departure station
 - `trip.arrivalStopArea` *(obj)*: Details about arrival station

### Places

Search for a place
```python
from models.station import Station

for place in Station.search_list_places("chatelet"):
    print(place['name'])
```

Place object attributes are:

 - `place.id` *(string)*: id
 - `place.placeType` *(string)*: ?
 - `place.name` *(string)*: Place name
 - `place.shortName` *(string)*: Station name
 - `place.coord` *(dict{lat, lon})*: Geographic coordinate
 - `place.train` *(boolean)*: is there trains
 - `place.bus` *(boolean)*: is there bus
 - `place.rer` *(boolean)*: is there RER
 - `place.tramway` *(boolean)*: is there tramway
 - `place.metro` *(boolean)*: is there metro
 - `place.navette` *(boolean)*: is there shuttle bus

### Stations 

Get more information about a station
```python
from models.station import Station

station = Station.find_station("GARE DE PARIS AUSTERLITZ")
```

Station object attributes are:

 - label *(string)*: Station name
 - value *(?)*: ?
 - coordonneeX *(?)*: ?
 - coordonneeY *(?)*: ?
 - name *(?)*: ?
 - typeRue *(?)*: ?
 - city *(?)*: ?
 - coordLambertX *(?)*: ?
 - coordLambertY *(?)*: ?
 - uic *(string)*: UIC
 - train *(boolean)*: is there trains
 - rer *(boolean)*: is there RER
 - tramway *(boolean)*: is there tramway
 - metro *(boolean)*: is there metro
 - bateau *(boolean)*: is there boat
 - navette *(boolean)*: is there shuttle bus
 - bus *(boolean)*: is there bus
 - stopPoint *(?)*: ?
 - ratp *(boolean)*: is it RATP
 - sncf *(boolean)*: is it SNCF
 - keywords *(List[string])*: other names
 - tempsReel *(boolean)*: is it real time
 - lignes *(boolean)*: ?
 - entryPointType *(?)*: ?

### Train

Train object attributes are:

 - modeTransportEnum *(string)*
 - lineTransportEnum *(string)*
 - typeTrain *(string)*
 - codeMission *(string)*
 - canceled *(boolean)*
 - delayed *(boolean)*
 - departureTime *(string)*
 - arrivalTime *(string)*
 - destinationMission *(string)*
 - platform *(string)*
 - deservedStations *(List[dict{label, time}])*
 - hastringaficDisruption *(boolean)*
 - hastringavauxDisruption *(boolean)*
 - disruptions *(List[[Disruption](disruption)])*
 
### Disruption
 
Disruption object attributes are:

 - id *(string)*: ?
 - creationDate *(string)*: creation date of the disruption
 - updateDate *(string)*: update date of the disruption
 - title *(string)*: title
 - type *(string)*: disruption type
 - validityPeriods *(List[dict{startDate, endDate, now}])*: period when there is the disruption 
 - detail *(string)*: detail in HTML
 - startingApplicationDate *(string)*: disruption begin
 - hasSubstitutionBus *(boolean)*: is there some substitution bus
 - line *(string)*: Line detail
 - transport *(string)*: ?
 
More informations on [`swagger.yml`](swagger.yml)