from typing import List
import java.lang


class OMFFileIndex(object):
    """
    A class to represent the Object Module Format (OMF) File Index data structure.


     short cMod 		 - Count or number of modules in the executable.
     short cRef 		 - Count or number of file name references.
     short [] modStart - array of indices into the nameoffset table for each module.  Each index is the start of the file name references for each module.
     short cRefCnt 	 - number of file name references per module.
     int [] nameRef 	 - array of offsets in to the names table.  For each module the offset to the first references file name is at nameRef[modStart] and continues for cRefCnt entries.
     String names 	 - file names.

    """





    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getCMod(self) -> int:
        """
        Returns the number of modules in the executable.
        @return the number of modules in the executable
        """
        ...

    def getCRef(self) -> int:
        """
        Returns the number of file name references in the executable.
        @return the number of file name references in the executable
        """
        ...

    def getCRefCnt(self) -> List[int]:
        """
        Returns the indices into the nameoffset table for each file.
        @return the indices into the nameoffset table for each file
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getModStart(self) -> List[int]:
        """
        Returns the array of indices into the nameoffset table for each module.
        @return the array of indices into the nameoffset table for each module
        """
        ...

    def getNameRef(self) -> List[int]:
        """
        Returns the array of offsets into the names table.
        @return the array of offsets in to the names table
        """
        ...

    def getNames(self) -> List[unicode]:
        """
        Returns the file names referenced in the executable.
        @return the file names referenced in the executable
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
    def CMod(self) -> int: ...

    @property
    def CRef(self) -> int: ...

    @property
    def CRefCnt(self) -> List[int]: ...

    @property
    def modStart(self) -> List[int]: ...

    @property
    def nameRef(self) -> List[int]: ...

    @property
    def names(self) -> List[unicode]: ...
