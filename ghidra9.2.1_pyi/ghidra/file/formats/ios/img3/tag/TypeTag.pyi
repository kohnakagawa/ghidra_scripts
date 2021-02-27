import ghidra.file.formats.ios.img3
import ghidra.program.model.data
import java.lang


class TypeTag(ghidra.file.formats.ios.img3.AbstractImg3Tag):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDataLength(self) -> int: ...

    def getMagic(self) -> unicode: ...

    def getTotalLength(self) -> int: ...

    def getType(self) -> int: ...

    def getUnknown0(self) -> int: ...

    def getUnknown1(self) -> int: ...

    def getUnknown2(self) -> int: ...

    def getUnknown3(self) -> int: ...

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
    def type(self) -> int: ...

    @property
    def unknown0(self) -> int: ...

    @property
    def unknown1(self) -> int: ...

    @property
    def unknown2(self) -> int: ...

    @property
    def unknown3(self) -> int: ...
