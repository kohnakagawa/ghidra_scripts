from typing import List
import java.lang


class IntSet(object):
    """
    Class for storing a set of integers
    """





    @overload
    def __init__(self, capacity: int):
        """
        Constructs a new empty int set
        @param capacity the initial storage size, the set will grow if needed.
        """
        ...

    @overload
    def __init__(self, values: List[int]):
        """
        Constructs a new IntSet and populates it with the given array of ints.
        @param values the array if ints to add to the set.
        """
        ...



    def add(self, value: int) -> None:
        """
        Add the int value to the set.
        @param value the value to add to the set.
        """
        ...

    def clear(self) -> None:
        """
        Removes all values from the set.
        """
        ...

    def contains(self, value: int) -> bool:
        """
        Returns true if the set contains the given value.
        @param value the value to test if it is in the set.
        @return true if the value is in the set.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getValues(self) -> List[int]:
        """
        Returns an array with all the values in the set.
        """
        ...

    def hashCode(self) -> int: ...

    def isEmpty(self) -> bool:
        """
        Returns true if the set is empty
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def remove(self, value: int) -> bool:
        """
        Removes the int value from the set.
        @param value the value to remove from the set.
        @return true if the value was in the set, false otherwise.
        """
        ...

    def size(self) -> int:
        """
        Returns the number of ints in the set.
        @return the number of ints in the set.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def empty(self) -> bool: ...

    @property
    def values(self) -> List[int]: ...
