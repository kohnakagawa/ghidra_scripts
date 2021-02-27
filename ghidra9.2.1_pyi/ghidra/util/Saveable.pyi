import ghidra.util
import java.lang


class Saveable(object):
    """
    Save and restore elements that are compatible with ObjectStorage objects.

     Important: Any class implementing this interface that
     may have its class path saved to the data base (i.e. user defined properties)
     should create a map in the ClassTranslator when it is moved
     or renamed between versions of Ghidra. It should also implement ExtensionPoint.
     For example, any class that implements the Saveable interface
     can potentially be saved as a property in the program. If used as a program
     property the class name gets saved to a database field in the property manager.
     If the class gets moved or renamed, the property manager won't be able to
     instantiate it. The ClassTranslator allows the saveable class
     to indicate its old path name (that was stored in the database) and its
     current path name (the actual location of the class it needs to instantiate
     for the property).
     The saveable class should call
         ClassTranslator.put(oldClassPath, newClassPath);
     in its static initializer.
     The property manager would then call
         String newPathName = ClassTranslator.get(oldPathName);
     when it can't find the class for the old path name.
     If the new path name isn't null the property manager can use it to get the class.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getObjectStorageFields(self) -> java.lang.Class:
        """
        Returns the field classes, in Java types, in the same order as used {@link #save} and
         {@link #restore}.
         <p>
         For example, if the save method calls <code>objStorage.putInt()</code> and then
         <code>objStorage.putFloat()</code>, then this method must return
         <code>Class[]{ Integer.class, Float.class }</code>.
        @return
        """
        ...

    def getSchemaVersion(self) -> int:
        """
        Get the storage schema version.  Any time there is a software release
         in which the implementing class has changed the data structure used
         for the save and restore methods, the schema version must be incremented.
         NOTE: While this could be a static method, the Saveable interface is unable to
         define such methods.
        @return storage schema version.
        """
        ...

    def hashCode(self) -> int: ...

    def isPrivate(self) -> bool:
        """
        Returns true if this saveable should not have it's changes broadcast.
        @return true if this saveable should not have it's changes broadcast.
        """
        ...

    def isUpgradeable(self, oldSchemaVersion: int) -> bool:
        """
        Determine if the implementation supports an storage upgrade of the specified
         oldSchemaVersion to the current schema version.
        @param oldSchemaVersion
        @return true if upgrading is supported for the older schema version.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restore(self, objStorage: ghidra.util.ObjectStorage) -> None:
        """
        Restore from the given ObjectStorage.
        @param objStorage Object that can handle Java primitives, Strings, and
         arrays of primitives and Strings
        @throws db.IllegalFieldAccessException if objStorage is improperly accessed.
        """
        ...

    def save(self, objStorage: ghidra.util.ObjectStorage) -> None:
        """
        Save to the given ObjectStorage.
        @param objStorage Object that can handle Java primitives, Strings, and
         arrays of primitives and Strings
        """
        ...

    def toString(self) -> unicode: ...

    def upgrade(self, oldObjStorage: ghidra.util.ObjectStorage, oldSchemaVersion: int, currentObjStorage: ghidra.util.ObjectStorage) -> bool:
        """
        Upgrade an older stored object to the current storage schema.
        @param oldObjStorage the old stored object
        @param oldSchemaVersion storage schema version number for the old object
        @param currentObjStorage new object for storage in the current schema
        @return true if data was upgraded to the currentObjStorage successfully.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def objectStorageFields(self) -> List[java.lang.Class]: ...

    @property
    def private(self) -> bool: ...

    @property
    def schemaVersion(self) -> int: ...
