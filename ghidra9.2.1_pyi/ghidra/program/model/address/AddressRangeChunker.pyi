from typing import Iterator
import ghidra.program.model.address
import java.lang
import java.util
import java.util.function


class AddressRangeChunker(object, java.lang.Iterable):
    """
    A class to break a range of addresses into 'chunks' of a give size.   This is useful to
     break-up processing of large swaths of addresses, such as when performing work in a
     background thread.  Doing this allows the client to iterator over the range, pausing
     enough to allow the UI to update.
    """





    @overload
    def __init__(self, range: ghidra.program.model.address.AddressRange, chunkSize: int): ...

    @overload
    def __init__(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address, chunkSize: int): ...

    def __iter__(self): ...

    def equals(self, __a0: object) -> bool: ...

    def forEach(self, __a0: java.util.function.Consumer) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def iterator(self) -> Iterator[ghidra.program.model.address.AddressRange]: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def spliterator(self) -> java.util.Spliterator: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
