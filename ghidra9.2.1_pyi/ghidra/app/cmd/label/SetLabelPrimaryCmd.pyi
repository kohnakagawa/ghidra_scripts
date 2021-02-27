import ghidra.framework.cmd
import ghidra.framework.model
import ghidra.program.model.symbol
import java.lang


class SetLabelPrimaryCmd(object, ghidra.framework.cmd.Command):
    """
    Command to make a label the primary label at an address.  Only really
     makes sense if there is more than one label at the address - otherwise
     the label will already be primary.
    """





    def __init__(self, addr: ghidra.program.model.address.Address, name: unicode, namespace: ghidra.program.model.symbol.Namespace):
        """
        Constructs a new command for setting the primary state of a label.
        @param addr the address of the label to make primary.
        @param name the name of the label to make primary.
        @param namespace the parent namespace of the label to make primary.
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

    def getSymbol(self) -> ghidra.program.model.symbol.Symbol:
        """
        Get transformed symbol
        @return symbol (may be null if command did not execute successfully)
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

    @property
    def symbol(self) -> ghidra.program.model.symbol.Symbol: ...
