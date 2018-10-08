import sys
from datetime import datetime
import locale

from flight import Flight, DATE_FORMAT
from route import Route

def load_flights():
  lines = sys.stdin.read().splitlines()

  # skip the first line of columns
  return lines[1:]

def parse_flight(flight):
  params = flight.split(",")

  params[2] = datetime.strptime(params[2], DATE_FORMAT)
  params[3] = datetime.strptime(params[3], DATE_FORMAT)
  params[5] = int(params[5])
  params[6] = int(params[6])
  params[7] = int(params[7])

  return Flight(*params)

def add_flight(routes, index):
  route = routes[index]

  if len(route.flights()[-1].connections) == 0:
    return routes

  if len(route.flights()[-1].connections) > 1:
    for connection in route.flights()[-1].connections[1:]:
      new = Route(route.flights()[0])

      for flight in route.flights()[1:]:
        new.add_route(flight)

      new.add_route(connection)
      routes.append(new)

  route.add_route(route.flights()[-1].connections[0])

  add_flight(routes, index)

  return routes

def display_flights(routes, bags):
  locale.setlocale(locale.LC_ALL, '')

  # create a decorative heading
  sys.stdout.write("-------------------------\n")
  heading = "Flights where {} bag(s) is/are allowed\n" . format(bags)
  sys.stdout.write(heading)

  for route in routes:
    if route.is_valid() and route.bags_allowed(bags):
      itinerary = "{} -> {} -> {}, Price: {}€ \n" .format(route.source(), route.connections(
      ), route.destination(), locale.currency(route.price(bags), grouping=True))

      sys.stdout.write(itinerary)

  # create a new empty line
  sys.stdout.write("\n")
