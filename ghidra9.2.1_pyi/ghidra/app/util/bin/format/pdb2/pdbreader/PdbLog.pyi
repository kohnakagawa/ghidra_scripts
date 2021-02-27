from typing import List
import ghidra.app.util.bin.format.pdb2.pdbreader
import ghidra.app.util.bin.format.pdb2.pdbreader.type
import java.lang
import java.util.function


class PdbLog(object):




    def __init__(self): ...



    @staticmethod
    def dispose() -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def logBadTypeRecordIndex(__a0: ghidra.app.util.bin.format.pdb2.pdbreader.AbstractTypeProgramInterface, __a1: int) -> None: ...

    @staticmethod
    def logDeserializationFailure(__a0: ghidra.app.util.bin.format.pdb2.pdbreader.PdbByteReader, __a1: int, __a2: java.lang.Exception) -> None: ...

    @staticmethod
    def logGetTypeClassMismatch(__a0: ghidra.app.util.bin.format.pdb2.pdbreader.type.AbstractMsType, __a1: java.lang.Class) -> None: ...

    @staticmethod
    def logSerializationItemClassMismatch(__a0: ghidra.app.util.bin.format.pdb2.pdbreader.IdMsParsable, __a1: java.lang.Class, __a2: int) -> None: ...

    @overload
    @staticmethod
    def message(__a0: unicode) -> None: ...

    @overload
    @staticmethod
    def message(__a0: java.util.function.Supplier) -> None: ...

    @overload
    @staticmethod
    def message(__a0: unicode, __a1: List[java.util.function.Supplier]) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def setEnabled(__a0: bool) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
