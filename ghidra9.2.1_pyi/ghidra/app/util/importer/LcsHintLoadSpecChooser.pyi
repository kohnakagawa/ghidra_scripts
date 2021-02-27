import ghidra.app.util.importer
import ghidra.app.util.opinion
import java.lang


class LcsHintLoadSpecChooser(object, ghidra.app.util.importer.LoadSpecChooser):
    """
    Chooses a LoadSpec for a Loader to use based on a provided Language and
     CompilerSpec.
    """

    CHOOSE_THE_FIRST_PREFERRED: ghidra.app.util.importer.LoadSpecChooser = ghidra.app.util.importer.LoadSpecChooser$$Lambda$1115/0x00000008014c6c40@546bee62



    def __init__(self, language: ghidra.program.model.lang.Language, compilerSpec: ghidra.program.model.lang.CompilerSpec):
        """
        Creates a new {@link LcsHintLoadSpecChooser}.
         <p>
         NOTE: It is assumed that the given {@link Language} is valid and it supports the given
         {@link CompilerSpec}.
        @param language The {@link Language} to use (should not be null)
        @param compilerSpec The {@link CompilerSpec} to use (f null default compiler spec will be used)
        """
        ...



    def choose(self, loaderMap: ghidra.app.util.opinion.LoaderMap) -> ghidra.app.util.opinion.LoadSpec: ...

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
