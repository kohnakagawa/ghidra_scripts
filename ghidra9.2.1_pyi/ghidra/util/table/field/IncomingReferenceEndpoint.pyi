import ghidra.program.model.address
import ghidra.program.model.symbol
import ghidra.util.table.field
import java.lang


class IncomingReferenceEndpoint(ghidra.util.table.field.ReferenceEndpoint):
    """
    Marker row object that signals to the table API that the references contained therein all
     share the to address, with each row showing the from address.
    """





    def __init__(self, r: ghidra.program.model.symbol.Reference, isOffcut: bool): ...



    def equals(self, __a0: object) -> bool: ...

    def getAddress(self) -> ghidra.program.model.address.Address: ...

    def getClass(self) -> java.lang.Class: ...

    def getReference(self) -> ghidra.program.model.symbol.Reference: ...

    def getReferenceType(self) -> ghidra.program.model.symbol.RefType: ...

    def getSource(self) -> ghidra.program.model.symbol.SourceType: ...

    def hashCode(self) -> int: ...

    def isOffcut(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
