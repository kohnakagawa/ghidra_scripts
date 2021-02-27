import ghidra.framework.cmd
import ghidra.framework.model
import java.lang


class SetVariableDataTypeCmd(object, ghidra.framework.cmd.Command):
    """
    Command to set the datatype on a stack variable.
    """





    @overload
    def __init__(self, var: ghidra.program.model.listing.Variable, dataType: ghidra.program.model.data.DataType, source: ghidra.program.model.symbol.SourceType):
        """
        Constructs a new command for setting the datatype on a stack/reg variable.
         Conflicting stack variables will be removed.
        @param var the variable for which to set the datatype.
        @param dataType the datatype to apply to the stack variable.
        @param source signature source
        """
        ...

    @overload
    def __init__(self, fnEntry: ghidra.program.model.address.Address, varName: unicode, dataType: ghidra.program.model.data.DataType, source: ghidra.program.model.symbol.SourceType):
        """
        Constructs a new command for setting the datatype on a stack/reg variable.
         Conflicting stack variables will be removed.
        @param fnEntry
        @param varName
        @param dataType
        @param source signature source
        """
        ...

    @overload
    def __init__(self, fnEntry: ghidra.program.model.address.Address, varName: unicode, dataType: ghidra.program.model.data.DataType, align: bool, force: bool, source: ghidra.program.model.symbol.SourceType):
        """
        Constructs a new command for setting the datatype on a stack/reg variable
        @param fnEntry
        @param varName
        @param dataType
        @param align maintain proper alignment/justification if supported by implementation (ignored for non-stack variables).
         			If false and this is a stack variable, the current stack address/offset will not change.
         			If true, the affect is implementation dependent since alignment can
         			not be performed without access to a compiler specification.
        @param force overwrite conflicting stack variables
        @param source signature source
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
