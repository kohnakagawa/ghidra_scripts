import ghidra.framework.data
import java.lang


class DefaultCheckinHandler(object, ghidra.framework.data.CheckinHandler):
    """
    DefaultCheckinHandler provides a simple
     check-in handler for use with
     DomainFile#checkin(CheckinHandler, boolean, ghidra.util.task.TaskMonitor)
    """





    def __init__(self, comment: unicode, keepCheckedOut: bool, createKeepFile: bool): ...



    def createKeepFile(self) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getComment(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def keepCheckedOut(self) -> bool: ...

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
    def comment(self) -> unicode: ...
