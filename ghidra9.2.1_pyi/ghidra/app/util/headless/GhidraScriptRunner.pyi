from typing import List
import ghidra
import java.lang


class GhidraScriptRunner(object, ghidra.GhidraLaunchable):
    """
    A simple class for running scripts outside of Ghidra.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def launch(self, layout: ghidra.GhidraApplicationLayout, args: List[unicode]) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
