import ghidra.app.util.bin
import ghidra.app.util.bin.format.macos.rm
import java.lang


class ResourceTypeFactory(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getResourceObject(reader: ghidra.app.util.bin.BinaryReader, header: ghidra.app.util.bin.format.macos.rm.ResourceHeader, resourceType: ghidra.app.util.bin.format.macos.rm.ResourceType) -> object: ...

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
