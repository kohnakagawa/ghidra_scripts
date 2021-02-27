import ghidra.app.plugin.core.format
import ghidra.util
import java.lang


class HexIntegerFormatModel(object, ghidra.app.plugin.core.format.UniversalDataFormatModel):
    NEXT_UNIT: int = -1
    PREVIOUS_UNIT: int = -1



    def __init__(self): ...



    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getByteOffset(self, __a0: ghidra.app.plugin.core.format.ByteBlock, __a1: int) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getColumnPosition(self, __a0: ghidra.app.plugin.core.format.ByteBlock, __a1: int) -> int: ...

    def getDataRepresentation(self, __a0: ghidra.app.plugin.core.format.ByteBlock, __a1: long) -> unicode: ...

    def getDataUnitSymbolSize(self) -> int: ...

    def getGroupSize(self) -> int: ...

    def getHelpLocation(self) -> ghidra.util.HelpLocation: ...

    def getName(self) -> unicode: ...

    def getUnitByteSize(self) -> int: ...

    def getUnitDelimiterSize(self) -> int: ...

    def hashCode(self) -> int: ...

    def isEditable(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def replaceValue(self, __a0: ghidra.app.plugin.core.format.ByteBlock, __a1: long, __a2: int, __a3: int) -> bool: ...

    def setGroupSize(self, __a0: int) -> None: ...

    def toString(self) -> unicode: ...

    def validateBytesPerLine(self, __a0: int) -> bool: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def dataUnitSymbolSize(self) -> int: ...

    @property
    def editable(self) -> bool: ...

    @property
    def groupSize(self) -> int: ...

    @groupSize.setter
    def groupSize(self, value: int) -> None: ...

    @property
    def helpLocation(self) -> ghidra.util.HelpLocation: ...

    @property
    def name(self) -> unicode: ...

    @property
    def unitByteSize(self) -> int: ...

    @property
    def unitDelimiterSize(self) -> int: ...
