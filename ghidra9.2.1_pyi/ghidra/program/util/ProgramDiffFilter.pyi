from typing import List
import ghidra.program.util
import java.lang


class ProgramDiffFilter(object):
    """
    The ProgramDiffFilter is used when determining or working with
     differences between two programs.
     It indicates the types of program differences we are interested in.
     Each difference type can be set to true, indicating interest in
     differences of that type between two programs. False indicates no interest
     in this type of program difference.
     Valid filter types are:
     BYTE_DIFFS, CODE_UNIT_DIFFS,
     PLATE_COMMENT_DIFFS, PRE_COMMENT_DIFFS, EOL_COMMENT_DIFFS,
     REPEATABLE_COMMENT_DIFFS, POST_COMMENT_DIFFS,
     REFERENCE_DIFFS,
     USER_DEFINED_DIFFS, BOOKMARK_DIFFS,
     SYMBOL_DIFFS,
     EQUATE_DIFFS, FUNCTION_DIFFS, PROGRAM_CONTEXT_DIFFS.
     Predefined filter type combinations are:
     COMMENT_DIFFS and ALL_DIFFS.
    """

    ALL_DIFFS: int = 32767
    BOOKMARK_DIFFS: int = 4096
    BYTE_DIFFS: int = 2
    CODE_UNIT_DIFFS: int = 4
    COMMENT_DIFFS: int = 248
    EOL_COMMENT_DIFFS: int = 8
    EQUATE_DIFFS: int = 512
    FUNCTION_DIFFS: int = 2048
    FUNCTION_TAG_DIFFS: int = 16384
    PLATE_COMMENT_DIFFS: int = 64
    POST_COMMENT_DIFFS: int = 32
    PRE_COMMENT_DIFFS: int = 16
    PROGRAM_CONTEXT_DIFFS: int = 1
    REFERENCE_DIFFS: int = 256
    REPEATABLE_COMMENT_DIFFS: int = 128
    SYMBOL_DIFFS: int = 1024
    USER_DEFINED_DIFFS: int = 8192



    @overload
    def __init__(self):
        """
        Creates new ProgramDiffFilter with none of the diff types selected.
        """
        ...

    @overload
    def __init__(self, type: int):
        """
        Creates new ProgramDiffFilter with the specified diff types selected.
        @param type one or more of the diff types "OR"ed together.
         <BR>i.e. CODE_UNIT_DIFFS | SYMBOL_DIFFS
        """
        ...

    @overload
    def __init__(self, filter: ghidra.program.util.ProgramDiffFilter):
        """
        Creates new ProgramDiffFilter equivalent to the specified ProgramDiffFilter.
        @param filter the diff filter this one should equal.
        """
        ...



    def addToFilter(self, filter: ghidra.program.util.ProgramDiffFilter) -> None:
        """
        set this filter to look for types of differences in addition to those
         types where it is already looking for differences.
         The filter that is passed as a parameter indicates the additional types
         of differences.
        @param filter filter indicating the additional types of differences
         to look for between the programs.
        """
        ...

    def clearAll(self) -> None:
        """
        Sets all the defined types of differences to false.
         Filter indicates no interest in any difference types.
        """
        ...

    def equals(self, obj: object) -> bool:
        """
        Determines whether or not this filter is equal to the object that
         is passed in.
        @param obj the object to compare this one with.
        @return true if the filter matches this one.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getFilter(self, type: int) -> bool:
        """
        getFilter determines whether or not the specified type of filter is set.
        @param type the set bits indicate the type of differences we want to
         check as being set in the filter.
         <BR>For example, one or more of the diff types "OR"ed together.
         <BR>i.e. CODE_UNIT_DIFFS | SYMBOL_DIFFS
        @return true if filtering for the specified type of differences.
        """
        ...

    @staticmethod
    def getPrimaryTypes() -> List[int]:
        """
        Gets all the valid individual types of differences for this filter.
         These are also referred to as primary difference types.
        @return an array containing all the currently defined difference types
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def selectAll(self) -> None:
        """
        Sets all the defined types of differences to true.
         Filter indicates interest in all difference types.
        """
        ...

    def setFilter(self, type: int, filter: bool) -> None:
        """
        setFilter specifies whether or not the indicated type of difference will be
         included by the filter (true) or not included (false).
        @param type the set bits indicate the type of differences we want to
         look for in the programs.
         <BR>For example, one or more of the diff types "OR"ed together.
         <BR>i.e. CODE_UNIT_DIFFS | SYMBOL_DIFFS
        @param filter true if you want to determine differences of the specified type.
        """
        ...

    def toString(self) -> unicode:
        """
        Returns a string representation of the current settings for this filter.
        """
        ...

    @staticmethod
    def typeToName(type: int) -> unicode:
        """
        <CODE>typeToName()</CODE> returns the name of the difference type.
          Only predefined types, as specified in <CODE>ProgramDiffFilter</CODE>,
          will return a name. Otherwise, an empty string is returned.
        @param type the type of difference whose name is wanted.
        @return the name of the predefined difference type. Otherwise, the empty string.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
