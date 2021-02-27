import ghidra.program.model.address
import ghidra.program.model.symbol
import java.lang


class GlobalNamespace(object, ghidra.program.model.symbol.Namespace):
    """
    The global namespace implementation class
    """

    DELIMITER: unicode = u'::'
    GLOBAL_NAMESPACE_ID: long = 0x0L
    GLOBAL_NAMESPACE_NAME: unicode = u'Global'
    NAMESPACE_DELIMITER: unicode = u'::'



    def __init__(self, memory: ghidra.program.model.mem.Memory):
        """
        Constructs a new GlobalNamespace
        @param memory the memory associated with this global namespace
        """
        ...



    def equals(self, obj: object) -> bool:
        """
        @see java.lang.Object#equals(java.lang.Object)
        """
        ...

    def getBody(self) -> ghidra.program.model.address.AddressSetView:
        """
        @see ghidra.program.model.symbol.Namespace#getBody()
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getID(self) -> long:
        """
        @see ghidra.program.model.symbol.Namespace#getID()
        """
        ...

    @overload
    def getName(self) -> unicode:
        """
        @see ghidra.program.model.symbol.Namespace#getName()
        """
        ...

    @overload
    def getName(self, includeNamespacePath: bool) -> unicode:
        """
        @see ghidra.program.model.symbol.Namespace#getName(boolean)
        """
        ...

    def getParentNamespace(self) -> ghidra.program.model.symbol.Namespace:
        """
        @see ghidra.program.model.symbol.Namespace#getParentNamespace()
        """
        ...

    def getSymbol(self) -> ghidra.program.model.symbol.Symbol:
        """
        @see ghidra.program.model.symbol.Namespace#getSymbol()
        """
        ...

    def hashCode(self) -> int: ...

    def isExternal(self) -> bool: ...

    def isGlobal(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setParentNamespace(self, parentNamespace: ghidra.program.model.symbol.Namespace) -> None:
        """
        @see ghidra.program.model.symbol.Namespace#setParentNamespace(ghidra.program.model.symbol.Namespace)
        """
        ...

    def toString(self) -> unicode:
        """
        @see java.lang.Object#toString()
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def ID(self) -> long: ...

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
