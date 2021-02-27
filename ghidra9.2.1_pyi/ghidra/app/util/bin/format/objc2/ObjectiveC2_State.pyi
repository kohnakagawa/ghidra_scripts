from typing import List
import ghidra.app.util.bin.format.objectiveC
import java.lang


class ObjectiveC2_State(ghidra.app.util.bin.format.objectiveC.ObjectiveC1_State):
    beenApplied: java.util.Set
    classIndexMap: java.util.Map
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
    variableMap: java.util.Map



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
