from typing import List
import ghidra.app.plugin.exceptionhandlers.gcc.sections
import ghidra.app.plugin.exceptionhandlers.gcc.structures.ehFrame
import ghidra.program.model.address
import java.lang


class EhFrameSection(ghidra.app.plugin.exceptionhandlers.gcc.sections.AbstractFrameSection):
    EH_FRAME_BLOCK_NAME: unicode = u'.eh_frame'



    def __init__(self, __a0: ghidra.util.task.TaskMonitor, __a1: ghidra.program.model.listing.Program): ...



    def analyze(self, __a0: int) -> List[object]: ...

    def equals(self, __a0: object) -> bool: ...

    def getCie(self, __a0: ghidra.program.model.address.Address) -> ghidra.app.plugin.exceptionhandlers.gcc.structures.ehFrame.Cie: ...

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
