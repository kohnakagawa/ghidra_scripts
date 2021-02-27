import ghidra.util.ascii
import java.lang


class ByteStreamCharMatcher(object):
    """
    ByteStreamCharMatcher are state machines used to look for char sequences within a stream of bytes.
     Bytes from the stream are added one a time and converted to character stream which are in
     turn fed into a char stream recognizer.  As each byte is added, an indication is returned if that byte caused
     a terminated sequence to be found.  A sequence is simply a pair of indexes indicated the start and
     end indexes into the byte stream where the char sequence started and ended respectively along with
     an indication that the sequence was null terminated.
    """









    def add(self, b: int) -> bool:
        """
        Adds the next contiguous byte to this matcher
        @param b the next contiguous byte in the search stream.
        @return true if the given byte triggered a sequence match.  Note that this byte may not be
         a part of the recognized sequence.
        """
        ...

    def endSequence(self) -> bool:
        """
        Tells the matcher that there are no more contiguous bytes.  If the current state of the
         matcher is such that there is a valid sequence that can be at the end of the stream, then
         a sequence will be created and true will be returned.
        @return true if there is a valid sequence at the end of the stream.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getSequence(self) -> ghidra.util.ascii.Sequence:
        """
        Returns the currently recognized sequence which only exists immediately after an add or
         end sequence is called with a return value of true.
        @return
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def reset(self) -> None:
        """
        Resets the internal state of this ByteMatcher so that it can be reused against another byte stream.
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
    def sequence(self) -> ghidra.util.ascii.Sequence: ...
