import ghidra.app.util.bin.format.macos.asd
import java.lang


class Entry(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getEntryDescriptor(self) -> ghidra.app.util.bin.format.macos.asd.EntryDescriptor: ...

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
    def entryDescriptor(self) -> ghidra.app.util.bin.format.macos.asd.EntryDescriptor: ...
