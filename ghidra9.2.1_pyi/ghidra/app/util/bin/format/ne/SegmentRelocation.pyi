from typing import List
import java.lang


class SegmentRelocation(object):
    """
    A class to represent a new-executable segment relocation.
    """

    FLAG_ADDITIVE: int = 4
    FLAG_IMPORT_NAME: int = 2
    FLAG_IMPORT_ORDINAL: int = 1
    FLAG_INTERNAL_REF: int = 0
    FLAG_OS_FIXUP: int = 3
    FLAG_TARGET_MASK: int = 3
    MOVEABLE: int = 255
    TYPE_FAR_ADDR: int = 3
    TYPE_FAR_ADDR_48: int = 12
    TYPE_LENGTHS: List[int] = array('i', [1, 0, 2, 4, 0, 2, 0, 0, 0, 0, 0, 0, 6, 4])
    TYPE_LO_BYTE: int = 0
    TYPE_MASK: int = 15
    TYPE_OFFSET: int = 5
    TYPE_OFFSET_32: int = 13
    TYPE_SEGMENT: int = 2
    TYPE_STRINGS: List[unicode] = array(java.lang.String, [u'Low Byte', u'???1', u'16-bit Segment Selector', u'32-bit Pointer', u'???4', u'16-bit Pointer', u'???6', u'???7', u'???8', u'???9', u'???10', u'48-bit Pointer', u'???12', u'32-bit Offset'])
    VALUES_SIZE: int = 5







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFlagByte(self) -> int:
        """
        Returns the relocation flags.
        @return the relocation flags
        """
        ...

    def getOffset(self) -> int:
        """
        Returns the relocation offset.
        @return the relocation offset
        """
        ...

    def getTargetOffset(self) -> int:
        """
        Returns the relocation target offset.
        @return the relocation target offset
        """
        ...

    def getTargetSegment(self) -> int:
        """
        Returns the relocation target segment.
        @return the relocation target segment
        """
        ...

    def getType(self) -> int:
        """
        Returns the relocation type.
        @return the relocation type
        """
        ...

    def getValues(self) -> List[long]:
        """
        Returns values required to reconstruct this object.
        @return values required to reconstruct this object
        """
        ...

    def hashCode(self) -> int: ...

    def isAdditive(self) -> bool:
        """
        Returns true if this relocation is additive.
         If this bit is set, then add relocation to existing value.
         Otherwise overwrite the existing value.
        @return true if this relocation is additive.
        """
        ...

    def isImportName(self) -> bool:
        """
        Returns true if this relocation is an import by name.
        @return true if this relocation is an import by name
        """
        ...

    def isImportOrdinal(self) -> bool:
        """
        Returns true if this relocation is an import by ordinal.
        @return true if this relocation is an import by ordinal
        """
        ...

    def isInternalRef(self) -> bool:
        """
        Returns true if this relocation is an internal reference.
        @return true if this relocation is an internal reference
        """
        ...

    def isOpSysFixup(self) -> bool:
        """
        Returns true if this relocation is an operating system fixup.
        @return true if this relocation is an operating system fixup
        """
        ...

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
    def additive(self) -> bool: ...

    @property
    def flagByte(self) -> int: ...

    @property
    def importName(self) -> bool: ...

    @property
    def importOrdinal(self) -> bool: ...

    @property
    def internalRef(self) -> bool: ...

    @property
    def offset(self) -> int: ...

    @property
    def opSysFixup(self) -> bool: ...

    @property
    def targetOffset(self) -> int: ...

    @property
    def targetSegment(self) -> int: ...

    @property
    def type(self) -> int: ...

    @property
    def values(self) -> List[long]: ...
