import java.lang


class OMFSegMapDesc(object):
    """
    A class to represent the Object Module Format (OMF) Segment Mapping Descriptor data structure.


     typedef struct OMFSegMapDesc {
         unsigned short  flags;       // descriptor flags bit field
         unsigned short  ovl;         // the logical overlay number
         unsigned short  group;       // group index into the descriptor array
         unsigned short  frame;       // logical segment index - interpreted via flags
         unsigned short  iSegName;    // segment or group name - index into sstSegName
         unsigned short  iClassName;  // class name - index into sstSegName
         unsigned long   offset;      // byte offset of the logical within the physical segment
         unsigned long   cbSeg;       // byte count of the logical segment or group
     } OMFSegMapDesc;

    """





    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getByteCount(self) -> int:
        """
        Returns the byte count of the logical segment or group.
        @return the byte count of the logical segment or group
        """
        ...

    def getByteOffset(self) -> int:
        """
        Returns the byte offset of the logical within the physical segment.
        @return the byte offset of the logical within the physical segment
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getClassName(self) -> int:
        """
        Returns the class name - index into sstSegName.
        @return the class name - index into sstSegName
        """
        ...

    def getFlags(self) -> int:
        """
        Returns the descriptor flags bit field.
        @return the descriptor flags bit field
        """
        ...

    def getGroupIndex(self) -> int:
        """
        Returns the group index into the descriptor array.
        @return the group index into the descriptor array
        """
        ...

    def getLogicalOverlayNumber(self) -> int:
        """
        Returns the logical overlay number.
        @return the logical overlay number
        """
        ...

    def getLogicalSegmentIndex(self) -> int:
        """
        Returns the logical segment index - interpreted via flags.
        @return the logical segment index - interpreted via flags
        """
        ...

    def getSegmentName(self) -> int:
        """
        Returns the segment or group name - index into sstSegName.
        @return the segment or group name - index into sstSegName
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
    def byteCount(self) -> int: ...

    @property
    def byteOffset(self) -> int: ...

    @property
    def className(self) -> int: ...

    @property
    def flags(self) -> int: ...

    @property
    def groupIndex(self) -> int: ...

    @property
    def logicalOverlayNumber(self) -> int: ...

    @property
    def logicalSegmentIndex(self) -> int: ...

    @property
    def segmentName(self) -> int: ...
