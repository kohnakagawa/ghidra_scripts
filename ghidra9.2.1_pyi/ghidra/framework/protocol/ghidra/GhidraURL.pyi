import ghidra.framework.model
import java.io
import java.lang
import java.net


class GhidraURL(object):
    MARKER_FILE_EXTENSION: unicode = u'.gpr'
    PROJECT_DIRECTORY_EXTENSION: unicode = u'.rep'
    PROTOCOL: unicode = u'ghidra'







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getDisplayString(url: java.net.URL) -> unicode:
        """
        Generate preferred display string for Ghidra URLs.
         Form can be parsed by the toURL method.
        @param url
        @return
        @see #toURL(String)
        """
        ...

    @staticmethod
    def getNormalizedURL(url: java.net.URL) -> java.net.URL:
        """
        Get a normalized URL which eliminates use of host names and additional URL refs
         which may prevent direct comparison.
        @param url
        @return normalized url
        """
        ...

    @staticmethod
    def getProjectLocation(localProjectURL: java.net.URL) -> unicode:
        """
        Get the project location path which corresponds to the specified
         local project URL.
        @param localProjectURL local Ghidra project URL
        @return project location path
        @throws IllegalArgumentException URL is not a valid local project URL
        """
        ...

    @staticmethod
    def getProjectName(localProjectURL: java.net.URL) -> unicode:
        """
        Get the project name which corresponds to the specified
         local project URL.
        @param localProjectURL local Ghidra project URL
        @return project name
        @throws IllegalArgumentException URL is not a valid local project URL
        """
        ...

    @staticmethod
    def getProjectStorageLocator(localProjectURL: java.net.URL) -> ghidra.framework.model.ProjectLocator:
        """
        Get the project locator which corresponds to the specified
         local project URL.
        @param localProjectURL local Ghidra project URL
        @return project locator
        @throws IllegalArgumentException URL is not a valid local project URL
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isLocalProjectURL(url: java.net.URL) -> bool:
        """
        Determine if the specified URL is a local project URL.
         No checking is performed as to the existence of the project.
        @param url
        @return true if specified URL refers to a local
         project (ghidra:/path/projectName...)
        """
        ...

    @staticmethod
    def isServerRepositoryURL(url: java.net.URL) -> bool:
        """
        Determine if the specified URL is any type of server "repository" URL.
         No checking is performed as to the existence of the server or repository.
        @param url
        @return true if specified URL refers to a Ghidra server
         repository (ghidra://host/repositoryNAME/path...)
        """
        ...

    @staticmethod
    def isServerURL(url: java.net.URL) -> bool:
        """
        Determine if the specified URL is any type of server URL.
         No checking is performed as to the existence of the server or repository.
        @param url
        @return true if specified URL refers to a Ghidra server
         repository (ghidra://host/repositoryNAME/path...)
        """
        ...

    @staticmethod
    def localProjectExists(url: java.net.URL) -> bool:
        """
        Determine if the specified URL refers to a local project and
         it exists.
        @param url
        @return true if specified URL refers to a local project and
         it exists.
        """
        ...

    @overload
    @staticmethod
    def makeURL(projectMarkerFile: java.io.File) -> java.net.URL:
        """
        Create a local project URL for a specified project marker file.
        @param projectMarkerFile project marker file
        @return local project URL
        """
        ...

    @overload
    @staticmethod
    def makeURL(dirPath: unicode, projectName: unicode) -> java.net.URL:
        """
        Create a URL which refers to a local Ghidra project
        @param dirPath absolute path of project location directory
        @param projectName name of project
        @return local Ghidra project URL
        """
        ...

    @overload
    @staticmethod
    def makeURL(host: unicode, port: int, repositoryName: unicode) -> java.net.URL:
        """
        Create a URL which refers to Ghidra Server repository and its root folder
        @param host server host name/address
        @param port optional server port (a value &lt;= 0 refers to the default port)
        @param repositoryName repository name
        @return Ghidra Server repository URL
        """
        ...

    @overload
    @staticmethod
    def makeURL(host: unicode, port: int, repositoryName: unicode, repositoryPath: unicode) -> java.net.URL:
        """
        Create a URL which refers to Ghidra Server repository content.  Path may correspond
         to either a file or folder.
        @param host server host name/address
        @param port optional server port (a value &lt;= 0 refers to the default port)
        @param repositoryName repository name
        @param repositoryPath absolute folder or file path within repository.
         Folder paths should end with a '/' character.
        @return Ghidra Server repository content URL
        """
        ...

    @overload
    @staticmethod
    def makeURL(host: unicode, port: int, repositoryName: unicode, repositoryPath: unicode, fileName: unicode, ref: unicode) -> java.net.URL:
        """
        Create a URL which refers to Ghidra Server repository content.  Path may correspond
         to either a file or folder.
        @param host server host name/address
        @param port optional server port (a value &lt;= 0 refers to the default port)
        @param repositoryName repository name
        @param repositoryPath absolute folder path within repository.
        @param fileName name of a file contained within the specified repository/path
        @param ref optional URL ref or null
         Folder paths should end with a '/' character.
        @return Ghidra Server repository content URL
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @staticmethod
    def toURL(projectPathOrURL: unicode) -> java.net.URL:
        """
        Create a Ghidra URL from a string form of Ghidra URL or local project path.
         This method can consume strings produced by the getDisplayString method.
        @param projectPathOrURL {@literal project path (<absolute-directory>/<project-name>)}
        @return local Ghidra project URL
        @see #getDisplayString(URL)
        @throws IllegalArgumentException invalid path or URL specified
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
