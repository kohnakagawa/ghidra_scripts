from typing import List
import ghidra.framework.model
import java.io
import java.lang
import java.net
import java.security
import java.util


class GhidraURLConnection(java.net.URLConnection):
    GHIDRA_NOT_FOUND: int = 404
    GHIDRA_OK: int = 200
    GHIDRA_UNAUTHORIZED: int = 401
    GHIDRA_WRAPPED_CONTENT: unicode = u'GhidraWrappedContent'
    REPOSITORY_SERVER_CONTENT: unicode = u'RepositoryServer'



    @overload
    def __init__(self, ghidraUrl: java.net.URL):
        """
        Construct a Ghidra URL connection which uses the default handler without
         any extension protocol.
        @param ghidraUrl ghidra protocol URL (e.g., {@literal ghidra://server/repo})
        @throws MalformedURLException if URL is invalid
        """
        ...

    @overload
    def __init__(self, url: java.net.URL, protocolHandler: ghidra.framework.protocol.ghidra.GhidraProtocolHandler):
        """
        Construct a Ghidra URL connection which requires an Ghidra protocol extension
        @param url extension URL without the ghidra protocol prefix (e.g., {@literal http://server/repo})
        @param protocolHandler Ghidra protocol extension handler
        @throws MalformedURLException if URL is invalid
        """
        ...



    def addRequestProperty(self, __a0: unicode, __a1: unicode) -> None: ...

    def connect(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getAllowUserInteraction(self) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getConnectTimeout(self) -> int: ...

    @overload
    def getContent(self) -> object:
        """
        Get content associated with the URL
        @return URL content generally in the form of GhidraURLWrappedContent, although other
         special cases may result in different content (Example: a server-only URL could result in
         content class of RepositoryServerAdapter).
        @throws IOException
        """
        ...

    @overload
    def getContent(self, __a0: List[java.lang.Class]) -> object: ...

    def getContentEncoding(self) -> unicode: ...

    def getContentLength(self) -> int: ...

    def getContentLengthLong(self) -> long: ...

    def getContentType(self) -> unicode: ...

    def getDate(self) -> long: ...

    @staticmethod
    def getDefaultAllowUserInteraction() -> bool: ...

    @staticmethod
    def getDefaultRequestProperty(__a0: unicode) -> unicode: ...

    @overload
    def getDefaultUseCaches(self) -> bool: ...

    @overload
    @staticmethod
    def getDefaultUseCaches(__a0: unicode) -> bool: ...

    def getDoInput(self) -> bool: ...

    def getDoOutput(self) -> bool: ...

    def getExpiration(self) -> long: ...

    @staticmethod
    def getFileNameMap() -> java.net.FileNameMap: ...

    def getFolderItemName(self) -> unicode:
        """
        Gets the repository folder item name associated with this connection.
         If an ambiguous path has been specified, the folder item name may become null
         after a connection is established (e.g., folder item name will be appended
         to folder path and item name will become null if item turns out to
         be a folder).
        @return folder item name or null
        """
        ...

    def getFolderPath(self) -> unicode:
        """
        Gets the repository folder path associated with this connection.
         If an ambiguous path has been specified, the folder path may change
         after a connection is established (e.g., folder item name will be appended
         to folder path and item name will become null if item turns out to
         be a folder).
        @return repository folder path or null
        """
        ...

    @overload
    def getHeaderField(self, __a0: int) -> unicode: ...

    @overload
    def getHeaderField(self, __a0: unicode) -> unicode: ...

    def getHeaderFieldDate(self, __a0: unicode, __a1: long) -> long: ...

    def getHeaderFieldInt(self, __a0: unicode, __a1: int) -> int: ...

    def getHeaderFieldKey(self, __a0: int) -> unicode: ...

    def getHeaderFieldLong(self, __a0: unicode, __a1: long) -> long: ...

    def getHeaderFields(self) -> java.util.Map: ...

    def getIfModifiedSince(self) -> long: ...

    def getInputStream(self) -> java.io.InputStream: ...

    def getLastModified(self) -> long: ...

    def getOutputStream(self) -> java.io.OutputStream: ...

    def getPermission(self) -> java.security.Permission: ...

    def getProjectData(self) -> ghidra.framework.model.ProjectData:
        """
        If URL connects and corresponds to a valid repository, this method
         may be used to obtain the associated ProjectData object.  The caller is
         responsible for closing the returned project data when no longer in-use,
         failure to do so may prevent release of repository handle to server.
         Only a single call to this method is permitted.
        @return transient project data or null if unavailable
        @throws IOException
        """
        ...

    def getReadTimeout(self) -> int: ...

    def getRepositoryName(self) -> unicode:
        """
        Gets the repository name associated with this <code>GhidraURLConnection</code>.
        @return the repository name or null if URL does not identify a specific repository
        """
        ...

    def getRequestProperties(self) -> java.util.Map: ...

    def getRequestProperty(self, __a0: unicode) -> unicode: ...

    def getResponseCode(self) -> int:
        """
        Gets the status code from a Ghidra URL response.
        @throws IOException if an error occurred connecting to the server.
        @return the Ghidra Status-Code, or -1
        """
        ...

    def getURL(self) -> java.net.URL: ...

    def getUseCaches(self) -> bool: ...

    @staticmethod
    def guessContentTypeFromName(__a0: unicode) -> unicode: ...

    @staticmethod
    def guessContentTypeFromStream(__a0: java.io.InputStream) -> unicode: ...

    def hashCode(self) -> int: ...

    def isReadOnly(self) -> bool:
        """
        Connection was opened as read-only
        @return true if read-only connection
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setAllowUserInteraction(self, __a0: bool) -> None: ...

    def setConnectTimeout(self, __a0: int) -> None: ...

    @staticmethod
    def setContentHandlerFactory(__a0: java.net.ContentHandlerFactory) -> None: ...

    @staticmethod
    def setDefaultAllowUserInteraction(__a0: bool) -> None: ...

    @staticmethod
    def setDefaultRequestProperty(__a0: unicode, __a1: unicode) -> None: ...

    @overload
    def setDefaultUseCaches(self, __a0: bool) -> None: ...

    @overload
    @staticmethod
    def setDefaultUseCaches(__a0: unicode, __a1: bool) -> None: ...

    def setDoInput(self, __a0: bool) -> None: ...

    def setDoOutput(self, __a0: bool) -> None: ...

    @staticmethod
    def setFileNameMap(__a0: java.net.FileNameMap) -> None: ...

    def setIfModifiedSince(self, __a0: long) -> None: ...

    def setReadOnly(self, state: bool) -> None:
        """
        Set the read-only state of the content.
         Extreme care must be taken when setting the state to false for local projects
         without the use of a ProjectLock.  This setting is currently ignored
         for server repositories which are always read-only in Headed mode and
         read-write in Headless mode.
        @param state read-only if true, otherwise read-write
        """
        ...

    def setReadTimeout(self, __a0: int) -> None: ...

    def setRequestProperty(self, __a0: unicode, __a1: unicode) -> None: ...

    def setUseCaches(self, __a0: bool) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def content(self) -> object: ...

    @property
    def contentType(self) -> unicode: ...

    @property
    def folderItemName(self) -> unicode: ...

    @property
    def folderPath(self) -> unicode: ...

    @property
    def inputStream(self) -> java.io.InputStream: ...

    @property
    def outputStream(self) -> java.io.OutputStream: ...

    @property
    def projectData(self) -> ghidra.framework.model.ProjectData: ...

    @property
    def readOnly(self) -> bool: ...

    @readOnly.setter
    def readOnly(self, value: bool) -> None: ...

    @property
    def repositoryName(self) -> unicode: ...

    @property
    def responseCode(self) -> int: ...
