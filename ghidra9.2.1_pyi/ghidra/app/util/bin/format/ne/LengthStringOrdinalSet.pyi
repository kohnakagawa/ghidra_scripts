import ghidra.app.util.bin.format.ne
import java.lang


class LengthStringOrdinalSet(ghidra.app.util.bin.format.ne.LengthStringSet):
    """
    A class to hold a length/string/ordinal set.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getIndex(self) -> long:
        """
        Returns the byte index of this string,
         relative to the beginning of the file.
        @return the byte index of this string
        """
        ...

    def getLength(self) -> int:
        """
        Returns the length of the string.
        @return the length of the string
        """
        ...

    def getOrdinal(self) -> int:
        """
        Returns the ordinal value.
        @return the ordinal value
        """
        ...

    def getString(self) -> unicode:
        """
        Returns the string.
        @return the string
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
    def ordinal(self) -> int: ...
