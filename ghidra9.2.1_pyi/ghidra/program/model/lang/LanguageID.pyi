import ghidra.program.model.lang
import java.lang


class LanguageID(object, java.lang.Comparable):
    """
    Represents an opinion's processor language (x86:LE:32:default, 8051:BE:16:default, etc).
    """





    def __init__(self, id: unicode):
        """
        Creates a new language ID.
        @param id The language ID (x86:LE:32:default, 8051:BE:16:default, etc).
        @throws IllegalArgumentException if the language ID is null or empty.
        """
        ...



    @overload
    def compareTo(self, o: ghidra.program.model.lang.LanguageID) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getIdAsString(self) -> unicode:
        """
        Gets the compiler spec ID as a string.
        @return The compilers spec ID as a string.
        @throws IllegalArgumentException if the compiler spec ID is not null or empty.
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
    def idAsString(self) -> unicode: ...
