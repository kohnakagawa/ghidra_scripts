from typing import List
import java.lang


class MultiComparableArrayIterator(object):
    """
    MultiComparableArrayIterator takes multiple arrays of comparable
     objects and iterates through them simultaneously. The arrays must contain objects
     that are comparable within each array and between the multiple arrays.
     All arrays must be sorted in ascending order when handed to this class.
     Iterating returns the next object(s) from one or more of the arrays based on
     the compareTo() of the next objects in each of the arrays. If a particular
     array doesn't contain the next object, based on all arrays, then a null is
     returned as the next object for that array.
    """





    @overload
    def __init__(self, __a0: List[java.lang.Comparable]): ...

    @overload
    def __init__(self, __a0: List[java.lang.Comparable], __a1: bool): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hasNext(self) -> bool:
        """
        Determines whether or not any of the original arrays has a
          next object.
        @return true if a next object can be obtained from any of
         the comparable object arrays.
        """
        ...

    def hashCode(self) -> int: ...

    def next(self) -> List[object]:
        """
        Returns the next comparable object(s). The next object could be from any
         one or more of the arrays. The object array returned corresponds to the
         comparable arrays originally passed to the constructor. All objects
         returned are effectively the same as determined by the compareTo() method.
         If the next object for one of the original comparable arrays is not the
         same as the next overall object, then a null is returned in its place.
        @return an array with the next object found for each of the original arrays.
         Some of these may be null, indicating the corresponding comparable array
         didn't possess the next object. However, that comparable array may still
         have objects on subsequent calls.
         There will be as many elements in this array as the number of comparable
         arrays passed to the constructor.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
