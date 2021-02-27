from typing import List
import generic.jar
import ghidra.framework
import java.io
import java.lang
import java.util
import utility.application


class Application(object):
    """
    The Application class provides a variety of static convenience methods for accessing Application
     elements that can be used once the #initializeApplication call has been made.

     In order to initialize an application, an ApplicationLayout and an
     ApplicationConfiguration must be provided.  The layout and configuration come in a
     variety of flavors, and are what makes the Application class usable across a range of tools.

     Example use case:

       ApplicationLayout layout = new GhidraApplicationLayout();
       ApplicationConfiguration configuration = new GhidraApplicationConfiguration();
       Application.initalizeApplication(layout, configuration);

    """









    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def findDataFileInAnyModule(relativePath: unicode) -> generic.jar.ResourceFile:
        """
        Finds the first file that exists with the relative path in any module.
        @param relativePath the path from the module root
        @return the first file that exists with the relative path in any module.
        """
        ...

    @staticmethod
    def findFilesByExtension(moduleName: unicode, extension: unicode) -> List[generic.jar.ResourceFile]:
        """
        Returns a list of all files with the given extension that are located in the named module.
        @param moduleName the name of the module for which to look for files with the given extension.
        @param extension the filename extension for which to find file.s
        @return a list of all files with the given extension that are located in the named module.
        """
        ...

    @staticmethod
    def findFilesByExtensionInApplication(extension: unicode) -> List[generic.jar.ResourceFile]:
        """
        Returns all files within any module's data directory that end with the given extension.
        @param extension the extension of files to be found.
        @return all files within any module's data directory that end with the given extension.
        """
        ...

    @staticmethod
    def findFilesByExtensionInMyModule(extension: unicode) -> List[generic.jar.ResourceFile]:
        """
        Returns a list of all files with the given extension that are located in the module
         of the calling class.
        @param extension the filename extension for which to find file.s
        @return a list of all files with the given extension that are located in the module
         of the calling class.
        """
        ...

    @staticmethod
    def findModuleSubDirectories(relativePath: unicode) -> List[generic.jar.ResourceFile]:
        """
        Returns a list of all directories in any module that have the given module relative path.  For
         example, a relative path of "foo/bar" will return all directories that are of the form
         {@code <module root>/data/foo/bar}
        @param relativePath the module relative path to search for.
        @return a list of all directories in any module that have the given module relative path.
        """
        ...

    @staticmethod
    def getApplicationLayout() -> utility.application.ApplicationLayout: ...

    @staticmethod
    def getApplicationProperty(propertyName: unicode) -> unicode:
        """
        Returns the value of the give application property name.
        @param propertyName the name of the application property to retrieve.
        @return the value of the give application property name.
        """
        ...

    @staticmethod
    def getApplicationReleaseName() -> unicode:
        """
        Returns the release name for this build.
        @return the application release name.
        """
        ...

    @staticmethod
    def getApplicationRootDirectories() -> java.util.Collection:
        """
        Returns a list of the application root directories.  An application root directory is a
         directory containing one or more modules.  Applications support multiple application root
         directories so that it can contain modules that don't have a common file system root.  This
         is useful if the application contains modules from more than one source code repository.
         Application roots are returned in the order they appear in the classpath.
        @return a list of root directories containing modules for this application.
        """
        ...

    @staticmethod
    def getApplicationRootDirectory() -> generic.jar.ResourceFile:
        """
        Returns the application root directory.   An application root directory is a
         directory containing one or more modules.  In development mode there may be multiple
         application root directories, which can be retrieved via
         {@link #getApplicationRootDirectories()}.
         <p>
         In an installation of the application, there will only be one application root directory.
         <p>
         <b>Note:  Be sure you understand that there may be multiple application root
         directories in development mode.</b>  In general you should not be using this method for
         searching for files yourself, but instead using
         the various <code>find*</code> methods of this class.
        @return Returns the application root directory.
        @see #getApplicationRootDirectories()
        """
        ...

    @staticmethod
    def getApplicationSourceRevisions() -> java.util.Map:
        """
        Return the source repository revisions used in the build process
         or null if not applicable.
        @return source revision map or null if not applicable
        """
        ...

    @staticmethod
    def getApplicationVersion() -> unicode:
        """
        Returns the version of this build.
        @return the version of this build.
        """
        ...

    @staticmethod
    def getBuildDate() -> unicode:
        """
        Returns the date this build was created.
        @return the date this build was created.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getInstallationDirectory() -> generic.jar.ResourceFile:
        """
        Returns the installation directory.  In an installation, there is only one application root
         and its parent is the installation directory.  If not an installation, then this call doesn't
         really make sense, but it will return the parent of the first installation root.
        @return
        """
        ...

    @staticmethod
    def getLibraryDirectories() -> java.util.Collection:
        """
        Returns a collection of module library directories. Library directories are optional for a module.
        @return a collection of module library directories.
        """
        ...

    @staticmethod
    def getModuleContainingClass(className: unicode) -> generic.jar.ResourceFile: ...

    @staticmethod
    def getModuleContainingResourceFile(file: generic.jar.ResourceFile) -> generic.jar.ResourceFile: ...

    @overload
    @staticmethod
    def getModuleDataFile(relativeDataPath: unicode) -> generic.jar.ResourceFile:
        """
        Returns the file relative to the calling class's module's data directory
        @param relativeDataPath the path relative the to module's data directory
        @throws FileNotFoundException if the file or module does not exist.
        """
        ...

    @overload
    @staticmethod
    def getModuleDataFile(moduleName: unicode, relativeDataPath: unicode) -> generic.jar.ResourceFile:
        """
        Returns the file relative to the named module's data directory. (i.e. "data/" will
         be prepended to the give path)
        @param moduleName the name of the module.
        @param relativeDataPath the path relative to the module's data directory.
        @throws FileNotFoundException if the file does not exist.
        """
        ...

    @overload
    @staticmethod
    def getModuleDataSubDirectory(relativePath: unicode) -> generic.jar.ResourceFile:
        """
        Returns the directory relative to the calling class's module's data directory.
        @param relativePath the path relative the module's data directory
        @throws FileNotFoundException if the directory does not exist.
        @throws IOException if an error occurred trying to access the directory.
        """
        ...

    @overload
    @staticmethod
    def getModuleDataSubDirectory(moduleName: unicode, relativePath: unicode) -> generic.jar.ResourceFile:
        """
        Return the directory relative the the name module's data directory. (i.e. "/data" will
         be prepended to the given path)
        @param moduleName the name of the module.
        @param relativePath the path relative to the module's data directory.
        @throws FileNotFoundException if the directory does not exist
        @throws IOException if an error occurred trying to access the directory.
        """
        ...

    @staticmethod
    def getModuleFile(moduleName: unicode, relativePath: unicode) -> generic.jar.ResourceFile:
        """
        Returns the file relative to the named module's directory.
        @param moduleName the name of the module.
        @param relativePath the path relative to the module's data directory.
        @throws FileNotFoundException if the file does not exist.
        """
        ...

    @staticmethod
    def getModuleRootDir(moduleName: unicode) -> generic.jar.ResourceFile:
        """
        Return the module root directory for the module with the given name.
        @param moduleName the name of the module.
        @return the module root directory for the module with the given name or null if not found.
        """
        ...

    @staticmethod
    def getModuleRootDirectories() -> java.util.Collection:
        """
        Returns a collection of all the module root directories. A module root directory is
         the top-level directory of a module.
        @return a collection of all the module root directories.
        """
        ...

    @staticmethod
    def getModuleSubDirectory(moduleName: unicode, relativePath: unicode) -> generic.jar.ResourceFile:
        """
        Return the directory relative the the name module's directory.
        @param moduleName the name of the module.
        @param relativePath the path relative to the module's root directory.
        @throws FileNotFoundException if the directory does not exist
        @throws IOException if an error occurred trying to access the directory.
        """
        ...

    @staticmethod
    def getMyModuleRootDirectory() -> generic.jar.ResourceFile:
        """
        Returns the module root directory that contains the class that called this method.
        @return the module root directory that contains the class that called this method.
        """
        ...

    @staticmethod
    def getName() -> unicode:
        """
        Returns the name of the application.
        @return the name of the application.
        """
        ...

    @overload
    @staticmethod
    def getOSFile(exactFilename: unicode) -> java.io.File:
        """
        Returns the OS specific file in the calling class's module.
        @param exactFilename the name of the OS specific file.
        @throws FileNotFoundException if the file does not exist.
        """
        ...

    @overload
    @staticmethod
    def getOSFile(moduleName: unicode, exactFilename: unicode) -> java.io.File:
        """
        Returns the OS specific file within the given module with the given name.
        @param moduleName the name of the module
        @param exactFilename the name of the OS file within the module.
        @throws FileNotFoundException if the file does not exist.
        """
        ...

    @staticmethod
    def getUserCacheDirectory() -> java.io.File:
        """
        Returns the cache directory specific to the user and the application.
         The intention is for directory contents to be preserved, however the
         specific location is platform specific and contents may be removed when
         not in use and may in fact be the same directory the user temp directory.
         This directory is specific to the application name but not the version.
         Resources stored within this directory should utilize some
         form of access locking and/or unique naming.
        @return cache directory
        """
        ...

    @staticmethod
    def getUserSettingsDirectory() -> java.io.File:
        """
        Returns the File containing the user configuration settings for this application.
        @return the File containing the user configuration settings for this application.
        """
        ...

    @staticmethod
    def getUserTempDirectory() -> java.io.File:
        """
        Returns the temporary directory specific to the user and the application.
         Directory has name of &lt;username&gt;-&lt;appname&gt;
         This directory may be removed at system reboot or during periodic
         system cleanup of unused temp files.
         This directory is specific to the application name but not the version.
         Resources stored within this directory should utilize some
         form of access locking or unique naming.  Transient resources should be
         deleted when no longer in use.
        @return temp directory
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def inSingleJarMode() -> bool:
        """
        Checks whether or not the application is in "single jar" mode.
        @return true if the application is in "single jar" mode; otherwise, false.
        """
        ...

    @staticmethod
    def initializeApplication(layout: utility.application.ApplicationLayout, configuration: ghidra.framework.ApplicationConfiguration) -> None:
        """
        Initializes the application.  The static methods of this class cannot be used until the
         application is initialized.
        @param layout The application layout to be used by the application.
        @param configuration The application configuration to be used by the application.
        """
        ...

    @staticmethod
    def initializeLogging(logFile: java.io.File, scriptLogFile: java.io.File) -> None:
        """
        If the Application was previously initialized with logging disabled, this method
         may be used to perform delayed logging initialization.
        @param logFile application log file, if null the default <i>application.log</i> will be stored
         within the user's application settings directory
        @param scriptLogFile scripting log file, if null the default <i>script.log</i> will be stored
         within the user's application settings directory
        @throws AssertException if Application has not yet been initialized, or logging
         was previously configured for the application.
        """
        ...

    @staticmethod
    def isInitialized() -> bool:
        """
        Checks to see if the application has been initialized.
        @return true if the application has been initialized; otherwise, false.
        """
        ...

    @staticmethod
    def isTestBuild() -> bool:
        """
        Returns true if this build was not built through the official build process, but instead
          was created using the "buildLocal" call.
        @return true if this build was not built using the official build process.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
