import java.lang


class DWARFLine(object):





    class DWARFFile(object):




        @overload
        def __init__(self, __a0: ghidra.app.util.bin.BinaryReader): ...

        @overload
        def __init__(self, __a0: unicode, __a1: long, __a2: long, __a3: long): ...



        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDirectoryIndex(self) -> long: ...

        def getModificationTime(self) -> long: ...

        def getName(self) -> unicode: ...

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
        def directoryIndex(self) -> long: ...

        @property
        def modificationTime(self) -> long: ...

        @property
        def name(self) -> unicode: ...

    def __init__(self, reader: ghidra.app.util.bin.BinaryReader): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFile(self, index: int, compileDirectory: unicode) -> unicode:
        """
        Get a file name given a file index.
        @param index index of the file
        @param compileDirectory current compile unit directory
        @return file name
        """
        ...

    def getFullFile(self, index: int, compileDirectory: unicode) -> unicode:
        """
        Get a file name with the full path included.
        @param index index of the file
        @param compileDirectory current compile unit directory
        @return file name with full path
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
