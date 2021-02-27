from typing import List
import ghidra.program.model.lang
import ghidra.util.classfinder
import java.lang


class InstructionSkipper(ghidra.util.classfinder.ExtensionPoint, object):








    def equals(self, __a0: object) -> bool: ...

    def getApplicableProcessor(self) -> ghidra.program.model.lang.Processor: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def shouldSkip(self, buffer: List[int], size: int) -> bool: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def applicableProcessor(self) -> ghidra.program.model.lang.Processor: ...
