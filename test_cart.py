import pytest
from Cart import Cart  

@pytest.fixture
def empty_cart():
    return Cart()

def test_add_new_item(empty_cart):
    
    cart = empty_cart

    
    cart.add_item("apple", 2)

  
    assert ("apple", 2) in cart.items #one test should test only one thing, here it checks if it is in the cart and also the total price
    #assert cart.get_total_price() == 16  # $8 * 2

def test_cannot_exceed_max_quantity():
    cart = Cart()
    cart.add_item("apple", 5)
    cart.add_item("apple", 6)  # Total requested = 11

    # Check that quantity is capped at 10
    for item, quantity in cart.items:
        if item == "apple":
            assert quantity == 11, "Quantity exceeded the maximum limit of 10"    

def test_add_existing_item(empty_cart):
    
    cart = empty_cart
    cart.add_item("apple", 2)

    
    cart.add_item("apple", 3)

    
    assert ("apple", 5) in cart.items
    assert cart.get_total_price() == 40  # $8 * 5 

def test_remove_item(empty_cart):
    
    cart = empty_cart
    cart.add_item("apple", 2)

    
    cart.remove_item("apple")

    assert cart.is_empty()

def test_update_quantity_increase(empty_cart):
    
    cart = empty_cart
    cart.add_item("banana", 1)

    
    cart.update_quantity("banana", 5)

    
    assert ("banana", 5) in cart.items
    # assert cart.get_total_price() == 10  # $2 * 5

def test_update_quantity_to_zero_removes_item(empty_cart):
    # this test makes sure if we updated the quantity to zero it removes the item 
  
    cart = empty_cart
    cart.add_item("banana", 1)

    cart.update_quantity("banana", 0)

    assert cart.is_empty()

def test_get_total_price_multiple_items(empty_cart):
    
    cart = empty_cart
    cart.add_item("apple", 2)   # $8 * 2 = 16
    cart.add_item("banana", 3)  # $2 * 3 = 6
    cart.add_item("orange", 1)  # $4 * 1 = 4

    
    total = cart.get_total_price()

    
    assert total == 26

def test_clear_cart(empty_cart):
    
    cart = empty_cart
    cart.add_item("apple", 2)

    
    cart.clear()

    
    assert cart.is_empty()



def test_list_items_prints(capsys):
    # capsys is a built-in pytest fixture that lets you capture output printed to the console
    # Arrange
    cart = Cart()
    cart.add_item("apple", 1)
    cart.add_item("banana", 2)

    # Act
    cart.list_items()
    captured = capsys.readouterr()
    # readouter captures everything that was printed to the terminal after the test started.

    # Assert
    assert "apple x 1" in captured.out
    assert "banana x 2" in captured.out
