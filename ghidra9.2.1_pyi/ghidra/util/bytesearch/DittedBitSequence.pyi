from typing import List
import ghidra.util.bytesearch
import java.lang


class DittedBitSequence(object):
    """
    A pattern of bits/mask to match to a stream of bytes.  The bits/mask can be of any length.
     The sequence can be initialized by:

        a string
        an array of bytes (no mask)
        an array of bytes and for mask

      The dits represent bits(binary) or nibbles(hex) that are don't care, for example:
         0x..d.4de2 ....0000 .1...... 00101101 11101001
      where 0x starts a hex number and '.' is a don't care nibble (hex) or bit (binary)
    """

    popcount: List[int]



    @overload
    def __init__(self): ...

    @overload
    def __init__(self, dittedBitData: unicode):
        """
        Constructor from a ditted-bit-sequence string where white space is ignored (e.g., "10..11.0");
        @param dittedBitData ditted sequence specified as a string
        @throws IllegalArgumentException if invalid dittedBitData specified
        """
        ...

    @overload
    def __init__(self, bytes: List[int]):
        """
        Construct a sequence of bytes to search for. No bits are masked off.
        @param bytes byte values that must match
        """
        ...

    @overload
    def __init__(self, op2: ghidra.util.bytesearch.DittedBitSequence):
        """
        Copy contructor
        @param op2 is bit sequence being copied
        """
        ...

    @overload
    def __init__(self, dittedBitData: unicode, hex: bool):
        """
        Constructor from a ditted-bit string where white space is ignored.  If there are no dits,
         {@code hex} is true, and {@code hex} does not begin with {code 0x}, {@code 0x} will be
         prepended to the string before constructing the {@link DittedBitSequence}.
        @param dittedBitData string of bits and dits or hex numbers and dits (e.g., 0.1..0, 0xAB..)
        @param hex true to force hex on the sequence
        """
        ...

    @overload
    def __init__(self, bytes: List[int], mask: List[int]):
        """
        Construct a bit pattern to search for consisting of
         0 bits, 1 bits, and don't care bits
        @param bytes is an array of bytes indicating the 0 and 1 bits that are cared about
        @param mask is an array of bytes masking off the bits that should be cared about, a 0 indicates a "don't care"
        """
        ...

    @overload
    def __init__(self, s1: ghidra.util.bytesearch.DittedBitSequence, s2: ghidra.util.bytesearch.DittedBitSequence): ...



    def concatenate(self, toConat: ghidra.util.bytesearch.DittedBitSequence) -> ghidra.util.bytesearch.DittedBitSequence:
        """
        Concatenates a sequence to the end of another sequence and
         returns a new sequence.
        @param toConat sequence to concatenate to this sequence
        @return a new sequence that is the concat of this and toConcat
        """
        ...

    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getHexString(self) -> unicode:
        """
        get a ditted hex string representing this sequence
        @return ditted hex string
        """
        ...

    def getIndex(self) -> int:
        """
        Get the index or identifying id attached to this pattern
        @return index or unique id attached to this sequence
        """
        ...

    def getMaskBytes(self) -> List[int]:
        """
        @return mask bytes which correspond to value bytes
        """
        ...

    def getNumFixedBits(self) -> int:
        """
        Get number of bits that must be 0/1
        @return number of bits that are not don't care (ditted)
        """
        ...

    def getNumInitialFixedBits(self, marked: int) -> int:
        """
        Get the number of bits that are fixed, not ditted (don't care)
        @param marked number of bytes in the pattern to check
        @return number of initial fixed bits
        """
        ...

    def getNumUncertainBits(self) -> int:
        """
        Get number of bits that are ditted (don't care)
        @return number of ditted bits (don't care)
        """
        ...

    def getSize(self) -> int:
        """
        get the size of this sequence in bytes
        @return size in bytes
        """
        ...

    def getValueBytes(self) -> List[int]:
        """
        @return value bytes
        """
        ...

    def hashCode(self) -> int: ...

    def isMatch(self, pos: int, val: int) -> bool:
        """
        Check for a match of a value at a certain offset in the pattern.
         An outside matcher will keep track of the match position within this
         ditted bit sequence.  Then call this method to match.
        @param pos position in the pattern to match
        @param val a byte to be match at the given byte offset in the pattern
        @return true if the byte matches the sequence mask/value
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setIndex(self, index: int) -> None:
        """
        Set a an index in a larger sequence, or identifing id on this pattern
        @param index - index in match sequence, or unique id
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def writeBits(self, buf: java.lang.StringBuffer) -> None: ...

    @property
    def hexString(self) -> unicode: ...

    @property
    def index(self) -> int: ...

    @index.setter
    def index(self, value: int) -> None: ...

    @property
    def maskBytes(self) -> List[int]: ...

    @property
    def numFixedBits(self) -> int: ...

    @property
    def numUncertainBits(self) -> int: ...

    @property
    def size(self) -> int: ...

    @property
    def valueBytes(self) -> List[int]: ...
