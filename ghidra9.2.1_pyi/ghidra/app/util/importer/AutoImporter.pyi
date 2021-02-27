from typing import List
import ghidra.app.util.bin
import ghidra.app.util.importer
import ghidra.framework.model
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.util.task
import java.io
import java.lang
import java.util.function


class AutoImporter(object):
    """
    Utility methods to do imports automatically (without requiring user interaction).
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @overload
    @staticmethod
    def importAsBinary(bytes: ghidra.app.util.bin.ByteProvider, programFolder: ghidra.framework.model.DomainFolder, language: ghidra.program.model.lang.Language, compilerSpec: ghidra.program.model.lang.CompilerSpec, consumer: object, messageLog: ghidra.app.util.importer.MessageLog, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.listing.Program: ...

    @overload
    @staticmethod
    def importAsBinary(file: java.io.File, programFolder: ghidra.framework.model.DomainFolder, language: ghidra.program.model.lang.Language, compilerSpec: ghidra.program.model.lang.CompilerSpec, consumer: object, messageLog: ghidra.app.util.importer.MessageLog, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.listing.Program: ...

    @staticmethod
    def importByLookingForLcs(file: java.io.File, programFolder: ghidra.framework.model.DomainFolder, language: ghidra.program.model.lang.Language, compilerSpec: ghidra.program.model.lang.CompilerSpec, consumer: object, messageLog: ghidra.app.util.importer.MessageLog, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.listing.Program: ...

    @overload
    @staticmethod
    def importByUsingBestGuess(provider: ghidra.app.util.bin.ByteProvider, programFolder: ghidra.framework.model.DomainFolder, consumer: object, messageLog: ghidra.app.util.importer.MessageLog, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.listing.Program: ...

    @overload
    @staticmethod
    def importByUsingBestGuess(file: java.io.File, programFolder: ghidra.framework.model.DomainFolder, consumer: object, messageLog: ghidra.app.util.importer.MessageLog, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.listing.Program: ...

    @staticmethod
    def importByUsingSpecificLoaderClass(__a0: java.io.File, __a1: ghidra.framework.model.DomainFolder, __a2: java.lang.Class, __a3: List[object], __a4: object, __a5: ghidra.app.util.importer.MessageLog, __a6: ghidra.util.task.TaskMonitor) -> ghidra.program.model.listing.Program: ...

    @staticmethod
    def importByUsingSpecificLoaderClassAndLcs(__a0: java.io.File, __a1: ghidra.framework.model.DomainFolder, __a2: java.lang.Class, __a3: List[object], __a4: ghidra.program.model.lang.Language, __a5: ghidra.program.model.lang.CompilerSpec, __a6: object, __a7: ghidra.app.util.importer.MessageLog, __a8: ghidra.util.task.TaskMonitor) -> ghidra.program.model.listing.Program: ...

    @overload
    @staticmethod
    def importFresh(provider: ghidra.app.util.bin.ByteProvider, programFolder: ghidra.framework.model.DomainFolder, consumer: object, messageLog: ghidra.app.util.importer.MessageLog, monitor: ghidra.util.task.TaskMonitor, loaderFilter: java.util.function.Predicate, loadSpecChooser: ghidra.app.util.importer.LoadSpecChooser, programNameOverride: unicode, optionChooser: ghidra.app.util.importer.OptionChooser, multipleProgramsStrategy: ghidra.app.util.importer.MultipleProgramsStrategy) -> List[ghidra.program.model.listing.Program]: ...

    @overload
    @staticmethod
    def importFresh(file: java.io.File, programFolder: ghidra.framework.model.DomainFolder, consumer: object, messageLog: ghidra.app.util.importer.MessageLog, monitor: ghidra.util.task.TaskMonitor, loaderFilter: java.util.function.Predicate, loadSpecChooser: ghidra.app.util.importer.LoadSpecChooser, programNameOverride: unicode, optionChooser: ghidra.app.util.importer.OptionChooser, multipleProgramsStrategy: ghidra.app.util.importer.MultipleProgramsStrategy) -> List[ghidra.program.model.listing.Program]: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
