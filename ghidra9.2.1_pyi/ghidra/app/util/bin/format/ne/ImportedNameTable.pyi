import ghidra.app.util.bin.format.ne
import java.lang


class ImportedNameTable(object):
    """
    A class to represent the new-executable imported name table.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getNameAt(self, offset: int) -> ghidra.app.util.bin.format.ne.LengthStringSet:
        """
        Returns the length/string set at the given offset.
        @param offset The offset, from the beginning of the Imported Name Table,
                        to the length/string set.
        @return the length/string set at the given offset
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
