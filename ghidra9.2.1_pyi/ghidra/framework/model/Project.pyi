from typing import List
import ghidra.framework.client
import ghidra.framework.model
import ghidra.framework.options
import java.lang
import java.net


class Project(object):
    """
    Interface to define methods to manage data and tools for users working on a
     particular effort. Project represents the container object for users, data,
     and tools to work together.
    """









    def addProjectView(self, projectURL: java.net.URL) -> ghidra.framework.model.ProjectData:
        """
        Add the given project URL to this project's list project views.
         The project view allows users to look at data files from another
         project.
        @param projectURL identifier for the project view
        @return project data for this view
        @throws IOException if I/O error occurs or if project/repository not found
        @throws MalformedURLException if projectURL is invalid
        """
        ...

    def close(self) -> None:
        """
        Close the project.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getLocalToolChest(self) -> ghidra.framework.model.ToolChest:
        """
        Return the local tool chest for the user logged in.
        """
        ...

    def getName(self) -> unicode:
        """
        Convenience method to get the name of this project.
        """
        ...

    def getOpenData(self) -> List[ghidra.framework.model.DomainFile]:
        """
        Get list of domain files that are open.
        @return the files; empty if no files
        """
        ...

    @overload
    def getProjectData(self) -> ghidra.framework.model.ProjectData:
        """
        Get the root domain data folder in the project.
        """
        ...

    @overload
    def getProjectData(self, projectLocator: ghidra.framework.model.ProjectLocator) -> ghidra.framework.model.ProjectData:
        """
        Returns the Project Data for the given Project locator.  The Project locator must
         be either the current active project or an currently open project view.
        """
        ...

    @overload
    def getProjectData(self, url: java.net.URL) -> ghidra.framework.model.ProjectData:
        """
        Returns the Project Data for the given Project URL.  The Project URL must
         correspond to the current active project or an currently open project view.
        """
        ...

    def getProjectLocator(self) -> ghidra.framework.model.ProjectLocator:
        """
        Get the project locator for this project.
        """
        ...

    def getProjectManager(self) -> ghidra.framework.model.ProjectManager:
        """
        Returns the project manager of this project.
        @return the project manager of this project.
        """
        ...

    def getProjectViews(self) -> List[ghidra.framework.model.ProjectLocator]:
        """
        Return the list of project views in this project.
        """
        ...

    def getRepository(self) -> ghidra.framework.client.RepositoryAdapter:
        """
        Get the repository that this project is associated with.
        @return null if the project is not associated with a remote
         repository
        """
        ...

    def getSaveableData(self, key: unicode) -> ghidra.framework.options.SaveState:
        """
        The analog for {@link #setSaveableData(String, SaveState)}.
        """
        ...

    def getToolManager(self) -> ghidra.framework.model.ToolManager:
        """
        Return the tool manager for this project.
        """
        ...

    def getToolServices(self) -> ghidra.framework.model.ToolServices:
        """
        Return the tool services for this project.
        """
        ...

    def getToolTemplate(self, tag: unicode) -> ghidra.framework.model.ToolTemplate:
        """
        Get the tool template with the given tag.
        @param tag ID or name for the tool template to get
        @return tool template
        """
        ...

    def getViewedProjectData(self) -> List[ghidra.framework.model.ProjectData]:
        """
        Get the project data for other projects that are
         currently being viewed.
        @return zero length array if there are no viewed projects open
        """
        ...

    def hasChanged(self) -> bool:
        """
        Return whether the project configuration has changed.
        """
        ...

    def hashCode(self) -> int: ...

    def isClosed(self) -> bool:
        """
        Returns whether this project instance has been closed
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def releaseFiles(self, consumer: object) -> None:
        """
        Releases all DomainObjects used by the given consumer
        @param consumer object no longer using any DomainObjects.
        """
        ...

    def removeProjectView(self, projectURL: java.net.URL) -> None:
        """
        Remove the project view from this project.
        @param projectURL identifier for the project
        """
        ...

    def restore(self) -> None:
        """
        Restore this project's state.
        """
        ...

    def save(self) -> None:
        """
        Save the project and the list of project views.
        """
        ...

    def saveSessionTools(self) -> bool:
        """
        Saves any tools that are associated with the opened project when the project is closed.
        @return True if the save was not cancelled.
        """
        ...

    def saveToolTemplate(self, tag: unicode, template: ghidra.framework.model.ToolTemplate) -> None:
        """
        Save the given tool template as part of the project.
        @param tag ID or name for the tool template
        @param template template to save
        """
        ...

    def setSaveableData(self, key: unicode, saveState: ghidra.framework.options.SaveState) -> None:
        """
        Allows the user to store data related to the project.
        @param key A value used to store and lookup saved data
        @param saveState a container of data that will be written out when persisted
        """
        ...

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
