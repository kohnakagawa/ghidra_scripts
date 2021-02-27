import generic.continues
import ghidra.app.util.importer
import java.lang


class MessageLogContinuesFactory(object):




    def __init__(self): ...



    @staticmethod
    def create(log: ghidra.app.util.importer.MessageLog) -> generic.continues.ContinuesFactory: ...

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
