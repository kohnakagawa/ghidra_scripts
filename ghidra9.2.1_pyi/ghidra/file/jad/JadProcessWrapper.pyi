from typing import List
import java.io
import java.lang


class JadProcessWrapper(object):
    outputDirectory: java.io.File
    outputFileExtension: unicode
    radix: ghidra.file.jad.Radix
    shouldDecompileDeadCode: bool
    shouldInsertNewLineBeforeOpeningBrace: bool
    shouldOutputFieldsBeforeMethods: bool
    shouldOutputSpaceBetweenKeywords: bool
    shouldOverwriteOutputFiles: bool
    shouldRestoreDirectoryStructure: bool
    shouldUseTabsForIndentation: bool
    verbose: bool



    def __init__(self, __a0: java.io.File): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getCommands(self) -> List[unicode]: ...

    def getInputDirectory(self) -> java.io.File: ...

    def getWorkingDirectory(self) -> java.io.File: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isJadPresent() -> bool: ...

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
    def commands(self) -> List[unicode]: ...

    @property
    def inputDirectory(self) -> java.io.File: ...

    @property
    def workingDirectory(self) -> java.io.File: ...
