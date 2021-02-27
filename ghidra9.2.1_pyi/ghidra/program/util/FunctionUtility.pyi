from typing import List
import ghidra.program.model.listing
import java.lang


class FunctionUtility(object):
    """
    Utility methods for performing function related actions.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getFunctionTitle(function: ghidra.program.model.listing.Function) -> unicode:
        """
        Gets a title string wrapped as HTML and indicating the function's name and the program
         containing it.
        @param function the function to be indicated in the title.
        @return the title string as HTML.
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isSameLanguage(program1: ghidra.program.model.listing.Program, program2: ghidra.program.model.listing.Program) -> bool:
        """
        Determines whether or not the two programs are considered to have the same processor
         language and compiler specification.
        @param program1 the first program
        @param program2 the second program
        @return true if the two programs have the same processor language and compiler spec.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def setUniqueParameterNames(__a0: ghidra.program.model.listing.Function, __a1: List[object]) -> None: ...

    def toString(self) -> unicode: ...

    @staticmethod
    def updateFunction(destinationFunction: ghidra.program.model.listing.Function, sourceFunction: ghidra.program.model.listing.Function) -> None:
        """
        Updates the destination function so its signature will match the source function's signature
         as closely as possible. This method will try to create conflict names if necessary for the
         function and its parameters.
        @param destinationFunction the destination function to update
        @param sourceFunction the source function to use as a template
        @throws InvalidInputException if the function name or a variable name is invalid or if a
         parameter data type is not a fixed length.
        @throws DuplicateNameException This shouldn't happen since it will try to create conflict
         names for the function and its variables if necessary. Otherwise, this would be because
         the function's name or a variable name already exists.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
