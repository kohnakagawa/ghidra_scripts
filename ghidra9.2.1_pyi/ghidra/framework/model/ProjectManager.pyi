from typing import List
import ghidra.framework.client
import ghidra.framework.model
import java.lang
import java.net


class ProjectManager(object):
    """
    Interface for methods to create, open, and delete projects; maintains a
     list of known project views that the user opened.
     It has a handle to the currently opened project. A project can be
     opened by one user at a time.
    """

    APPLICATION_TOOLS_DIR_NAME: unicode = u'tools'
    APPLICATION_TOOL_EXTENSION: unicode = u'.tcd'







    def createProject(self, projectLocator: ghidra.framework.model.ProjectLocator, repAdapter: ghidra.framework.client.RepositoryAdapter, remember: bool) -> ghidra.framework.model.Project:
        """
        Create a project on the local filesystem.
        @param projectLocator location for where the project should be created
        @param repAdapter repository adapter if this project is to be a
                shared project; may be null if the project is not shared.
        @param remember if false the new project should not be remembered (i.e., recently opened, etc.)
        @return the new project
        @throws IOException if user cannot access/write the project location
        """
        ...

    def deleteProject(self, projectLocator: ghidra.framework.model.ProjectLocator) -> bool:
        """
        Delete the project in the given location.
        @param projectLocator project location
        @return false if no project was deleted.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def forgetViewedProject(self, url: java.net.URL) -> None:
        """
        Remove the project url from the list of known viewed projects.
        @param url project identifier
        """
        ...

    def getActiveProject(self) -> ghidra.framework.model.Project:
        """
        Get the project that is currently open.
        @return currently open project, return null if there is no
         project opened
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getLastOpenedProject(self) -> ghidra.framework.model.ProjectLocator:
        """
        Get the last opened (active) project.
        @return project last opened by the user; returns NULL if a project
         was never opened OR the last opened project is no longer valid
        """
        ...

    def getMostRecentServerInfo(self) -> ghidra.framework.model.ServerInfo:
        """
        Get the information that was last used to access a repository
         managed by a Ghidra server.
        """
        ...

    def getRecentProjects(self) -> List[ghidra.framework.model.ProjectLocator]:
        """
        Get list of projects that user most recently opened.
        @return list of project URLs
        """
        ...

    def getRecentViewedProjects(self) -> List[java.net.URL]:
        """
        Get list of projects that user most recently viewed.
        @return list of project URLs
        """
        ...

    def getRepositoryServerAdapter(self, host: unicode, portNumber: int, forceConnect: bool) -> ghidra.framework.client.RepositoryServerAdapter:
        """
        Establish a connection to the given host and port number.
        @param host server name or IP address
        @param portNumber server port or 0 for default
        @param forceConnect if true and currently not connected, an attempt will be be to connect
        @return a handle to the remote server containing shared repositories
        """
        ...

    def getUserToolChest(self) -> ghidra.framework.model.ToolChest:
        """
        Return the user's ToolChest
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def openProject(self, projectLocator: ghidra.framework.model.ProjectLocator, doRestore: bool, resetOwner: bool) -> ghidra.framework.model.Project:
        """
        Open a project from the file system. Add the project url
         to the list of known projects.
        @param projectLocator project location
        @param doRestore true if the project should be restored
        @param resetOwner if true, the owner of the project will be changed to the current user.
        @return opened project
        @throws NotFoundException if the file for the project was
         not found.
        @throws NotOwnerException if the project owner is not the user
        @throws LockException if the project is already opened by another user
        """
        ...

    def projectExists(self, projectLocator: ghidra.framework.model.ProjectLocator) -> bool:
        """
        Returns true if a project with the given projectLocator exists.
        @param projectLocator project location
        """
        ...

    def rememberProject(self, projectLocator: ghidra.framework.model.ProjectLocator) -> None:
        """
        Keep the projectLocator on the list of known projects.
        @param projectLocator project location
        """
        ...

    def rememberViewedProject(self, url: java.net.URL) -> None:
        """
        Keep the url on the list of known projects.
        @param url project identifier
        """
        ...

    def setLastOpenedProject(self, projectLocator: ghidra.framework.model.ProjectLocator) -> None:
        """
        Set the projectLocator of last opened (active) project; this projectLocator is returned
         in the getLastOpenedProject() method.
        @param projectLocator project location of last project that was opened
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
    def activeProject(self) -> ghidra.framework.model.Project: ...

    @property
    def lastOpenedProject(self) -> ghidra.framework.model.ProjectLocator: ...

    @lastOpenedProject.setter
    def lastOpenedProject(self, value: ghidra.framework.model.ProjectLocator) -> None: ...

    @property
    def mostRecentServerInfo(self) -> ghidra.framework.model.ServerInfo: ...

    @property
    def recentProjects(self) -> List[ghidra.framework.model.ProjectLocator]: ...

    @property
    def recentViewedProjects(self) -> List[java.net.URL]: ...

    @property
    def userToolChest(self) -> ghidra.framework.model.ToolChest: ...
