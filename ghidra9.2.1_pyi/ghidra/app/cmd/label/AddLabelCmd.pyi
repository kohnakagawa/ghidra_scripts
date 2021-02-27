import ghidra.framework.cmd
import ghidra.framework.model
import ghidra.program.model.address
import ghidra.program.model.symbol
import java.lang


class AddLabelCmd(object, ghidra.framework.cmd.Command):
    """
    Command to add a label.
    """





    @overload
    def __init__(self, addr: ghidra.program.model.address.Address, name: unicode, source: ghidra.program.model.symbol.SourceType):
        """
        Constructs a new command for adding a label.
        @param addr address where the label is to be added.
        @param name name of the new label. A null name will cause a default label be added.
        @param source the source of this symbol
        """
        ...

    @overload
    def __init__(self, addr: ghidra.program.model.address.Address, name: unicode, useLocalNamespace: bool, source: ghidra.program.model.symbol.SourceType):
        """
        Constructs a new command for adding a label.
        @param addr address where the label is to be added.
        @param name name of the new label. A null name will cause a default label
         be added.
        @param useLocalNamespace If true, the namespace will be that of the lowest level namespace
         for the indicated address. If false, the global namespace is used for the namespace.
        @param source the source of this symbol: Symbol.DEFAULT, Symbol.IMPORTED, Symbol.ANALYSIS, or Symbol.USER_DEFINED.
        """
        ...

    @overload
    def __init__(self, addr: ghidra.program.model.address.Address, name: unicode, namespace: ghidra.program.model.symbol.Namespace, source: ghidra.program.model.symbol.SourceType):
        """
        Constructs a new command for adding a label.
        @param addr address where the label is to be added.
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

    def getLabelAddr(self) -> ghidra.program.model.address.Address: ...

    def getLabelName(self) -> unicode: ...

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

    def getSymbol(self) -> ghidra.program.model.symbol.Symbol: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setLabelAddr(self, addr: ghidra.program.model.address.Address) -> None: ...

    def setLabelName(self, name: unicode) -> None: ...

    def setNamespace(self, namespace: ghidra.program.model.symbol.Namespace) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def labelAddr(self) -> ghidra.program.model.address.Address: ...

    @labelAddr.setter
    def labelAddr(self, value: ghidra.program.model.address.Address) -> None: ...

    @property
    def labelName(self) -> unicode: ...

    @labelName.setter
    def labelName(self, value: unicode) -> None: ...

    @property
    def name(self) -> unicode: ...

    @property
    def namespace(self) -> None: ...  # No getter available.

    @namespace.setter
    def namespace(self, value: ghidra.program.model.symbol.Namespace) -> None: ...

    @property
    def statusMsg(self) -> unicode: ...

    @property
    def symbol(self) -> ghidra.program.model.symbol.Symbol: ...
