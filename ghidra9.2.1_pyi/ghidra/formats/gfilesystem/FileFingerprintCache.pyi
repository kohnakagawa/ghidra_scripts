import java.lang


class FileFingerprintCache(object):
    """
    A best-effort cache of MD5 values of local files based on their {name,timestamp,length} fingerprint.

     Used to quickly verify that a local file hasn't changed.
    """





    def __init__(self): ...



    def add(self, path: unicode, md5: unicode, timestamp: long, length: long) -> None:
        """
        Add a file's fingerprint to the cache.
        @param path String path to the file
        @param md5 hex-string md5 of the file
        @param timestamp long last modified timestamp of the file
        @param length long file size
        """
        ...

    def clear(self) -> None:
        """
        Clears the cache.
        """
        ...

    def contains(self, path: unicode, md5: unicode, timestamp: long, length: long) -> bool:
        """
        Returns true if the specified file with the specified fingerprints (timestamp, length)
         was previously added to the cache with the specified md5.
        @param path String path to the file
        @param md5 hex-string md5 of the file
        @param timestamp long last modified timestamp of the file
        @param length long file size
        @return true if the fingerprint has previously been added to the cache.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getMD5(self, path: unicode, timestamp: long, length: long) -> unicode:
        """
        Retrieves the md5 for the specified file that has the specified fingerprint (timestamp, length).
        @param path String path to the file
        @param timestamp long last modified timestamp of the file
        @param length long file size
        @return hex-string md5 or null if not present in the cache.
        """
        ...

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
