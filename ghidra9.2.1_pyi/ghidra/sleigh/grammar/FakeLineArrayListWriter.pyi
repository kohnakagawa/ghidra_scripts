from typing import List
import ghidra.sleigh.grammar
import java.io
import java.lang


class FakeLineArrayListWriter(ghidra.sleigh.grammar.LineArrayListWriter):




    def __init__(self): ...



    @overload
    def append(self, __a0: int) -> java.io.Writer: ...

    @overload
    def append(self, __a0: java.lang.CharSequence) -> java.lang.Appendable: ...

    @overload
    def append(self, __a0: java.lang.CharSequence, __a1: int, __a2: int) -> java.io.Writer: ...

    def close(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def flush(self) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def getLines(self) -> List[unicode]: ...

    def hashCode(self) -> int: ...

    def newLine(self) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def nullWriter() -> java.io.Writer: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @overload
    def write(self, __a0: int) -> None: ...

    @overload
    def write(self, __a0: unicode) -> None: ...

    @overload
    def write(self, __a0: List[int]) -> None: ...

    @overload
    def write(self, __a0: unicode, __a1: int, __a2: int) -> None: ...

    @overload
    def write(self, cbuf: List[int], off: int, len: int) -> None: ...
