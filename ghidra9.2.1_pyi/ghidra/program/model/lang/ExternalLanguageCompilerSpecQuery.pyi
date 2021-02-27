import java.lang


class ExternalLanguageCompilerSpecQuery(object):
    """
    Analog to LanguageCompilerSpecQuery, for use with querying External Languages.
     That is, languages that exist in other products, like IDA-Pro's 'metapc.'
    """

    compilerSpecID: ghidra.program.model.lang.CompilerSpecID
    endian: ghidra.program.model.lang.Endian
    externalProcessorName: unicode
    externalTool: unicode
    size: int



    def __init__(self, externalProcessorName: unicode, externalTool: unicode, endian: ghidra.program.model.lang.Endian, size: int, compilerSpecID: ghidra.program.model.lang.CompilerSpecID): ...



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
