import ghidra.app.util.bin.format.macho.commands.dyld
import ghidra.util.task
import java.lang


class BindProcessor(ghidra.app.util.bin.format.macho.commands.dyld.AbstractDyldInfoProcessor):




    def __init__(self, program: ghidra.program.model.listing.Program, header: ghidra.app.util.bin.format.macho.MachHeader, provider: ghidra.app.util.bin.ByteProvider, command: ghidra.app.util.bin.format.macho.commands.DyldInfoCommand): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def process(self, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
