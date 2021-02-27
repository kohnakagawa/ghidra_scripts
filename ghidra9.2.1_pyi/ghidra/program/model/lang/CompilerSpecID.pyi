import ghidra.program.model.lang
import java.lang


class CompilerSpecID(object, java.lang.Comparable):
    """
    Represents an opinion's compiler (gcc, borlandcpp, etc).
    """





    def __init__(self, id: unicode):
        """
        Creates a new compiler spec ID.
        @param id The compiler ID (gcc, borlandcpp, etc).
        """
        ...



    @overload
    def compareTo(self, o: ghidra.program.model.lang.CompilerSpecID) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getIdAsString(self) -> unicode:
        """
        Gets the compiler spec ID as a string.
        @return The compilers spec ID as a string.
        @throws IllegalArgumentException if the compiler spec ID is null or empty.
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
