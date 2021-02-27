from typing import List
import java.lang
import java.util


class SleighUtil(object):
    """
    Utilities for Collections
    """





    def __init__(self): ...



    @staticmethod
    def compareArrays(a: List[int], b: List[int]) -> int:
        """
        Compare two byte arrays by their corresponding entries

         If the two arrays have differing lengths, the shorter precedes the longer. Otherwise, they
         are compared as in C's {@code memcmp}, except that Java {@code byte}s are signed.
        @param a the first array
        @param b the second array
        @return a comparison result as in {@link Comparable#compareTo(Object)}
        """
        ...

    @staticmethod
    def compareInOrder(a: java.util.Collection, b: java.util.Collection) -> int:
        """
        Compare two collections by their corresponding elements in order

         If the collections have differing sizes, the ordering does not matter. The smaller
         collection precedes the larger. Otherwise, each corresponding pair of elements are compared.
         Once an unequal pair is found, the collections are ordered by those elements. This is
         analogous to {@link String} comparison.
        @param a the first set
        @param b the second set
        @return a comparison result as in {@link Comparable#compareTo(Object)}
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
