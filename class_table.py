import random

# Table class - holds one random fries flavor
class Table:
    def __init__(self):
        self.flavors = ['Original', 'Sichuan Chili', 'Beef Gravy']
        self.current_fries = None

    # pick a random flavor
    def place_fries(self):
        self.current_fries = random.choice(self.flavors)

    # return current flavor
    def get_fries(self):
        return self.current_fries
