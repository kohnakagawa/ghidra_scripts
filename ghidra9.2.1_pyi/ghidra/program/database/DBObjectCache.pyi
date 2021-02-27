from typing import List
import db
import java.lang


class DBObjectCache(object):
    """
    Generic cache implementation for objects that extend DatabaseObject. This is a reference based
     cache such that objects are only ever automatically removed from the cache when there are no
     references to that object. It also maintains a small "hard" cache so that recently accessed objects
     are not prematurely removed from the cache if there are no references to them.
    """





    def __init__(self, hardCacheSize: int):
        """
        Constructs a new DBObjectCache with a given hard cache size.  The hard cache size is
         the minimum number of objects to keep in the cache. Typically, the cache will contain
         more than this number, but the excess objects are subject to garbage collections
        @param hardCacheSize the minimum number of objects to keep in the cache.
        """
        ...



    @overload
    def delete(self, key: long) -> None:
        """
        Removes the object with the given key from the cache.
        @param key the key of the object to remove.
        """
        ...

    @overload
    def delete(self, __a0: List[object]) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    @overload
    def get(self, key: long) -> object:
        """
        Retrieves the database object with the given key from the cache.
        @param key the key of the object to retrieve.
        @return the cached object or null if the object with that key is not currently cached.
        """
        ...

    @overload
    def get(self, objectRecord: db.Record) -> object:
        """
        Retrieves the database object with the given record and associated key from the cache.
         This form should be used in conjunction with record iterators to avoid unnecessary
         record query during a possible object refresh.  To benefit from the record the cached
         object must implement the {@link DatabaseObject#refresh(Record)} method which by default
         ignores the record and simply calls {@link DatabaseObject#refresh()}.
        @param objectRecord the valid record corresponding to the object to be retrieved and possibly
         used to refresh the associated object if found in cache
        @return the cached object or null if the object with that key is not currently cached.
        """
        ...

    def getCachedObjects(self) -> List[object]:
        """
        Returns an List of all the cached objects.
        @return an List of all the cached objects.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def invalidate(self) -> None:
        """
        Marks all the cached objects as invalid.  Invalid objects will have to refresh themselves
         before they are allowed to be used. If an invalidated object cannot refresh itself, then
         the object is removed from the cache and discarded and the application can no longer use
         that instance of the object.
        """
        ...

    def keyChanged(self, oldKey: long, newKey: long) -> None: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setHardCacheSize(self, size: int) -> None:
        """
        Sets the number of objects to protect against garbage collection.
        @param size the minimum number of objects to keep in the cache.
        """
        ...

    def size(self) -> int:
        """
        Returns the number of objects currently in the cache.
        @return the number of objects currently in the cache.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def cachedObjects(self) -> List[object]: ...

    @property
    def hardCacheSize(self) -> None: ...  # No getter available.

    @hardCacheSize.setter
    def hardCacheSize(self, value: int) -> None: ...
