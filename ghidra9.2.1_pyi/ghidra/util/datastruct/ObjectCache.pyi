import java.lang


class ObjectCache(object):
    """
    ObjectClass provides a fixed-size long-key-based object cache.
     Both a hard and weak cache are maintained, where the weak cache is only
     limited by available memory.  This cache mechanism is useful in ensuring that
     only a single object instance for a given key exists.

     The weak cache is keyed, while the hard cache simply maintains the presence of
     an object in the weak cache.
    """





    def __init__(self, hardCacheSize: int):
        """
        Construct a keyed-object cache of size hardCacheSize.
        @param hardCacheSize hard cache size.
        """
        ...



    def contains(self, key: long) -> bool:
        """
        Determine if the keyed-object exists in the cache.
        @param key object key
        @return true if object is cached
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def get(self, key: long) -> object:
        """
        Get the object from cache which corresponds to the specified key.
        @param key object key
        @return cached object
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def put(self, key: long, obj: object) -> None:
        """
        Add an object to the cache
        @param key object key
        @param obj the object
        """
        ...

    def remove(self, key: long) -> None:
        """
        Remove the specified keyed object from both hard and weak caches.
         An object should be removed from the cache when it becomes invalid.
        @param key object key
        """
        ...

    def setHardCacheSize(self, size: int) -> None:
        """
        Adjust the hard cache size
        @param size new hard cache size
        """
        ...

    def size(self) -> int:
        """
        Return the hard cache size
        @return the hard cache size
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
    def hardCacheSize(self) -> None: ...  # No getter available.

    @hardCacheSize.setter
    def hardCacheSize(self, value: int) -> None: ...
