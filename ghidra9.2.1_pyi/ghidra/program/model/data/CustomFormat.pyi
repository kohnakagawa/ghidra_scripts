from typing import List
import ghidra.program.model.data
import java.lang


class CustomFormat(object):
    """
    Container object for a DataType and a byte array that is the format for
     the data type.
    """





    def __init__(self, dataType: ghidra.program.model.data.DataType, format: List[int]):
        """
        Constructor
        @param dataType data type associated with this format
        @param format bytes that define the format
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getBytes(self) -> List[int]:
        """
        Get the bytes that define this format.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDataType(self) -> ghidra.program.model.data.DataType:
        """
        Get the data type associated with this format.
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
    def bytes(self) -> List[int]: ...

    @property
    def dataType(self) -> ghidra.program.model.data.DataType: ...
