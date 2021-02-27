import ghidra.app.util.importer
import ghidra.app.util.opinion
import java.lang


class CsHintLoadSpecChooser(object, ghidra.app.util.importer.LoadSpecChooser):
    """
    Chooses a LoadSpec for a Loader to use based on a provided CompilerSpec.
    """

    CHOOSE_THE_FIRST_PREFERRED: ghidra.app.util.importer.LoadSpecChooser = ghidra.app.util.importer.LoadSpecChooser$$Lambda$1115/0x00000008014c6c40@546bee62



    @overload
    def __init__(self, compilerSpecID: unicode):
        """
        Creates a new {@link CsHintLoadSpecChooser}
        @param compilerSpecID The {@link CompilerSpecID} to use (should not be null)
        """
        ...

    @overload
    def __init__(self, compilerSpecID: ghidra.program.model.lang.CompilerSpecID):
        """
        Creates a new {@link CsHintLoadSpecChooser}
        @param compilerSpecID The {@link CompilerSpecID} to use (should not be null)
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
