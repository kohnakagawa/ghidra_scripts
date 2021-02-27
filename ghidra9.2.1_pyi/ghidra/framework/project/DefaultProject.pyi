from typing import List
import ghidra.framework.client
import ghidra.framework.model
import ghidra.framework.options
import java.lang
import java.net


class DefaultProject(object, ghidra.framework.model.Project):
    """
    Implementation for a Project.
    """









    def addProjectView(self, url: java.net.URL) -> ghidra.framework.model.ProjectData: ...

    def close(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getLocalToolChest(self) -> ghidra.framework.model.ToolChest:
        """
        Get the local tool chest for the user logged in.
        @return the tool chest
        """
        ...

    def getName(self) -> unicode: ...

    def getOpenData(self) -> List[ghidra.framework.model.DomainFile]: ...

    @overload
    def getProjectData(self) -> ghidra.framework.model.ProjectData: ...

    @overload
    def getProjectData(self, locator: ghidra.framework.model.ProjectLocator) -> ghidra.framework.model.ProjectData: ...

    @overload
    def getProjectData(self, url: java.net.URL) -> ghidra.framework.model.ProjectData: ...

    def getProjectLocator(self) -> ghidra.framework.model.ProjectLocator:
        """
        Get the project URL for this project.
        """
        ...

    def getProjectManager(self) -> ghidra.framework.model.ProjectManager: ...

    def getProjectViews(self) -> List[ghidra.framework.model.ProjectLocator]: ...

    def getRepository(self) -> ghidra.framework.client.RepositoryAdapter: ...

    def getSaveableData(self, key: unicode) -> ghidra.framework.options.SaveState: ...

    def getToolManager(self) -> ghidra.framework.model.ToolManager: ...

    def getToolServices(self) -> ghidra.framework.model.ToolServices:
        """
        Get the tool services for this project.
        """
        ...

    def getToolTemplate(self, tag: unicode) -> ghidra.framework.model.ToolTemplate: ...

    def getViewedProjectData(self) -> List[ghidra.framework.model.ProjectData]: ...

    def hasChanged(self) -> bool: ...

    def hashCode(self) -> int: ...

    def isClosed(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def releaseFiles(self, consumer: object) -> None: ...

    def removeProjectView(self, url: java.net.URL) -> None:
        """
        Remove the view from this project.
        """
        ...

    def restore(self) -> None: ...

    def save(self) -> None: ...

    def saveSessionTools(self) -> bool: ...

    def saveToolTemplate(self, tag: unicode, template: ghidra.framework.model.ToolTemplate) -> None: ...

    def setSaveableData(self, key: unicode, saveState: ghidra.framework.options.SaveState) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def closed(self) -> bool: ...

    @property
    def localToolChest(self) -> ghidra.framework.model.ToolChest: ...

    @property
    def name(self) -> unicode: ...

    @property
    def openData(self) -> List[object]: ...

    @property
    def projectData(self) -> ghidra.framework.model.ProjectData: ...

    @property
    def projectLocator(self) -> ghidra.framework.model.ProjectLocator: ...

    @property
    def projectManager(self) -> ghidra.framework.model.ProjectManager: ...

    @property
    def projectViews(self) -> List[ghidra.framework.model.ProjectLocator]: ...

    @property
    def repository(self) -> ghidra.framework.client.RepositoryAdapter: ...

    @property
    def toolManager(self) -> ghidra.framework.model.ToolManager: ...

    @property
    def toolServices(self) -> ghidra.framework.model.ToolServices: ...

    @property
    def viewedProjectData(self) -> List[ghidra.framework.model.ProjectData]: ...
