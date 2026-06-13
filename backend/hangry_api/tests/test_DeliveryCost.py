from api.controllers import Delivery
from django_mock_queries.query import MockSet, MockModel


def build_order(*quantities):
  order = MockSet()
  for quantity in quantities:
    order.add(MockModel(quantity=quantity))
  return order


def test_LotsOfItems():
  # Arrange
  order = build_order(5, 5, 5)
  delivery_distance = 6

  # Act
  cost = Delivery.calculate(order, delivery_distance)

  # Assert
  assert cost == 7.5


def test_MiddleOfTheRoadItems():
  # Arrange
  order = build_order(2, 2, 2)
  delivery_distance = 4

  # Act
  cost = Delivery.calculate(order, delivery_distance)

  # Assert
  assert cost == 5


def test_LittleItems():
  # Arrange
  order = build_order(3, 1)
  delivery_distance = 2

  # Act
  cost = Delivery.calculate(order, delivery_distance)

  # Assert
  assert cost == 3.5


def test_MoreThanTenItemsButShortDistanceGetsMiddleDeliveryFee():
  # Arrange
  order = build_order(5, 5, 1)
  delivery_distance = 4

  # Act
  cost = Delivery.calculate(order, delivery_distance)

  # Assert
  assert cost == 5


def test_ExactlyTenItemsAndLongDistanceGetsMiddleDeliveryFee():
  # Arrange
  order = build_order(5, 5)
  delivery_distance = 6

  # Act
  cost = Delivery.calculate(order, delivery_distance)

  # Assert
  assert cost == 5


def test_ExactlyFiveItemsAndMiddleDistanceGetsBaseDeliveryFee():
  # Arrange
  order = build_order(2, 3)
  delivery_distance = 4

  # Act
  cost = Delivery.calculate(order, delivery_distance)

  # Assert
  assert cost == 3.5
