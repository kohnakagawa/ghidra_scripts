import ghidra.framework.plugintool.dialog
import java.lang


class ExtensionDetails(object, java.lang.Comparable):
    """
    Representation of a Ghidra extension. This class encapsulates all information required to
     uniquely identify an extension and where (or if) it has been installed.

     Note that hashCode and equals have been implemented for this. Two extension
     descriptions are considered equal if they have the same #name attribute; all other
     fields are unimportant save for display purposes.
    """





    def __init__(self, name: unicode, description: unicode, author: unicode, createdOn: unicode, version: unicode):
        """
        Constructor.
        @param name unique name of the extension; cannot be null
        @param description brief explanation of what the extension does; can be null
        @param author creator of the extension; can be null
        @param createdOn creation date of the extension, can be null
        @param version the extension version
        """
        ...



    @overload
    def compareTo(self, other: ghidra.framework.plugintool.dialog.ExtensionDetails) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, obj: object) -> bool: ...

    def getArchivePath(self) -> unicode:
        """
        Returns the location where the extension archive is located. If there is no
         archive this will be null.
        @return the archive path, or null
        """
        ...

    def getAuthor(self) -> unicode: ...

    def getClass(self) -> java.lang.Class: ...

    def getCreatedOn(self) -> unicode: ...

    def getDescription(self) -> unicode: ...

    def getInstallPath(self) -> unicode:
        """
        Returns the location where this extension is installed. If the extension is
         not installed this will be null.
        @return the extension path, or null
        """
        ...

    def getName(self) -> unicode: ...

    def getVersion(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def isInstalled(self) -> bool:
        """
        An extension is known to be installed if it has a valid installation path AND that path
         contains a Module.manifest file.
         <p>
         Note: The module manifest file is a marker that indicates several things; one of which is
         the installation status of an extension. When a user marks an extension to be uninstalled (by
         checking the appropriate checkbox in the {@link ExtensionTableModel}), the only thing
         that is done is to remove this manifest file, which tells the {@link ExtensionTableProvider}
         to remove the entire extension directory on the next launch.
        @return true if the extension is installed.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setArchivePath(self, path: unicode) -> None: ...

    def setAuthor(self, author: unicode) -> None: ...

    def setCreatedOn(self, date: unicode) -> None: ...

    def setDescription(self, description: unicode) -> None: ...

    def setInstallPath(self, path: unicode) -> None: ...

    def setName(self, name: unicode) -> None: ...

    def setVersion(self, version: unicode) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def archivePath(self) -> unicode: ...

    @archivePath.setter
    def archivePath(self, value: unicode) -> None: ...

    @property
    def author(self) -> unicode: ...

    @author.setter
    def author(self, value: unicode) -> None: ...

    @property
    def createdOn(self) -> unicode: ...

    @createdOn.setter
    def createdOn(self, value: unicode) -> None: ...

    @property
    def description(self) -> unicode: ...

    @description.setter
    def description(self, value: unicode) -> None: ...

    @property
    def installPath(self) -> unicode: ...

    @installPath.setter
    def installPath(self, value: unicode) -> None: ...

    @property
    def installed(self) -> bool: ...

    @property
    def name(self) -> unicode: ...

    @name.setter
    def name(self, value: unicode) -> None: ...

    @property
    def version(self) -> unicode: ...

    @version.setter
    def version(self, value: unicode) -> None: ...
