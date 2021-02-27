import ghidra.sleigh.grammar
import java.lang


class MessageFormattingUtils(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def format(location: ghidra.sleigh.grammar.Location, message: java.lang.CharSequence) -> unicode:
        """
        Format a log message.
        @param location Referenced file location
        @param message Message
        @return Formatted string with location prepended to message.
        """
        ...

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
