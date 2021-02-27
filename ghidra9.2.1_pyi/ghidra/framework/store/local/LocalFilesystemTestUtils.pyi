import ghidra.framework.store.local
import java.lang


class LocalFilesystemTestUtils(object):








    @staticmethod
    def createIndexedV0Filesystem(rootPath: unicode, isVersioned: bool, readOnly: bool, enableAsyncronousDispatching: bool) -> ghidra.framework.store.local.IndexedLocalFileSystem:
        """
        Create empty V0 Indexed filesystem.  This is an original Indexed filesystem with the addition
         of a version 0 indicator within the index file.
        @param rootPath path for root directory (must already exist).
        @param isVersioned if true item versioning will be enabled.
        @param readOnly if true modifications within this file-system will not be allowed
         and result in an ReadOnlyException
        @param enableAsyncronousDispatching if true a separate dispatch thread will be used
         to notify listeners.  If false, blocking notification will be performed.
        @throws IOException
        """
        ...

    @staticmethod
    def createIndexedV1Filesystem(rootPath: unicode, isVersioned: bool, readOnly: bool, enableAsyncronousDispatching: bool) -> ghidra.framework.store.local.IndexedV1LocalFileSystem:
        """
        Create empty mangled filesystem
        @param rootPath path for root directory (must already exist).
        @param isVersioned if true item versioning will be enabled.
        @param readOnly if true modifications within this file-system will not be allowed
         and result in an ReadOnlyException
        @param enableAsyncronousDispatching if true a separate dispatch thread will be used
         to notify listeners.  If false, blocking notification will be performed.
        @throws IOException
        """
        ...

    @staticmethod
    def createMangledFilesystem(rootPath: unicode, isVersioned: bool, readOnly: bool, enableAsyncronousDispatching: bool) -> ghidra.framework.store.local.MangledLocalFileSystem:
        """
        Create empty mangled filesystem
        @param rootPath path for root directory (must already exist).
        @param isVersioned if true item versioning will be enabled.
        @param readOnly if true modifications within this file-system will not be allowed
         and result in an ReadOnlyException
        @param enableAsyncronousDispatching if true a separate dispatch thread will be used
         to notify listeners.  If false, blocking notification will be performed.
        @throws IOException
        """
        ...

    @staticmethod
    def createOriginalIndexedFilesystem(rootPath: unicode, isVersioned: bool, readOnly: bool, enableAsyncronousDispatching: bool) -> ghidra.framework.store.local.IndexedLocalFileSystem:
        """
        Create empty original Indexed filesystem.  The original index file lacked any version indicator
         but will be treated as a version 0 index.
        @param rootPath path for root directory (must already exist).
        @param isVersioned if true item versioning will be enabled.
        @param readOnly if true modifications within this file-system will not be allowed
         and result in an ReadOnlyException
        @param enableAsyncronousDispatching if true a separate dispatch thread will be used
         to notify listeners.  If false, blocking notification will be performed.
        @throws IOException
        """
        ...

    def equals(self, __a0: object) -> bool: ...

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
