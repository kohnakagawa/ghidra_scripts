import ghidra.app.util.bin.format.macho.commands
import ghidra.util.task
import java.lang


class AbstractClassicProcessor(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def perform(self, segmentName: unicode, sectionName: unicode, addressValue: long, fromDylib: unicode, nList: ghidra.app.util.bin.format.macho.commands.NList, isWeak: bool, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
