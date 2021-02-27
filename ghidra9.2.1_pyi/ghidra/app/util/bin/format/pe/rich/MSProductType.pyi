from typing import List
import ghidra.app.util.bin.format.pe.rich
import java.lang


class MSProductType(java.lang.Enum):
    Assembler: ghidra.app.util.bin.format.pe.rich.MSProductType = Assembler
    CVTRes: ghidra.app.util.bin.format.pe.rich.MSProductType = CVTRes
    CXX_Compiler: ghidra.app.util.bin.format.pe.rich.MSProductType = C++ Compiler
    C_Compiler: ghidra.app.util.bin.format.pe.rich.MSProductType = C Compiler
    Export: ghidra.app.util.bin.format.pe.rich.MSProductType = Linker
    Import: ghidra.app.util.bin.format.pe.rich.MSProductType = Linker
    ImportExport: ghidra.app.util.bin.format.pe.rich.MSProductType = Linker
    Linker: ghidra.app.util.bin.format.pe.rich.MSProductType = Linker
    Unknown: ghidra.app.util.bin.format.pe.rich.MSProductType = Unknown







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

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
    def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.pe.rich.MSProductType: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.util.bin.format.pe.rich.MSProductType]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
