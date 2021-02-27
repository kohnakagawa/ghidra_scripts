import ghidra.framework.model
import ghidra.program.database
import ghidra.program.model.listing
import ghidra.util.task
import java.io
import java.lang
import java.util


class TestProgramManager(object):
    """
    A class to handle locating, opening and caching (within a JVM) programs in the test
     environment.  (This code was formerly inside of TestEnv.)
    """





    def __init__(self): ...



    def add(self, p: ghidra.program.model.listing.Program) -> None: ...

    def addOpenProgram(self, program: ghidra.program.model.listing.Program) -> None: ...

    @overload
    def addProgramToProject(self, folder: ghidra.framework.model.DomainFolder, programName: unicode) -> ghidra.framework.model.DomainFile:
        """
        Copies the specified program zip file to the JUnit test project's folder. <b>This
         means that the program will appear in the FrontEndTool as part of the project.</b>  That is
         the only reason to use this method vice openProgram().
        @param folder the folder into which the domain file will be inserted
        @param programName the name of the program zip file without the ".gzf" extension.
        @return the file
        @throws FileNotFoundException if the file cannot be found
        """
        ...

    @overload
    def addProgramToProject(self, project: ghidra.framework.model.Project, programName: unicode) -> ghidra.framework.model.DomainFile:
        """
        Copies the specified program zip file to the JUnit test project's root folder. <b>This
         means that the program will appear in the FrontEndTool as part of the project.</b>  That is
         the only reason to use this method vice openProgram().
        @param project the project into which the file will be restored
        @param programName the name of the program zip file without the ".gzf" extension
        @return the file
        @throws FileNotFoundException if the file cannot be found
        """
        ...

    def disposeOpenPrograms(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getDbTestDir() -> java.io.File: ...

    def getOpenPrograms(self) -> java.util.Set: ...

    def getProgram(self, progName: unicode) -> ghidra.program.database.ProgramDB:
        """
        Open a read-only test program from the test data directory.
         This program must be released prior to disposing this test environment.
         NOTE: Some tests rely on this method returning null when file does
         not yet exist within the resource area (e.g., test binaries for P-Code Tests)
        @param progName name of program database within the test data directory.
        @return program or null if program file not found
        """
        ...

    def hashCode(self) -> int: ...

    def isProgramCached(self, name: unicode) -> bool:
        """
        Determine if the specified program already exists with the program cache
        @param name the program name
        @return true if the specified program already exists with the program cache
        """
        ...

    def markAllProgramsAsUnchanged(self) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def release(self, program: ghidra.program.model.listing.Program) -> None: ...

    def removeAllConsumersExcept(self, p: ghidra.program.model.listing.Program, consumer: object) -> None: ...

    def removeFromProgramCache(self, name: unicode) -> None:
        """
        Remove specified program from cache
        @param name the program name
        """
        ...

    def saveToCache(self, progName: unicode, program: ghidra.program.database.ProgramDB, replace: bool, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Save a program to the cached program store.  A SaveAs will be performed on the
         program to its cached storage location.
        @param progName program name
        @param program program object
        @param replace if true any existing cached database with the same name will be replaced
        @param monitor task monitor
        @throws IOException if the database cannot be created
        @throws DuplicateNameException if already cached
        @throws CancelledException if the save operation is cancelled
        """
        ...

    @staticmethod
    def setDbTestDir(newDbTestDir: java.io.File) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def openPrograms(self) -> java.util.Set: ...
