"""
Find Combinations
"""

from route import Route
from utils import parse_flight, add_flight, display_flights, load_flights

# main program
def main():
  flights = []
  routes = []

  lines = load_flights()

  for line in lines:
    flights.append(parse_flight(line))

  for flight in flights:
    flight.add_connections(flights)

  for flight in flights:
    if len(flight.connections) != 0:
      routes.append(Route(flight))

  for i in range(len(routes)):
    add_flight(routes, i)

  #print bags
  display_flights(routes, 0)
  display_flights(routes, 1)
  display_flights(routes, 2)

# if main module
if __name__ == "__main__":
  main()
