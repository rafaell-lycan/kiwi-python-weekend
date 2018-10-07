"""
TODO:
3. Find the matches
4. Print the matches
"""

import sys

from datetime import datetime
from flight import Flight

DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"

# parse flight to Flight Class
def parse_flight(flight):
  params = flight.split(",")

  params[2] = datetime.strptime(params[2], DATE_FORMAT)
  params[3] = datetime.strptime(params[3], DATE_FORMAT)
  params[5] = int(params[5])
  params[6] = int(params[6])
  params[7] = int(params[7])

  return Flight(*params)

flights = []
lines = sys.stdin.read().splitlines()

for line in lines[1:]:
  flights.append(parse_flight(line))

for flight in flights:
  print(flight.flight_number, flight.price())
