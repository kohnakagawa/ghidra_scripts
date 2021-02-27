import ghidra.util.datastruct
import java.io
import java.lang


class FullKeySet(object, ghidra.util.datastruct.ShortKeySet, java.io.Serializable):
    """
    Implementation of the ShortKeySet interface that always contains
     all the possible keys.  Used to save storage when sets are full.
    """





    def __init__(self, numKeys: int):
        """
        Construct a new FullKeySet
        @param numKeys the number of keys in the set.
        """
        ...



    def containsKey(self, key: int) -> bool:
        """
        @see ghidra.util.datastruct.ShortKeySet#containsKey(short)
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFirst(self) -> int:
        """
        @see ghidra.util.datastruct.ShortKeySet#getFirst()
        """
        ...

    def getLast(self) -> int:
        """
        @see ghidra.util.datastruct.ShortKeySet#getLast()
        """
        ...

    def getNext(self, key: int) -> int:
        """
        @see ghidra.util.datastruct.ShortKeySet#getNext(short)
        """
        ...

    def getPrevious(self, key: int) -> int:
        """
        @see ghidra.util.datastruct.ShortKeySet#getPrevious(short)
        """
        ...

    def hashCode(self) -> int: ...

    def isEmpty(self) -> bool:
        """
        @see ghidra.util.datastruct.ShortKeySet#isEmpty()
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def put(self, key: int) -> None:
        """
        @see ghidra.util.datastruct.ShortKeySet#put(short)
        """
        ...

    def remove(self, key: int) -> bool:
        """
        @see ghidra.util.datastruct.ShortKeySet#remove(short)
        """
        ...

    def removeAll(self) -> None:
        """
        @see ghidra.util.datastruct.ShortKeySet#removeAll()
        """
        ...

    def size(self) -> int:
        """
        Returns the number of keys currently in the set.
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
    def first(self) -> int: ...

    @property
    def last(self) -> int: ...
