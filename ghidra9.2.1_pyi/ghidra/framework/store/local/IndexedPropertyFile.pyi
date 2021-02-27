import ghidra.util
import java.io
import java.lang


class IndexedPropertyFile(ghidra.util.PropertyFile):
    NAME_PROPERTY: unicode = u'NAME'
    PARENT_PATH_PROPERTY: unicode = u'PARENT'



    @overload
    def __init__(self, file: java.io.File):
        """
        Construct an existing PropertyFile.
        @param file
        @throws FileNotFoundException if property file does not exist
        @throws IOException if error occurs reading property file
        """
        ...

    @overload
    def __init__(self, dir: java.io.File, storageName: unicode):
        """
        Construct an existing PropertyFile.
        @param dir parent directory
        @param storageName stored property file name (without extension)
        @throws FileNotFoundException if property file does not exist
        @throws IOException if error occurs reading property file
        """
        ...

    @overload
    def __init__(self, dir: java.io.File, storageName: unicode, parentPath: unicode, name: unicode):
        """
        Construct a new or existing PropertyFile.
         This form ignores retained property values for NAME and PARENT path.
        @param dir parent directory
        @param storageName stored property file name (without extension)
        @param parentPath path to parent
        @param name name of the property file
        @throws IOException
        """
        ...



    def delete(self) -> None:
        """
        Delete the file for this PropertyFile.
        """
        ...

    def equals(self, obj: object) -> bool: ...

    def exists(self) -> bool:
        """
        Return whether the file for this PropertyFile exists.
        """
        ...

    def getBoolean(self, propertyName: unicode, defaultValue: bool) -> bool:
        """
        Return the boolean value with the given propertyName.
        @param propertyName name of property that is a boolean
        @param defaultValue value to use if the property does not exist
        @return boolean value
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getFileID(self) -> unicode:
        """
        Returns the FileID associated with this file.
        @return FileID associated with this file
        """
        ...

    def getFolder(self) -> java.io.File:
        """
        Return the parent file to this PropertyFile.
        """
        ...

    def getInt(self, propertyName: unicode, defaultValue: int) -> int:
        """
        Return the int value with the given propertyName.
        @param propertyName name of property that is an int
        @param defaultValue value to use if the property does not exist
        @return int value
        """
        ...

    def getLong(self, propertyName: unicode, defaultValue: long) -> long:
        """
        Return the long value with the given propertyName.
        @param propertyName name of property that is a long
        @param defaultValue value to use if the property does not exist
        @return long value
        """
        ...

    def getName(self) -> unicode:
        """
        Return the name of this PropertyFile.  A null value may be returned
         if this is an older property file and the name was not specified at
         time of construction.
        """
        ...

    def getParentPath(self) -> unicode:
        """
        Return the path to the parent of this PropertyFile.
        """
        ...

    def getPath(self) -> unicode:
        """
        Return the path to this PropertyFile.  A null value may be returned
         if this is an older property file and the name and parentPath was not specified at
         time of construction.
        """
        ...

    def getStorageName(self) -> unicode:
        """
        Return the storage name of this PropertyFile.  This name does not include the property
         file extension (.prp)
        """
        ...

    def getString(self, propertyName: unicode, defaultValue: unicode) -> unicode:
        """
        Return the string value with the given propertyName.
        @param propertyName name of property that is a string
        @param defaultValue value to use if the property does not exist
        @return string value
        """
        ...

    def hashCode(self) -> int: ...

    def isReadOnly(self) -> bool:
        """
        Returns true if file is writable
        """
        ...

    def lastModified(self) -> long:
        """
        Return the time of last modification in number of milliseconds.
        """
        ...

    def moveTo(self, newParent: java.io.File, newStorageName: unicode, newParentPath: unicode, newName: unicode) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def putBoolean(self, propertyName: unicode, value: bool) -> None:
        """
        Assign the boolean value to the given propertyName.
        @param propertyName name of property to set
        @param value value to set
        """
        ...

    def putInt(self, propertyName: unicode, value: int) -> None:
        """
        Assign the int value to the given propertyName.
        @param propertyName name of property to set
        @param value value to set
        """
        ...

    def putLong(self, propertyName: unicode, value: long) -> None:
        """
        Assign the long value to the given propertyName.
        @param propertyName name of property to set
        @param value value to set
        """
        ...

    def putString(self, propertyName: unicode, value: unicode) -> None:
        """
        Assign the string value to the given propertyName.
        @param propertyName name of property to set
        @param value value to set
        """
        ...

    def readState(self) -> None: ...

    def remove(self, propertyName: unicode) -> None:
        """
        Remove the specified property
        @param propertyName
        """
        ...

    def setFileID(self, fileId: unicode) -> None:
        """
        Set the FileID associated with this file.
        @param fileId
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    def writeState(self) -> None:
        """
        Write the contents of this PropertyFile.
        @throws IOException thrown if there was a problem writing the file
        """
        ...
