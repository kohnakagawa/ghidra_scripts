from typing import List
import ghidra.app.services
import ghidra.formats.gfilesystem
import ghidra.framework.model
import ghidra.program.model.listing
import ghidra.util.task
import java.lang
import java.util


class ProgramMappingService(object):
    """
    Provides a best-effort[1] mapping / association between Ghidra Program/DomainFile objects and
     GFilesystem files (identified by their FSRL).

     As there is no current feature that allows you to quickly query the metadata of Programs/DomainFile
     objects in the current project, finding a Program by its MD5 or by a original source location
     string is not easily possible.

     Threadsafe.

     The current implementation searches current open Ghidra Programs and maintains a
     short-lived, in-memory only mapping of FSRL-DomainFile paths
     (manually updated by users of the ProgramMappingService when
     they do an import or other operation that creates a Ghidra DomainFile by calling
     #createAssociation(FSRL, DomainFile) and friends.)

     [1] - best-effort (adverb): meaning a dirty hack.
    """

    PROGRAM_METADATA_MD5: unicode = u'Executable MD5'
    PROGRAM_SOURCE_FSRL: unicode = u'FSRL'







    @staticmethod
    def clear() -> None:
        """
        Clears {@link ProgramMappingService} data.
         <p>
         This should be done whenever the project is opened/closed.
        """
        ...

    @overload
    @staticmethod
    def createAssociation(fsrl: ghidra.formats.gfilesystem.FSRL, domainFile: ghidra.framework.model.DomainFile) -> None:
        """
        Creates a short-lived association between a {@link FSRL} and a {@link DomainFile}.
        @param fsrl {@link FSRL} of where the DomainFile was imported from.
        @param domainFile {@link DomainFile} to associate with
        """
        ...

    @overload
    @staticmethod
    def createAssociation(fsrl: ghidra.formats.gfilesystem.FSRL, program: ghidra.program.model.listing.Program) -> None:
        """
        Creates a short-lived association between a {@link FSRL} and an open {@link Program}.
         <p>
        @param fsrl {@link FSRL} of where the {@link Program} was imported from.
        @param program {@link Program} to associate to.
        """
        ...

    @staticmethod
    def createAutoAssocation(program: ghidra.program.model.listing.Program) -> None:
        """
        Attempts to create an association between the specified open {@code program} and
         any {@link FSRL} metadata found in the {@link Program}s properties.
         <p>
         Used by event handlers that get notified about a {@link Program} being opened to
         opportunistically link that program to its source FSRL if the metadata is present.
         <p>
        @param program {@link Program} to rummage around in its metadata looking for FSRL info.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def findMatchingOpenProgram(fsrl: ghidra.formats.gfilesystem.FSRL, consumer: object) -> ghidra.program.model.listing.Program:
        """
        Returns a currently open Ghidra {@link Program} that has metadata that links it
         to the specified {@code file} parameter.
         <p>
         (ie. an open program has a MD5 or FSRL metadata value that matches the file)
         <p>
         See also {@link #isFileOpen(FSRL)}.
         <p>
        @param fsrl {@link FSRL} to use when inspecting each open Program's metadata.
        @param consumer Object that will be used to pin the matching Program open.  Caller
         must release the consumer when done.
        @return Already open {@link Program} that has matching metadata, or null if not found.
        """
        ...

    @overload
    @staticmethod
    def findMatchingProgramOpenIfNeeded(fsrl: ghidra.formats.gfilesystem.FSRL, consumer: object, programManager: ghidra.app.services.ProgramManager, openState: int) -> ghidra.program.model.listing.Program:
        """
        Returns an open {@link Program} instance that matches the specified
         {@link FSRL}, either from the set of currently open programs, or by
         requesting the specified {@link ProgramManager} to
         open a {@link DomainFile} that was found to match this GFile.
         <p>
        @param fsrl {@link FSRL} of program original location.
        @param consumer Object that will be used to pin the matching Program open.  Caller
         must release the consumer when done.
        @param programManager {@link ProgramManager} that will be used to open DomainFiles
         if necessary.
        @param openState one of {@link ProgramManager#OPEN_VISIBLE}, {@link ProgramManager#OPEN_HIDDEN}, {@link ProgramManager#OPEN_VISIBLE}
        @return {@link Program} which was imported from the specified FSRL, or null if not found.
        """
        ...

    @overload
    @staticmethod
    def findMatchingProgramOpenIfNeeded(fsrl: ghidra.formats.gfilesystem.FSRL, domainFile: ghidra.framework.model.DomainFile, consumer: object, programManager: ghidra.app.services.ProgramManager, openState: int) -> ghidra.program.model.listing.Program:
        """
        Returns an open {@link Program} instance that matches the specified
         {@link FSRL}, either from the set of currently open programs, or by
         requesting the specified {@link ProgramManager} to
         open a {@link DomainFile} that was found to match this GFile.
         <p>
        @param fsrl {@link FSRL} of program original location.
        @param domainFile optional {@link DomainFile} that corresponds to the FSRL param.
        @param consumer Object that will be used to pin the matching Program open.  Caller
         must release the consumer when done.
        @param programManager {@link ProgramManager} that will be used to open DomainFiles
         if necessary.
        @param openState one of {@link ProgramManager#OPEN_VISIBLE}, {@link ProgramManager#OPEN_HIDDEN}, {@link ProgramManager#OPEN_VISIBLE}
        @return {@link Program} which was imported from the specified FSRL, or null if not found.
        """
        ...

    @staticmethod
    def getCachedDomainFileFor(fsrl: ghidra.formats.gfilesystem.FSRL) -> ghidra.framework.model.DomainFile:
        """
        Returns a reference to a {@link DomainFile} in the current {@link Project} that matches
         the specified {@link FSRL}.
         <p>
         This method only consults an internal fsrl-to-DomainFile mapping that is short-lived
         and not persisted.
         <p>
        @param fsrl {@link FSRL} to search for
        @return {@link DomainFile} that was previously associated via {@link #createAssociation(FSRL, DomainFile)}
         and friends.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isFileImportedIntoProject(fsrl: ghidra.formats.gfilesystem.FSRL) -> bool:
        """
        Returns true if the specified {@link FSRL} has a matched Ghidra {@link DomainFile}
         in the current project.
         <p>
        @param fsrl {@link FSRL} to search for
        @return boolean true if file exists in project.
        """
        ...

    @staticmethod
    def isFileOpen(fsrl: ghidra.formats.gfilesystem.FSRL) -> bool:
        """
        Returns true if there is a current open Ghidra {@link Program} that has metadata
         that links it to the specified {@link FSRL}.
         <p>
         (ie. an open program has a MD5 or FSRL metadata value that matches the fsrl param.)
        @param fsrl {@link FSRL} to search for in open program info.
        @return boolean true if found.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def searchProjectForMatchingFiles(__a0: List[object], __a1: ghidra.util.task.TaskMonitor) -> java.util.Map: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
