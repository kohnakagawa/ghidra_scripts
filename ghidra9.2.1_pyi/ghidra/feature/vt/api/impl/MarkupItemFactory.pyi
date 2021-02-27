import ghidra.feature.vt.api.db
import ghidra.util.task
import java.lang
import java.util


class MarkupItemFactory(object):








    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def generateMarkupItems(__a0: ghidra.util.task.TaskMonitor, __a1: ghidra.feature.vt.api.db.VTAssociationDB) -> java.util.Collection: ...

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
