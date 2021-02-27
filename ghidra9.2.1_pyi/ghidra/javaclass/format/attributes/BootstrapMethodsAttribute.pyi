from typing import List
import ghidra.javaclass.format.attributes
import ghidra.program.model.data
import java.lang


class BootstrapMethodsAttribute(ghidra.javaclass.format.attributes.AbstractAttributeInfo):




    def __init__(self, __a0: ghidra.app.util.bin.BinaryReader): ...



    def equals(self, __a0: object) -> bool: ...

    def getAttributeLength(self) -> int: ...

    def getAttributeNameIndex(self) -> int: ...

    def getBootstrapMethods(self) -> List[ghidra.javaclass.format.attributes.BootstrapMethods]: ...

    def getClass(self) -> java.lang.Class: ...

    def getNumberOfBootstrapMethods(self) -> int: ...

    def getOffset(self) -> long: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toDataType(self) -> ghidra.program.model.data.DataType: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def bootstrapMethods(self) -> List[ghidra.javaclass.format.attributes.BootstrapMethods]: ...

    @property
    def numberOfBootstrapMethods(self) -> int: ...