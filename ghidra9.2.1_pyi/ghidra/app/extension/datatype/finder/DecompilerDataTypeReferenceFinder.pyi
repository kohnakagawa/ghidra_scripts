import ghidra.app.services
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.util.task
import java.lang
import java.util.function


class DecompilerDataTypeReferenceFinder(object, ghidra.app.services.DataTypeReferenceFinder):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    @overload
    def findReferences(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.data.DataType, __a2: java.util.function.Consumer, __a3: ghidra.util.task.TaskMonitor) -> None: ...

    @overload
    def findReferences(self, __a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.data.Composite, __a2: unicode, __a3: java.util.function.Consumer, __a4: ghidra.util.task.TaskMonitor) -> None: ...

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
