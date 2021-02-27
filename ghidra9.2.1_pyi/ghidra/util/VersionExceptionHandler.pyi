import ghidra.framework.model
import ghidra.util.exception
import java.awt
import java.lang


class VersionExceptionHandler(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isUpgradeOK(parent: java.awt.Component, domainFile: ghidra.framework.model.DomainFile, actionName: unicode, ve: ghidra.util.exception.VersionException) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def showVersionError(parent: java.awt.Component, filename: unicode, contentType: unicode, actionName: unicode, ve: ghidra.util.exception.VersionException) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
