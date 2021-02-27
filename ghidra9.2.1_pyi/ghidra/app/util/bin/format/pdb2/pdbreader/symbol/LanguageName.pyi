from typing import List
import ghidra.app.util.bin.format.pdb2.pdbreader.symbol
import java.lang


class LanguageName(java.lang.Enum):
    BASIC: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.LanguageName = Basic
    C: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.LanguageName = C
    COBOL: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.LanguageName = COBOL
    CPP: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.LanguageName = C++
    CSHARP: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.LanguageName = C#
    CVTPGD: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.LanguageName = CVTPGD
    CVTRES: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.LanguageName = CVTRES
    FORTRAN: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.LanguageName = FORTRAN
    HLSL: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.LanguageName = HLSL
    ILASM: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.LanguageName = ILASM
    INVALID: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.LanguageName = ???
    JAVA: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.LanguageName = Java
    JSCRIPT: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.LanguageName = JScript
    LINK: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.LanguageName = LINK
    MASM: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.LanguageName = MASM
    MSIL: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.LanguageName = MSIL
    PASCAL: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.LanguageName = Pascal
    VISUALBASIC: ghidra.app.util.bin.format.pdb2.pdbreader.symbol.LanguageName = VisualBasic
    label: unicode
    value: int







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def fromValue(__a0: int) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.LanguageName: ...

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
    def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.pdb2.pdbreader.symbol.LanguageName: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.app.util.bin.format.pdb2.pdbreader.symbol.LanguageName]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
