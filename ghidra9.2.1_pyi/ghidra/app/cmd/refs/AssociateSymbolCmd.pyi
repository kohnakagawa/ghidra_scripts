import ghidra.framework.cmd
import ghidra.framework.model
import java.lang


class AssociateSymbolCmd(object, ghidra.framework.cmd.Command):
    """
    Command class for associating a reference with a specific label
    """





    @overload
    def __init__(self, ref: ghidra.program.model.symbol.Reference, symbolName: unicode):
        """
        Create a associate symbol command for a global symbol
        @param ref
        @param symbolName
        """
        ...

    @overload
    def __init__(self, ref: ghidra.program.model.symbol.Reference, scope: ghidra.program.model.symbol.Namespace):
        """
        Constructor.
        @param ref the reference to associate with a symbol
        @param scope scope that has the symbol to associate with the reference
        """
        ...

    @overload
    def __init__(self, ref: ghidra.program.model.symbol.Reference, symbolName: unicode, scope: ghidra.program.model.symbol.Namespace):
        """
        Constructor
        @param ref the reference to associate with a symbol
        @param symbolName the name of the symbol with which to associate the reference.
        @param scope scope of the symbol with the given symbolName
        """
        ...



    def applyTo(self, obj: ghidra.framework.model.DomainObject) -> bool:
        """
        @see ghidra.framework.cmd.Command#applyTo(ghidra.framework.model.DomainObject)
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode:
        """
        @see ghidra.framework.cmd.Command#getName()
        """
        ...

    def getStatusMsg(self) -> unicode:
        """
        @see ghidra.framework.cmd.Command#getStatusMsg()
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
    def name(self) -> unicode: ...

    @property
    def statusMsg(self) -> unicode: ...
