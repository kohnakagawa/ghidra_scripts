import ghidra.program.model.listing
import java.lang


class CodeUnitDetails(object):
    """
    This is a class with static methods for obtaining information about a code unit and its
     references. The information is provided as a String.
    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getCodeUnitDetails(cu: ghidra.program.model.listing.CodeUnit) -> unicode:
        """
        Gets a string that indicates the code unit along with its overrides.
         This can contain new line characters.
        @param cu the code unit
        @return info about the code unit.
        """
        ...

    @staticmethod
    def getInstructionDetails(cu: ghidra.program.model.listing.CodeUnit) -> unicode:
        """
        Gets a string that indicates the code unit along with its overrides and its "from" references.
         This can contain new line characters.
        @param cu the code unit
        @return info about the code unit and its references.
        """
        ...

    @staticmethod
    def getReferenceDetails(cu: ghidra.program.model.listing.CodeUnit) -> unicode:
        """
        Gets a string that indicates the references from a code unit.
         This can contain new line characters.
         <br>Note: Data currently only indicates references on the minimum address.
        @param cu the code unit
        @return info about the code unit's references.
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
