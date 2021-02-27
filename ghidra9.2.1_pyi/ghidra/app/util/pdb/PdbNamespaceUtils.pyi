import ghidra.app.util
import java.lang


class PdbNamespaceUtils(object):




    def __init__(self): ...



    @staticmethod
    def convertToGhidraPath(__a0: ghidra.app.util.SymbolPath, __a1: int) -> ghidra.app.util.SymbolPath: ...

    @overload
    @staticmethod
    def convertToGhidraPathName(__a0: ghidra.app.util.SymbolPath) -> ghidra.app.util.SymbolPath: ...

    @overload
    @staticmethod
    def convertToGhidraPathName(__a0: ghidra.app.util.SymbolPath, __a1: int) -> ghidra.app.util.SymbolPath: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def fixUnnamed(__a0: unicode, __a1: int) -> unicode: ...

    def getClass(self) -> java.lang.Class: ...

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
