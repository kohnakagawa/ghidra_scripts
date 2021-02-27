from typing import List
import ghidra.program.model.data
import java.lang


class DataTypeProviderContext(object):
    """
    Interface for objects that can provide new instances of dataTypes
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDataTypeComponent(self, offset: int) -> ghidra.program.model.data.DataTypeComponent:
        """
        Get one data type from buffer at the current position plus offset.
        @param offset the displacement from the current position.
        @return the data type at offset from the current position.
        @throws IndexOutOfBoundsException if offset is negative
        """
        ...

    def getDataTypeComponents(self, start: int, end: int) -> List[ghidra.program.model.data.DataTypeComponent]:
        """
        Get an array of DataTypeComponents that begin at start or before end.
           DataTypes that begin before start are not returned
           DataTypes that begin before end, but terminate after end ARE returned
        @param start start offset
        @param end end offset
        @return array of DataTypes that exist between start and end.
        """
        ...

    def getUniqueName(self, baseName: unicode) -> unicode:
        """
        Get a unique name for a data type given a prefix name
        @param baseName prefix for unique name
        @return a unique data type name
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
