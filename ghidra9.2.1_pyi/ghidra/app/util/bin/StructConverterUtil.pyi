from typing import List
import ghidra.program.model.data
import java.lang


class StructConverterUtil(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def main(args: List[unicode]) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def parseName(clazz: java.lang.Class) -> unicode: ...

    @overload
    @staticmethod
    def toDataType(clazz: java.lang.Class) -> ghidra.program.model.data.DataType:
        """
        This is a convenience method for converting a class into structure.
         The class is reflected to extract the field members.
         Only private non-static fields are considered.
         Any field names that start with underscore ("_") are ignored.
        @param clazz the class to reflect
        @return a structure representing the class fields.
        """
        ...

    @overload
    @staticmethod
    def toDataType(object: object) -> ghidra.program.model.data.DataType:
        """
        This is a convenience method for converting a class into structure.
         The class is reflected to extract the field members.
         Only private non-static fields are considered.
         Any field names that start with underscore ("_") are ignored.
        @param object the object to reflect
        @return a structure representing the class fields.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
