import json
import sys
import os.path

if len(sys.argv) != 2:
    print(f'Usage: python {sys.argv[0]} <IATA CODE>')
    sys.exit(1)

iata = sys.argv[1]
with open(os.path.join(os.path.dirname(sys.argv[0]), "airports.json")) as fp:
    matching = [stn for stn in json.load(fp) if stn["iata_code"] == iata]

    if matching:
        print(f'{matching[0]["name"]}, {matching[0]["country"]}')
        print(f'Google maps: https://google.com/maps/@{matching[0]["_geoloc"]["lat"]},{matching[0]["_geoloc"]["lng"]},11z')
    else:
        print(f'No airport matching "{iata}"')
