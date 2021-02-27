from typing import List
import ghidra.app.services
import ghidra.app.util.opinion
import ghidra.formats.gfilesystem
import ghidra.framework.model
import ghidra.framework.plugintool
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class ImporterUtilities(object):
    """
    Utilities for importing files.

     Note: if a method takes a TaskMonitor, then that method should only be called
     from a background task.
    """

    CONTAINER_FILES_FILTER: ghidra.util.filechooser.GhidraFileFilter = ghidra.util.filechooser.ExtensionFileFilter@6fb87a34
    LOADABLE_FILES_FILTER: ghidra.util.filechooser.GhidraFileFilter = ghidra.util.filechooser.ExtensionFileFilter@38b36d0a



    def __init__(self): ...



    @staticmethod
    def addContentToProgram(__a0: ghidra.framework.plugintool.PluginTool, __a1: ghidra.program.model.listing.Program, __a2: ghidra.formats.gfilesystem.FSRL, __a3: ghidra.app.util.opinion.LoadSpec, __a4: List[object], __a5: ghidra.util.task.TaskMonitor) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def importSingleFile(__a0: ghidra.framework.plugintool.PluginTool, __a1: ghidra.app.services.ProgramManager, __a2: ghidra.formats.gfilesystem.FSRL, __a3: ghidra.framework.model.DomainFolder, __a4: ghidra.app.util.opinion.LoadSpec, __a5: unicode, __a6: List[object], __a7: ghidra.util.task.TaskMonitor) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def setProgramProperties(program: ghidra.program.model.listing.Program, fsrl: ghidra.formats.gfilesystem.FSRL, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Ensure that a {@link Program}'s metadata includes its import origin.
        @param program imported {@link Program} to modify
        @param fsrl {@link FSRL} of the import source.
        @param monitor {@link TaskMonitor} to use when accessing filesystem stuff.
        @throws CancelledException if user cancels
        @throws IOException if IO error
        """
        ...

    @staticmethod
    def showAddToProgramDialog(fsrl: ghidra.formats.gfilesystem.FSRL, program: ghidra.program.model.listing.Program, tool: ghidra.framework.plugintool.PluginTool, monitor: ghidra.util.task.TaskMonitor) -> None: ...

    @overload
    @staticmethod
    def showImportDialog(tool: ghidra.framework.plugintool.PluginTool, programManager: ghidra.app.services.ProgramManager, fsrl: ghidra.formats.gfilesystem.FSRL, destinationFolder: ghidra.framework.model.DomainFolder, suggestedPath: unicode) -> None:
        """
        Displays the appropriate import dialog for the specified {@link FSRL file}.
         <p>
         If the file is a container of other files, a batch import dialog will be used,
         otherwise the normal single file import dialog will be shown.
        @param tool {@link PluginTool} will be used as the parent tool for dialogs
        @param programManager optional {@link ProgramManager} instance to use to open imported
         			binaries with, or null
        @param fsrl {@link FSRL} of the file to import
        @param destinationFolder {@link DomainFolder} destination folder where the imported file
         			will default to.  (the user will be able to choose a different location)
        @param suggestedPath optional string path that will automatically be pre-pended
         			to the destination filename
        """
        ...

    @overload
    @staticmethod
    def showImportDialog(tool: ghidra.framework.plugintool.PluginTool, programManager: ghidra.app.services.ProgramManager, fsrl: ghidra.formats.gfilesystem.FSRL, destinationFolder: ghidra.framework.model.DomainFolder, suggestedPath: unicode, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Displays the appropriate import dialog for the specified {@link FSRL file}.
         <p>
         If the file is a container of other files, a batch import dialog will be used,
         otherwise the normal single file import dialog will be shown.]
         <p>
         If you are not in a monitored task, then call
         {@link #showImportDialog(PluginTool, ProgramManager, FSRL, DomainFolder, String)}.
        @param tool {@link PluginTool} will be used as the parent tool for dialogs
        @param programManager optional {@link ProgramManager} instance to use to open imported
         			binaries with, or null
        @param fsrl {@link FSRL} of the file to import
        @param destinationFolder {@link DomainFolder} destination folder where the imported file
         			will default to.  (the user will be able to choose a different location)
        @param suggestedPath optional string path that will automatically be pre-pended
         			to the destination filename
        @param monitor the task monitor to use for monitoring; cannot be null
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
