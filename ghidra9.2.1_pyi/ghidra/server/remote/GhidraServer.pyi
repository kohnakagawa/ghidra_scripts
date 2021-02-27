from typing import List
import ghidra.framework.remote
import java.io
import java.lang
import java.rmi
import java.rmi.server
import javax.security.auth
import javax.security.auth.callback


class GhidraServer(java.rmi.server.UnicastRemoteObject, ghidra.framework.remote.GhidraServerHandle):








    def checkCompatibility(self, __a0: int) -> None: ...

    def clone(self) -> object: ...

    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    @overload
    @staticmethod
    def exportObject(__a0: java.rmi.Remote) -> java.rmi.server.RemoteStub: ...

    @overload
    @staticmethod
    def exportObject(__a0: java.rmi.Remote, __a1: int) -> java.rmi.Remote: ...

    @overload
    @staticmethod
    def exportObject(__a0: java.rmi.Remote, __a1: int, __a2: java.io.ObjectInputFilter) -> java.rmi.Remote: ...

    @overload
    @staticmethod
    def exportObject(__a0: java.rmi.Remote, __a1: int, __a2: java.rmi.server.RMIClientSocketFactory, __a3: java.rmi.server.RMIServerSocketFactory) -> java.rmi.Remote: ...

    @overload
    @staticmethod
    def exportObject(__a0: java.rmi.Remote, __a1: int, __a2: java.rmi.server.RMIClientSocketFactory, __a3: java.rmi.server.RMIServerSocketFactory, __a4: java.io.ObjectInputFilter) -> java.rmi.Remote: ...

    def getAuthenticationCallbacks(self) -> List[javax.security.auth.callback.Callback]: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getClientHost() -> unicode: ...

    @staticmethod
    def getLog() -> java.io.PrintStream: ...

    @staticmethod
    def getRMIClientSocketFactory() -> java.rmi.server.RMIClientSocketFactory: ...

    @staticmethod
    def getRMIServerSocketFactory() -> java.rmi.server.RMIServerSocketFactory: ...

    def getRef(self) -> java.rmi.server.RemoteRef: ...

    def getRepositoryServer(self, __a0: javax.security.auth.Subject, __a1: List[javax.security.auth.callback.Callback]) -> ghidra.framework.remote.RemoteRepositoryServerHandle: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def main(__a0: List[unicode]) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def setLog(__a0: java.io.OutputStream) -> None: ...

    def toString(self) -> unicode: ...

    @staticmethod
    def toStub(__a0: java.rmi.Remote) -> java.rmi.Remote: ...

    @staticmethod
    def unexportObject(__a0: java.rmi.Remote, __a1: bool) -> bool: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def authenticationCallbacks(self) -> List[javax.security.auth.callback.Callback]: ...
