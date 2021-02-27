from typing import List
import ghidra.program.model.address
import ghidra.program.model.lang
import java.lang


class ContextCache(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getContext(self, ctx: ghidra.program.model.lang.ProcessorContextView, buf: List[int]) -> None: ...

    def getContextSize(self) -> int: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def registerVariable(self, register: ghidra.program.model.lang.Register) -> None: ...

    def setContext(self, ctx: ghidra.program.model.lang.ProcessorContext, addr: ghidra.program.model.address.Address, num: int, mask: int, value: int) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def contextSize(self) -> int: ...