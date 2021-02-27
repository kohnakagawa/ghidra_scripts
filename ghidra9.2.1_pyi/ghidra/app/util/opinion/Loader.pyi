from typing import List
import ghidra.app.util
import ghidra.app.util.bin
import ghidra.app.util.importer
import ghidra.app.util.opinion
import ghidra.framework.model
import ghidra.program.model.listing
import ghidra.util.classfinder
import ghidra.util.task
import java.lang
import java.util


class Loader(ghidra.util.classfinder.ExtensionPoint, java.lang.Comparable, object):
    """
    An interface that all loaders must implement. A particular loader implementation should be
     designed to identify one and only one file format.

     NOTE:  ALL loader CLASSES MUST END IN "Loader".  If not, the ClassSearcher will not find
     them.
    """

    COMMAND_LINE_ARG_PREFIX: unicode = u'-loader'







    @overload
    def compareTo(self, o: ghidra.app.util.opinion.Loader) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def findSupportedLoadSpecs(self, provider: ghidra.app.util.bin.ByteProvider) -> java.util.Collection:
        """
        If this {@link Loader} supports loading the given {@link ByteProvider}, this methods returns
         a {@link Collection} of all supported {@link LoadSpec}s that contain discovered load
         specification information that this {@link Loader} will need to load.  If this {@link Loader}
         cannot support loading the given {@link ByteProvider}, an empty {@link Collection} is
         returned.
        @param provider The bytes being loaded.
        @return A {@link Collection} of {@link LoadSpec}s that this {@link Loader} supports loading,
           or an empty {@link Collection} if this {@link Loader} doesn't support loading the given
           {@link ByteProvider}.
        @throws IOException if there was an IO-related issue finding the {@link LoadSpec}s.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDefaultOptions(self, provider: ghidra.app.util.bin.ByteProvider, loadSpec: ghidra.app.util.opinion.LoadSpec, domainObject: ghidra.framework.model.DomainObject, loadIntoProgram: bool) -> List[ghidra.app.util.Option]:
        """
        Gets the default {@link Loader} options.
        @param provider The bytes of the thing being loaded.
        @param loadSpec The {@link LoadSpec}.
        @param domainObject The {@link DomainObject} being loaded.
        @param loadIntoProgram True if the load is adding to an existing {@link DomainObject};
           otherwise, false.
        @return A list of the {@link Loader}'s default options.
        """
        ...

    def getName(self) -> unicode:
        """
        Gets the {@link Loader}'s name, which is used both for display purposes, and to identify the
         {@link Loader} in the opinion files.
        @return The {@link Loader}'s name.
        """
        ...

    def getPreferredFileName(self, provider: ghidra.app.util.bin.ByteProvider) -> unicode:
        """
        The preferred file name to use when loading.
         <p>
         The default behavior of this method is to return the (cleaned up) name of the given
           {@link ByteProvider}.
         <p>
         NOTE: This method may get called frequently, so only parse the given {@link ByteProvider}
         if absolutely necessary.
        @param provider The bytes to load.
        @return The preferred file name to use when loading.
        """
        ...

    def getTier(self) -> ghidra.app.util.opinion.LoaderTier:
        """
        For ordering purposes; lower tier numbers are more important (and listed
         first).
        @return the tier of the loader
        """
        ...

    def getTierPriority(self) -> int:
        """
        For ordering purposes; lower numbers are more important (and listed
         first, within its tier).
        @return the ordering of the loader within its tier
        """
        ...

    def hashCode(self) -> int: ...

    def load(self, __a0: ghidra.app.util.bin.ByteProvider, __a1: unicode, __a2: ghidra.framework.model.DomainFolder, __a3: ghidra.app.util.opinion.LoadSpec, __a4: List[object], __a5: ghidra.app.util.importer.MessageLog, __a6: object, __a7: ghidra.util.task.TaskMonitor) -> List[object]: ...

    def loadInto(self, __a0: ghidra.app.util.bin.ByteProvider, __a1: ghidra.app.util.opinion.LoadSpec, __a2: List[object], __a3: ghidra.app.util.importer.MessageLog, __a4: ghidra.program.model.listing.Program, __a5: ghidra.util.task.TaskMonitor) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def supportsLoadIntoProgram(self) -> bool:
        """
        Checks to see if this {@link Loader} supports loading into an existing {@link Program}.
         <p>
         The default behavior of this method is to return false.
        @return True if this {@link Loader} supports loading into an existing {@link Program};
           otherwise, false.
        """
        ...

    def toString(self) -> unicode: ...

    def validateOptions(self, __a0: ghidra.app.util.bin.ByteProvider, __a1: ghidra.app.util.opinion.LoadSpec, __a2: List[object], __a3: ghidra.program.model.listing.Program) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def name(self) -> unicode: ...

    @property
    def tier(self) -> ghidra.app.util.opinion.LoaderTier: ...

    @property
    def tierPriority(self) -> int: ...
