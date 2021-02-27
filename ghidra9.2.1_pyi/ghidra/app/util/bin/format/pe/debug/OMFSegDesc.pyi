import java.lang


class OMFSegDesc(object):
    """
    A class to represent the Object Module Format (OMF) Segment Descriptor data structure.
     Information describing each segment in a module.


     typedef struct OMFSegDesc {
         unsigned short  Seg;            // segment index
         unsigned short  pad;            // pad to maintain alignment
         unsigned long   Off;            // offset of code in segment
         unsigned long   cbSeg;          // number of bytes in segment
     } OMFSegDesc;

    """





    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getAlignmentPad(self) -> int:
        """
        Returns the pad to maintain alignment.
        @return the pad to maintain alignment
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getNumberOfBytes(self) -> int:
        """
        Returns the number of bytes in segment.
        @return the number of bytes in segment
        """
        ...

    def getOffset(self) -> int:
        """
        Returns the offset of code in segment.
        @return the offset of code in segment
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
    def alignmentPad(self) -> int: ...

    @property
    def numberOfBytes(self) -> int: ...

    @property
    def offset(self) -> int: ...

    @property
    def segmentIndex(self) -> int: ...
