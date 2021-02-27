import ghidra.app.plugin.core.eclipse
import ghidra.framework.options
import ghidra.util.task
import java.io
import java.lang


class EclipseIntegrationService(object):
    """
    Service that provides Eclipse-related functionality.
    """









    def connectToEclipse(self, port: int) -> ghidra.app.plugin.core.eclipse.EclipseConnection:
        """
        Attempts to connect to Eclipse on the given port.  This may result in Eclipse
         being launched.  If the launch and/or connection fails, an error message will
         be displayed.
        @param port The port to connect to.
        @return The (possibly failed) connection.  Check the status of the {@link EclipseConnection}
           for details on the connection.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getEclipseExecutableFile(self) -> java.io.File:
        """
        Gets the Eclipse executable file.
        @return The Eclipse executable file.
        @throws FileNotFoundException if the executable file does not exist.
        """
        ...

    def getEclipseIntegrationOptions(self) -> ghidra.framework.options.ToolOptions:
        """
        Gets the Eclipse Integration options.
        @return The Eclipse Integration options.
        """
        ...

    def getEclipseWorkspaceDir(self) -> java.io.File:
        """
        Gets the Eclipse workspace directory.  If it is defined, the directory may or may not exist.
         If it is undefined, Eclipse will be in control of selecting a workspace directory to use.
        @return The Eclipse workspace directory. The directory may or may not exist.  Could return
           null if the workspace directory is undefined.
        """
        ...

    def handleEclipseError(self, error: unicode, askAboutOptions: bool, t: java.lang.Throwable) -> None:
        """
        Displays the given Eclipse related error message in an error dialog.
        @param error The error message to display in a dialog.
        @param askAboutOptions True if we should ask the user if they want to be taken to the Eclipse
           options; otherwise, false.
        @param t An optional throwable to tie to the message.
        """
        ...

    def hashCode(self) -> int: ...

    def isEclipseFeatureInstalled(self, filter: java.io.FilenameFilter) -> bool:
        """
        Checks to see if a feature is installed in Eclipse.
        @param filter A filename filter that matches the feature file to check.
        @return True if the specified feature is installed.
        @throws FileNotFoundException if Eclipse is not installed.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def offerGhidraDevInstallation(self, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Offers to install GhidraDev into Eclipse's dropins directory.
        @param monitor The task monitor used to cancel the installation.
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
    def eclipseExecutableFile(self) -> java.io.File: ...

    @property
    def eclipseIntegrationOptions(self) -> ghidra.framework.options.ToolOptions: ...

    @property
    def eclipseWorkspaceDir(self) -> java.io.File: ...
