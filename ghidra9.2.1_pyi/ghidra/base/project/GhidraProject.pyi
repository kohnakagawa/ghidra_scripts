import ghidra.base.project
import ghidra.framework.client
import ghidra.framework.cmd
import ghidra.framework.model
import ghidra.framework.options
import ghidra.framework.project
import ghidra.program.model.lang
import ghidra.program.model.listing
import java.io
import java.lang


class GhidraProject(object):
    """
    Helper class for using Ghidra in a "batch" mode. This class provides methods
     for importing, opening, saving, and analyzing program.

     Note: Before using this class you must initialize the Ghidra system.  See
     Application#initializeApplication for more information.
    """









    @overload
    @staticmethod
    def analyze(program: ghidra.program.model.listing.Program) -> None:
        """
        Invokes the auto-analyzer on the program. Depending on which analyzers
         are in the classpath, generally will disassemble at entry points, and
         create and analyze functions that are called.
        @param program the program to analyze.
        """
        ...

    @overload
    def analyze(self, program: ghidra.program.model.listing.Program, debug: bool) -> None:
        """
        Debug version of the auto_analyzer. Same as regular analyzer except that
         any stack traces are not trapped.
        @param program the program to be analyzed
        @param debug true to allow stack traces to propagate out.
        """
        ...

    def checkPoint(self, program: ghidra.program.model.listing.Program) -> None:
        """
        Creates a checkpoint in the program. Any changes since the last
         checkpoint can be instantly undone by calling the rollback command.
        @param program the program to be checkpointed.
        """
        ...

    @overload
    def close(self) -> None:
        """
        Closes the ghidra project, closing (without saving!) any open programs in
         that project. Also deletes the project if created as a temporary project.
        """
        ...

    @overload
    def close(self, program: ghidra.program.model.listing.Program) -> None:
        """
        Closes the given program. Any changes in the program will be lost.
        @param program the program to close.
        """
        ...

    @staticmethod
    def createProject(projectDirPath: unicode, projectName: unicode, temporary: bool) -> ghidra.base.project.GhidraProject:
        """
        Creates a new non-shared Ghidra project to be used for storing programs.

         <P><B>Note:  Calling this method will delete any existing project files on disk that
         match the given project name.
         </B>
        @param projectDirPath the directory path to contain the new Ghidra project.
        @param projectName the name of the project to be created.
        @param temporary if true, deletes the the project when it is closed - useful for testing.
        @return an open ghidra project.
        @throws IOException if there was a problem accessing the project
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def execute(self, cmd: ghidra.framework.cmd.Command, program: ghidra.program.model.listing.Program) -> None:
        """
        Executes the give command on the program.
        @param cmd the command to be applied to the program.
        @param program the program on which the command is to be applied.
        """
        ...

    def getAnalysisOptions(self, program: ghidra.program.model.listing.Program) -> ghidra.framework.options.Options:
        """
        Returns a PropertList containing all the analysis option properties that
         can be set. Changing the value of the analysis properties will affect
         what happens when the analyze call is made.
        @param program the program whose analysis options are to be set.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getProject(self) -> ghidra.framework.model.Project:
        """
        Returns the underlying Project instance or null if project was opened for
         READ access only.
        """
        ...

    def getProjectManager(self) -> ghidra.framework.project.DefaultProjectManager:
        """
        Returns the project manager
        @return the project manager
        """
        ...

    def getRootFolder(self) -> ghidra.framework.model.DomainFolder:
        """
        Get the root folder for the Ghidra project.
        """
        ...

    @staticmethod
    def getServerRepository(host: unicode, port: int, repositoryName: unicode, createIfNeeded: bool) -> ghidra.framework.client.RepositoryAdapter:
        """
        Get/Create shared repository.
        @param host Ghidra Server host
        @param port Ghidra Server port (0 = use default port)
        @param repositoryName
        @param createIfNeeded if true repository will be created if it does not exist
        @throws DuplicateNameException
        """
        ...

    def hashCode(self) -> int: ...

    @overload
    def importProgram(self, file: java.io.File) -> ghidra.program.model.listing.Program: ...

    @overload
    def importProgram(self, file: java.io.File, domainFolder: ghidra.framework.model.DomainFolder) -> ghidra.program.model.listing.Program: ...

    @overload
    def importProgram(self, file: java.io.File, processor: ghidra.program.model.lang.Processor) -> ghidra.program.model.listing.Program: ...

    @overload
    def importProgram(self, file: java.io.File, loaderClass: java.lang.Class) -> ghidra.program.model.listing.Program: ...

    @overload
    def importProgram(self, file: java.io.File, language: ghidra.program.model.lang.Language, compilerSpec: ghidra.program.model.lang.CompilerSpec) -> ghidra.program.model.listing.Program: ...

    @overload
    def importProgram(self, file: java.io.File, domainFolder: ghidra.framework.model.DomainFolder, language: ghidra.program.model.lang.Language, compilerSpec: ghidra.program.model.lang.CompilerSpec) -> ghidra.program.model.listing.Program: ...

    @overload
    def importProgram(self, file: java.io.File, loaderClass: java.lang.Class, language: ghidra.program.model.lang.Language, compilerSpec: ghidra.program.model.lang.CompilerSpec) -> ghidra.program.model.listing.Program: ...

    def importProgramFast(self, file: java.io.File) -> ghidra.program.model.listing.Program: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def openProgram(self, folderPath: unicode, programName: unicode, readOnly: bool) -> ghidra.program.model.listing.Program:
        """
        Opens a program.
        @param folderPath the path of the program within the project. ("\" is root)
        @param programName the name of the program to open.
        @param readOnly flag if the program will only be read and not written.
        @return an open program.
        @throws IOException if there was a problem accessing the program
        """
        ...

    @overload
    @staticmethod
    def openProject(projectsDir: unicode, projectName: unicode) -> ghidra.base.project.GhidraProject:
        """
        Returns an instance of an open Ghidra Project that can be used to
         open/save programs.
        @param projectsDir the directory containing the Ghidra project.
        @param projectName the name of the ghidra project.
        @return an open ghidra project.
        @throws IOException if there was a problem accessing the project
        """
        ...

    @overload
    @staticmethod
    def openProject(projectsDir: unicode, projectName: unicode, restoreProject: bool) -> ghidra.base.project.GhidraProject:
        """
        Returns an instance of an open Ghidra Project that can be used to
         open/save programs.
        @param projectsDir the directory containing the Ghidra project.
        @param projectName the name of the ghidra project.
        @param restoreProject if true the project tool state is restored
        @return an open ghidra project.
        @throws IOException if there was a problem accessing the project
        """
        ...

    def rollback(self, program: ghidra.program.model.listing.Program) -> None:
        """
        Rolls back any changes to the program since the last checkpoint.
        @param program the program to be rolled back.
        """
        ...

    def save(self, program: ghidra.program.model.listing.Program) -> None:
        """
        Saves any changes in the program back to its file. If the program does
         not have an associated file (it was created), then it is an error to call
         this method, use saveAs instead.
         Any open transaction will be terminated.
        @param program the program to be saved.
        @throws IOException if there was a problem accessing the program
        """
        ...

    def saveAs(self, program: ghidra.program.model.listing.Program, folderPath: unicode, name: unicode, overWrite: bool) -> None:
        """
        Saves the given program to the project with the given name.
        @param program the program to be saved
        @param folderPath the path where to save the program.
        @param name the name to save the program as.
        @param overWrite if true, any existing program with that name will be
                    over-written.
        @throws DuplicateFileException if a file exists with that name and overwrite is false or overwrite failed
        @throws InvalidNameException the name is null or has invalid characters.
        @throws IOException if there was a problem accessing the program
        """
        ...

    def saveAsPackedFile(self, program: ghidra.program.model.listing.Program, file: java.io.File, overWrite: bool) -> None:
        """
        Saves the given program to as a packed file.
        @param program the program to be saved
        @param file the packed file destination.
        @param overWrite if true, any existing program with that name will be
                    over-written.
        @throws InvalidNameException the name is null or has invalid characters.
        @throws IOException if there was a problem accessing the program
        """
        ...

    def setDeleteOnClose(self, toDelete: bool) -> None:
        """
        Updates the flag passed to this project at construction time.
        @param toDelete true to delete on close; false in the opposite condition
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def deleteOnClose(self) -> None: ...  # No getter available.

    @deleteOnClose.setter
    def deleteOnClose(self, value: bool) -> None: ...

    @property
    def project(self) -> ghidra.framework.model.Project: ...

    @property
    def projectManager(self) -> ghidra.framework.project.DefaultProjectManager: ...

    @property
    def rootFolder(self) -> ghidra.framework.model.DomainFolder: ...
