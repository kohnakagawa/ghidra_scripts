from typing import List
import db.buffers
import ghidra.framework.remote
import ghidra.framework.store
import ghidra.server.store
import java.lang


class RepositoryFile(object):








    def checkout(self, __a0: ghidra.framework.store.CheckoutType, __a1: unicode, __a2: unicode) -> ghidra.framework.store.ItemCheckoutStatus: ...

    def delete(self, __a0: int, __a1: unicode) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getCheckout(self, __a0: long, __a1: unicode) -> ghidra.framework.store.ItemCheckoutStatus: ...

    def getCheckouts(self, __a0: unicode) -> List[ghidra.framework.store.ItemCheckoutStatus]: ...

    def getClass(self) -> java.lang.Class: ...

    def getItem(self) -> ghidra.framework.remote.RepositoryItem: ...

    def getName(self) -> unicode: ...

    def getParent(self) -> ghidra.server.store.RepositoryFolder: ...

    def getPathname(self) -> unicode: ...

    def getVersions(self, __a0: unicode) -> List[ghidra.framework.store.Version]: ...

    def hasCheckouts(self) -> bool: ...

    def hashCode(self) -> int: ...

    def isCheckinActive(self) -> bool: ...

    def itemChanged(self) -> None: ...

    def length(self) -> long: ...

    def moveTo(self, __a0: ghidra.server.store.RepositoryFolder, __a1: unicode, __a2: unicode) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def openDatabase(self, __a0: long, __a1: unicode) -> db.buffers.LocalManagedBufferFile: ...

    @overload
    def openDatabase(self, __a0: int, __a1: int, __a2: unicode) -> db.buffers.LocalManagedBufferFile: ...

    def terminateCheckout(self, __a0: long, __a1: unicode, __a2: bool) -> None: ...

    def toString(self) -> unicode: ...

    def updateCheckoutVersion(self, __a0: long, __a1: int, __a2: unicode) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def checkinActive(self) -> bool: ...

    @property
    def item(self) -> ghidra.framework.remote.RepositoryItem: ...

    @property
    def name(self) -> unicode: ...

    @property
    def parent(self) -> ghidra.server.store.RepositoryFolder: ...

    @property
    def pathname(self) -> unicode: ...