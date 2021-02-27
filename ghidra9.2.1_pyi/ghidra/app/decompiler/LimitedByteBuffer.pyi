import java.io
import java.lang


class LimitedByteBuffer(object):
    """
    Class for accumulating bytes into an automatically expanding buffer with an explicit upper limit to the size
    """





    def __init__(self, initial: int, amax: int):
        """
        Create the buffer specifying its initial and limiting capacity
        @param initial is the number of bytes to be initially allocated for the buffer
        @param amax is the absolute maximum number of bytes the buffer is allowed to expand to before throwing exceptions
        """
        ...



    def append(self, b: int) -> None:
        """
        Append a byte into the buffer.  The buffer's internal storage is expanded as necessary, but only up to
         the specified maximum. If this append exceeds that maximum, then an exception is thrown
        @param b is the byte to append
        @throws IOException
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getInputStream(self) -> java.io.ByteArrayInputStream:
        """
        Generate an InputStream from the bytes that have been appended to the buffer
         The buffer is NOT copied
        @return the new InputStream
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
    def inputStream(self) -> java.io.ByteArrayInputStream: ...
