import ghidra.program.model.listing
import ghidra.program.util
import java.lang


class CommentType(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getCommentType(cu: ghidra.program.model.listing.CodeUnit, loc: ghidra.program.util.ProgramLocation, defaultCommentType: int) -> int:
        """
        Get the comment type from the current location. If the cursor
         is not over a comment, then just return EOL as the default.
        @param cu
        @param loc
        @param defaultCommentType
        @return comment type
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isCommentAllowed(cu: ghidra.program.model.listing.CodeUnit, loc: ghidra.program.util.ProgramLocation) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
