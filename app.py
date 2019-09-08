import argparse
from terminaltables import AsciiTable
import sys
from models.trip import Trip
from models.station import Station, PlaceType

parser = argparse.ArgumentParser(description='Process some integers.')
subparsers = parser.add_subparsers(dest='command', help='commands')

# Trains parser
trains_parser = subparsers.add_parser('trains', help='Next train from the departure station')
trains_parser.add_argument('dep_station', help='Departure station')
trains_parser.add_argument('arr_station', help='Arrival station', nargs='?', default='')

# Search Places parser
search_parser = subparsers.add_parser('search', help='Next train from the departure station')
search_parser.add_argument('query', help='query')

args = parser.parse_args()
print(args)

if(args.command == "trains"):
    dep_station = Station.find_station(args.dep_station)
    if(args.arr_station != ""):
        arr_station = Station.find_station(args.arr_station)
        if(arr_station is None):
            print("Unknown arrival station")
            sys.exit(1)
    else:
        arr_station = None

    trip = Trip.next_trains(dep_station, arr_station)
    for train in trip.nextTrainsList:
        print(train)

elif(args.command == "search"):
    list_station = Station.search_list_places(args.query)
    list_attr = [attr for attr in PlaceType.__members__ if attr != PlaceType.no_filter.name]
    table = [["Name", "Station name"] + [attr[0].upper() + attr[1:] for attr in list_attr]]
    for station in list_station:
        table_station = [station['name'], station["shortName"]]
        for attr in list_attr:
            table_station += ["X" if station[attr] else ""]
        table.append(table_station)
    print(AsciiTable(table).table)
