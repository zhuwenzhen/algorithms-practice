"""
There are many asteroids, they are stored in an array,
each asteroid has its mass and flying directions,
it can go either left or right, there is a space station in the rightmost,
you are requested to return a boolean value whether the station will be destroyed by collision.
An asteroid with bigger mass can “eat” an asteroid with small mass during collision.

Solution: use an stack

Follow-up:
can you optimize space? (reduce space to O(1))
This problem is equivalent to can you find an asteroid that go right,
which makes all the asteroids in its right side who goes left has smaller mass than it?
If an asteroid satisfy this condition, then the space station will be destroyed.
The people who posted this problem says he used this approach and passed all test cases.
"""

class asteroid:
    def __init__(self, mass, velocity):
        self.mass = mass
        self.velocity = velocity

class Solution:
    def destroyed(self, asteroids):
        momentum = 0.0
        for a in asteroids:
            momentum += a.mass * a.velocity
            if momentum > 0.0:
                return True
        return False

