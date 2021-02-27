from typing import List
import ghidra.pcode.emulate
import java.lang


class EmulateExecutionState(java.lang.Enum):
    BREAKPOINT: ghidra.pcode.emulate.EmulateExecutionState = BREAKPOINT
    EXECUTE: ghidra.pcode.emulate.EmulateExecutionState = EXECUTE
    FAULT: ghidra.pcode.emulate.EmulateExecutionState = FAULT
    INSTRUCTION_DECODE: ghidra.pcode.emulate.EmulateExecutionState = INSTRUCTION_DECODE
    STOPPED: ghidra.pcode.emulate.EmulateExecutionState = STOPPED







    @overload
    def compareTo(self, __a0: java.lang.Enum) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDeclaringClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def name(self) -> unicode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def ordinal(self) -> int: ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def valueOf(__a0: unicode) -> ghidra.pcode.emulate.EmulateExecutionState: ...

    @overload
    @staticmethod
    def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

    @staticmethod
    def values() -> List[ghidra.pcode.emulate.EmulateExecutionState]: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
