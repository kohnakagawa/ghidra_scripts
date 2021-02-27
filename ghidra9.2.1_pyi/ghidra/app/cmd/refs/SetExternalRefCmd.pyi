import ghidra.framework.cmd
import ghidra.framework.model
import java.lang


class SetExternalRefCmd(object, ghidra.framework.cmd.Command):
    """
    Command class for adding external references.
    """





    @overload
    def __init__(self, fromAddr: ghidra.program.model.address.Address, opIndex: int, extName: unicode, extLabel: unicode, extAddr: ghidra.program.model.address.Address, source: ghidra.program.model.symbol.SourceType):
        """
        Constructs a new command for adding an external reference from data using {@link RefType#DATA}.
        @param fromAddr from address (source of the reference)
        @param opIndex operand index
        @param extName name of external program
        @param extLabel label within the external program, may be null if extAddr is not null
        @param extAddr address within the external program, may be null
        @param source the source of this reference
        @deprecated the other constructor form should be used with an appropriate RefType specified.
         {@link RefType#DATA} should be used for address table pointer references.
        """
        ...

    @overload
    def __init__(self, fromAddr: ghidra.program.model.address.Address, opIndex: int, extName: unicode, extLabel: unicode, extAddr: ghidra.program.model.address.Address, refType: ghidra.program.model.symbol.RefType, source: ghidra.program.model.symbol.SourceType):
        """
        Constructs a new command for adding external references.
        @param fromAddr from address (source of the reference)
        @param opIndex operand index
        @param extName name of external program
        @param extLabel label within the external program, may be null if extAddr is not null
        @param extAddr address within the external program, may be null
        @param refType reference type (NOTE: data/pointer should generally utilize {@link RefType#DATA}
        @param source the source of this reference
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
