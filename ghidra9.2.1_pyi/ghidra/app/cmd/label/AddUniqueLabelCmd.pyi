import ghidra.framework.cmd
import ghidra.framework.model
import ghidra.program.model.symbol
import java.lang


class AddUniqueLabelCmd(object, ghidra.framework.cmd.Command):
    """
    Command to add a label. If the label already
     exists somewhere else, the address is appended to make
     it unique.
    """





    def __init__(self, address: ghidra.program.model.address.Address, name: unicode, namespace: ghidra.program.model.symbol.Namespace, source: ghidra.program.model.symbol.SourceType):
        """
        Constructs a new command for adding a label.
        @param address address where the label is to be added.
        @param name name of the new label. A null name will cause a default label
         be added.
        @param namespace the namespace of the label. (i.e. the namespace this label is associated with)
        @param source the source of this symbol
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

    def getNewSymbol(self) -> ghidra.program.model.symbol.Symbol:
        """
        Returns the newly created symbol.
        @return the newly created symbol
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
    def newSymbol(self) -> ghidra.program.model.symbol.Symbol: ...

    @property
    def statusMsg(self) -> unicode: ...
