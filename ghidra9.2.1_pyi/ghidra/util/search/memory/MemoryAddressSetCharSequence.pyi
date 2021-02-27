import ghidra.program.model.address
import java.lang
import java.util.stream


class MemoryAddressSetCharSequence(object, java.lang.CharSequence):
    """
    This class implements the CharSequence interface using Memory and an AddressSet.  The
     idea is that each byte in memory at the addresses specified in the AddressSet will form
     a contiguous sequence of characters.
    """





    @overload
    def __init__(self, memory: ghidra.program.model.mem.Memory, addressSet: ghidra.program.model.address.AddressSetView): ...

    @overload
    def __init__(self, memory: ghidra.program.model.mem.Memory, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address): ...



    def charAt(self, index: int) -> int: ...

    def chars(self) -> java.util.stream.IntStream: ...

    def codePoints(self) -> java.util.stream.IntStream: ...

    @staticmethod
    def compare(__a0: java.lang.CharSequence, __a1: java.lang.CharSequence) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getAddressAtIndex(self, index: int) -> ghidra.program.model.address.Address:
        """
        Takes an index and returns the matching Address
        @param index index to search on
        @return Address address matched to index
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def length(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def subSequence(self, start: int, end: int) -> java.lang.CharSequence: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
