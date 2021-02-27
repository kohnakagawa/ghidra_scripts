from typing import List
import ghidra.program.model.listing
import ghidra.program.util
import java.lang
import java.util.function


class DataLocationListContext(object):
    """
    Context mix-in interface that ActionContexts can implement if they can provide a list of
     Data object's ProgramLocation's.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getCount(self) -> int:
        """
        Returns the number of {@link Data} objects for the current action context.
        @return the number of {@link Data} objects for the current action context.
        """
        ...

    @overload
    def getDataLocationList(self) -> List[ghidra.program.util.ProgramLocation]:
        """
        Returns a list of the locations of the current {@link Data} objects in the current action context.
        @return a list of the locations of the current {@link Data} objects in the current action context.
        """
        ...

    @overload
    def getDataLocationList(self, filter: java.util.function.Predicate) -> List[ghidra.program.util.ProgramLocation]:
        """
        Returns a list of the locations of the current {@link Data} objects in the current action context that pass the given filter.
         <P>
        @param filter a filter to apply to the current context's Data list, <code>null</code>
         implies all elements match.
        @return a list of the locations of the current {@link Data} objects in the current action context that pass the given filter.
        """
        ...

    def getProgram(self) -> ghidra.program.model.listing.Program:
        """
        Returns the program for the current action context.
        @return the program for the current action context.
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
    def count(self) -> int: ...

    @property
    def dataLocationList(self) -> List[object]: ...

    @property
    def program(self) -> ghidra.program.model.listing.Program: ...
