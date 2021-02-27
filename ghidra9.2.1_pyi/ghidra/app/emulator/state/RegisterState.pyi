from typing import List
import java.lang
import java.util


class RegisterState(object):








    def dispose(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getKeys(self) -> java.util.Set: ...

    def getVals(self, key: unicode) -> List[int]: ...

    def hashCode(self) -> int: ...

    def isInitialized(self, key: unicode) -> List[bool]: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def setVals(self, key: unicode, vals: List[int], setInitiailized: bool) -> None: ...

    @overload
    def setVals(self, key: unicode, val: long, size: int, setInitiailized: bool) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def keys(self) -> java.util.Set: ...