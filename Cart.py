class Cart:
    def __init__(self):
        self.items=[]
    def add_item(self,item,quantity=1):
        for i in range(len(self.items)):
            if self.items[i][0]== item:
                self.items[i]=(item,self.items[i][1] +quantity)
                return
        self.items.append((item,quantity))

       # removes items
    def remove_item(self,item):
        self.items=[entry for entry in self.items if entry[0] != item] 

       # updates the list when we add products also checks if the product all exists then if yes add the quantity
    def update_quantity(self,item,quantity):
        for i in range(len(self.items)):
            if self.items[i][0]== item:
                if quantity <=0:
                    self.remove_item(item)
                else:
                    self.items[i]= (item,quantity)
                return

    def get_total_price(self):
        total = 0
        for item, quantity in self.items:
            price = self.get_price(item)
            total += price * quantity
        return total                         



# to make it simple we add a fixed price by ourselves
    def get_price(self, item):
        
        prices = {
            "apple": 8,
            "banana": 2,
            "orange": 4
        }
        return prices.get(item, 0)    
            

# this makes the cart empty by removing all the items

    def clear(self):
        self.items = []
# tells us when zhe cart is empty
    def is_empty(self):
        return len(self.items) == 0

    def list_items(self):
        for item, quantity in self.items:
            print(f"{item} x {quantity}")

