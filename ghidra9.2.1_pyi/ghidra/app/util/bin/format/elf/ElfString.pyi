import ghidra.app.util.bin.format
import ghidra.app.util.bin.format.elf
import java.lang


class ElfString(object):




    def __init__(self):
        """
        DO NOT USE THIS CONSTRUCTOR, USE create*(GenericFactory ...) FACTORY METHODS INSTEAD.
        """
        ...



    @staticmethod
    def createElfString(reader: ghidra.app.util.bin.format.FactoryBundledWithBinaryReader, stringOffset: int, header: ghidra.app.util.bin.format.elf.ElfHeader) -> ghidra.app.util.bin.format.elf.ElfString:
        """
        Read an ElfString at the readers current position.  ElfString only supports
         null-terminated ASCII strings.
        @param reader reader positioned at start of string
        @param stringOffset string offset from start of string table
        @param header Elf header object
        @return Elf string object
        @throws IOException
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getString(self) -> unicode:
        """
        @return string object
        """
        ...

    def getStringOffset(self) -> int:
        """
        @return string offset within string table
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
    def string(self) -> unicode: ...

    @property
    def stringOffset(self) -> int: ...
