from typing import List
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.program.model.pcode
import ghidra.program.model.symbol
import java.lang


class LocalVariableInfo(ghidra.program.model.listing.LocalVariableImpl):








    def compareTo(self, __a0: object) -> int: ...

    def createLocalVariable(self, __a0: ghidra.program.model.listing.Function, __a1: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Variable: ...

    def equals(self, __a0: object) -> bool: ...

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

    def getRegisters(self) -> List[object]: ...

    def getSource(self) -> ghidra.program.model.symbol.SourceType: ...

    def getStackOffset(self) -> int: ...

    def getSymbol(self) -> ghidra.program.model.symbol.Symbol: ...

    def getVariableStorage(self) -> ghidra.program.model.listing.VariableStorage: ...

    def hasAssignedStorage(self) -> bool: ...

    def hasStackStorage(self) -> bool: ...

    def hashCode(self) -> int: ...

    def isCompoundVariable(self) -> bool: ...

    def isEquivalent(self, __a0: ghidra.program.model.listing.Variable) -> bool: ...

    def isMemoryVariable(self) -> bool: ...

    def isRegisterVariable(self) -> bool: ...

    def isStackVariable(self) -> bool: ...

    def isUniqueVariable(self) -> bool: ...

    def isValid(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setComment(self, __a0: unicode) -> None: ...

    @overload
    def setDataType(self, __a0: ghidra.program.model.data.DataType, __a1: ghidra.program.model.symbol.SourceType) -> None: ...

    @overload
    def setDataType(self, __a0: ghidra.program.model.data.DataType, __a1: bool, __a2: bool, __a3: ghidra.program.model.symbol.SourceType) -> None: ...

    @overload
    def setDataType(self, __a0: ghidra.program.model.data.DataType, __a1: ghidra.program.model.listing.VariableStorage, __a2: bool, __a3: ghidra.program.model.symbol.SourceType) -> None: ...

    def setFirstUseOffset(self, __a0: int) -> bool: ...

    def setName(self, __a0: unicode, __a1: ghidra.program.model.symbol.SourceType) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...