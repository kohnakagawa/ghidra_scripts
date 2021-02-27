from typing import List
import ghidra.framework.client
import ghidra.framework.model
import ghidra.framework.project
import java.lang
import java.net


class TestProjectManager(ghidra.framework.project.DefaultProjectManager):
    """
    This class exists to open access to the DefaultProjectManager for tests
    """









    def addDefaultTools(self, toolChest: ghidra.framework.model.ToolChest) -> None:
        """
        Add the default tools to the given tool chest.  This method does not attempt to merge the
         user's previous tools, as does {@link #installTools(ToolChest)}.
        @param toolChest tool chest which to add the default tools
        """
        ...

    def createProject(self, projectLocator: ghidra.framework.model.ProjectLocator, repAdapter: ghidra.framework.client.RepositoryAdapter, remember: bool) -> ghidra.framework.model.Project: ...

    def deleteProject(self, projectLocator: ghidra.framework.model.ProjectLocator) -> bool:
        """
        Delete the project in the given location and remove it from the list of known projects.
        @return false if no project was deleted.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def forgetViewedProject(self, url: java.net.URL) -> None: ...

    @staticmethod
    def get() -> ghidra.framework.model.ProjectManager: ...

    def getActiveProject(self) -> ghidra.framework.model.Project: ...

    def getClass(self) -> java.lang.Class: ...

    def getLastOpenedProject(self) -> ghidra.framework.model.ProjectLocator:
        """
        Get the last opened (active) project.
        @return project last opened by the user; returns NULL if a project
         was never opened OR the last opened project is no longer valid
        """
        ...

    def getMostRecentServerInfo(self) -> ghidra.framework.model.ServerInfo: ...

    def getRecentProjects(self) -> List[ghidra.framework.model.ProjectLocator]:
        """
        Get list of project locations that user most recently opened.
        @return list of project locations
        """
        ...

    def getRecentViewedProjects(self) -> List[java.net.URL]: ...

    def getRepositoryServerAdapter(self, host: unicode, portNumber: int, forceConnect: bool) -> ghidra.framework.client.RepositoryServerAdapter: ...

    def getUserToolChest(self) -> ghidra.framework.model.ToolChest: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def openProject(self, projectLocator: ghidra.framework.model.ProjectLocator, doRestore: bool, resetOwner: bool) -> ghidra.framework.model.Project: ...

    def projectExists(self, projectLocator: ghidra.framework.model.ProjectLocator) -> bool:
        """
        Returns true if the specified project exists.
        """
        ...

    def rememberProject(self, projectLocator: ghidra.framework.model.ProjectLocator) -> None:
        """
        Keep the specified project on the list of known projects.
        """
        ...

    def rememberViewedProject(self, url: java.net.URL) -> None: ...

    def setLastOpenedProject(self, projectLocator: ghidra.framework.model.ProjectLocator) -> None:
        """
        Update the last opened project preference.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
