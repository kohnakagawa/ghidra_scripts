from typing import List
import ghidra.app.decompiler
import ghidra.program.model.listing
import java.lang


class PrettyPrinter(object):
    """
    This class is used to convert a C language
     token group into readable C code.
    """

    INDENT_STRING: unicode = u' '



    def __init__(self, function: ghidra.program.model.listing.Function, tokgroup: ghidra.app.decompiler.ClangTokenGroup):
        """
        Constructs a new pretty printer using the specified C language token group.
        @param tokgroup the C language token group
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFunction(self) -> ghidra.program.model.listing.Function: ...

    def getLines(self) -> List[ghidra.app.decompiler.ClangLine]:
        """
        Returns an array list of the C language lines contained in the
         C language token group.
        @return an array list of the C language lines
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def print(self, removeInvalidChars: bool) -> ghidra.app.decompiler.DecompiledFunction:
        """
        Prints the C language token group
         into a string of C code.
        @param removeInvalidChars true if invalid character should be
         removed from functions and labels.
        @return a string of readable C code
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def function(self) -> ghidra.program.model.listing.Function: ...

    @property
    def lines(self) -> java.util.ArrayList: ...
