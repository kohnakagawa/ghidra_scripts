import java.lang


class BitFieldPacking(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getZeroLengthBoundary(self) -> int:
        """
        A non-zero value indicates the fixed alignment size for bit-fields which follow
         a zero-length bitfield if greater than a bitfields base type normal alignment.
         Corresponds to EMPTY_FIELD_BOUNDARY in GCC.
         This value is only used when {@link #isTypeAlignmentEnabled()} returns false.
        @return fixed alignment size as number of bytes for a bit-field which follows
         a zero-length bit-field
        """
        ...

    def hashCode(self) -> int: ...

    def isTypeAlignmentEnabled(self) -> bool:
        """
        Control whether the alignment of bit-field types is respected when laying out structures.
         Corresponds to PCC_BITFIELD_TYPE_MATTERS in GCC.
        @return true when the alignment of the bit-field type should be used to impact the
         alignment of the containing structure, and ensure that individual bit-fields will not
         straddle an alignment boundary.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    def useMSConvention(self) -> bool:
        """
        Control if the alignment and packing of bit-fields follows MSVC conventions.
         When this is enabled it takes precedence over all other bitfield packing controls.
        @return true if MSVC packing conventions are used, else false (e.g., GNU conventions apply).
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def typeAlignmentEnabled(self) -> bool: ...

    @property
    def zeroLengthBoundary(self) -> int: ...
