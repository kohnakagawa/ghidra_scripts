from typing import List
import ghidra.formats.gfilesystem
import java.lang


class FSRL(object):
    """
    A _F_ile _S_ystem _R_esource _L_ocator, (name and string format patterned after URLs)

     Used to locate a resource (by name) on a "filesystem", in a recursively nested fashion.

     The string format of FSRLs is  + "://" +  +
     [ + "|" pipe +  ]*

     See #fromPartString(FSRL, String) for more format info.

     Read the string format from right-to-left for easiest understanding... ie.
     "file://z|y://x" reads as "file x inside a filesystem y inside a container file z".

     FSRL instances are immutable and thread-safe.

     Examples (pipes shown in red since they are hard to see):

     file://dir/subdir -- simplest example, locates a file on local computer filesystem.
     file://dir/subdir/example.zip|zip://readme.txt -- points to a file named "readme.txt" in a zip file.
     file://dir/subdir/example.zip|zip://dir/nested.tar|tar://file.txt -- points to
     a file inside a TAR archive, which is inside a ZIP archive, which is on the local filesystem.
     file://dir/subdir/example.zip?MD5=1234567|zip://readme.txt?MD5=987654 --
     points to a file named "readme.txt" (with a MD5 hash) in a zip file (that has another
     MD5 hash).


     See FSRLRoot for examples of how FSRL and FSRLRoot's are related.

     FSRL's can be created either piecemeal, from the bottom up, starting with a root filesystem
     FSRL and calling #appendPath(String) or FSRLRoot#nestedFS(FSRL, String) methods
     to create deeper and deeper nested FSRLs,

     or

     FSRL's can be created from strings using #fromString(String).

     FSRLs that have a MD5 value are FileSystemService#getFullyQualifiedFSRL(FSRL, ghidra.util.task.TaskMonitor).

    """

    PARAM_MD5: unicode = u'MD5'







    def appendPath(self, relPath: unicode) -> ghidra.formats.gfilesystem.FSRL:
        """
        Creates a new {@link FSRL} instance, using the same {@link FSRLRoot} as this instance,
         combining the current {@link #getPath() path} with the {@code relPath} value.
         <p>
        @param relPath
        @return new {@link FSRL} instance with additional path appended.
        """
        ...

    def equals(self, obj: object) -> bool: ...

    @overload
    @staticmethod
    def fromString(fsrlStr: unicode) -> ghidra.formats.gfilesystem.FSRL:
        """
        Creates a {@link FSRL} from a raw string.  The parent portions of the FSRL
         are not intern()'d so will not be shared with other FSRL instances.
         <p>
         See {@link #fromPartString(FSRL, String)} for details of character encoding fixups.
         <p>
        @param fsrlStr something like "fstype://path/path|fs2type://path2/path2|etc://etc/etc"
        @return new {@link FSRL} instance, never null
        @throws MalformedURLException if empty string or bad format
        """
        ...

    @overload
    @staticmethod
    def fromString(parent: ghidra.formats.gfilesystem.FSRL, fsrlStr: unicode) -> ghidra.formats.gfilesystem.FSRL:
        """
        Creates a {@link FSRL} from a raw string.
         <p>
         See {@link #fromPartString(FSRL, String)} for details of character encoding fixups.
         <p>
        @param parent Parent {@link FSRL}
        @param fsrlStr something like "fstype://path/path|fs2type://path2/path2|etc://etc/etc"
        @return new {@link FSRL} instance, never null
        @throws MalformedURLException if empty string or bad format
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getFS(self) -> ghidra.formats.gfilesystem.FSRLRoot:
        """
        Returns the {@link FSRLRoot} object that represents the entire
         {@link GFileSystem filesystem} for this FSRL.
         <p>
         Never returns NULL, and calling getFS() on a {@link FSRLRoot} object
         returns itself.
        @return {@link FSRLRoot} instance that is the parent of this {@link FSRL}, never
         null.
        """
        ...

    def getMD5(self) -> unicode:
        """
        Returns the MD5 string associated with this file.
         <p>
         NULL if no MD5 value present.
         <p>
        @return md5 string associated with this file object, or null if not present.
        """
        ...

    @overload
    def getName(self) -> unicode:
        """
        Returns the name portion of this FSRL's path, everything after the last '/'
         <p>
         "file://path/name.ext" returns "name.ext"
        @return name portion of this FSRL path, or null if path is null also.
        """
        ...

    @overload
    def getName(self, nestedDepth: int) -> unicode:
        """
        Returns the name portion of the FSRL part at parent depth {@code nestedDepth}, where 0
         is ourself (equiv to just calling {@link #getName()}, 1 is the parent
         container's name, etc.
         <p>
        @param nestedDepth relative parent index of FSRL part to query, 0 == this instance.
        @return name portion of the path of the specified FSRL part.
        @throws IOException if nestedDepth is larger than number of FSRL parent parts.
        """
        ...

    def getNestingDepth(self) -> int:
        """
        Returns the number of {@link FSRLRoot}s there are in this {@link FSRL}.
         <p>
         A single level FSRL such as "file://path" will return 1.<br>
         A two level FSRL such as "file://path|subfs://path2" will return 2.<br>
         etc.<br>
        @return number of levels in this FSRL, min value returned is 1.
        """
        ...

    def getPath(self) -> unicode:
        """
        Returns the full path/filename of this FSRL.  Does not include parent filesystem path
         or info.
         <p>
         "file://path|subfs://subpath/blah" returns "/subpath/blah"
         <p>
         May return null if this instance is a {@link FSRLRoot}.
        @return string path and filename of this object.  Null if this {@link FSRL} is a
         {@link FSRLRoot}.
        """
        ...

    def hashCode(self) -> int: ...

    def isDescendantOf(self, potentialParent: ghidra.formats.gfilesystem.FSRL) -> bool:
        """
        Returns {@code true} if this object is a child or descendant of the
         specified {@code potentialParent} parameter.
         <p>
        @param potentialParent {@link FSRL} to test against
        @return boolean true if the specified {@link FSRL} is a parent (ignoring md5 hashes)
         of this instance.
        """
        ...

    @overload
    def isEquivalent(self, fsrlStr: unicode) -> bool:
        """
        Returns true if the two FSRLs are the same, excluding any MD5 values.
        @param fsrlStr string-ified {@link FSRL}
        @return boolean true if this instance is the same as the specified string-ified fsrl,
         ignoring any md5 values.
        """
        ...

    @overload
    def isEquivalent(self, other: ghidra.formats.gfilesystem.FSRL) -> bool:
        """
        Returns true if the two {@link FSRL}s are the same, excluding any MD5 values.
        @param other {@link FSRL} to compare with
        @return boolean true if this instance is the same as the specified FSRL, ignoring
         any md5 values.
        """
        ...

    def makeNested(self, fstype: unicode) -> ghidra.formats.gfilesystem.FSRLRoot:
        """
        Creates a new {@link FSRLRoot} instance that is a child of this FSRL.
         <p>
         See {@link FSRLRoot#nestedFS(FSRL, FSRLRoot)} and {@link FSRLRoot#nestedFS(FSRL, String)}.
        @param fstype file system type string.
        @return new {@link FSRLRoot} instance
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def split(self) -> List[ghidra.formats.gfilesystem.FSRL]:
        """
        Splits a {@link FSRL} into a {@link List}, with each element pointing to
         each level of the full FSRL.
         <p>
         Example: "file://path|subfs://blah|subfs2://blah2"
         <p>
         Produces a list of 3 elements:<br>
         "file://path"<br>
         "file://path|subfs://blah"<br>
         "file://path|subfs://blah|subfs2://blah2"
         <p>
        @return {@link List} of {@link FSRL} elements pointing to each level of this FSRL.
        """
        ...

    def toPrettyFullpathString(self) -> unicode:
        """
        Returns a string containing the full FSRL, without FS "fstype://" portions
         <p>
         Example:
         <p>
         {@code "fsrl://path/filename?MD5=1234|subfsrl://subpath/subfile"}
         <p>
         will result in
         <p>
         {@code "path/filename|subpath/subfile"}.
        @return formatted string such as: "path/filename|subpath/subfile"
        """
        ...

    def toPrettyString(self) -> unicode:
        """
        Returns a string containing the full FSRL, excluding MD5 portions.
        @return string with full FSRL, excluding MD5 portions.
        """
        ...

    def toString(self) -> unicode:
        """
        Returns a string containing the full FSRL.
         <p>
         Example: "file://path|subfs://blah?MD5=1234567"
        @return string with full FSRL
        """
        ...

    def toStringPart(self) -> unicode:
        """
        Returns a string containing just the current {@link FSRL} protocol and path.
         <p>
         Example: "file://path|subfs://blah?MD5=123456" returns "subfs://blah?MD5=123456"
        @return string containing just the current {@link FSRL} protocol and path.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def withMD5(self, newMD5: unicode) -> ghidra.formats.gfilesystem.FSRL:
        """
        Creates a new {@link FSRL} instance, using the same information as this instance,
         but with a new {@link #getMD5() MD5} value.
        @param newMD5 string md5
        @return new {@link FSRL} instance with the same path and the specified md5 value.
        """
        ...

    @overload
    def withPath(self, newpath: unicode) -> ghidra.formats.gfilesystem.FSRL:
        """
        Creates a new {@link FSRL} instance, using the same {@link FSRLRoot} as this instance,
         but with a new path.
         <p>
         See also {@link #appendPath(String)}.
         <p>
        @param newpath string path
        @return new {@link FSRL} instance with the specified path.
        """
        ...

    @overload
    def withPath(self, copyPath: ghidra.formats.gfilesystem.FSRL) -> ghidra.formats.gfilesystem.FSRL:
        """
        Creates a new {@link FSRL} instance using the same path and other metadata
         present in the {@code copyPath} instance.
         <p>
         Used when re-root'ing a FSRL path onto another parent object (usually during intern()'ing)
        @param copyPath
        @return new FSRL instance
        """
        ...

    @property
    def FS(self) -> ghidra.formats.gfilesystem.FSRLRoot: ...

    @property
    def MD5(self) -> unicode: ...

    @property
    def name(self) -> unicode: ...

    @property
    def nestingDepth(self) -> int: ...

    @property
    def path(self) -> unicode: ...
