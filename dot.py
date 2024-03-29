class Person:
    granularity = 20
    radius = 0.25

    def __init__(self, id, pos0, target, mass):
        self.id = id
        self.position = pos0
        self.target = target
        self.mass = mass
        self.velocity = (self.target[0] - self.position[0], self.target[1] - self.position[1])

    def vector(self):
        return (self.target[0] - self.position[0], self.target[1] - self.position[1])

    def move(self):
        self.position = (self.position[0] + (self.velocity[0] / Person.granularity), self.position[1] + (self.velocity[1] / Person.granularity))
        return self.position
        
class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self):
        return self.a + self.b

    def __sub__(self):
        return self.a - self.b
    
    