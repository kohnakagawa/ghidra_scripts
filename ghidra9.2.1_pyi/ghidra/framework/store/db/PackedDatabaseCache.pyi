import ghidra.framework.store.db
import java.lang


class PackedDatabaseCache(object):








    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def getCache() -> ghidra.framework.store.db.PackedDatabaseCache: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isEnabled() -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
