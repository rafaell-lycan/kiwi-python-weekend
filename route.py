from itertools import combinations
from flight import Flight

class Route(object):

  # constructor
  def __init__(self, first_flight):
    self.route = [first_flight]
    self.current = 0

  def flights(self):
    return self.route

  # get price based on the amount of bags
  def price(self):
    result = 0
    for route in self.route:
      result += route.price()

    return result

  # get the beginning of the trip
  def source(self):
    return self.route[0].source

  def destination(self):
    return self.route[-1].destination

  # add a flight to a route
  def add_route(self, flight):
    self.route.append(flight)
