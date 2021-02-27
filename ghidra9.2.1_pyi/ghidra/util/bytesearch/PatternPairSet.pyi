from typing import List
import ghidra.util.bytesearch
import ghidra.xml
import java.lang
import java.util


class PatternPairSet(object):
    """
    A set of "pre" DittedBitSequences and a set of "post" Patterns are paired to form a larger pattern.
     To match, a sequence from the "pre" sequence set must first match, then one of the "post" patterns
     is matched relative to the matching "pre" pattern.  This class is really a storage object for the
     patterns and provides a mechanism to read the pre/post patterns from an XML file.

     The larger pattern has the idea of bits of check, which means the number of bits that are fixed to
     a value when matching (not don't care).  There is a pre pattern bits of check and post pattern bits
     of check.  The bits of check are used to statistically gauge the accuracy of the pattern.

     An example of the XML format follows:


          0xe12fff1.
          0xe12fff1e 0x46c0
          0xe12fff1e 0xe1a00000



           0xe24dd...                              11101001 00101101 .1...... ....0000
           11101001 00101101 .1...... ....0000     0xe24dd...
           11101001 00101101 .1...... ....0000     0x........ 0xe24dd...






      Note: The post Patterns can also have a set of rules that must be satisfied along with one of the
      Pattern DittedBitSequence matches.
    """





    def __init__(self):
        """
        Construct an empty PatternPairSet.  Use XML to initialize the pattern sets.
        """
        ...



    def createFinalPatterns(self, __a0: java.util.ArrayList) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def extractPostPatterns(self, __a0: java.util.ArrayList) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def getPostBitsOfCheck(self) -> int:
        """
        Get the required number of fixed bits after the prepattern
        @return number of post bits
        """
        ...

    def getPostPatterns(self) -> List[ghidra.util.bytesearch.Pattern]:
        """
        Get the "post" parts of the patterns
        @return post patterns
        """
        ...

    def getPreSequences(self) -> List[ghidra.util.bytesearch.DittedBitSequence]:
        """
        Get the "pre" parts of the patterns
        @return pre sequences
        """
        ...

    def getTotalBitsOfCheck(self) -> int:
        """
        Get the required number of fixed bits in the whole pattern
        @return number of total fixed bits
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restoreXml(self, parser: ghidra.xml.XmlPullParser, pfactory: ghidra.util.bytesearch.PatternFactory) -> None:
        """
        Restore PatternPairSet from XML pull parser
        @param parser XML pull parser
        @param pfactory pattern factory user to construct patterns
        @throws IOException if pull parsing fails
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def postBitsOfCheck(self) -> int: ...

    @property
    def postPatterns(self) -> java.util.ArrayList: ...

    @property
    def preSequences(self) -> java.util.ArrayList: ...

    @property
    def totalBitsOfCheck(self) -> int: ...
