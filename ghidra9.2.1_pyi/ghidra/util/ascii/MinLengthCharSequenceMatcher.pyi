import ghidra.util.ascii
import java.lang


class MinLengthCharSequenceMatcher(object):
    """
    Instances of this class will find sequences of characters that are in the given char set and
     of a minimum length.  Characters a fed one at a time into this object. Adding a char may trigger
     the discovery of a sequence if the char is a 0 or not in the char set and we already have seen
     a sequence of included chars at least as long as the minimum length.
    """





    def __init__(self, minimumSequenceLength: int, charSet: ghidra.util.ascii.CharSetRecognizer, alignment: int): ...



    def addChar(self, c: int) -> bool:
        """
        Adds a character to this sequence matcher.
        @param c the character to add.
        @return a Sequence if the added char triggered an end of a valid sequence, otherwise null.
        """
        ...

    def endSequence(self) -> bool:
        """
        Indicates there are no more contiguous chars to add to this matcher.  If a minimum or more
         number of included chars have been seen before this call, then a sequence is returned.
        @return a Sequence if there was a sequence of chars &gt;= the min length just before this call.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getSequence(self) -> ghidra.util.ascii.Sequence: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def reset(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def sequence(self) -> ghidra.util.ascii.Sequence: ...
