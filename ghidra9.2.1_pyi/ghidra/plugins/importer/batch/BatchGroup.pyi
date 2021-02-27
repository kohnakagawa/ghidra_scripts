from typing import List
import ghidra.app.util.bin
import ghidra.app.util.opinion
import ghidra.formats.gfilesystem
import ghidra.plugins.importer.batch
import ghidra.plugins.importer.batch.BatchGroup
import java.lang
import java.util


class BatchGroup(object):
    """
    A group of LoadSpecs (possibly from different user added sources)
     that have a common BatchSegregatingCriteria.

     All the Apps must have the same set of LoadSpecs to be included in the same
     BatchGroup.

     Each BatchGroup has a single selected (BatchGroupLoadSpec) that applies
     to all the Apps in the group.
    """






    class BatchLoadConfig(object):








        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getFSRL(self) -> ghidra.formats.gfilesystem.FSRL: ...

        def getLoadSpec(self, __a0: ghidra.plugins.importer.batch.BatchGroupLoadSpec) -> ghidra.app.util.opinion.LoadSpec: ...

        def getLoadSpecs(self) -> java.util.Collection: ...

        def getLoader(self) -> ghidra.app.util.opinion.Loader: ...

        def getPreferredFileName(self) -> unicode: ...

        def getUasi(self) -> ghidra.plugins.importer.batch.UserAddedSourceInfo: ...

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

        @property
        def FSRL(self) -> ghidra.formats.gfilesystem.FSRL: ...

        @property
        def loadSpecs(self) -> java.util.Collection: ...

        @property
        def loader(self) -> ghidra.app.util.opinion.Loader: ...

        @property
        def preferredFileName(self) -> unicode: ...

        @property
        def uasi(self) -> ghidra.plugins.importer.batch.UserAddedSourceInfo: ...

    def __init__(self, criteria: ghidra.plugins.importer.batch.BatchSegregatingCriteria):
        """
        Creates a new {@link BatchGroup} keyed on the specified
         {@link BatchSegregatingCriteria criteria}.
        @param criteria {@link BatchSegregatingCriteria} of this {@link BatchGroup}.
        """
        ...



    def add(self, provider: ghidra.app.util.bin.ByteProvider, loadSpecs: java.util.Collection, fsrl: ghidra.formats.gfilesystem.FSRL, uasi: ghidra.plugins.importer.batch.UserAddedSourceInfo) -> None:
        """
        Adds {@link LoadSpec}s to this group.
        @param provider The {@link ByteProvider}.
        @param loadSpecs {@link LoadSpec}s to add to this group.
        @param fsrl {@link FSRL} of the application's import source file.
        @param uasi {@link UserAddedSourceInfo}
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getBatchLoadConfig(self) -> List[ghidra.plugins.importer.batch.BatchGroup.BatchLoadConfig]:
        """
        Returns the list of current {@link BatchLoadConfig} in this group.
        @return {@link List} of {@link BatchLoadConfig} {@link BatchLoadConfig} wrappers.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getCriteria(self) -> ghidra.plugins.importer.batch.BatchSegregatingCriteria:
        """
        Returns the {@link BatchSegregatingCriteria} of this group.
        @return {@link BatchSegregatingCriteria} of this group.
        """
        ...

    def getSelectedBatchGroupLoadSpec(self) -> ghidra.plugins.importer.batch.BatchGroupLoadSpec:
        """
        Returns the selected {@link BatchGroupLoadSpec} that applies to the entire
         {@link BatchGroup}.
        @return selected {@link BatchGroupLoadSpec} that applies to the entire {@link BatchGroup}.
        """
        ...

    def hashCode(self) -> int: ...

    def isEmpty(self) -> bool:
        """
        Returns true if there are no applications in this group.
        @return boolean true if there are no applications in this group.
        """
        ...

    def isEnabled(self) -> bool:
        """
        Returns true if this group is 'enabled', which means that it has a selected
         {@link BatchGroupLoadSpec} and the user has chosen to mark this group as importable.
        @return boolean enabled status.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeDescendantsOf(self, fsrl: ghidra.formats.gfilesystem.FSRL) -> None:
        """
        Removes any applications that are inside the specified container file.
        @param fsrl {@link FSRL} of a container.
        """
        ...

    def setEnabled(self, enabled: bool) -> None:
        """
        Sets the enabled status of this group.
        @param enabled boolean
        """
        ...

    def setSelectedBatchGroupLoadSpec(self, selectedBatchGroupLoadSpec: ghidra.plugins.importer.batch.BatchGroupLoadSpec) -> None:
        """
        Sets the current {@link BatchGroupLoadSpec} for the entire group of applications.
        @param selectedBatchGroupLoadSpec {@link BatchGroupLoadSpec} to set
        """
        ...

    def size(self) -> int:
        """
        Returns the number of applications in this group.
        @return number of applications in this group.
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
    def batchLoadConfig(self) -> List[object]: ...

    @property
    def criteria(self) -> ghidra.plugins.importer.batch.BatchSegregatingCriteria: ...

    @property
    def empty(self) -> bool: ...

    @property
    def enabled(self) -> bool: ...

    @enabled.setter
    def enabled(self, value: bool) -> None: ...

    @property
    def selectedBatchGroupLoadSpec(self) -> ghidra.plugins.importer.batch.BatchGroupLoadSpec: ...

    @selectedBatchGroupLoadSpec.setter
    def selectedBatchGroupLoadSpec(self, value: ghidra.plugins.importer.batch.BatchGroupLoadSpec) -> None: ...
