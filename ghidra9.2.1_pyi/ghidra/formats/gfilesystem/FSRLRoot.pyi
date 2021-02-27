from typing import List
import ghidra.formats.gfilesystem
import java.lang


class FSRLRoot(ghidra.formats.gfilesystem.FSRL):
    """
    A type of FSRL that is specific to the filesystem's identity.

     A FSRL's parent is always a FSRLRoot.

     A FSRLRoot's parent is always a FSRL (ie. the container the filesystem data is in), or null.

     Examples of relationship between FSRL and FSRLRoots:


     	FSRLRoot [ file:// ]
    	  "file://"

     	  "file:///filename.txt"

        "file:///filename.txt|subfs://"

    """









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

    def getContainer(self) -> ghidra.formats.gfilesystem.FSRL:
        """
        Returns the parent containerfile FSRL, or null if this FSRLRoot specifies
         a root-level filesystem.
         <p>
        @return {@link FSRL} of the container object that this filesystem is nested under.
        """
        ...

    def getFS(self) -> ghidra.formats.gfilesystem.FSRLRoot: ...

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
        Always returns null for a FSRLRoot.
        @return null because this is a {@link FSRLRoot} instance which never has a path and
         therefore doesn't have a name part of a path.
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
        Always returns null for a FSRLRoot.
        @return null because this is a {@link FSRLRoot} instance which never has paths.
        """
        ...

    def getProtocol(self) -> unicode:
        """
        Returns the "protocol" portion of this FSRLRoot, for example, in a FSRLRoot of
         "file://", this method would return "file".
         <p>
        @return string protocol / filesystem type.
        """
        ...

    def hasContainer(self) -> bool:
        """
        Returns true if there is a parent containerfile, or false if this FSRLRoot specifies
         a root-level filesystem.
        @return boolean true if this {@link FSRLRoot} has a parent container, or false if not.
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

    @staticmethod
    def makeRoot(protocol: unicode) -> ghidra.formats.gfilesystem.FSRLRoot:
        """
        Creates a {@link FSRLRoot} without a parent container, using the supplied
         {@code protocol} string as its type.
        @param protocol string protocol name
        @return new {@link FSRLRoot} instance.
        """
        ...

    @overload
    @staticmethod
    def nestedFS(containerFile: ghidra.formats.gfilesystem.FSRL, fstype: unicode) -> ghidra.formats.gfilesystem.FSRLRoot:
        """
        Creates a {@link FSRLRoot} as a child of a container {@link FSRL}, using the supplied
         {@code protocol} string as its type.
        @param containerFile {@link FSRL} of the container that contains this nested filesystem.
        @param fstype the filesystem type.
        @return new {@link FSRLRoot} instance with a parent pointing to the specified containerFile.
        """
        ...

    @overload
    @staticmethod
    def nestedFS(containerFile: ghidra.formats.gfilesystem.FSRL, copyFSRL: ghidra.formats.gfilesystem.FSRLRoot) -> ghidra.formats.gfilesystem.FSRLRoot:
        """
        Create a copy of {@code copyFSRL}, but using a different {@code containerFile} parent.
         <p>
         (ie. re-parents copyFSRL so its parent is containerFile)
        @param containerFile {@link FSRL} of new parent
        @param copyFSRL {@link FSRLRoot} that will be copied and re-parented.
        @return new {@link FSRLRoot}
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

    def withPathMD5(self, newPath: unicode, newMD5: unicode) -> ghidra.formats.gfilesystem.FSRL:
        """
        Creates a new {@link FSRL} as a child of this {@link FSRLRoot}, using the supplied
         path and MD5 values.
         <p>
        @param newPath string path and filename of the object inside this filesystem, should
         not be null.
        @param newMD5 string md5 of the object inside this filesystem, null ok.
        @return new {@link FSRL} instance which is a child of this {@link FSRLRoot}.
        """
        ...

    @property
    def FS(self) -> ghidra.formats.gfilesystem.FSRLRoot: ...

    @property
    def container(self) -> ghidra.formats.gfilesystem.FSRL: ...

    @property
    def name(self) -> unicode: ...

    @property
    def path(self) -> unicode: ...

    @property
    def protocol(self) -> unicode: ...
