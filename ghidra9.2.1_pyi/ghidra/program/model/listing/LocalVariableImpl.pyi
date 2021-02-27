from typing import List
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.program.model.pcode
import ghidra.program.model.symbol
import java.lang


class LocalVariableImpl(ghidra.program.model.listing.VariableImpl, ghidra.program.model.listing.LocalVariable):




    @overload
    def __init__(self, name: unicode, dataType: ghidra.program.model.data.DataType, stackOffset: int, program: ghidra.program.model.listing.Program):
        """
        Construct a stack variable at the specified stack offset with a first-use offset of 0.
        @param name variable name or null for default naming
        @param dataType a fixed-length datatype.  (NOTE: Should be cloned to program datatype manager
         prior to determining storage elements since their length may change)
        @param stackOffset signed stack offset
        @param program target program
        @throws InvalidInputException if dataType restrictions are violated, an invalid storage
         address is specified, or unable to resolve storage element for specified datatype
        @throws AddressOutOfBoundsException if invalid stack offset specified
        """
        ...

    @overload
    def __init__(self, name: unicode, dataType: ghidra.program.model.data.DataType, stackOffset: int, program: ghidra.program.model.listing.Program, sourceType: ghidra.program.model.symbol.SourceType):
        """
        Construct a stack variable at the specified stack offset with a first-use offset of 0.
        @param name variable name
        @param dataType a fixed-length datatype.  (NOTE: Should be cloned to program datatype manager
         prior to determining storage elements since their length may change)
        @param stackOffset
        @param program target program
        @param sourceType name source type
        @throws InvalidInputException if dataType restrictions are violated, an invalid storage
         address is specified, or unable to resolve storage element for specified datatype
        @throws AddressOutOfBoundsException if invalid stack offset specified
        """
        ...

    @overload
    def __init__(self, name: unicode, firstUseOffset: int, dataType: ghidra.program.model.data.DataType, storageAddr: ghidra.program.model.address.Address, program: ghidra.program.model.listing.Program):
        """
        Construct a variable with a single storage element at the specified address.  If address
         is contained within a register it may get realigned to the register based upon the resolved
         datatype length.  Variable storage will be aligned to the least-significant portion of the
         register.
        @param name variable name or null for default naming
        @param firstUseOffset first use function-relative offset (i.e., start of scope).
        @param dataType a fixed-length datatype.  (NOTE: Should be cloned to program datatype manager
         prior to determining storage elements since their length may change)
        @param storageAddr storage address or null if no storage has been identified
        @param program target program
        @throws InvalidInputException if dataType restrictions are violated, an invalid storage
         address is specified, or unable to resolve storage element for specified datatype
        """
        ...

    @overload
    def __init__(self, name: unicode, firstUseOffset: int, dataType: ghidra.program.model.data.DataType, register: ghidra.program.model.lang.Register, program: ghidra.program.model.listing.Program):
        """
        Construct a register variable with the specified register storage.
        @param name variable name or null for default naming
        @param firstUseOffset first use function-relative offset (i.e., start of scope).
        @param dataType a fixed-length datatype.  (NOTE: Should be cloned to program datatype manager
         prior to determining storage elements since their length may change)
        @param register the register used for the storage.
        @param program target program
        @throws InvalidInputException if dataType restrictions are violated, an invalid storage
         element is specified, or error while resolving storage element for specified datatype
        """
        ...

    @overload
    def __init__(self, name: unicode, firstUseOffset: int, dataType: ghidra.program.model.data.DataType, storage: ghidra.program.model.listing.VariableStorage, program: ghidra.program.model.listing.Program):
        """
        Construct a variable with one or more associated storage elements.  Storage elements
         may get slightly modified to adjust for the resolved datatype size.
        @param name variable name or null for default naming
        @param firstUseOffset first use function-relative offset (i.e., start of scope).
        @param dataType a fixed-length datatype.  (NOTE: Should be cloned to program datatype manager
         prior to determining storage elements since their length may change)
        @param storage variable storage (may not be null)
        @param program target program
        @throws InvalidInputException if dataType restrictions are violated, an invalid storage
         element is specified, or error while resolving storage element for specified datatype
        """
        ...

    @overload
    def __init__(self, name: unicode, firstUseOffset: int, dataType: ghidra.program.model.data.DataType, storage: ghidra.program.model.listing.VariableStorage, force: bool, program: ghidra.program.model.listing.Program):
        """
        Construct a variable with one or more associated storage elements.  Storage elements
         may get slightly modified to adjust for the resolved datatype size.
        @param name variable name or null for default naming
        @param firstUseOffset first use function-relative offset (i.e., start of scope).
        @param dataType a fixed-length datatype.  (NOTE: Should be cloned to program datatype manager
         prior to determining storage elements since their length may change)
        @param storage variable storage (may not be null)
        @param force if true storage will be forced even if incorrect size
        @param program target program
        @throws InvalidInputException if dataType restrictions are violated, an invalid storage
         element is specified, or error while resolving storage element for specified datatype
        """
        ...

    @overload
    def __init__(self, name: unicode, firstUseOffset: int, dataType: ghidra.program.model.data.DataType, storageAddr: ghidra.program.model.address.Address, program: ghidra.program.model.listing.Program, sourceType: ghidra.program.model.symbol.SourceType):
        """
        Construct a variable with a single storage element at the specified address.  If address
         is contained within a register it may get realigned to the register based upon the resolved
         datatype length.  Variable storage will be aligned to the least-significant portion of the
         register.
        @param name variable name
        @param firstUseOffset first use function-relative offset (i.e., start of scope).
        @param dataType a fixed-length datatype.  (NOTE: Should be cloned to program datatype manager
         prior to determining storage elements since their length may change)
        @param storageAddr storage address or null if no storage has been identified
        @param program target program
        @param sourceType name source type
        @throws InvalidInputException if dataType restrictions are violated, an invalid storage
         address is specified, or unable to resolve storage element for specified datatype
        """
        ...

    @overload
    def __init__(self, name: unicode, firstUseOffset: int, dataType: ghidra.program.model.data.DataType, register: ghidra.program.model.lang.Register, program: ghidra.program.model.listing.Program, sourceType: ghidra.program.model.symbol.SourceType):
        """
        Construct a variable with one or more associated storage elements.  Storage elements
         may get slightly modified to adjust for the resolved datatype size.
        @param name variable name
        @param firstUseOffset first use function-relative offset (i.e., start of scope).
        @param dataType a fixed-length datatype.  (NOTE: Should be cloned to program datatype manager
         prior to determining storage elements since their length may change)
        @param register the register used for the storage.
        @param program target program
        @param sourceType name source type
        @throws InvalidInputException if dataType restrictions are violated, an invalid storage
         element is specified, or error while resolving storage element for specified datatype
        """
        ...

    @overload
    def __init__(self, name: unicode, firstUseOffset: int, dataType: ghidra.program.model.data.DataType, storage: ghidra.program.model.listing.VariableStorage, force: bool, program: ghidra.program.model.listing.Program, sourceType: ghidra.program.model.symbol.SourceType):
        """
        Construct a variable with one or more associated storage elements.  Storage elements
         may get slightly modified to adjust for the resolved datatype size.
        @param name variable name
        @param firstUseOffset first use function-relative offset (i.e., start of scope).
        @param dataType a fixed-length datatype.  (NOTE: Should be cloned to program datatype manager
         prior to determining storage elements since their length may change)
        @param storage variable storage (may not be null)
        @param force if true storage will be forced even if incorrect size
        @param program target program
        @param sourceType name source type
        @throws InvalidInputException if dataType restrictions are violated, an invalid storage
         element is specified, or error while resolving storage element for specified datatype
        """
        ...



    def compareTo(self, __a0: object) -> int: ...

    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getComment(self) -> unicode: ...

    def getDataType(self) -> ghidra.program.model.data.DataType: ...

    def getFirstStorageVarnode(self) -> ghidra.program.model.pcode.Varnode: ...

    def getFirstUseOffset(self) -> int: ...

    def getFunction(self) -> ghidra.program.model.listing.Function: ...

    def getLastStorageVarnode(self) -> ghidra.program.model.pcode.Varnode: ...

    def getLength(self) -> int: ...

    def getMinAddress(self) -> ghidra.program.model.address.Address: ...

    def getName(self) -> unicode: ...

    def getProgram(self) -> ghidra.program.model.listing.Program: ...

    def getRegister(self) -> ghidra.program.model.lang.Register: ...

    def getRegisters(self) -> List[ghidra.program.model.lang.Register]: ...

    def getSource(self) -> ghidra.program.model.symbol.SourceType: ...

    def getStackOffset(self) -> int: ...

    def getSymbol(self) -> ghidra.program.model.symbol.Symbol: ...

    def getVariableStorage(self) -> ghidra.program.model.listing.VariableStorage: ...

    def hasAssignedStorage(self) -> bool: ...

    def hasStackStorage(self) -> bool: ...

    def hashCode(self) -> int: ...

    def isCompoundVariable(self) -> bool: ...

    def isEquivalent(self, otherVar: ghidra.program.model.listing.Variable) -> bool: ...

    def isMemoryVariable(self) -> bool: ...

    def isRegisterVariable(self) -> bool: ...

    def isStackVariable(self) -> bool: ...

    def isUniqueVariable(self) -> bool: ...

    def isValid(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setComment(self, comment: unicode) -> None: ...

    @overload
    def setDataType(self, type: ghidra.program.model.data.DataType, source: ghidra.program.model.symbol.SourceType) -> None: ...

    @overload
    def setDataType(self, type: ghidra.program.model.data.DataType, align: bool, force: bool, source: ghidra.program.model.symbol.SourceType) -> None: ...

    @overload
    def setDataType(self, type: ghidra.program.model.data.DataType, storage: ghidra.program.model.listing.VariableStorage, force: bool, source: ghidra.program.model.symbol.SourceType) -> None: ...

    def setFirstUseOffset(self, firstUseOffset: int) -> bool: ...

    def setName(self, name: unicode, source: ghidra.program.model.symbol.SourceType) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def comment(self) -> unicode: ...

    @comment.setter
    def comment(self, value: unicode) -> None: ...

    @property
    def dataType(self) -> ghidra.program.model.data.DataType: ...

    @property
    def firstUseOffset(self) -> int: ...

    @firstUseOffset.setter
    def firstUseOffset(self, value: int) -> None: ...

    @property
    def function(self) -> ghidra.program.model.listing.Function: ...
