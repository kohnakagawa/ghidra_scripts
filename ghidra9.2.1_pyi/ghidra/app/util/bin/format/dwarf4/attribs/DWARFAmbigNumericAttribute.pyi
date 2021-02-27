import ghidra.app.util.bin.format.dwarf4.attribs
import java.lang


class DWARFAmbigNumericAttribute(ghidra.app.util.bin.format.dwarf4.attribs.DWARFNumericAttribute):
    """
    Stores a integer value (with ambiguous signedness) in a long, with a mask that will
     allow the consumer at a later time to treat the value as signed or unsigned.

     When supplied with a long value that was originally a smaller integer with its high-bit
     set, java will sign-extend the value to 64 bits.  To treat this as an unsigned
     value, the mask needs to match the bitwidth of the supplied value, and is used to return
     the relevant number of bits from the value. (See NumberUtil.UNSIGNED_BYTE_MASK, etc)

     This allows us to simplify the storage of a variable sized int value
     (1 byte, 2 byte, 4 byte, 8 byte) using just a 8 byte long and an 8 byte mask.
    """





    def __init__(self, value: long, mask: long): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getUnsignedValue(self) -> long: ...

    def getValue(self) -> long: ...

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
    def unsignedValue(self) -> long: ...
