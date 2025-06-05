import pytest
from Cart import Cart  # Replace with the actual import

@pytest.fixture
def empty_cart():
    return Cart()

def test_add_new_item(empty_cart):
    # Arrange
    cart = empty_cart

    # Act
    cart.add_item("apple", 2)

    # Assert
    assert ("apple", 2) in cart.items
    assert cart.get_total_price() == 6  # $3 * 2

def test_add_existing_item(empty_cart):
    # Arrange
    cart = empty_cart
    cart.add_item("apple", 2)

    # Act
    cart.add_item("apple", 3)

    # Assert
    assert ("apple", 5) in cart.items
    assert cart.get_total_price() == 15  # $3 * 5

def test_remove_item(empty_cart):
    # Arrange
    cart = empty_cart
    cart.add_item("apple", 2)

    # Act
    cart.remove_item("apple")

    # Assert
    assert cart.is_empty()

def test_update_quantity_increase(empty_cart):
    # Arrange
    cart = empty_cart
    cart.add_item("banana", 1)

    # Act
    cart.update_quantity("banana", 5)

    # Assert
    assert ("banana", 5) in cart.items
    assert cart.get_total_price() == 10  # $2 * 5

def test_update_quantity_to_zero_removes_item(empty_cart):
    # Arrange
    cart = empty_cart
    cart.add_item("banana", 1)

    # Act
    cart.update_quantity("banana", 0)

    # Assert
    assert cart.is_empty()

def test_get_total_price_multiple_items(empty_cart):
    # Arrange
    cart = empty_cart
    cart.add_item("apple", 2)   # $3 * 2 = 6
    cart.add_item("banana", 3)  # $2 * 3 = 6
    cart.add_item("orange", 1)  # $4 * 1 = 4

    # Act
    total = cart.get_total_price()

    # Assert
    assert total == 16

def test_clear_cart(empty_cart):
    # Arrange
    cart = empty_cart
    cart.add_item("apple", 2)

    # Act
    cart.clear()

    # Assert
    assert cart.is_empty()

def test_is_empty_on_new_cart():
    # Arrange & Act
    cart = Cart()

    # Assert
    assert cart.is_empty()

def test_list_items_prints(capsys):
    # Arrange
    cart = Cart()
    cart.add_item("apple", 1)
    cart.add_item("banana", 2)

    # Act
    cart.list_items()
    captured = capsys.readouterr()

    # Assert
    assert "apple x 1" in captured.out
    assert "banana x 2" in captured.out
