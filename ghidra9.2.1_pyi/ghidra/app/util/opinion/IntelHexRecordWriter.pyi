from typing import List
import ghidra.app.util.opinion
import ghidra.program.model.address
import java.lang


class IntelHexRecordWriter(object):




    def __init__(self, maxBytesPerLine: int, dropExtraBytes: bool):
        """
        Constructor
        @param maxBytesPerLine the maximum number of bytes to write per line in the hex output
        @param dropExtraBytes if true, only lines matching {@link #maxBytesPerLine} will be output;
         remaining bytes will be left out
        """
        ...



    def addByte(self, address: ghidra.program.model.address.Address, b: int) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def finish(self, entryPoint: ghidra.program.model.address.Address) -> List[ghidra.app.util.opinion.IntelHexRecord]: ...

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
