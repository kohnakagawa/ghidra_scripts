from typing import List
import java.io
import java.lang


class ByteProviderPaddedInputStream(java.io.InputStream):
    """
    Wraps a ByteProvider and presents it as an InputStream.

     This InputStream will be limited to a region of the underlying ByteProvider, and
     has an optional amount of padding at the end of the stream where the stream will appear
     to have bytes with a value of zero.
    """





    def __init__(self, provider: ghidra.app.util.bin.ByteProvider, startOffset: long, length: long, padCount: long):
        """
        Create a new {@link ByteProviderInputStream} instance, using the specified
         {@link ByteProvider} as the source of the bytes returned from this stream.
         <p>
         The source ByteProvider is not closed when this stream is closed.
         <p>
         The total number of bytes that can be read from this instance will be length + padCount.
         <p>
        @param provider the {@link ByteProvider} to wrap.
        @param startOffset the starting offset in the ByteProvider.
        @param length the number of bytes from the {@link ByteProvider} to allow to be read by this InputStream.
        @param padCount the number of fake zero bytes to add after the real {@code length} bytes.
        """
        ...



    def available(self) -> int: ...

    def close(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def mark(self, __a0: int) -> None: ...

    def markSupported(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def nullInputStream() -> java.io.InputStream: ...

    @overload
    def read(self) -> int: ...

    @overload
    def read(self, __a0: List[int]) -> int: ...

    @overload
    def read(self, __a0: List[int], __a1: int, __a2: int) -> int: ...

    def readAllBytes(self) -> List[int]: ...

    @overload
    def readNBytes(self, __a0: int) -> List[int]: ...

    @overload
    def readNBytes(self, __a0: List[int], __a1: int, __a2: int) -> int: ...

    def reset(self) -> None: ...

    def skip(self, __a0: long) -> long: ...

    def toString(self) -> unicode: ...

    def transferTo(self, __a0: java.io.OutputStream) -> long: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
