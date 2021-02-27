from typing import List
import java.lang


class ObjectiveC1_State(object):
    beenApplied: java.util.Set
    encodings: ghidra.app.util.bin.format.objectiveC.ObjectiveC1_TypeEncodings
    is32bit: bool
    is64bit: bool
    isARM: bool
    isPowerPC: bool
    isX86: bool
    methodMap: java.util.Map
    monitor: ghidra.util.task.TaskMonitor
    pointerSize: int
    program: ghidra.program.model.listing.Program
    thumbCodeLocations: java.util.Set



    def __init__(self, program: ghidra.program.model.listing.Program, monitor: ghidra.util.task.TaskMonitor, categoryPath: ghidra.program.model.data.CategoryPath): ...



    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getObjectiveCSectionNames(self) -> List[unicode]: ...

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

    @property
    def objectiveCSectionNames(self) -> List[object]: ...
