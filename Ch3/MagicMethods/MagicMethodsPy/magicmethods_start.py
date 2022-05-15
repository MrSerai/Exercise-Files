# Exercise file for Python for the C# Developer LinkedIn Learning course by Joe Marini
#python data model >> special methods

class magicmethods():
    """Someone who Lives on mars"""
 
    def __init__(self, name, size):
        self._name = name
        self._size = size
    def __str__(self):
        return f"Magic Medthods object {self._name} is {self._size}"
    
    def __repr__(self):
        return f"<magicmethods class (name:{self._name}),(size:{self._size})>"
    pass
class Martian:
       pass
#mm1 = magicmethods("Obj1", 10)
#mm2 = magicmethods("Obj2", 20)
#mm3 = magicmethods("Obj1", 10)

#print(mm1)
#print(repr(mm1))

#the line below shows more of the magic methods
print(dir(magicmethods))


Mm=Martian()
#the __dict__ method returns a classes/object Attributes
print(Mm.__dict__)
Mm.first_name='Owen'
Mm.last_name="Phelp"
print(Mm.__dict__)


#the  __doc__ method returns the documentation text within  the class
print(magicmethods.__doc__)