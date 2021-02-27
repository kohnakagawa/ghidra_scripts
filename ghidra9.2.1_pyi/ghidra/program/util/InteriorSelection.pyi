import ghidra.program.model.address
import ghidra.program.util
import java.lang


class InteriorSelection(object):
    """
    Specifies a selection that consists of components inside a structure.
    """





    def __init__(self, from_: ghidra.program.util.ProgramLocation, to: ghidra.program.util.ProgramLocation, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address):
        """
        Construct a new interior selection.
        @param from start location
        @param to end location
        @param start start address
        @param end end address
        """
        ...



    def equals(self, obj: object) -> bool:
        """
        @see java.lang.Object#equals(Object)
        """
        ...

    def getByteLength(self) -> int:
        """
        Get the number of bytes contained in the selection.
        @return int
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getEndAddress(self) -> ghidra.program.model.address.Address:
        """
        Get the end address of this selection.
        @return Address
        """
        ...

    def getFrom(self) -> ghidra.program.util.ProgramLocation:
        """
        Get the start location.
        @return ProgramLocation
        """
        ...

    def getStartAddress(self) -> ghidra.program.model.address.Address:
        """
        Get the start address of this selection.
        @return Address
        """
        ...

    def getTo(self) -> ghidra.program.util.ProgramLocation:
        """
        Get the end location.
        @return ProgramLocation
        """
        ...

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

    @property
    def byteLength(self) -> int: ...

    @property
    def endAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def from(self) -> ghidra.program.util.ProgramLocation: ...

    @property
    def startAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def to(self) -> ghidra.program.util.ProgramLocation: ...
