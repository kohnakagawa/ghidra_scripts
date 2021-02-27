import ghidra.app.util.bin.format
import ghidra.app.util.bin.format.mz
import ghidra.app.util.bin.format.ne
import java.lang


class NewExecutable(object):
    """
    A class to manage loading New Executables (NE).
    """





    def __init__(self, factory: generic.continues.GenericFactory, bp: ghidra.app.util.bin.ByteProvider, baseAddr: ghidra.program.model.address.SegmentedAddress):
        """
        Constructs a new instance of an new executable.
        @param factory is the object factory to bundle with the reader
        @param bp the byte provider
        @param baseAddr the image base of the executable
        @throws IOException if an I/O error occurs.
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
        Returns the DOS header from the new executable.
        @return the DOS header from the new executable
        """
        ...

    def getWindowsHeader(self) -> ghidra.app.util.bin.format.ne.WindowsHeader:
        """
        Returns the Windows header from the new executable.
        @return the Windows header from the new executable
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

    @property
    def windowsHeader(self) -> ghidra.app.util.bin.format.ne.WindowsHeader: ...
