import ghidra.program.model.address
import ghidra.program.model.symbol
import java.lang


class Library(ghidra.program.model.symbol.Namespace, object):
    """
    Interface for a Library namespace.
    """

    DELIMITER: unicode = u'::'
    GLOBAL_NAMESPACE_ID: long = 0x0L
    NAMESPACE_DELIMITER: unicode = u'::'
    UNKNOWN: unicode = u'<EXTERNAL>'







    def equals(self, __a0: object) -> bool: ...

    def getAssociatedProgramPath(self) -> unicode:
        """
        @return the associated program within the project which corresponds to this library
        """
        ...

    def getBody(self) -> ghidra.program.model.address.AddressSetView: ...

    def getClass(self) -> java.lang.Class: ...

    def getID(self) -> long: ...

    @overload
    def getName(self) -> unicode: ...

    @overload
    def getName(self, __a0: bool) -> unicode: ...

    def getParentNamespace(self) -> ghidra.program.model.symbol.Namespace: ...

    def getSymbol(self) -> ghidra.program.model.symbol.Symbol: ...

    def hashCode(self) -> int: ...

    def isExternal(self) -> bool: ...

    def isGlobal(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setParentNamespace(self, __a0: ghidra.program.model.symbol.Namespace) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def ID(self) -> long: ...

    @property
    def associatedProgramPath(self) -> unicode: ...

    @property
    def body(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def external(self) -> bool: ...

    @property
    def global(self) -> bool: ...

    @property
    def name(self) -> unicode: ...

    @property
    def parentNamespace(self) -> ghidra.program.model.symbol.Namespace: ...

    @parentNamespace.setter
    def parentNamespace(self, value: ghidra.program.model.symbol.Namespace) -> None: ...

    @property
    def symbol(self) -> ghidra.program.model.symbol.Symbol: ...
