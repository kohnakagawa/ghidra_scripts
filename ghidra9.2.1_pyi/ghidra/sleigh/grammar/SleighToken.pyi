import ghidra.sleigh.grammar
import java.lang
import org.antlr.runtime


class SleighToken(org.antlr.runtime.CommonToken):




    @overload
    def __init__(self, type: int): ...

    @overload
    def __init__(self, oldToken: org.antlr.runtime.Token): ...

    @overload
    def __init__(self, type: int, text: unicode): ...

    @overload
    def __init__(self, type: int, line: int, charPos: int): ...

    @overload
    def __init__(self, input: org.antlr.runtime.CharStream, type: int, channel: int, start: int, stop: int): ...



    def equals(self, __a0: object) -> bool: ...

    def getChannel(self) -> int: ...

    def getCharPositionInLine(self) -> int: ...

    def getClass(self) -> java.lang.Class: ...

    def getInputStream(self) -> org.antlr.runtime.CharStream: ...

    def getLine(self) -> int: ...

    def getLocation(self) -> ghidra.sleigh.grammar.Location: ...

    def getStartIndex(self) -> int: ...

    def getStopIndex(self) -> int: ...

    def getText(self) -> unicode: ...

    def getTokenIndex(self) -> int: ...

    def getType(self) -> int: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setChannel(self, __a0: int) -> None: ...

    def setCharPositionInLine(self, __a0: int) -> None: ...

    def setInputStream(self, __a0: org.antlr.runtime.CharStream) -> None: ...

    def setLine(self, __a0: int) -> None: ...

    def setLocation(self, location: ghidra.sleigh.grammar.Location) -> None: ...

    def setStartIndex(self, __a0: int) -> None: ...

    def setStopIndex(self, __a0: int) -> None: ...

    def setText(self, __a0: unicode) -> None: ...

    def setTokenIndex(self, __a0: int) -> None: ...

    def setType(self, __a0: int) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def location(self) -> ghidra.sleigh.grammar.Location: ...

    @location.setter
    def location(self, value: ghidra.sleigh.grammar.Location) -> None: ...
