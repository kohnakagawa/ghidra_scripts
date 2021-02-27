import generic.jar
import ghidra.util.task
import java.lang


class GhidraScriptService(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def refreshScriptList(self) -> None: ...

    def runScript(self, scriptName: unicode, listener: ghidra.util.task.TaskListener) -> None: ...

    def toString(self) -> unicode: ...

    def tryToEditFileInEclipse(self, file: generic.jar.ResourceFile) -> bool:
        """
        Attempts to edit the provided file in Eclipse.
        @param file The file to edit in Eclipse.
        @return True if the file opened in Eclipse; otherwise, false.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
