from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format.macos.cfm
import java.lang


class CFragLocatorKind(java.lang.Enum):
    kCFBundleCFragLocator: ghidra.app.util.bin.format.macos.cfm.CFragLocatorKind = kCFBundleCFragLocator
    kCFBundlePreCFragLocator: ghidra.app.util.bin.format.macos.cfm.CFragLocatorKind = kCFBundlePreCFragLocator
    kDataForkCFragLocator: ghidra.app.util.bin.format.macos.cfm.CFragLocatorKind = kDataForkCFragLocator
    kMemoryCFragLocator: ghidra.app.util.bin.format.macos.cfm.CFragLocatorKind = kMemoryCFragLocator
    kNamedFragmentCFragLocator: ghidra.app.util.bin.format.macos.cfm.CFragLocatorKind = kNamedFragmentCFragLocator
    kResourceCFragLocator: ghidra.app.util.bin.format.macos.cfm.CFragLocatorKind = kResourceCFragLocator







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def get(__a0: ghidra.app.util.bin.BinaryReader) -> ghidra.app.util.bin.format.macos.cfm.CFragLocatorKind: ...

    def getClass(self) -> java.lang.Class: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.macos.cfm.CFragLocatorKind: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.util.bin.format.macos.cfm.CFragLocatorKind]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
