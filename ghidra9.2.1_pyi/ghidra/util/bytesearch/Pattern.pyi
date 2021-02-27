from typing import List
import generic.jar
import ghidra.util.bytesearch
import ghidra.xml
import java.io
import java.lang
import java.util


class Pattern(ghidra.util.bytesearch.DittedBitSequence):
    """
    Pattern is an association of a DittedBitSequence to match,
     a set of post rules after a match is found that must be satisfied,
     and a set of actions to be taken if the pattern matches.

     These patterns can be restored from an XML file.
    """





    @overload
    def __init__(self):
        """
        Construct an empty pattern.  Use XML to initialize
        """
        ...

    @overload
    def __init__(self, seq: ghidra.util.bytesearch.DittedBitSequence, offset: int, postArray: List[ghidra.util.bytesearch.PostRule], matchArray: List[ghidra.util.bytesearch.MatchAction]):
        """
        Construct the pattern based on a DittedByteSequence a match offset, post matching rules,
         and a set of actions to take when the match occurs.
        @param seq DittedByteSequence
        @param offset offset from the actual match location to report a match
        @param postArray post set of rules to check for the match
        @param matchArray MatchActions to apply when a match occurs
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

    @property
    def markOffset(self) -> int: ...

    @property
    def matchActions(self) -> List[ghidra.util.bytesearch.MatchAction]: ...

    @matchActions.setter
    def matchActions(self, value: List[ghidra.util.bytesearch.MatchAction]) -> None: ...

    @property
    def postRules(self) -> List[ghidra.util.bytesearch.PostRule]: ...
