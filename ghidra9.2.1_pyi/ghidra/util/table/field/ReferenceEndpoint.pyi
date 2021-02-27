import ghidra.program.model.address
import ghidra.program.model.symbol
import java.lang


class ReferenceEndpoint(object):
    """
    An object that is one end of a Reference.  This is used by table models that want to
     show all references from one location to many other locations or models that wish to
     show all references to one location from many other locations.
    """









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

    @property
    def address(self) -> ghidra.program.model.address.Address: ...

    @property
    def offcut(self) -> bool: ...

    @property
    def reference(self) -> ghidra.program.model.symbol.Reference: ...

    @property
    def referenceType(self) -> ghidra.program.model.symbol.RefType: ...

    @property
    def source(self) -> ghidra.program.model.symbol.SourceType: ...
