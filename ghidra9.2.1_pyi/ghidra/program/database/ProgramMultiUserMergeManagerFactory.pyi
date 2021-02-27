import ghidra.framework.data
import ghidra.framework.model
import java.lang


class ProgramMultiUserMergeManagerFactory(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getMergeManager(resultsObj: ghidra.framework.model.DomainObject, sourceObj: ghidra.framework.model.DomainObject, originalObj: ghidra.framework.model.DomainObject, latestObj: ghidra.framework.model.DomainObject) -> ghidra.framework.data.DomainObjectMergeManager: ...

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
