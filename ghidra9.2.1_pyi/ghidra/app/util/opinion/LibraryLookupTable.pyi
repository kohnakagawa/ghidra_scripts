import generic.jar
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class LibraryLookupTable(object):




    def __init__(self): ...



    @overload
    @staticmethod
    def createFile(program: ghidra.program.model.listing.Program, overwrite: bool, monitor: ghidra.util.task.TaskMonitor) -> generic.jar.ResourceFile: ...

    @overload
    @staticmethod
    def createFile(program: ghidra.program.model.listing.Program, overwrite: bool, inSystem: bool, monitor: ghidra.util.task.TaskMonitor) -> generic.jar.ResourceFile: ...

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
