from typing import List
import ghidra.util.bytesearch
import java.lang


class Match(object):
    """
    Represents a match of a DittedBitSequence at a given offset in a byte sequence.

     There is a hidden assumption that the sequence is actually a Pattern
     that might have a ditted-bit-sequence, a set of match actions,
     and post match rules/checks
    """





    def __init__(self, sequence: ghidra.util.bytesearch.DittedBitSequence, offset: long):
        """
        Construct a Match of a DittedBitSequence at an offset within a byte stream.
         Object normally used when a match occurs during a MemoryBytePatternSearch.
        @param sequence that matched
        @param offset from the start of byte stream where the matched occured
        """
        ...



    def checkPostRules(self, streamoffset: long) -> bool:
        """
        Check that the possible post rules are satisfied
        @param streamoffset offset within from match location to check postrules.
        @return true if post rules are satisfied
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getHexString(self) -> unicode:
        """
        @return ditted bit sequence as a string
        """
        ...

    def getMarkOffset(self) -> long:
        """
        @return the offset of the match within a longer byte sequence
        """
        ...

    def getMatchActions(self) -> List[ghidra.util.bytesearch.MatchAction]:
        """
        @return actions associated with this match
        """
        ...

    def getMatchStart(self) -> long:
        """
        @return offset of match in sequence of bytes
        """
        ...

    def getNumPostBits(self) -> int:
        """
        If the sequence corresponds to a PatternPair, return the number of postbits
        @return the number of post bits
        """
        ...

    def getSequence(self) -> ghidra.util.bytesearch.DittedBitSequence:
        """
        @return the sequence that was matched
        """
        ...

    def getSequenceIndex(self) -> int:
        """
        @return index of sequence in a possibly longer set of sequences
        """
        ...

    def getSequenceSize(self) -> int:
        """
        @return size in bytes of sequence
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
    def hexString(self) -> unicode: ...

    @property
    def markOffset(self) -> long: ...

    @property
    def matchActions(self) -> List[ghidra.util.bytesearch.MatchAction]: ...

    @property
    def matchStart(self) -> long: ...

    @property
    def numPostBits(self) -> int: ...

    @property
    def sequence(self) -> ghidra.util.bytesearch.DittedBitSequence: ...

    @property
    def sequenceIndex(self) -> int: ...

    @property
    def sequenceSize(self) -> int: ...
