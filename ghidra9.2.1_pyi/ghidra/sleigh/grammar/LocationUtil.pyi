from typing import List
import ghidra.sleigh.grammar
import java.lang


class LocationUtil(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def maximum(__a0: List[object]) -> ghidra.sleigh.grammar.Location: ...

    @staticmethod
    def minimum(__a0: List[object]) -> ghidra.sleigh.grammar.Location: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
