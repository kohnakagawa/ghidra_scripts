from typing import List
import ghidra.pcode.emulate
import ghidra.pcode.emulate.callother
import ghidra.program.model.pcode
import java.lang


class OpBehaviorOtherNOP(object, ghidra.pcode.emulate.callother.OpBehaviorOther):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def evaluate(self, emu: ghidra.pcode.emulate.Emulate, out: ghidra.program.model.pcode.Varnode, inputs: List[ghidra.program.model.pcode.Varnode]) -> None: ...

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
