import java.lang


class MemoryByteIterator(object):
    """
    Class to iterate over the bytes in memory for an address set.
    """





    def __init__(self, mem: ghidra.program.model.mem.Memory, set: ghidra.program.model.address.AddressSetView):
        """
        Construct a memoryIterator
        @param mem the memory providing the bytes
        @param set the set of addresses for which to iterate bytes
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hasNext(self) -> bool:
        """
        Returns true if there are more bytes to iterate over
        """
        ...

    def hashCode(self) -> int: ...

    def next(self) -> int:
        """
        Returns the next byte.
        @throws MemoryAccessException if the next byte could not be read
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
