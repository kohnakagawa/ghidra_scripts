from typing import List
import generic.io
import ghidra.util.task
import java.io
import java.lang
import java.util.jar


class ProjectJarWriter(generic.io.JarWriter):
    """
    Class to write files in a project to a jar output stream.
    """





    @overload
    def __init__(self, jarOut: java.util.jar.JarOutputStream):
        """
        @param jarOut the the jar file output stream the zip entries are
         to be written to.
        """
        ...

    @overload
    def __init__(self, jarOut: java.util.jar.JarOutputStream, excludedExtensions: List[unicode]): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getJarOutputStream(self) -> java.util.jar.JarOutputStream:
        """
        Return the jar output stream being used by this JarWriter.
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def main(args: List[unicode]) -> None:
        """
        Simple test for the JarWriter
        @param args args[0] is the source directory, args[1] is the output filename
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def outputEntry(self, path: unicode, time: long, in_: java.io.InputStream, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        Outputs an individual entry to the jar.  The data input stream will be read until and EOF is read.
        @param path entry path within the jar file
        @param time entry time
        @param in data input stream
        @param monitor cancellable task monitor
        @return true if entry is output to the jar file successfully.
        """
        ...

    def outputFile(self, baseFile: java.io.File, jarPath: unicode, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        Outputs an individual file to the jar.
        @param baseFile the file to be output
        @param jarPath the base path to prepend to the file as it is written
         to the jar output stream.
        @param monitor cancellable task monitor
        @return true if file is output to the jar file successfully.
        """
        ...

    def outputRecursively(self, baseFile: java.io.File, jarPath: unicode, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        Recursively outputs a directory to the jar output stream
         If baseFile is a file then it is simply output to the jar.
        @param baseFile the file or directory to be output
        @param jarPath the base path to prepend to the files as they are written
         to the jar output stream.
        @return true if all files are recursively output to the jar file.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
