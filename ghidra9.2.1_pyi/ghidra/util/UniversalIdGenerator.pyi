from typing import List
import ghidra.util
import java.lang


class UniversalIdGenerator(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def initialize() -> None: ...

    @staticmethod
    def main(args: List[unicode]) -> None: ...

    @staticmethod
    def nextID() -> ghidra.util.UniversalID: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
