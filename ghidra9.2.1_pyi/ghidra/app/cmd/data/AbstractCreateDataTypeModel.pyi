import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.listing
import java.lang


class AbstractCreateDataTypeModel(object):




    @overload
    def __init__(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.Address, __a2: ghidra.app.util.datatype.microsoft.DataValidationOptions): ...

    @overload
    def __init__(self, __a0: ghidra.program.model.listing.Program, __a1: int, __a2: ghidra.program.model.address.Address, __a3: ghidra.app.util.datatype.microsoft.DataValidationOptions): ...



    def checkAgainstMaxCount(self, __a0: unicode, __a1: int, __a2: int) -> None: ...

    def checkEntryCount(self, __a0: unicode, __a1: int, __a2: int) -> None: ...

    def checkNonNegative(self, __a0: unicode, __a1: int) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getAddress(self) -> ghidra.program.model.address.Address: ...

    def getClass(self) -> java.lang.Class: ...

    def getCount(self) -> int: ...

    def getDataType(self) -> ghidra.program.model.data.DataType: ...

    def getName(self) -> unicode: ...

    def getProgram(self) -> ghidra.program.model.listing.Program: ...

    def hashCode(self) -> int: ...

    def isBlockedByInstructions(self) -> bool: ...

    def isDataTypeAlreadyBasedOnCount(self) -> bool: ...

    def isLoadedAndInitializedAddress(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    def validate(self) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def address(self) -> ghidra.program.model.address.Address: ...

    @property
    def blockedByInstructions(self) -> bool: ...

    @property
    def count(self) -> int: ...

    @property
    def dataType(self) -> ghidra.program.model.data.DataType: ...

    @property
    def dataTypeAlreadyBasedOnCount(self) -> bool: ...

    @property
    def loadedAndInitializedAddress(self) -> bool: ...

    @property
    def name(self) -> unicode: ...

    @property
    def program(self) -> ghidra.program.model.listing.Program: ...