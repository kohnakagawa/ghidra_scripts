import ghidra.app.plugin.exceptionhandlers.gcc
import java.lang


class DwarfDecoderFactory(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    @staticmethod
    def getDecoder(__a0: int) -> ghidra.app.plugin.exceptionhandlers.gcc.DwarfEHDecoder: ...

    @overload
    @staticmethod
    def getDecoder(__a0: ghidra.app.plugin.exceptionhandlers.gcc.DwarfEHDataDecodeFormat, __a1: ghidra.app.plugin.exceptionhandlers.gcc.DwarfEHDataApplicationMode, __a2: bool) -> ghidra.app.plugin.exceptionhandlers.gcc.DwarfEHDecoder: ...

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
