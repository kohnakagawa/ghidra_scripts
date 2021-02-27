from typing import List
import generic.jar
import ghidra.util.bytesearch
import ghidra.xml
import java.io
import java.lang
import java.util


class GenericByteSequencePattern(ghidra.util.bytesearch.Pattern):
    """
    Templated simple DittedBitSequence Pattern for a byte/mask pattern and associated action.
     The DittedBitSequence is provided by value and mask in byte arrays.

     This class is normally used to find some number of SequencePatterns within a seqence of bytes.
     When the byte/mask pattern is matched, the GenericMatchAction will be "applied".
    """





    @overload
    def __init__(self, bytesSequence: List[int], action: ghidra.util.bytesearch.GenericMatchAction):
        """
        Construct a sequence of bytes with no mask, and associated action
         to be called if this pattern matches.
        @param bytesSequence sequence of bytes to match
        @param action action to apply if the match succeeds
        """
        ...

    @overload
    def __init__(self, bytesSequence: List[int], mask: List[int], action: ghidra.util.bytesearch.GenericMatchAction):
        """
        Construct a sequence of bytes with a mask, and associated action
         to be called if this pattern matches.
        @param bytesSequence sequence of bytes to match
        @param mask mask, bits that are 1 must match the byteSequence bits
        @param action to apply if the match succeeds
        """
        ...



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

    def getMarkOffset(self) -> int: ...

    def getMaskBytes(self) -> List[int]:
        """
        @return mask bytes which correspond to value bytes
        """
        ...

    def getMatchActions(self) -> List[ghidra.util.bytesearch.MatchAction]: ...

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

    def getPostRules(self) -> List[ghidra.util.bytesearch.PostRule]: ...

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

    @staticmethod
    def readPatterns(__a0: generic.jar.ResourceFile, __a1: java.util.ArrayList, __a2: ghidra.util.bytesearch.PatternFactory) -> None: ...

    @staticmethod
    def readPostPatterns(__a0: java.io.File, __a1: java.util.ArrayList, __a2: ghidra.util.bytesearch.PatternFactory) -> None: ...

    def restoreXml(self, parser: ghidra.xml.XmlPullParser, pfactory: ghidra.util.bytesearch.PatternFactory) -> None: ...

    @staticmethod
    def restoreXmlAttributes(__a0: java.util.ArrayList, __a1: java.util.ArrayList, __a2: ghidra.xml.XmlPullParser, __a3: ghidra.util.bytesearch.PatternFactory) -> None: ...

    def setIndex(self, index: int) -> None:
        """
        Set a an index in a larger sequence, or identifing id on this pattern
        @param index - index in match sequence, or unique id
        """
        ...

    def setMatchActions(self, actions: List[ghidra.util.bytesearch.MatchAction]) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def writeBits(self, buf: java.lang.StringBuffer) -> None: ...
