import ghidra.framework.cmd
import ghidra.framework.model
import java.lang


class CreateDataInStructureCmd(object, ghidra.framework.cmd.Command):
    """
    Command to Create data inside of a structure.
    """





    @overload
    def __init__(self, addr: ghidra.program.model.address.Address, componentPath: List[int], dt: ghidra.program.model.data.DataType):
        """
        Constructs a new command for creating data inside a structure.
         Simple pointer conversion will NOT be performed.
        @param addr the address of the structure in which to apply the given datatype.
        @param componentPath the component path of the component where the datatype
         will be applied.
        @param dt the datatype to apply in the structure.
        """
        ...

    @overload
    def __init__(self, addr: ghidra.program.model.address.Address, componentPath: List[int], dt: ghidra.program.model.data.DataType, stackPointers: bool):
        """
        This is the same as {@link #CreateDataInStructureCmd(Address, int[], DataType)} except that
         it allows the caller to control whether or not a pointer data type is created when a
         non-pointer data type is applied at a location that previously contained a pointer data
         type.
        @param addr the address of the structure in which to apply the given datatype.
        @param componentPath the component path of the component where the datatype
         will be applied.
        @param dt the datatype to apply in the structure.
        @param stackPointers if true simple pointer conversion is enabled
         (see {@link DataUtilities#reconcileAppliedDataType(DataType, DataType, boolean)}).
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
