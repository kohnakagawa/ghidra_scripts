import ghidra.framework.client
import ghidra.framework.model
import ghidra.framework.protocol.ghidra
import java.lang


class DefaultLocalGhidraProtocolConnector(ghidra.framework.protocol.ghidra.GhidraProtocolConnector):
    """
    DefaultLocalGhidraProtocolConnector provides support for the
     Ghidra URL protocol which specifies a local Ghidra project without extension.
     This connector is responsible for producing a suitable ProjectLocator
     for accessing the project files.
    """









    def connect(self, readOnlyAccess: bool) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFolderItemName(self) -> unicode:
        """
        Gets the repository folder item name associated with the URL.
         If an ambiguous path has been specified, the folder item name may become null
         after a connection is established (e.g., folder item name will be appended
         to folder path and item name will become null if item turns out to
         be a folder).
        @return folder item name or null
        """
        ...

    def getFolderPath(self) -> unicode:
        """
        Gets the repository folder path associated with the URL.
         If an ambiguous path has been specified, the folder path may change
         after a connection is established (e.g., folder item name will be appended
         to folder path and item name will become null if item turns out to
         be a folder).
        @return repository folder path or null
        """
        ...

    def getLocalProjectLocator(self) -> ghidra.framework.model.ProjectLocator:
        """
        Get the ProjectLocator associated with a local project URL.
        @return project locator object or null if URL supplies a a RepositoryAdapter and/or
         RepositoryServerAdapter.
        """
        ...

    def getRepositoryAdapter(self) -> ghidra.framework.client.RepositoryAdapter:
        """
        Get the RepositoryAdapter associated with a URL which specifies a repository.
        @return repository adapter or null if a project locator is supplied instead
        """
        ...

    def getRepositoryName(self) -> unicode:
        """
        Gets the repository name associated with the URL.
        @return the repository name or null if URL does not identify a specific repository
        """
        ...

    def getRepositoryServerAdapter(self) -> ghidra.framework.client.RepositoryServerAdapter:
        """
        Get the RepositoryServerAdapter associated with a URL which specifies a repository or
         repository server.
        @return repository server adapter or null if a project locator is supplied instead
        """
        ...

    def getResponseCode(self) -> int:
        """
        Gets the status code from a Ghidra URL connect response.
        @return the Ghidra Status-Code, or -1 if not yet connected
        @see #connect(boolean)
        """
        ...

    def hashCode(self) -> int: ...

    def isReadOnly(self) -> bool: ...

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
    def localProjectLocator(self) -> ghidra.framework.model.ProjectLocator: ...

    @property
    def readOnly(self) -> bool: ...
