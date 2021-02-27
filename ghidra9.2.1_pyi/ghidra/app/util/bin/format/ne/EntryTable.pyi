from typing import List
import ghidra.app.util.bin.format.ne
import java.lang


class EntryTable(object):
    """
    A class to represent a new-executable entry table.
    """









    def equals(self, __a0: object) -> bool: ...

    def getBundles(self) -> List[ghidra.app.util.bin.format.ne.EntryTableBundle]:
        """
        Returns an array of the entry table bundles in this
         entry table.
        @return an array of entry table bundles
        """
        ...

    def getClass(self) -> java.lang.Class: ...

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
    def bundles(self) -> List[ghidra.app.util.bin.format.ne.EntryTableBundle]: ...
