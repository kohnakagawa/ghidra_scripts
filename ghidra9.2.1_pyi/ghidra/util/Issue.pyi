from typing import List
import ghidra.util
import java.lang


class Issue(object):








    def equals(self, __a0: object) -> bool: ...

    def getCategory(self) -> unicode:
        """
        Returns the category for this issue.  Categories may use '.' as separators to present
         a hierarchical category structure.
        @return the category for this issue.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode:
        """
        Returns a detailed description of the issue.
        @return a detailed description of the issue.
        """
        ...

    def getPossibleFixups(self) -> List[ghidra.util.Fixup]:
        """
        Returns a list of possible Fixup objects for this issue.
        @return a list of possible Fixup objects for this issue. This list may be empty, but not null.
        """
        ...

    def getPrimaryLocation(self) -> ghidra.util.Location:
        """
        Returns a Location object that describes where the issue occurred.
        @return a Location object that describes where the issue occurred. May return null
         if the issue is not related to a specific location.
        """
        ...

    def getSecondaryLocations(self) -> List[ghidra.util.Location]:
        """
        Returns a list of locations related to the issue that are not the primary issue location.
        @return a list of locations related to the issue that are not the primary issue location.
         This list may be empty, but not null.
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
    def category(self) -> unicode: ...

    @property
    def description(self) -> unicode: ...

    @property
    def possibleFixups(self) -> List[object]: ...

    @property
    def primaryLocation(self) -> ghidra.util.Location: ...

    @property
    def secondaryLocations(self) -> List[object]: ...
