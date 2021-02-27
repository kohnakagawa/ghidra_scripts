from typing import List
import ghidra.feature.vt.api.util
import java.lang


class ErrorStatus(object):




    def __init__(self): ...



    def addException(self, __a0: ghidra.feature.vt.api.util.VersionTrackingApplyException) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getExceptions(self) -> List[object]: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def printLogMessage(self) -> unicode: ...

    def printMessage(self) -> unicode: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def exceptions(self) -> List[object]: ...