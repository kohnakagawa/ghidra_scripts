import ghidra.app.util.bin.format
import ghidra.app.util.bin.format.mz
import java.lang


class OldStyleExecutable(object):
    """
    A class to manage loading Old-style (MZ) Executables.
    """





    def __init__(self, factory: generic.continues.GenericFactory, bp: ghidra.app.util.bin.ByteProvider):
        """
        Constructs a new instance of an old-style executable
        @param bp the byte provider
        @throws IOException if an I/O error occurs
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getBinaryReader(self) -> ghidra.app.util.bin.format.FactoryBundledWithBinaryReader:
        """
        Returns the underlying binary reader.
        @return the underlying binary reader
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDOSHeader(self) -> ghidra.app.util.bin.format.mz.DOSHeader:
        """
        Returns the DOS Header from this old-style executable.
        @return the DOS Header from this old-style executable
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
    def DOSHeader(self) -> ghidra.app.util.bin.format.mz.DOSHeader: ...

    @property
    def binaryReader(self) -> ghidra.app.util.bin.format.FactoryBundledWithBinaryReader: ...
