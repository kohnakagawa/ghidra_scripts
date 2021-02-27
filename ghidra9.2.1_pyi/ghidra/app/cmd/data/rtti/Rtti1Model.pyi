import ghidra.app.cmd.data
import ghidra.app.cmd.data.rtti
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.listing
import java.lang


class Rtti1Model(ghidra.app.cmd.data.rtti.AbstractCreateRttiDataModel):
    DATA_TYPE_NAME: unicode = u'RTTIBaseClassDescriptor'



    def __init__(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.Address, __a2: ghidra.app.util.datatype.microsoft.DataValidationOptions): ...



    def checkAgainstMaxCount(self, __a0: unicode, __a1: int, __a2: int) -> None: ...

    def checkEntryCount(self, __a0: unicode, __a1: int, __a2: int) -> None: ...

    def checkNonNegative(self, __a0: unicode, __a1: int) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getAddress(self) -> ghidra.program.model.address.Address: ...

    def getAttributes(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getCount(self) -> int: ...

    @overload
    def getDataType(self) -> ghidra.program.model.data.DataType: ...

    @overload
    @staticmethod
    def getDataType(__a0: ghidra.program.model.listing.Program) -> ghidra.program.model.data.DataType: ...

    def getMDisp(self) -> int: ...

    def getName(self) -> unicode: ...

    def getNumBases(self) -> int: ...

    def getPDisp(self) -> int: ...

    def getProgram(self) -> ghidra.program.model.listing.Program: ...

    def getRtti0Address(self) -> ghidra.program.model.address.Address: ...

    def getRtti0Model(self) -> ghidra.app.cmd.data.TypeDescriptorModel: ...

    def getRtti3Address(self) -> ghidra.program.model.address.Address: ...

    def getRtti3Model(self) -> ghidra.app.cmd.data.rtti.Rtti3Model: ...

    def getVDisp(self) -> int: ...

    def hashCode(self) -> int: ...

    def isBlockedByInstructions(self) -> bool: ...

    def isDataTypeAlreadyBasedOnCount(self) -> bool: ...

    def isLoadedAndInitializedAddress(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def refersToRtti0(self, __a0: ghidra.program.model.address.Address) -> bool: ...

    def toString(self) -> unicode: ...

    def validate(self) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def MDisp(self) -> int: ...

    @property
    def PDisp(self) -> int: ...

    @property
    def VDisp(self) -> int: ...

    @property
    def attributes(self) -> int: ...

    @property
    def dataType(self) -> ghidra.program.model.data.DataType: ...

    @property
    def name(self) -> unicode: ...

    @property
    def numBases(self) -> int: ...

    @property
    def rtti0Address(self) -> ghidra.program.model.address.Address: ...

    @property
    def rtti0Model(self) -> ghidra.app.cmd.data.TypeDescriptorModel: ...

    @property
    def rtti3Address(self) -> ghidra.program.model.address.Address: ...

    @property
    def rtti3Model(self) -> ghidra.app.cmd.data.rtti.Rtti3Model: ...