import ghidra.app.util.opinion
import ghidra.plugins.importer.batch
import java.lang


class BatchGroupLoadSpec(object, java.lang.Comparable):
    """
    Similar to a LoadSpec, but not associated with a Loader.

     This has the same information as a LoadSpec, but for all the members of a
     BatchGroup.
    """

    lcsPair: ghidra.program.model.lang.LanguageCompilerSpecPair
    preferred: bool



    def __init__(self, loadSpec: ghidra.app.util.opinion.LoadSpec): ...



    @overload
    def compareTo(self, o: ghidra.plugins.importer.batch.BatchGroupLoadSpec) -> int: ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, obj: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def matches(self, loadSpec: ghidra.app.util.opinion.LoadSpec) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
