import java.lang


class LanguageCompilerSpecQuery(object):
    compilerSpecID: ghidra.program.model.lang.CompilerSpecID
    endian: ghidra.program.model.lang.Endian
    processor: ghidra.program.model.lang.Processor
    size: int
    variant: unicode



    def __init__(self, processor: ghidra.program.model.lang.Processor, endian: ghidra.program.model.lang.Endian, size: int, variant: unicode, compilerSpecID: ghidra.program.model.lang.CompilerSpecID):
        """
        Constructs a new LanguageCompilerSpecQuery
        @param processor the language's processor
        @param endian the processor's endianness
        @param size the size of an address
        @param variant the processor variant
        @param compilerSpecID the compiler spec id
        """
        ...



    def equals(self, __a0: object) -> bool: ...

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
