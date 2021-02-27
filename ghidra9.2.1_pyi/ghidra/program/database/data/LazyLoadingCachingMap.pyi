import java.lang
import java.util


class LazyLoadingCachingMap(object):
    """
    Instances of this class will provide a simple map interface to a cached set of key,value
     pairs.  This class requires that the map can be generated from scratch at any time and
     that adding/removing items from this map is just a mirroring of those changes elsewhere.
     This map is lazy in that it won't load the data until needed and it will use a soft reference
     to maintain the map until such time as the java garbage collector decides to reclaim it.

     This class uses a ghidra Lock object to coordinate threaded access when loading the
     underlying map data.  It manages both the lock and its own synchronization to avoid
     race conditions and deadlocks.
    """









    def clear(self) -> None:
        """
        Removes any cached map of values and restores the map to its initial state.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def get(self, __a0: object) -> object: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def put(self, __a0: object, __a1: object) -> None: ...

    def remove(self, __a0: object) -> None: ...

    def toString(self) -> unicode: ...

    def values(self) -> java.util.Collection:
        """
        Returns an unmodifiable view of the values in this map.
        @return an unmodifiable view of the values in this map.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
