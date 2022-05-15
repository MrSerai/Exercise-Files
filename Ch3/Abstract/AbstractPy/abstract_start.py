# Exercise file for Python for the C# Developer LinkedIn Learning course by Joe Marini
from abc import ABC, abstractmethod



class graphicshape(ABC):
    def __init__(self):
        super().__init__()
    @abstractmethod
    def calc_area(self):
        pass
 

class circle(graphicshape):
    def __init__(self, radius):
        self._radius = radius

    def calc_area(self):
        return 3.14*(self._radius**2)

class square(graphicshape):
    def __init__(self, side):
        self._side = side
    
    def calc_area(self):
        return self._side * self._side


#g = graphicshape()

c = circle(10)
print(c.calc_area())
s = square(12)
print(s.calc_area())
