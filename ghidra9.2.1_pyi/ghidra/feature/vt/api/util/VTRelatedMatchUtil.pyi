import ghidra.feature.vt.api.main
import ghidra.program.model.listing
import ghidra.util.task
import java.lang
import java.util


class VTRelatedMatchUtil(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def getCalleesOf(__a0: ghidra.program.model.listing.Function) -> java.util.Set: ...

    @staticmethod
    def getCallersOf(__a0: ghidra.program.model.listing.Function) -> java.util.Set: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getRelatedMatches(__a0: ghidra.util.task.TaskMonitor, __a1: ghidra.feature.vt.api.main.VTSession, __a2: ghidra.feature.vt.api.main.VTMatch) -> java.util.Collection: ...

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
