from typing import List
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.util.bytesearch
import ghidra.util.task
import java.lang


class MemoryBytePatternSearcher(object):
    """
    Multi pattern/mask/action memory searcher
     Patterns must be supplied/added, or a pre-initialized searchState supplied

     Preload search patterns and actions, then call search method.
    """





    @overload
    def __init__(self, searchName: unicode):
        """
        Create with no patternList, must add patterns before searching
        @param searchName name of search
        """
        ...

    @overload
    def __init__(self, searchName: unicode, root: ghidra.util.bytesearch.SequenceSearchState):
        """
        Create with an initialized SequenceSearchState
        @param searchName name of search
        @param root search state pre-initialized
        """
        ...

    @overload
    def __init__(self, __a0: unicode, __a1: java.util.ArrayList): ...



    def addPattern(self, pattern: ghidra.util.bytesearch.Pattern) -> None:
        """
        Add a search pattern
        @param pattern - pattern(bytes/mask/action)
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def postMatchApply(self, matchactions: List[ghidra.util.bytesearch.MatchAction], addr: ghidra.program.model.address.Address) -> None:
        """
        Called after any match rules are applied
         Can use for cross post rule matching state application and cleanup.
        @param matchactions actions that matched
        @param addr adress of match
        """
        ...

    def preMatchApply(self, matchactions: List[ghidra.util.bytesearch.MatchAction], addr: ghidra.program.model.address.Address) -> None:
        """
        Called before any match rules are applied
        @param matchactions actions that matched
        @param addr address of match
        """
        ...

    def search(self, program: ghidra.program.model.listing.Program, searchSet: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Search initialized memory blocks for all patterns(bytes/mask/action).
         Call associated action for each pattern matched.
        @param program to be searched
        @param searchSet set of bytes to restrict search, if null or empty then search all memory blocks
        @param monitor allow canceling and reporting of progress
        @throws CancelledException if canceled
        """
        ...

    def setSearchExecutableOnly(self, doExecutableBlocksOnly: bool) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def searchExecutableOnly(self) -> None: ...  # No getter available.

    @searchExecutableOnly.setter
    def searchExecutableOnly(self, value: bool) -> None: ...
