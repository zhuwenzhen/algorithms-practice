"""
607. Two Sum III - Data structure design
Design and implement a TwoSum class.
It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example
add(1); add(3); add(5);
find(4) // return true
find(7) // return false
"""

class TwoSum:

    def __init__(self):
        # initialize your data structure here
        self.count = {}
    # Add the number to an internal data structure.
    def add(self, number):
        if number in self.count:
            self.count[number] += 1
        else:
            self.count[number] = 1
    # Find if there exists any pair of numbers which sum is equal to the value.
    # @param value {int}
    # @return true if can be found or false
    def find(self, value):
        for num in self.count:
            if value - num in self.count and \
                (value - num != num or self.count[num] > 1):
                return True
        return False