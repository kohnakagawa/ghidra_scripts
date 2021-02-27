import java.lang


class FileCacheNameIndex(object):
    """
    A best-effort cache of MD5 values of files, where the file is identified by its parent's
     MD5 combined with the file's path inside its parent's 'namespace'.
    """





    def __init__(self): ...



    def add(self, parentMD5: unicode, name: unicode, fileMD5: unicode) -> None:
        """
        Adds a filename mapping to this cache.
        @param parentMD5 the md5 string of the parent object
        @param name the name of this object
        @param fileMD5 the md5 string of this object
        @throws IOException if missing or bad md5 values.
        """
        ...

    def clear(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def get(self, parentMD5: unicode, name: unicode) -> unicode:
        """
        Retrieves a filename mapping from this cache.
        @param parentMD5 the md5 string of the parent object
        @param name the name of the requested object.
        @return the md5 string of the requested object, or null if not in cache.
        @throws IOException if missing or bad parent md5 values.
        """
        ...

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
