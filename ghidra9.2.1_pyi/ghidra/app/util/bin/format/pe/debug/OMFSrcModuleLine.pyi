from typing import List
import java.lang


class OMFSrcModuleLine(object):
    """
    A class to represent the Object Module Format (OMF) Source Module Line data structure.

     short seg            - segment index.

     short cPair          - Count or number of source line pairs to follow.

     int [] offsets       - offset within the code segment of the start of the line.

     short [] linenumbers - line numbers that are in the source file that cause code to be emitted to the code segment.

    """





    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getLinenumbers(self) -> List[int]:
        """
        Returns the line numbers that are in the source file that cause code to be emitted to the code segment.
        @return the line numbers that are in the source file that cause code to be emitted to the code segment
        """
        ...

    def getOffsets(self) -> List[int]:
        """
        Returns the offset within the code segment of the start of the line.
        @return the offset within the code segment of the start of the line
        """
        ...

    def getPairCount(self) -> int:
        """
        Returns the count or number of source line pairs to follow.
        @return the count or number of source line pairs to follow
        """
        ...

    def getSegmentIndex(self) -> int:
        """
        Returns the segment index.
        @return the segment index
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
    def linenumbers(self) -> List[int]: ...

    @property
    def offsets(self) -> List[int]: ...

    @property
    def pairCount(self) -> int: ...

    @property
    def segmentIndex(self) -> int: ...
