from typing import List
import ghidra.app.util.bin.format.ne
import java.lang


class ModuleReferenceTable(object):
    """
    A class to represent the new-executable module reference table.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getNames(self) -> List[ghidra.app.util.bin.format.ne.LengthStringSet]:
        """
        Returns the array of names.
        @return the array of names
        """
        ...

    def getOffsets(self) -> List[int]:
        """
        Returns the array of offsets.
        @return the array of offsets
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
    def names(self) -> List[ghidra.app.util.bin.format.ne.LengthStringSet]: ...

    @property
    def offsets(self) -> List[int]: ...
