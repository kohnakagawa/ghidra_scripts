from typing import List
import ghidra.framework.remote
import ghidra.framework.store
import ghidra.framework.store.local
import ghidra.server.remote
import ghidra.server.store
import java.lang


class Repository(object, ghidra.framework.store.FileSystemListener, ghidra.framework.store.local.RepositoryLogger):
    ANONYMOUS_USER: ghidra.framework.remote.User = -anonymous- (read-only)



    def __init__(self, __a0: ghidra.server.RepositoryManager, __a1: unicode, __a2: java.io.File, __a3: unicode): ...



    def addHandle(self, __a0: ghidra.server.remote.RepositoryHandleImpl) -> None: ...

    def anonymousAccessAllowed(self) -> bool: ...

    def dropHandle(self, __a0: ghidra.server.remote.RepositoryHandleImpl) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def flushChangeEvents(self) -> None: ...

    def folderCreated(self, __a0: unicode, __a1: unicode) -> None: ...

    def folderDeleted(self, __a0: unicode, __a1: unicode) -> None: ...

    def folderMoved(self, __a0: unicode, __a1: unicode, __a2: unicode) -> None: ...

    def folderRenamed(self, __a0: unicode, __a1: unicode, __a2: unicode) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def getFolder(self, __a0: unicode, __a1: unicode, __a2: bool) -> ghidra.server.store.RepositoryFolder: ...

    def getItemCount(self) -> int: ...

    def getName(self) -> unicode: ...

    def getServerUserList(self, __a0: unicode) -> List[unicode]: ...

    def getSyncObject(self) -> object: ...

    def getUser(self, __a0: unicode) -> ghidra.framework.remote.User: ...

    def getUserList(self, __a0: unicode) -> List[ghidra.framework.remote.User]: ...

    def hashCode(self) -> int: ...

    def itemChanged(self, __a0: unicode, __a1: unicode) -> None: ...

    def itemCreated(self, __a0: unicode, __a1: unicode) -> None: ...

    def itemDeleted(self, __a0: unicode, __a1: unicode) -> None: ...

    def itemMoved(self, __a0: unicode, __a1: unicode, __a2: unicode, __a3: unicode) -> None: ...

    def itemRenamed(self, __a0: unicode, __a1: unicode, __a2: unicode) -> None: ...

    def log(self, __a0: unicode, __a1: unicode, __a2: unicode) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setUserList(self, __a0: unicode, __a1: List[ghidra.framework.remote.User], __a2: bool) -> None: ...

    def suspendEventDispatching(self) -> None: ...

    def syncronize(self) -> None: ...

    def toString(self) -> unicode: ...

    def validate(self) -> None: ...

    def validateAdminPrivilege(self, __a0: unicode) -> ghidra.framework.remote.User: ...

    def validateReadPrivilege(self, __a0: unicode) -> ghidra.framework.remote.User: ...

    def validateWritePrivilege(self, __a0: unicode) -> ghidra.framework.remote.User: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def itemCount(self) -> int: ...

    @property
    def name(self) -> unicode: ...

    @property
    def syncObject(self) -> object: ...
