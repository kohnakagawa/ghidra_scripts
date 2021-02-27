from typing import List
import java.lang


class ProgramMergeFilter(object):
    """
    The ProgramMergeFilter is used to specify which portions of a
     program should be merged into another program.
     It indicates the types of program differences to merge.
     Each merge type can have its filter set to IGNORE or REPLACE.
     IGNORE indicates no interest in replacing or merging that type of difference.
     REPLACE indicates to replace differences in program1 with differences of
     that type from program2.
     Some merge types (for example, COMMENTS and SYMBOLS) allow the filter to be
     set to MERGE.
     MERGE indicates that the type should
     be taken from Program2 and merged into Program1 with whatever is alreaady there.
    """

    ALL: int = 131071
    BOOKMARKS: int = 2048
    BYTES: int = 2
    CODE_UNITS: int = 12
    COMMENTS: int = 992
    DATA: int = 8
    EOL_COMMENTS: int = 128
    EQUATES: int = 16384
    FUNCTIONS: int = 8192
    FUNCTION_TAGS: int = 65536
    IGNORE: int = 0
    INSTRUCTIONS: int = 4
    INVALID: int = -1
    MERGE: int = 2
    PLATE_COMMENTS: int = 32
    POST_COMMENTS: int = 512
    PRE_COMMENTS: int = 64
    PRIMARY_SYMBOL: int = 32768
    PROGRAM_CONTEXT: int = 1
    PROPERTIES: int = 4096
    REFERENCES: int = 16
    REPEATABLE_COMMENTS: int = 256
    REPLACE: int = 1
    SYMBOLS: int = 1024



    @overload
    def __init__(self):
        """
        Creates new ProgramMergeFilter with none of the merge types selected.
        """
        ...

    @overload
    def __init__(self, filter: ghidra.program.util.ProgramMergeFilter):
        """
        Creates new ProgramMergeFilter that is equal to the specified ProgramMergeFilter.
        """
        ...

    @overload
    def __init__(self, type: int, filter: int):
        """
        Creates new ProgramMergeFilter with the specified merge types selected.
        @param type the type of difference to look for between the programs.
        @param filter IGNORE, REPLACE, or MERGE. Indicates
         which program difference to include of the specified type.
         If a particular type cannot be set to MERGE then it will be set to REPLACE.
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

    @staticmethod
    def filterToName(type: int) -> unicode:
        """
        <CODE>filterToName</CODE> returns the string associated with an
         individual (primary) merge difference setting.
        @param type the type of filter.
         Valid types are: IGNORE, REPLACE, MERGE.
        @return the string indicating the merge difference setting.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getFilter(self, type: int) -> int:
        """
        getFilter determines whether or not the specified type of filter is set.
         Valid types are: BYTES, INSTRUCTIONS, DATA,
         SYMBOLS, PRIMARY_SYMBOL, COMMENTS, PROGRAM_CONTEXT, PROPERTIES, BOOKMARKS, FUNCTIONS.
         INVALID is returned if combinations of merge types (e.g. ALL) are
         passed in.
        @param type the merge type.
        @return IGNORE, REPLACE, or MERGE. INVALID if parameter is a combination of
         types or not a predefined primary type.
        """
        ...

    @staticmethod
    def getPrimaryTypes() -> List[int]:
        """
        Gets all the valid individual types of differences for this filter.
        @return an array containing all the currently defined primary difference
         types.
        """
        ...

    def hashCode(self) -> int: ...

    def isSet(self) -> bool:
        """
        Determines if at least one of the filter types is set to REPLACE or MERGE.
        @return true if at least one type is set.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setFilter(self, type: int, filter: int) -> None:
        """
        setFilter specifies whether or not the indicated type of item will
         not be included by the filter (IGNORE), replaced in the first program using the type of
         item in the second program (REPLACE), or included from both programs (MERGE).
         Valid types are: BYTES, INSTRUCTIONS, DATA, REFERENCES,
         SYMBOLS, PRIMARY_SYMBOL, COMMENTS, PROPERTIES, BOOKMARKS, FUNCTIONS, ALL, or combinations of
         these "OR"ed together.
         if <CODE>MERGE</CODE> is not valid for an included primary type, then it
         will be set to <CODE>REPLACE</CODE> instead for that primary type.
        @param type the type(s) of difference(s) to include.
        @param filter IGNORE, REPLACE, or MERGE. Indicates whether to include none,
         one, or both programs' differences of the specified type.
        """
        ...

    def toString(self) -> unicode:
        """
        Returns a printable string indicating the current settings of this filter.
        @return the current settings for this filter.
        """
        ...

    @staticmethod
    def typeToName(type: int) -> unicode:
        """
        <CODE>typeToName()</CODE> returns the name of a predefined merge type.
          Only predefined types, as specified in <CODE>ProgramMergeFilter</CODE>,
          will return a name. Otherwise, an empty string is returned.
        @param type the type of merge difference whose name is wanted.
         Valid types are: BYTES, INSTRUCTIONS, DATA, REFERENCES,
         SYMBOLS, PRIMARY_SYMBOL, COMMENTS, PROGRAM_CONTEXT, PROPERTIES, BOOKMARKS, FUNCTIONS, ALL.
        @return the name of the predefined merge difference type.
         Otherwise, the empty string.
        """
        ...

    def validatePredefinedType(self, type: int) -> bool:
        """
        validatePredefinedType determines whether or not the indicated type
         of filter item is a valid predefined type.
         Valid types are: BYTES, INSTRUCTIONS, DATA,
         SYMBOLS, PRIMARY_SYMBOL, COMMENTS, PROGRAM_CONTEXT, PROPERTIES, BOOKMARKS, FUNCTIONS, ALL.
        @param type the type of difference to look for between the programs.
        @return true if this is a pre-defined merge type.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def set(self) -> bool: ...
