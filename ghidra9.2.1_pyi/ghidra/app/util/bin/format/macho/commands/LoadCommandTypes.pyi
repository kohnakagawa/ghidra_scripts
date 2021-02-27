import ghidra.app.util.bin.format
import ghidra.app.util.bin.format.macho
import ghidra.app.util.bin.format.macho.commands
import java.lang


class LoadCommandTypes(object):
    """
    Constants for the cmd field of all load commands, the type
    """

    LC_BUILD_VERSION: int = 50
    LC_CODE_SIGNATURE: int = 29
    LC_DATA_IN_CODE: int = 41
    LC_DYLD_ENVIRONMENT: int = 39
    LC_DYLD_INFO: int = 34
    LC_DYLD_INFO_ONLY: int = -2147483614
    LC_DYLIB_CODE_SIGN_DRS: int = 43
    LC_DYSYMTAB: int = 11
    LC_ENCRYPTION_INFO: int = 33
    LC_ENCRYPTION_INFO_64: int = 44
    LC_FUNCTION_STARTS: int = 38
    LC_FVMFILE: int = 9
    LC_IDENT: int = 8
    LC_IDFVMLIB: int = 7
    LC_ID_DYLIB: int = 13
    LC_ID_DYLINKER: int = 15
    LC_LAZY_LOAD_DYLIB: int = 32
    LC_LINKER_OPTIONS: int = 45
    LC_LOADFVMLIB: int = 6
    LC_LOAD_DYLIB: int = 12
    LC_LOAD_DYLINKER: int = 14
    LC_LOAD_UPWARD_DYLIB: int = -2147483613
    LC_LOAD_WEAK_DYLIB: int = -2147483624
    LC_MAIN: int = -2147483608
    LC_NOTE: int = 49
    LC_OPTIMIZATION_HINT: int = 46
    LC_PREBIND_CKSUM: int = 23
    LC_PREBOUND_DYLIB: int = 16
    LC_PREPAGE: int = 10
    LC_REEXPORT_DYLIB: int = -2147483617
    LC_REQ_DYLD: int = -2147483648
    LC_ROUTINES: int = 17
    LC_ROUTINES_64: int = 26
    LC_RPATH: int = -2147483620
    LC_SEGMENT: int = 1
    LC_SEGMENT_64: int = 25
    LC_SEGMENT_SPLIT_INFO: int = 30
    LC_SOURCE_VERSION: int = 42
    LC_SUB_CLIENT: int = 20
    LC_SUB_FRAMEWORK: int = 18
    LC_SUB_LIBRARY: int = 21
    LC_SUB_UMBRELLA: int = 19
    LC_SYMSEG: int = 3
    LC_SYMTAB: int = 2
    LC_THREAD: int = 4
    LC_TWOLEVEL_HINTS: int = 22
    LC_UNIXTHREAD: int = 5
    LC_UUID: int = 27
    LC_VERSION_MIN_IPHONEOS: int = 37
    LC_VERSION_MIN_MACOSX: int = 36
    LC_VERSION_MIN_TVOS: int = 47
    LC_VERSION_MIN_WATCHOS: int = 48



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getLoadCommand(reader: ghidra.app.util.bin.format.FactoryBundledWithBinaryReader, header: ghidra.app.util.bin.format.macho.MachHeader) -> ghidra.app.util.bin.format.macho.commands.LoadCommand: ...

    @staticmethod
    def getLoadCommentTypeName(type: int) -> unicode:
        """
        Returns a string for the given load command type.
        @param type the load command type
        @return a string for the given load command type
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
