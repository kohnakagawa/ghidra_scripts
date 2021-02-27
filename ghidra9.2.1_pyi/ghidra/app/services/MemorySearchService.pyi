from typing import List
import ghidra.app.context
import java.lang


class MemorySearchService(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def search(self, bytes: List[int], context: ghidra.app.context.NavigatableActionContext) -> None: ...

    def setIsMnemonic(self, isMnemonic: bool) -> None: ...

    def setSearchText(self, maskedString: unicode) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def isMnemonic(self) -> None: ...  # No getter available.

    @isMnemonic.setter
    def isMnemonic(self, value: bool) -> None: ...

    @property
    def searchText(self) -> None: ...  # No getter available.

    @searchText.setter
    def searchText(self, value: unicode) -> None: ...
