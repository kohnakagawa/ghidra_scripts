import java.lang


class DataTypeInfo(object):




    def __init__(self, dataTypeHandle: object, dataTypeLength: int, dataTypeAlignment: int):
        """
        Constructor for DataTypeInfo.
        @param dataTypeHandle any Object providing identity for this data type
        @param dataTypeLength the length of the data type
        @param dataTypeAlignment the alignment of the data type
        """
        ...



    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDataTypeAlignment(self) -> int: ...

    def getDataTypeHandle(self) -> object: ...

    def getDataTypeLength(self) -> int: ...

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
    def dataTypeAlignment(self) -> int: ...

    @property
    def dataTypeHandle(self) -> object: ...

    @property
    def dataTypeLength(self) -> int: ...
