import ghidra.framework.model
import java.lang


class FrontEndService(object):
    """
    Interface for accessing front-end functionality.
    """









    def addProjectListener(self, l: ghidra.framework.model.ProjectListener) -> None:
        """
        Adds the specified listener to the front-end tool.
        @param l the project listener
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeProjectListener(self, l: ghidra.framework.model.ProjectListener) -> None:
        """
        Removes the specified listener from the front-end tool.
        @param l the project listener
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
