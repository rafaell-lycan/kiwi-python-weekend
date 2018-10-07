from datetime import datetime, timedelta

DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"
MIN_TIME = timedelta(hours=1)
MAX_TIME = timedelta(hours=4)

class Flight(object):

  # constructor
  def __init__(self, source, destination, departure, arrival, flight_number, price, bags_allowed, bag_price):
    self.source = source
    self.destination = destination
    self.departure = departure
    self.arrival = arrival
    self.flight_number = flight_number
    self.seat_price = price
    self.bags_allowed = bags_allowed
    self.bag_price = bag_price
    self.connections = []

  # calculate the price given the amount of bags
  def price(self, bags):
    return self.seat_price + (bags * self.bag_price)

  # add a connection the to flight
  def add_connections(self, flights):
    for flight in flights:
      if (
          self.destination == flight.source and
          MIN_TIME <= flight.departure - self.arrival <= MAX_TIME
        ):
        self.connections.append(flight)
