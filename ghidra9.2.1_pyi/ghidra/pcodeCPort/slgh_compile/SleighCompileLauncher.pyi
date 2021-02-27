from typing import List
import ghidra
import java.lang


class SleighCompileLauncher(object, ghidra.GhidraLaunchable):
    FILE_IN_DEFAULT_EXT: unicode = u'.slaspec'
    FILE_OUT_DEFAULT_EXT: unicode = u'.sla'



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def launch(self, __a0: ghidra.GhidraApplicationLayout, __a1: List[unicode]) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def runMain(__a0: List[unicode]) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
