import ghidra.app.util.opinion
import java.lang


class LoadSpecChooser(object):
    """
    Chooses a LoadSpec for a Loader to use based on some criteria
    """

    CHOOSE_THE_FIRST_PREFERRED: ghidra.app.util.importer.LoadSpecChooser = ghidra.app.util.importer.LoadSpecChooser$$Lambda$1115/0x00000008014c6c40@546bee62







    def choose(self, loaderMap: ghidra.app.util.opinion.LoaderMap) -> ghidra.app.util.opinion.LoadSpec:
        """
        Chooses a {@link LoadSpec} for a {@link Loader} to use based on some criteria
        @param loaderMap A {@link LoaderMap}
        @return The chosen {@link LoadSpec}, or null if one could not be found
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
