from typing import List
import generic.continues
import ghidra.app.util.bin
import ghidra.app.util.bin.format.mz
import ghidra.app.util.bin.format.pe
import ghidra.app.util.bin.format.pe.PortableExecutable
import ghidra.util
import java.io
import java.lang


class PortableExecutable(object):
    """
    A class to manage loading Portable Executables (PE).
    """

    DEBUG: bool
    NAME: unicode = u'PORTABLE_EXECUTABLE'




    class SectionLayout(java.lang.Enum):
        FILE: ghidra.app.util.bin.format.pe.PortableExecutable.SectionLayout = FILE
        MEMORY: ghidra.app.util.bin.format.pe.PortableExecutable.SectionLayout = MEMORY







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.app.util.bin.format.pe.PortableExecutable.SectionLayout: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.app.util.bin.format.pe.PortableExecutable.SectionLayout]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    @staticmethod
    def computeAlignment(value: int, alignment: int) -> int: ...

    @overload
    @staticmethod
    def createPortableExecutable(factory: generic.continues.GenericFactory, bp: ghidra.app.util.bin.ByteProvider, layout: ghidra.app.util.bin.format.pe.PortableExecutable.SectionLayout) -> ghidra.app.util.bin.format.pe.PortableExecutable:
        """
        Constructs a new Portable Executable using the specified byte provider and layout.
          <p>
         Same as calling <code>createFileAlignedPortableExecutable(factory, bp, layout, true, false)</code>
        @param factory generic factory instance
        @param bp the byte provider
        @param layout specifies the layout of the underlying provider and governs RVA resolution
        @throws IOException if an I/O error occurs.
        @see #createPortableExecutable(GenericFactory, ByteProvider, SectionLayout, boolean, boolean)
        """
        ...

    @overload
    @staticmethod
    def createPortableExecutable(factory: generic.continues.GenericFactory, bp: ghidra.app.util.bin.ByteProvider, layout: ghidra.app.util.bin.format.pe.PortableExecutable.SectionLayout, advancedProcess: bool, parseCliHeaders: bool) -> ghidra.app.util.bin.format.pe.PortableExecutable:
        """
        Constructs a new Portable Executable using the specified byte provider and layout.
        @param factory generic factory instance
        @param bp the byte provider
        @param layout specifies the layout of the underlying provider and governs RVA resolution
        @param advancedProcess if true, the data directories are also processed
        @param parseCliHeaders if true, CLI headers are parsed (if present)
        @throws IOException if an I/O error occurs.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDOSHeader(self) -> ghidra.app.util.bin.format.mz.DOSHeader:
        """
        Returns the DOS header from the PE image.
        @return the DOS header from the PE image
        """
        ...

    def getFileLength(self) -> long: ...

    def getNTHeader(self) -> ghidra.app.util.bin.format.pe.NTHeader:
        """
        Returns the NT header from the PE image.
        @return the NT header from the PE image
        """
        ...

    def getRichHeader(self) -> ghidra.app.util.bin.format.pe.RichHeader:
        """
        Returns the Rich header from the PE image.
        @return the Rich header from the PE image
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

    def writeHeader(self, raf: java.io.RandomAccessFile, dc: ghidra.util.DataConverter) -> None: ...

    @property
    def DOSHeader(self) -> ghidra.app.util.bin.format.mz.DOSHeader: ...

    @property
    def NTHeader(self) -> ghidra.app.util.bin.format.pe.NTHeader: ...

    @property
    def fileLength(self) -> long: ...

    @property
    def richHeader(self) -> ghidra.app.util.bin.format.pe.RichHeader: ...
