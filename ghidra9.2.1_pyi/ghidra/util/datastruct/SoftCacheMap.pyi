from typing import Iterator
from typing import List
import java.lang
import java.util
import java.util.function


class SoftCacheMap(object, java.util.Map):
    """
    Class to manage a "soft" HaspMap that keeps its keys as soft references so
     they can be reclaimed if needed. Useful for caching.
    """





    def __init__(self, cacheSize: int):
        """
        Constructs a new SoftCacheMap that has at most cacheSize entries.
        @param cacheSize the max number of entries to cache.
        """
        ...

    def __iter__(self): ...

    def clear(self) -> None:
        """
        @see java.util.Map#clear()
        """
        ...

    def compute(self, __a0: object, __a1: java.util.function.BiFunction) -> object: ...

    def computeIfAbsent(self, __a0: object, __a1: java.util.function.Function) -> object: ...

    def computeIfPresent(self, __a0: object, __a1: java.util.function.BiFunction) -> object: ...

    def containsKey(self, key: object) -> bool:
        """
        @see java.util.Map#containsKey(java.lang.Object)
        """
        ...

    def containsValue(self, value: object) -> bool:
        """
        @see java.util.Map#containsValue(java.lang.Object)
        """
        ...

    @staticmethod
    def copyOf(__a0: java.util.Map) -> java.util.Map: ...

    @staticmethod
    def entry(__a0: object, __a1: object) -> java.util.Map.Entry: ...

    def entrySet(self) -> java.util.Set:
        """
        @see java.util.Map#entrySet()
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def forEach(self, __a0: java.util.function.BiConsumer) -> None: ...

    def getClass(self) -> java.lang.Class: ...

    def getOrDefault(self, __a0: object, __a1: object) -> object: ...

    def hashCode(self) -> int: ...

    def isEmpty(self) -> bool:
        """
        @see java.util.Map#isEmpty()
        """
        ...

    def keySet(self) -> java.util.Set:
        """
        @see java.util.Map#keySet()
        """
        ...

    def merge(self, __a0: object, __a1: object, __a2: java.util.function.BiFunction) -> object: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    @staticmethod
    def of() -> java.util.Map: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object) -> java.util.Map: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object) -> java.util.Map: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object) -> java.util.Map: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object, __a6: object, __a7: object) -> java.util.Map: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object, __a6: object, __a7: object, __a8: object, __a9: object) -> java.util.Map: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object, __a6: object, __a7: object, __a8: object, __a9: object, __a10: object, __a11: object) -> java.util.Map: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object, __a6: object, __a7: object, __a8: object, __a9: object, __a10: object, __a11: object, __a12: object, __a13: object) -> java.util.Map: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object, __a6: object, __a7: object, __a8: object, __a9: object, __a10: object, __a11: object, __a12: object, __a13: object, __a14: object, __a15: object) -> java.util.Map: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object, __a6: object, __a7: object, __a8: object, __a9: object, __a10: object, __a11: object, __a12: object, __a13: object, __a14: object, __a15: object, __a16: object, __a17: object) -> java.util.Map: ...

    @overload
    @staticmethod
    def of(__a0: object, __a1: object, __a2: object, __a3: object, __a4: object, __a5: object, __a6: object, __a7: object, __a8: object, __a9: object, __a10: object, __a11: object, __a12: object, __a13: object, __a14: object, __a15: object, __a16: object, __a17: object, __a18: object, __a19: object) -> java.util.Map: ...

    @staticmethod
    def ofEntries(__a0: List[java.util.Map.Entry]) -> java.util.Map: ...

    def put(self, __a0: object, __a1: object) -> object: ...

    def putAll(self, t: java.util.Map) -> None:
        """
        @see java.util.Map#putAll(java.util.Map)
        """
        ...

    def putIfAbsent(self, __a0: object, __a1: object) -> object: ...

    @overload
    def remove(self, key: object) -> V:
        """
        @see java.util.Map#remove(java.lang.Object)
        """
        ...

    @overload
    def remove(self, __a0: object, __a1: object) -> bool: ...

    @overload
    def replace(self, __a0: object, __a1: object) -> object: ...

    @overload
    def replace(self, __a0: object, __a1: object, __a2: object) -> bool: ...

    def replaceAll(self, __a0: java.util.function.BiFunction) -> None: ...

    def size(self) -> int:
        """
        @see java.util.Map#size()
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
    def empty(self) -> bool: ...
