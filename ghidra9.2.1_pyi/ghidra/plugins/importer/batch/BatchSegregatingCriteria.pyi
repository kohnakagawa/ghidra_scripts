from typing import List
import ghidra.plugins.importer.batch
import java.lang


class BatchSegregatingCriteria(object):
    """
    Set of identifying pieces of info that allow us to segregate files that we are
     importing into groups.

     Criteria are:

     Filename extension of source file
     Loader name
     Set of LanguageCompilerSpecs and preferred flags (ie. BatchGroupLoadSpec)

    """





    def __init__(self, loader: ghidra.app.util.opinion.Loader, loadSpecs: java.util.Collection, provider: ghidra.app.util.bin.ByteProvider): ...



    def equals(self, obj: object) -> bool: ...

    def getBatchGroupLoadSpecs(self) -> List[ghidra.plugins.importer.batch.BatchGroupLoadSpec]:
        """
        Return the {@link BatchGroupLoadSpec}s as a sorted list.
        @return sorted list of {@link BatchGroupLoadSpec}s.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getFileExt(self) -> unicode: ...

    def getFirstPreferredLoadSpec(self) -> ghidra.plugins.importer.batch.BatchGroupLoadSpec: ...

    def getLoader(self) -> unicode: ...

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
    def batchGroupLoadSpecs(self) -> List[object]: ...

    @property
    def fileExt(self) -> unicode: ...

    @property
    def firstPreferredLoadSpec(self) -> ghidra.plugins.importer.batch.BatchGroupLoadSpec: ...

    @property
    def loader(self) -> unicode: ...
