from typing import List
import ghidra.formats.gfilesystem
import ghidra.formats.gfilesystem.factory
import java.lang


class GFileSystemProbeBytesOnly(ghidra.formats.gfilesystem.factory.GFileSystemProbe, object):
    """
    A GFileSystemProbe interface for filesystems that can be detected using
     just a few bytes from the beginning of the containing file.

     Filesystem probes of this type are given precedence when possible since they
     tend to be simpler and quicker.
    """

    MAX_BYTESREQUIRED: int = 65536







    def equals(self, __a0: object) -> bool: ...

    def getBytesRequired(self) -> int:
        """
        The minimum number of bytes needed to be supplied to the
         {@link #probeStartBytes(FSRL, byte[])} method.
         <p>
        @return min number of bytes needed for probe
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def probeStartBytes(self, containerFSRL: ghidra.formats.gfilesystem.FSRL, startBytes: List[int]) -> bool:
        """
        Probes the supplied {@code startBytes} byte[] array to determine if this filesystem
         implementation can handle the file.
        @param containerFSRL the {@link FSRL} of the file containing the bytes being probed.
        @param startBytes a byte array, with a length of at least {@link #getBytesRequired()}
         containing bytes from the beginning (ie. offset 0) of the probed file.
        @return {@code true} if the specified file is handled by this filesystem implementation,
         {@code false} if not.
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
    def bytesRequired(self) -> int: ...
