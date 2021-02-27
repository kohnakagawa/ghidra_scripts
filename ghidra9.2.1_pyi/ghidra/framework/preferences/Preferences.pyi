from typing import List
import java.lang


class Preferences(object):
    """
    Uses Properties to manage user preferences as name/value pairs.  All methods
     are static.
    """

    APPLICATION_PREFERENCES_FILENAME: unicode = u'preferences'
    LAST_EXPORT_DIRECTORY: unicode = u'LastExportDirectory'
    LAST_IMPORT_DIRECTORY: unicode = u'LastImportDirectory'
    LAST_NEW_PROJECT_DIRECTORY: unicode = u'LastNewProjectDirectory'
    LAST_OPENED_ARCHIVE_DIRECTORY: unicode = u'LastOpenedArchiveDirectory'
    LAST_TOOL_EXPORT_DIRECTORY: unicode = u'LastToolExportDirectory'
    LAST_TOOL_IMPORT_DIRECTORY: unicode = u'LastToolImportDirectory'
    PROJECT_DIRECTORY: unicode = u'ProjectDirectory'







    @staticmethod
    def clear() -> None:
        """
        Clears all properties in this Preferences object.
         <p>
         <b>Warning: </b>Save any changes pending before calling this method, as this call will
         erase any changes not written do disk via {@link #store()}
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getFilename() -> unicode:
        """
        Get the filename that will be used in the store() method.
        @return the filename
        """
        ...

    @staticmethod
    def getPluginPaths() -> List[unicode]:
        """
        Return the paths in the UserPluginPath property.
         Return zero length array if this property is not set.
        @return the paths
        """
        ...

    @overload
    @staticmethod
    def getProperty(name: unicode) -> unicode:
        """
        Get the property with the given name.
         <p>
         Note: all <code>getProperty(...)</code> methods will first check {@link System#getProperty(String)}
         for a value first.  This allows users to override preferences from the command-line.
        @param name the property name
        @return the current property value; null if not set
        """
        ...

    @overload
    @staticmethod
    def getProperty(name: unicode, defaultValue: unicode) -> unicode:
        """
        Get the property with the given name; if there is no property, return the defaultValue.
         <p>
         Note: all <code>getProperty(...)</code> methods will first check {@link System#getProperty(String)}
         for a value first.  This allows users to override preferences from the command-line.
        @param name the property name
        @param defaultValue the default value
        @return the property value; default value if not set
        @see #getProperty(String, String, boolean)
        """
        ...

    @overload
    @staticmethod
    def getProperty(name: unicode, defaultValue: unicode, useHistoricalValue: bool) -> unicode:
        """
        Get the property with the given name; if there is no property, return the defaultValue.
         <p>
         This version of <code>getProperty</code> will, when <code>useHistoricalValue</code> is true, look
         for the given preference value in the last used installation of the application.
         <p>
         Note: all <code>getProperty(...)</code> methods will first check {@link System#getProperty(String)}
         for a value first.  This allows users to override preferences from the command-line.
        @param name The name of the property for which to get a value
        @param defaultValue The value to use if there is no value yet set for the given name
        @param useHistoricalValue True signals to check the last used application installation for a
                value for the given name <b>if that value has not yet been set</b>.
        @return the property with the given name; if there is no property,
                 return the defaultValue.
        @see #getProperty(String)
        @see #getProperty(String, String)
        """
        ...

    @staticmethod
    def getPropertyNames() -> List[unicode]:
        """
        Get an array of known property names.
        @return if there are no properties, return a zero-length array
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def removeProperty(name: unicode) -> unicode:
        """
        Removes the given preference from this preferences object.
        @param name the name of the preference key to remove.
        @return the value that was stored with the given key.
        """
        ...

    @staticmethod
    def setFilename(name: unicode) -> None:
        """
        Set the filename so that when the store() method is called, the
         preferences are written to this file.
        @param name the filename
        """
        ...

    @staticmethod
    def setPluginPaths(paths: List[unicode]) -> None:
        """
        Set the paths to be used as the UserPluginPath property.
        @param paths the paths
        """
        ...

    @staticmethod
    def setProperty(name: unicode, value: unicode) -> None:
        """
        Set the property value.  If a null value is passed, then the property is removed from
         this collection of preferences.
        @param name property name
        @param value value for property
        """
        ...

    @staticmethod
    def store() -> bool:
        """
        Store the preferences in a file for the current filename.
        @return true if the file was written
        @throws RuntimeException if the preferences filename was not set
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
