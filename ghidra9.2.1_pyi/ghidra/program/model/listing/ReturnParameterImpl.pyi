from typing import List
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.program.model.pcode
import ghidra.program.model.symbol
import java.lang


class ReturnParameterImpl(ghidra.program.model.listing.ParameterImpl):
    """
    ReturnParameterImpl represent the function return value.
     This is special type of parameter whose ordinal is -1 and allows for the use
     of the 'void' datatype.
    """





    @overload
    def __init__(self, dataType: ghidra.program.model.data.DataType, program: ghidra.program.model.listing.Program):
        """
        Construct a return parameter which has no specific storage specified.
        @param dataType a fixed-length datatype.  (NOTE: Should be cloned to program datatype manager
         prior to determining storage elements since their length may change)
        @param program target program
        @throws InvalidInputException if dataType restrictions are violated
        """
        ...

    @overload
    def __init__(self, param: ghidra.program.model.listing.Parameter, program: ghidra.program.model.listing.Program):
        """
        Construct a return parameter from another.
        @param param parameter to be copied
        @param program target program
        @throws InvalidInputException if dataType restrictions are violated
        """
        ...

    @overload
    def __init__(self, dataType: ghidra.program.model.data.DataType, stackOffset: int, program: ghidra.program.model.listing.Program):
        """
        Construct a return parameter at the specified stack offset.
        @param dataType a fixed-length datatype.  (NOTE: Should be cloned to program datatype manager
         prior to determining storage elements since their length may change)
        @param stackOffset stack offset
        @param program target program
        @throws InvalidInputException if dataType restrictions are violated, an invalid storage
         address is specified, or unable to resolve storage element for specified datatype
        """
        ...

    @overload
    def __init__(self, dataType: ghidra.program.model.data.DataType, storageAddr: ghidra.program.model.address.Address, program: ghidra.program.model.listing.Program):
        """
        Construct a return parameter with a single varnode at the specified address.
        @param dataType a fixed-length datatype.  (NOTE: Should be cloned to program datatype manager
         prior to determining storage elements since their length may change)
        @param storageAddr storage address or null if no storage has been identified
        @param program target program
        @throws InvalidInputException if dataType restrictions are violated, an invalid storage
         address is specified, or unable to resolve storage element for specified datatype
        """
        ...

    @overload
    def __init__(self, dataType: ghidra.program.model.data.DataType, register: ghidra.program.model.lang.Register, program: ghidra.program.model.listing.Program):
        """
        Construct a return parameter using the specified register.
        @param dataType a fixed-length datatype.  (NOTE: Should be cloned to program datatype manager
         prior to determining storage elements since their length may change)
        @param register storage register
        @param program target program
        @throws InvalidInputException if dataType restrictions are violated, an invalid storage
         address is specified, or unable to resolve storage element for specified datatype
        """
        ...

    @overload
    def __init__(self, dataType: ghidra.program.model.data.DataType, storage: ghidra.program.model.listing.VariableStorage, program: ghidra.program.model.listing.Program):
        """
        Construct a return parameter with one or more associated storage elements.  Storage elements
         may get slightly modified to adjust for the resolved datatype size.
        @param dataType a fixed-length datatype.  (NOTE: Should be cloned to program datatype manager
         prior to determining storage elements since their length may change)
        @param storage variable storage or null for unassigned storage
        @param program target program
        @throws InvalidInputException if dataType restrictions are violated, an invalid storage
         element is specified, or error while resolving storage element for specified datatype
        """
        ...

    @overload
    def __init__(self, dataType: ghidra.program.model.data.DataType, storage: ghidra.program.model.listing.VariableStorage, force: bool, program: ghidra.program.model.listing.Program):
        """
        Construct a return parameter with one or more associated storage elements.  Storage elements
         may get slightly modified to adjust for the resolved datatype size.
        @param dataType a fixed-length datatype.  (NOTE: Should be cloned to program datatype manager
         prior to determining storage elements since their length may change)
        @param storage variable storage or null for unassigned storage
        @param force if true storage will be forced even if incorrect size
        @param program target program
        @throws InvalidInputException if dataType restrictions are violated, an invalid storage
         element is specified, or error while resolving storage element for specified datatype
        """
        ...



    def compareTo(self, __a0: object) -> int: ...

    def equals(self, obj: object) -> bool: ...

    def getAutoParameterType(self) -> ghidra.program.model.listing.AutoParameterType: ...

    def getClass(self) -> java.lang.Class: ...

    def getComment(self) -> unicode: ...

    def getDataType(self) -> ghidra.program.model.data.DataType: ...

    def getFirstStorageVarnode(self) -> ghidra.program.model.pcode.Varnode: ...

    def getFirstUseOffset(self) -> int: ...

    def getFormalDataType(self) -> ghidra.program.model.data.DataType: ...

    def getFunction(self) -> ghidra.program.model.listing.Function: ...

    def getLastStorageVarnode(self) -> ghidra.program.model.pcode.Varnode: ...

    def getLength(self) -> int: ...

    def getMinAddress(self) -> ghidra.program.model.address.Address: ...

    def getName(self) -> unicode: ...

    def getOrdinal(self) -> int: ...

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

    def isAutoParameter(self) -> bool: ...

    def isCompoundVariable(self) -> bool: ...

    def isEquivalent(self, otherVar: ghidra.program.model.listing.Variable) -> bool: ...

    def isForcedIndirect(self) -> bool: ...

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

    def setName(self, name: unicode, source: ghidra.program.model.symbol.SourceType) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
