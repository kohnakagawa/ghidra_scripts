from typing import List
import ghidra.formats.gfilesystem
import ghidra.formats.gfilesystem.FSUtilities
import ghidra.util.task
import java.awt
import java.io
import java.lang
import java.util


class FSUtilities(object):
    GFILE_NAME_TYPE_COMPARATOR: java.util.Comparator = ghidra.formats.gfilesystem.FSUtilities$$Lambda$780/0x0000000800d3cc40@11547665
    SEPARATOR: unicode = u'/'
    SEPARATOR_CHARS: unicode = u'/\\:'




    class StreamCopyResult(object):
        bytesCopied: long
        md5: List[int]



        def __init__(self, __a0: long, __a1: List[int]): ...



        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

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



    def __init__(self): ...



    @staticmethod
    def appendPath(paths: List[unicode]) -> unicode:
        """
        Concats path strings together, taking care to ensure that there is a correct
         path separator character between each part.
         <p>
         Handles forward or back slashes as path separator characters in the input, but
         only adds forward slashes when separating the path strings that need a separator.
         <p>
        @param paths vararg list of path strings, empty or null elements are ok and are skipped.
        @return null if all params null, "" empty string if all are empty, or
         "path_element[1]/path_element[2]/.../path_element[N]" otherwise.
        """
        ...

    @staticmethod
    def displayException(originator: object, parent: java.awt.Component, title: unicode, message: unicode, throwable: java.lang.Throwable) -> None:
        """
        Displays a filesystem related {@link Throwable exception} in the most user-friendly manner
         possible, even if we have to do some hacky things with helping the user with
         crypto problems.
         <p>
        @param originator a Logger instance, "this", or YourClass.class
        @param parent a parent component used to center the dialog (or null if you
                    don't have one)
        @param title the title of the pop-up dialog (main subject of message)
        @param message the details of the message
        @param throwable the Throwable that describes the cause of the error
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def escapeDecode(s: unicode) -> unicode:
        """
        Returns a decoded version of the input stream where "%nn" escape sequences are
         replaced with their actual characters, using UTF-8 decoding rules.
         <p>
        @param s string with escape sequences in the form "%nn", or null.
        @return string with all escape sequences replaced with native characters, or null if
         original parameter was null.
        @throws MalformedURLException if bad escape sequence format.
        """
        ...

    @staticmethod
    def escapeEncode(s: unicode) -> unicode:
        """
        Returns a copy of the input string with FSRL problematic[1] characters escaped
         as "%nn" sequences, where nn are hexdigits specifying the numeric ascii value
         of that character.
         <p>
         Characters that need more than a byte to encode will result in multiple "%nn" values
         that encode the necessary UTF8 codepoints.
         <p>
         [1] - non-ascii / unprintable / FSRL portion separation characters.
        @param s string, or null.
        @return string with problematic characters escaped as "%nn" sequences, or null
         if parameter was null.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getExtension(path: unicode, extLevel: int) -> unicode:
        """
        Returns the "extension" of the filename part of the path string.
         <p>
         Ie. everything after the nth last '.' char in the filename, including that '.' character.
         <p>
         Using: "path/filename.ext1.ext2"
         <P>
         Gives:
         <UL>
         	<LI>extLevel 1: ".ext2"</LI>
          <LI>extLevel 2: ".ext1.ext2"</LI>
          <LI>extLevel 3: <code>null</code></LI>
         </UL>
        @param path path/filename.ext string
        @param extLevel number of ext levels; must be greater than 0
        @return ".ext1" for "path/filename.notext.ext1" level 1, ".ext1.ext2" for
                 "path/filename.ext1.ext2" level 2, etc. or null if there was no dot character
        @throws IllegalArgumentException if the given level is less than 1
        """
        ...

    @staticmethod
    def getFileMD5(f: java.io.File, monitor: ghidra.util.task.TaskMonitor) -> unicode:
        """
        Calculate the MD5 of a file.
        @param f {@link File} to read.
        @param monitor {@link TaskMonitor} to watch for cancel
        @return md5 as a hex encoded string, never null.
        @throws IOException if error
        @throws CancelledException if cancelled
        """
        ...

    @staticmethod
    def getFilesystemDescriptionFromClass(clazz: java.lang.Class) -> unicode:
        """
        Returns the description value of the {@link FileSystemInfo} annotation attached to the
         specified class.
        @param clazz Class to query.
        @return File system description string.
        """
        ...

    @staticmethod
    def getFilesystemPriorityFromClass(clazz: java.lang.Class) -> int:
        """
        Returns the priority value of the {@link FileSystemInfo} annotation attached to the
         specified class.
        @param clazz Class to query.
        @return File system priority integer.
        """
        ...

    @staticmethod
    def getFilesystemTypeFromClass(clazz: java.lang.Class) -> unicode:
        """
        Returns the type value of the {@link FileSystemInfo} annotation attached to the
         specified class.
        @param clazz Class to query.
        @return File system type string.
        """
        ...

    @staticmethod
    def getSafeFilename(untrustedFilename: unicode) -> unicode:
        """
        Best-effort of sanitizing an untrusted string that will be used to create
         a file on the user's local filesystem.
        @param untrustedFilename filename string with possibly bad / hostile characters or sequences.
        @return sanitized filename
        """
        ...

    @staticmethod
    def getStreamMD5(is_: java.io.InputStream, monitor: ghidra.util.task.TaskMonitor) -> unicode:
        """
        Calculate the MD5 of a stream.
        @param is {@link InputStream} to read
        @param monitor {@link TaskMonitor} to watch for cancel
        @return md5 as a hex encoded string, never null.
        @throws IOException if error
        @throws CancelledException if cancelled
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def infoMapToString(info: java.util.Map) -> unicode:
        """
        Converts a string -&gt; string mapping into a "key: value" multi-line string.
        @param info map of string key to string value.
        @return Multi-line string "key: value" string.
        """
        ...

    @staticmethod
    def isSameFS(__a0: List[object]) -> bool: ...

    @staticmethod
    def listFileSystem(__a0: ghidra.formats.gfilesystem.GFileSystem, __a1: ghidra.formats.gfilesystem.GFile, __a2: List[object], __a3: ghidra.util.task.TaskMonitor) -> List[object]: ...

    @staticmethod
    def normalizeNativePath(path: unicode) -> unicode:
        """
        Returns a copy of the string path that has been fixed to have correct slashes
         and a correct leading root slash '/'.
        @param path String forward or backslash path
        @return String path with all forward slashes and a leading root slash.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def streamCopy(is_: java.io.InputStream, os: java.io.OutputStream, monitor: ghidra.util.task.TaskMonitor) -> ghidra.formats.gfilesystem.FSUtilities.StreamCopyResult:
        """
        Copies a stream and calculates the md5 at the same time.
         <p>
         Does not close the passed-in InputStream or OutputStream.
        @param is {@link InputStream} to copy.  NOTE: not closed by this method.
        @param os {@link OutputStream} to write to.  NOTE: not closed by this method.
        @return {@link StreamCopyResult} with md5 and bytes copied count, never null.
        @throws IOException if error
        @throws CancelledException if canceled
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
