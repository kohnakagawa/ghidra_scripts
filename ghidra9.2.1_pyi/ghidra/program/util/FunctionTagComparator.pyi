import ghidra.program.util
import java.lang


class FunctionTagComparator(ghidra.program.util.ProgramDiff.ProgramDiffComparatorImpl):
    """
    Compares the function tags in two programs.

     Two sets of tags are considered equal if they contain the name and comment
     attributes.
    """





    def __init__(self): ...



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
