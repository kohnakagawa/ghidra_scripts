from typing import List
import ghidra.app.util.bin.format.pdb
import ghidra.program.model.data
import ghidra.util.task
import java.lang
import java.util.function


class DefaultCompositeMember(ghidra.app.util.bin.format.pdb.CompositeMember):








    @staticmethod
    def applyDataTypeMembers(__a0: ghidra.program.model.data.Composite, __a1: bool, __a2: int, __a3: List[object], __a4: java.util.function.Consumer, __a5: ghidra.util.task.TaskMonitor) -> bool: ...

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
