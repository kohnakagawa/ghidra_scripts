from typing import List
import ghidra.util.classfinder
import java.lang


class Recognizer(ghidra.util.classfinder.ExtensionPoint, object):
    """
    NOTE:  ALL Recognizer CLASSES MUST END IN "Recognizer".  If not,
     the ClassSearcher will not find them.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getPriority(self) -> int:
        """
        Return the recognizer priority; for instance, a GZIP/TAR recognizer
         should have higher priority than just the GZIP recognizer (because the
         GZIP/TAR will unzip part of the payload and then test against the TAR
         recognizer...so every GZIP/TAR match will also match GZIP). Note that
         higher is more specific, which is opposite the convention used with the
         Loader hierarchy.
        @return the recognizer priority
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def numberOfBytesRequired(self) -> int:
        """
        How many bytes (maximum) does this recognizer need to recognize its
         format?
        @return the maximum number of bytes needed to send to this recognizer in
                 the recognize(...) method
        """
        ...

    def recognize(self, bytes: List[int]) -> unicode:
        """
        Ask the recognizer to recognize some bytes. Return a description String
         if recognized; otherwise, null. DO NOT MUNGE THE BYTES. Right now for
         efficiency's sake the array of bytes is just passed to each recognizer in
         turn. Abuse this and we will need to create copies, and everyone loses.
        @param bytes the bytes to recognize
        @return a String description of the recognition, or null if it is not
                 recognized
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
    def priority(self) -> int: ...
