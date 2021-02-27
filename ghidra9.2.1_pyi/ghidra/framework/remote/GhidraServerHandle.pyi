from typing import List
import ghidra.framework.remote
import java.lang
import java.rmi
import javax.security.auth
import javax.security.auth.callback


class GhidraServerHandle(java.rmi.Remote, object):
    """
    GhidraServerHandle provides access to a remote server.
     This remote interface facilitates user login/authentication, providing
     a more useful handle to the associated repository server.
    """

    BIND_NAME: unicode = u'GhidraServer9.0'
    BIND_NAME_PREFIX: unicode = u'GhidraServer'
    DEFAULT_PORT: int = 13100
    INTERFACE_VERSION: int = 11
    MIN_GHIDRA_VERSION: unicode = u'9.0'







    def checkCompatibility(self, serverInterfaceVersion: int) -> None:
        """
        Check server interface compatibility
        @param serverInterfaceVersion client/server interface version
        @throws RemoteException
        @see #INTERFACE_VERSION
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getAuthenticationCallbacks(self) -> List[javax.security.auth.callback.Callback]:
        """
        Returns user authentication proxy object.
        @throws RemoteException
        @return authentication callbacks which must be satisfied or null if authentication not
         required.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getRepositoryServer(self, user: javax.security.auth.Subject, authCallbacks: List[javax.security.auth.callback.Callback]) -> ghidra.framework.remote.RemoteRepositoryServerHandle:
        """
        Get a handle to the repository server.
        @param user user subject containing GhidraPrincipal
        @param authCallbacks valid authentication callback objects which have been satisfied, or
         null if server does not require authentication.
        @return repository server handle.
        @throws LoginException if user authentication fails
        @throws RemoteException
        @see #getAuthenticationCallbacks()
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
    def authenticationCallbacks(self) -> List[javax.security.auth.callback.Callback]: ...
