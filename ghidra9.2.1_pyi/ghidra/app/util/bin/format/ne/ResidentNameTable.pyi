from typing import List
import ghidra.app.util.bin.format.ne
import java.lang


class ResidentNameTable(object):
    """
    A class to represent the new-executable resident name table.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getNames(self) -> List[ghidra.app.util.bin.format.ne.LengthStringOrdinalSet]:
        """
        Returns the array of names defined in the resident name table.
        @return the array of names defined in the resident name table
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
    def names(self) -> List[ghidra.app.util.bin.format.ne.LengthStringOrdinalSet]: ...
