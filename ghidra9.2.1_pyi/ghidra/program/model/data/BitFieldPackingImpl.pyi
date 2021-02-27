import ghidra.program.model.data
import java.lang


class BitFieldPackingImpl(object, ghidra.program.model.data.BitFieldPacking):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getZeroLengthBoundary(self) -> int: ...

    def hashCode(self) -> int: ...

    def isTypeAlignmentEnabled(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setTypeAlignmentEnabled(self, typeAlignmentEnabled: bool) -> None:
        """
        Control whether the alignment of bit-field types is respected when laying out structures.
         Corresponds to PCC_BITFIELD_TYPE_MATTERS in gcc.
        @param typeAlignmentEnabled true if the alignment of the bit-field type should be used
         to impact the alignment of the containing structure, and ensure that individual bit-fields
         will not straddle an alignment boundary.
        """
        ...

    def setUseMSConvention(self, useMSConvention: bool) -> None:
        """
        Control if the alignment and packing of bit-fields follows MSVC conventions.
         When this is enabled it takes precedence over all other bitfield packing controls.
        @param useMSConvention true if MSVC packing conventions are used, else false (e.g., GNU conventions apply).
        """
        ...

    def setZeroLengthBoundary(self, zeroLengthBoundary: int) -> None:
        """
        Indicate a fixed alignment size in bytes which should be used for zero-length bit-fields.
        @param zeroLengthBoundary fixed alignment size as number of bytes for a bit-field
         which follows a zero-length bit-field.  A value of 0 causes zero-length type size to be used.
        """
        ...

    def toString(self) -> unicode: ...

    def useMSConvention(self) -> bool: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def typeAlignmentEnabled(self) -> bool: ...

    @typeAlignmentEnabled.setter
    def typeAlignmentEnabled(self, value: bool) -> None: ...

    @property
    def zeroLengthBoundary(self) -> int: ...

    @zeroLengthBoundary.setter
    def zeroLengthBoundary(self, value: int) -> None: ...
