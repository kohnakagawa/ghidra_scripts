import ghidra.framework.main
import ghidra.framework.model
import java.lang


class AppInfo(object):
    """
    Class with static methods to maintain application info, e.g., a handle to the
     tool that is the Ghidra Project Window, the user's name, etc.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def exitGhidra() -> None: ...

    @staticmethod
    def getActiveProject() -> ghidra.framework.model.Project: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getFrontEndTool() -> ghidra.framework.main.FrontEndTool: ...

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
