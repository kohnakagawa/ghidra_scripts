import ghidra.app.util.bin
import ghidra.app.util.opinion
import java.lang
import java.util
import java.util.function


class LoaderService(object):
    """
    Factory and utility methods for working with Loaders.
    """

    ACCEPT_ALL: java.util.function.Predicate



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def getAllLoaderNames() -> java.util.Collection:
        """
        Gets all known {@link Loader}s' names.
        @return All known {@link Loader}s' names.  The {@link Loader} names are sorted
         according to their corresponding {@link Loader}s {@link Loader#compareTo(Loader) natural
         ordering}.
        """
        ...

    @staticmethod
    def getAllSupportedLoadSpecs(provider: ghidra.app.util.bin.ByteProvider) -> ghidra.app.util.opinion.LoaderMap:
        """
        Gets all supported {@link LoadSpec}s for loading the given {@link ByteProvider}.
        @param provider The {@link ByteProvider} to load.
        @return All supported {@link LoadSpec}s in the form of a {@link LoaderMap}.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getLoaderClassByName(name: unicode) -> java.lang.Class:
        """
        Gets the {@link Loader} {@link Class} that corresponds to the given simple {@link Class}
         name.
        @param name The name of the {@link Loader} to get the {@link Class} of.
        @return The {@link Loader} {@link Class} that corresponds to the given simple {@link Class}
           name.
        """
        ...

    @staticmethod
    def getSupportedLoadSpecs(provider: ghidra.app.util.bin.ByteProvider, loaderFilter: java.util.function.Predicate) -> ghidra.app.util.opinion.LoaderMap:
        """
        Gets all supported {@link LoadSpec}s for loading the given {@link ByteProvider}.
        @param provider The {@link ByteProvider} to load.
        @param loaderFilter A {@link Predicate} that will filter out undesired {@link Loader}s.
        @return All supported {@link LoadSpec}s in the form of a {@link LoaderMap}.
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
