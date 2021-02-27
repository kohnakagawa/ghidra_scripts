from typing import List
import generic.jar
import ghidra.framework.plugintool
import ghidra.framework.plugintool.dialog
import java.io
import java.lang
import java.util


class ExtensionUtils(object):
    """
    Utility class for managing Ghidra Extensions.

     Extensions are defined as any archive or folder that contains an extension.properties
     file. This properties file can contain the following attributes:

     name (required)
     description
     author
     createdOn (format: mm/dd/yyyy)


      Extensions may be installed/uninstalled by users at runtime, using the ExtensionTableProvider.
      Installation consists of unzipping the extension archive to an installation folder, currently
      Ghidra/Extensions. To uninstall, the unpacked folder is simply removed.
    """

    PROPERTIES_FILE_NAME: unicode
    PROPERTIES_FILE_NAME_UNINSTALLED: unicode



    def __init__(self): ...



    @staticmethod
    def cleanupUninstalledExtensions() -> None:
        """
        Attempts to delete any extension directories that do not contain a Module.manifest
         file. This indicates that the extension was slated to be uninstalled by the user.
        @see #uninstall
        """
        ...

    @staticmethod
    def createExtensionDetailsFromProperties(props: java.util.Properties) -> ghidra.framework.plugintool.dialog.ExtensionDetails:
        """
        Extracts properties from a Java Properties file to create an {@link ExtensionDetails}
         object.
        @param props the java properties object
        @return a new extension details object
        """
        ...

    @overload
    @staticmethod
    def createExtensionDetailsFromPropertyFile(resourceFile: generic.jar.ResourceFile) -> ghidra.framework.plugintool.dialog.ExtensionDetails:
        """
        Extracts information from a Java Properties file to create an {@link ExtensionDetails}
         object.
        @param resourceFile the resource file file to parse
        @return a new extension details object
        """
        ...

    @overload
    @staticmethod
    def createExtensionDetailsFromPropertyFile(file: java.io.File) -> ghidra.framework.plugintool.dialog.ExtensionDetails:
        """
        Extracts information from a Java Properties file to create an {@link ExtensionDetails}
         object.
        @param file the file to parse
        @return a new extension details object
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def findExtensionPropertyFiles(sourceFile: generic.jar.ResourceFile, includeUninstalled: bool) -> List[generic.jar.ResourceFile]:
        """
        Returns a list of files representing all the <code>extension.properties</code> files found
         under a given directory. This will ONLY search the given directory and its immediate children.
         The conops are as follows:
         <ul>
         <li>If sourceFile is a directory and it contains an extension.properties file, then that file is returned</li>
         <li>If sourceFile does not contain an extension.properties file, then any immediate directories are searched (ignoring Skeleton directory)</li>
         </ul>
         <p>
         Note: This will NOT search zip files. If you have a zip, call {@link #getPropertiesFromArchive(File)}
         instead.
        @param sourceFile the directory to inspect
        @param includeUninstalled if true, include extensions that have been marked for removal
        @return list of extension.properties files
        """
        ...

    @staticmethod
    def findFilesWithName(__a0: java.io.File, __a1: unicode, __a2: List[object]) -> None: ...

    @staticmethod
    def getArchivedExtensions() -> java.util.Set:
        """
        Returns all archived extensions. These are all the extensions found in
         {@link ApplicationLayout#getExtensionArchiveDir}.
        @return set of archived extensions
        @throws ExtensionException if the extension details cannot be retrieved
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getExtensions() -> java.util.Set:
        """
        Returns a set of all extensions known to Ghidra, represented by
         {@link ExtensionDetails} objects. This will include all installed
         AND archived extensions.
         <p>
         Note that this method will only look in the known extension folder locations:
         <ul>
         <li>{@link ApplicationLayout#getExtensionArchiveDir}</li>
         <li>{@link ApplicationLayout#getExtensionInstallationDirs}</li>
         </ul>
         If users install extensions from other locations, the installed version of
         the extension will be known, but the source archive location will not be retained.
        @return list of unique extensions
        @throws ExtensionException if extensions cannot be retrieved
        """
        ...

    @staticmethod
    def getExtensionsInstalledSinceLastToolLaunch(tool: ghidra.framework.plugintool.PluginTool) -> java.util.Set:
        """
        Finds any extensions that have been installed since the last time a given tool was launched.
        @param tool the tool to check
        @return set of new extensions
        """
        ...

    @staticmethod
    def getInstalledExtensions(includeUninstalled: bool) -> java.util.Set:
        """
        Returns all installed extensions. These are all the extensions found in
         {@link ApplicationLayout#getExtensionInstallationDirs}.
        @param includeUninstalled if true, include extensions that have been marked for removal
        @return set of installed extensions
        @throws ExtensionException if the extension details cannot be retrieved
        """
        ...

    @staticmethod
    def getPropertiesFromArchive(file: java.io.File) -> java.util.Properties:
        """
        Given a zip file, returns the {@link Properties} defined in the embedded extension.properties file.
        @param file the extension archive file
        @return the properties file, or null if doesn't exist
        @throws ExtensionException if there's a problem unpacking the zip file
        """
        ...

    def hashCode(self) -> int: ...

    @overload
    @staticmethod
    def install(rFile: generic.jar.ResourceFile) -> bool:
        """
        Installs the given extension file. This can be either an archive (zip) or a
         directory that contains an extension.properties file.
        @param rFile the extension to install
        @return true if the extension was successfully installed
        """
        ...

    @overload
    @staticmethod
    def install(extension: ghidra.framework.plugintool.dialog.ExtensionDetails, overwrite: bool) -> bool:
        """
        Installs the given extension.
        @param extension the extension to install
        @param overwrite if true, any existing extension will be overwritten
        @return true if the install was successful
        """
        ...

    @staticmethod
    def isExtension(rFile: generic.jar.ResourceFile) -> bool:
        """
        Returns true if the given file or directory is a valid ghidra extension.
         <p>
         Note: This means that the zip or directory contains an extension.properties file.
        @param rFile the resource zip or directory to inspect
        @return true if the given file represents a valid extension
        @throws ExtensionException if there's an error processing a zip file
        """
        ...

    @staticmethod
    def isInstalled(extensionName: unicode) -> bool:
        """
        Returns true if an extension with the given name exists in the install folder.
        @param extensionName the name of the extension
        @return true if installed
        """
        ...

    @staticmethod
    def isZip(file: java.io.File) -> bool:
        """
        Returns true if the given file is a valid .zip archive.
        @param file the file to test
        @return true if file is a valid zip
        @throws ExtensionException if there's an error reading the zip file
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def removeStateFiles(extension: ghidra.framework.plugintool.dialog.ExtensionDetails) -> bool:
        """
        Recursively searches a given directory for any module manifest and extension
         properties files that are in an installed state and converts them to an uninstalled
         state.

         Specifically, the following will be renamed:
         <UL>
         <LI>Module.manifest to Module.manifest.uninstalled</LI>
         <LI>extension.properties = extension.properties.uninstalled</LI>
         </UL>
        @param extension the extension to modify
        @return false if any renames fail
        """
        ...

    @staticmethod
    def restoreStateFiles(rootDir: java.io.File) -> bool:
        """
        Recursively searches a given directory for any module manifest and extension
         properties files that are in an uninstalled state and restores them.

         Specifically, the following will be renamed:
         <UL>
         <LI>Module.manifest.uninstalled to Module.manifest</LI>
         <LI>extension.properties.uninstalled = extension.properties</LI>
         </UL>
        @param rootDir the directory to search
        @return false if any renames fail
        """
        ...

    def toString(self) -> unicode: ...

    @staticmethod
    def uninstall(extension: ghidra.framework.plugintool.dialog.ExtensionDetails) -> bool:
        """
        Uninstalls a given extension.
        @param extension the extension to uninstall
        @return true if successfully uninstalled
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
