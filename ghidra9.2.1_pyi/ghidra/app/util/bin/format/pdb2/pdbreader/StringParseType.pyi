from typing import List
import ghidra.app.util.bin.format.pdb2.pdbreader
import java.lang


class StringParseType(java.lang.Enum):
    StringNt: ghidra.app.util.bin.format.pdb2.pdbreader.StringParseType = StringNt
    StringSt: ghidra.app.util.bin.format.pdb2.pdbreader.StringParseType = StringSt
    StringUtf8Nt: ghidra.app.util.bin.format.pdb2.pdbreader.StringParseType = StringUtf8Nt
    StringUtf8St: ghidra.app.util.bin.format.pdb2.pdbreader.StringParseType = StringUtf8St
    StringWcharNt: ghidra.app.util.bin.format.pdb2.pdbreader.StringParseType = StringWcharNt







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
    def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.pdb2.pdbreader.StringParseType: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.util.bin.format.pdb2.pdbreader.StringParseType]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
