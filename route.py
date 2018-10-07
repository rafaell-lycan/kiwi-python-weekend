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
  def price(self, bags):
    result = 0
    for route in self.route:
      result += route.price(bags)

    return result

  # get the beginning of the trip
  def source(self):
    return self.route[0].source

  def destination(self):
    return self.route[-1].destination

  # filter by the amount of bags
  def bags_allowed(self, bags):
    for route in self.route:
      if route.bags_allowed < bags:
        return False

    return True

  # check if the source/destination are different in each leg
  def is_valid(self):
    for pair in combinations(self.route, 2):
      if (pair[0].source == pair[1].source and
        pair[0].destination == pair[1].destination):
        return False

    return True

  # add a flight to a route
  def add_route(self, flight):
    self.route.append(flight)
