import ghidra.framework.model
import java.lang


class ProjectDataService(object):
    """
    Interface for providing the ProjectData
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getProjectData(self) -> ghidra.framework.model.ProjectData:
        """
        Returns the ProjectData for the currently open project.
        """
        ...

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

    @property
    def projectData(self) -> ghidra.framework.model.ProjectData: ...
