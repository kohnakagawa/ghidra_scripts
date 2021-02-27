import ghidra.formats.gfilesystem
import ghidra.util.task
import java.lang
import javax.swing


class GIconProvider(object):
    """
    GFileSystem add-on interface to allow filesystems to override how image files
     are converted into viewable Icon instances.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getIcon(self, file: ghidra.formats.gfilesystem.GFile, monitor: ghidra.util.task.TaskMonitor) -> javax.swing.Icon:
        """
        A method that {@link GFileSystem file systems} can implement if they need to preprocess
         image files so that Ghidra can display them.
        @param file {@link GFile} to read and convert into an Icon.
        @param monitor {@link TaskMonitor} to watch and update with progress.
        @return new {@link Icon} instance with contents of the GFile.
        @throws IOException if problem reading or converting image.
        @throws CancelledException if user cancels.
        """
        ...

    @staticmethod
    def getIconForFile(file: ghidra.formats.gfilesystem.GFile, monitor: ghidra.util.task.TaskMonitor) -> javax.swing.Icon:
        """
        Helper static method that will get an Icon from a data file.
        @param file {@link GFile} to read and convert into an Icon.
        @param monitor {@link TaskMonitor} to watch and update with progress.
        @return new {@link Icon} instance with contents of the GFile, or null if the
         file couldn't be converted into an image.
        @throws CancelledException if the user cancels.
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
