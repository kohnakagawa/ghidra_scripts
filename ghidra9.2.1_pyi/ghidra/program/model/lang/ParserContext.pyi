import ghidra.program.model.lang
import java.lang


class ParserContext(object):
    """
    ParserContext represents a language provider specific parser context
     which may be cached.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getPrototype(self) -> ghidra.program.model.lang.InstructionPrototype: ...

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

    @property
    def prototype(self) -> ghidra.program.model.lang.InstructionPrototype: ...
