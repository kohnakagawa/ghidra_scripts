import ghidra.formats.gfilesystem
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class GFileSystemProgramProvider(object):
    """
    GFileSystem add-on interface that allows a filesystem publish the fact that
     it supports an import feature allowing the caller to import binaries directly into
     Ghidra without going through a Loader.
    """









    def canProvideProgram(self, file: ghidra.formats.gfilesystem.GFile) -> bool:
        """
        Returns true if this GFileSystem can convert the specified GFile instance into
         a Ghidra Program.
        @param file GFile file or directory instance.
        @return boolean true if calls to {@link #getProgram(GFile, LanguageService, TaskMonitor, Object)}
         will be able to convert the file into a program.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getProgram(self, file: ghidra.formats.gfilesystem.GFile, languageService: ghidra.program.model.lang.LanguageService, monitor: ghidra.util.task.TaskMonitor, consumer: object) -> ghidra.program.model.listing.Program:
        """
        NOTE: ONLY OVERRIDE THIS METHOD IF YOU CANNOT PROVIDE AN INPUT STREAM
         TO THE INTERNAL FILES OF THIS FILE SYSTEM!
         <br>
         BE SURE TO REGISTER THE GIVEN CONSUMER ON THE PROGRAM.
         <br>
         Returns a program for the given file.
         <br>
        @param file the file to convert into a program
        @param languageService the language service for locating languages and compiler specifications
        @param monitor a task monitor
        @param consumer the consumer for the program to be returned
        @return a program for the given file
        @throws Exception if errors occur
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
