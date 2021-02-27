from typing import List
import ghidra.framework.remote
import java.lang


class RepositoryServerHandle(object):
    """
    RepositoryServerHandle provides access to a repository server.
    """









    def anonymousAccessAllowed(self) -> bool:
        """
        @return true if server allows anonymous access.
         Individual repositories must grant anonymous access separately.
        @throws IOException if an IO error occurs
        """
        ...

    def canSetPassword(self) -> bool:
        """
        Returns true if the user's password can be changed.
        @throws IOException if an IO error occurs
        """
        ...

    def connected(self) -> None:
        """
        Verify that server is alive and connected.
        @throws IOException if connection verification fails
        """
        ...

    def createRepository(self, name: unicode) -> ghidra.framework.remote.RepositoryHandle:
        """
        Create a new repository on the server.  The newly created RepositoryHandle will contain
         a unique project ID for the client.
        @param name repository name.
         This ID will be used to identify and maintain checkout data.
        @return handle to new repository.
        @throws DuplicateFileException
        @throws UserAccessException
        @throws IOException if an IO error occurs
        """
        ...

    def deleteRepository(self, name: unicode) -> None:
        """
        Delete a repository.
        @param name repository name.
        @throws UserAccessException if user does not have permission to delete repository
        @throws IOException if an IO error occurs
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getAllUsers(self) -> List[unicode]:
        """
        Returns a list of all known users.
        @throws IOException if an IO error occurs
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getPasswordExpiration(self) -> long:
        """
        Returns the amount of time in milliseconds until the
         user's password will expire.
        @return time until expiration or -1 if it will not expire
        @throws IOException if an IO error occurs
        """
        ...

    def getRepository(self, name: unicode) -> ghidra.framework.remote.RepositoryHandle:
        """
        Get a handle to an existing repository.
        @param name repository name.
        @return repository handle or null if repository does not exist.
        @throws UserAccessException if user does not have permission to access repository
        @throws IOException if an IO error occurs
        """
        ...

    def getRepositoryNames(self) -> List[unicode]:
        """
        Returns a list of all repository names which are accessable by the current user.
        @throws IOException if an IO error occurs
        """
        ...

    def getUser(self) -> unicode:
        """
        Returns current user for which this handle belongs.
        @throws IOException if an IO error occurs
        """
        ...

    def hashCode(self) -> int: ...

    def isReadOnly(self) -> bool:
        """
        @return true if user has restricted read-only access to server (e.g., anonymous user)
        @throws IOException if an IO error occurs
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setPassword(self, saltedSHA256PasswordHash: List[int]) -> bool:
        """
        Set the password for the user.
        @param saltedSHA256PasswordHash SHA256 salted password hash
        @return true if password changed
        @throws IOException if an IO error occurs
        @see ghidra.util.HashUtilities#getSaltedHash(String, char[]) HashUtilities.getSaltedHash("SHA-256", char[])
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
    def allUsers(self) -> List[unicode]: ...

    @property
    def password(self) -> None: ...  # No getter available.

    @password.setter
    def password(self, value: List[int]) -> None: ...

    @property
    def passwordExpiration(self) -> long: ...

    @property
    def readOnly(self) -> bool: ...

    @property
    def repositoryNames(self) -> List[unicode]: ...

    @property
    def user(self) -> unicode: ...
