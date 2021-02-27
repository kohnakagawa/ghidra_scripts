from typing import List
import ghidra.app.util.bin.format.pef
import java.lang


class PackedDataOpcodes(java.lang.Enum):
    kPEFPkDataBlock: ghidra.app.util.bin.format.pef.PackedDataOpcodes = kPEFPkDataBlock
    kPEFPkDataRepeat: ghidra.app.util.bin.format.pef.PackedDataOpcodes = kPEFPkDataRepeat
    kPEFPkDataRepeatBlock: ghidra.app.util.bin.format.pef.PackedDataOpcodes = kPEFPkDataRepeatBlock
    kPEFPkDataRepeatZero: ghidra.app.util.bin.format.pef.PackedDataOpcodes = kPEFPkDataRepeatZero
    kPEFPkDataReserved5: ghidra.app.util.bin.format.pef.PackedDataOpcodes = kPEFPkDataReserved5
    kPEFPkDataReserved6: ghidra.app.util.bin.format.pef.PackedDataOpcodes = kPEFPkDataReserved6
    kPEFPkDataReserved7: ghidra.app.util.bin.format.pef.PackedDataOpcodes = kPEFPkDataReserved7
    kPEFPkDataZero: ghidra.app.util.bin.format.pef.PackedDataOpcodes = kPEFPkDataZero







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def get(__a0: int) -> ghidra.app.util.bin.format.pef.PackedDataOpcodes: ...

    def getClass(self) -> java.lang.Class: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    def getValue(self) -> int: ...

    def hashCode(self) -> int: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.pef.PackedDataOpcodes: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.util.bin.format.pef.PackedDataOpcodes]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def value(self) -> int: ...
