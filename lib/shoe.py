#!/usr/bin/env python3

class Shoe:
    # first test
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "Old"
# test if worked 
# stan_smith = Shoe("Adidas", 9) 
# print(stan_smith.brand)
# print(stan_smith.size)

    # second test
    @property
    def size(self):
        return self._size
    @size.setter
    def size(self, value):
        # shoesize should be int
        if not isinstance (value, int) :
            print("size must be an integer")
        self._size = value

# s = Shoe("Nike", "large")
# print(s.size)
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

stan_smith = Shoe("Adidas", 9)
stan_smith.cobble()
assert(stan_smith.condition == "New")