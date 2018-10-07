"""
TODO:
4. Print the matches
"""

import sys
from datetime import datetime
from flight import Flight, DATE_FORMAT
from route import Route

def add_flight(routes, index):
  route = routes[index]

  if len(route.flights()[-1].connections) == 0:
    return

  if len(route.flights()[-1].connections) > 1:
    for connection in route.flights()[-1].connections[1:]:
      new = Route(route.flights()[0])

      for flight in route.flights()[1:]:
        new.add_route(flight)

      new.add_route(connection)
      routes.append(new)

  route.add_route(route.flights()[-1].connections[0])

  add_flight(routes, index)


def parse_flight(flight):
  params = flight.split(",")

  params[2] = datetime.strptime(params[2], DATE_FORMAT)
  params[3] = datetime.strptime(params[3], DATE_FORMAT)
  params[5] = int(params[5])
  params[6] = int(params[6])
  params[7] = int(params[7])

  return Flight(*params)

flights = []
routes = []

lines = sys.stdin.read().splitlines()

# skip the first line of columns
for line in lines[1:]:
  flights.append(parse_flight(line))

for flight in flights:
  flight.add_connections(flights)

for flight in flights:
  if len(flight.connections) != 0:
    routes.append(Route(flight))

for i in range(len(routes)):
  add_flight(routes, i)

for route in routes:
  if route.is_valid():
    print(route.source(), route.destination(), route.price(2), len(route.flights()))
