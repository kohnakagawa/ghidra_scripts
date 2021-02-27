import ghidra.framework.cmd
import ghidra.framework.model
import java.lang


class CreateDataCmd(object, ghidra.framework.cmd.Command):
    """
    This command will create a data of type dataType at the given address.  This
     command will only work for fixed length dataTypes.  If there are any existing
     instructions in the area to be made into data, the command will fail.  Existing data
     in the area may be replaced with the new dataType (with optional pointer conversion).
     If the existing dataType is a pointer, then
     the existing data will be changed into a pointer to the given dataType.  If the given dataType
     is a default-pointer, it will become a pointer to the existing type.
    """





    @overload
    def __init__(self, addr: ghidra.program.model.address.Address, dataType: ghidra.program.model.data.DataType):
        """
        Constructs a command for creating data at an address.
         Simple pointer conversion will NOT be performed and existing
         defined data will not be cleared, however existing Undefined data will
         be cleared.
        @param addr the address at which to apply the datatype.
        @param dataType the datatype to be applied at the given address.
        """
        ...

    @overload
    def __init__(self, addr: ghidra.program.model.address.Address, force: bool, dataType: ghidra.program.model.data.DataType):
        """
        Constructs a command for creating data at an address.
         Simple pointer conversion will NOT be performed.
         Existing Undefined data will always be cleared even when force is false.
        @param addr the address at which to apply the datatype.  Offcut data
         address allowed, provided force==true.
        @param force if true any existing conflicting data will be cleared
        @param dataType the datatype to be applied at the given address.
        """
        ...

    @overload
    def __init__(self, addr: ghidra.program.model.address.Address, dataType: ghidra.program.model.data.DataType, isCycle: bool, stackPointers: bool):
        """
        This is the same as {@link #CreateDataCmd(Address, DataType)} except that
         it allows the caller to control whether or not pointer conversion should be handled.
         Existing Undefined data will always be cleared.
        @param addr the address at which to apply the datatype.
        @param dataType the datatype to be applied at the given address.
        @param isCycle true indicates this is from a cycle group action.
        @param stackPointers if true simple pointer conversion is enabled
         (see {@link DataUtilities#reconcileAppliedDataType(DataType, DataType, boolean)}).
        """
        ...

    @overload
    def __init__(self, addr: ghidra.program.model.address.Address, force: bool, stackPointers: bool, dataType: ghidra.program.model.data.DataType):
        """
        This is the same as {@link #CreateDataCmd(Address, boolean, DataType)} except that
         it allows the caller to control whether or not pointer conversion should be handled.
        @param addr the address at which to apply the datatype.  Offcut data
         address allowed, provided force==true.
        @param force if true any existing conflicting data will be cleared
        @param stackPointers if true simple pointer conversion is enabled
         (see {@link DataUtilities#reconcileAppliedDataType(DataType, DataType, boolean)}).
        @param dataType the datatype to be applied at the given address.
        """
        ...

    @overload
    def __init__(self, addr: ghidra.program.model.address.Address, dataType: ghidra.program.model.data.DataType, stackPointers: bool, clearMode: ghidra.program.model.data.DataUtilities.ClearDataMode):
        """
        This constructor provides the most flexibility when creating data, allowing optional pointer conversion and
         various clearing options for conflicting data.
        @param addr the address at which to apply the datatype.
        @param dataType the datatype to be applied at the given address.
        @param stackPointers if true simple pointer conversion is enabled
         (see {@link DataUtilities#reconcileAppliedDataType(DataType, DataType, boolean)}).
        @param clearMode indicates how conflicting data should be cleared
        """
        ...



    def applyTo(self, obj: ghidra.framework.model.DomainObject) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode: ...

    def getStatusMsg(self) -> unicode: ...

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
