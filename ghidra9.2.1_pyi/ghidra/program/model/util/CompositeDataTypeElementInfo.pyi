import ghidra.program.model.util
import java.lang


class CompositeDataTypeElementInfo(ghidra.program.model.util.DataTypeInfo):




    @overload
    def __init__(self, dataTypeInfo: ghidra.program.model.util.DataTypeInfo, dataTypeOffset: int):
        """
        Constructor for CompositeDataTypeElementInfo (copy-ish).
        @param dataTypeInfo the dataType this CompositeDataTypeElementInfo is based upon
        @param dataTypeOffset the offset of the element within the outer composite data type
        """
        ...

    @overload
    def __init__(self, dataTypeHandle: object, dataTypeOffset: int, dataTypeLength: int, dataTypeAlignment: int):
        """
        Constructor for CompositeDataTypeElementInfo.
        @param dataTypeHandle any Object providing identity for this data type
        @param dataTypeOffset the offset of the element within the outer composite data type
        @param dataTypeLength the length of the data type
        @param dataTypeAlignment the alignment of the data type
        """
        ...



    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDataTypeAlignment(self) -> int: ...

    def getDataTypeHandle(self) -> object: ...

    def getDataTypeLength(self) -> int: ...

    def getDataTypeOffset(self) -> int: ...

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
    def dataTypeOffset(self) -> int: ...
