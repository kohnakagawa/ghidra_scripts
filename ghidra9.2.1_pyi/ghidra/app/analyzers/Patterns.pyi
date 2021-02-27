from typing import List
import generic.jar
import ghidra.program.model.listing
import ghidra.util.constraint
import java.lang


class Patterns(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def findPatternFiles(__a0: ghidra.program.model.listing.Program, __a1: ghidra.util.constraint.ProgramDecisionTree) -> List[generic.jar.ResourceFile]: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getPatternDecisionTree() -> ghidra.util.constraint.ProgramDecisionTree: ...

    @staticmethod
    def hasPatternFiles(__a0: ghidra.program.model.listing.Program, __a1: ghidra.util.constraint.ProgramDecisionTree) -> bool: ...

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
