import java.lang


class KeyRange(object):
    """
    Class for holding a range of database keys (long values)
    """

    maxKey: long
    minKey: long



    def __init__(self, minKey: long, maxKey: long):
        """
        Constructs a new key range.  Keys must be ordered and unsigned.
        @param minKey the min key (inclusive)
        @param maxKey the max key (inclusive)
        """
        ...



    def contains(self, key: long) -> bool:
        """
        Tests if the given key is in the range.
        @param key the key to test
        @return true if the key is in the range, false otherwise
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def length(self) -> long:
        """
        Return the number of keys contained within range.
        @return number of keys contained within range
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
