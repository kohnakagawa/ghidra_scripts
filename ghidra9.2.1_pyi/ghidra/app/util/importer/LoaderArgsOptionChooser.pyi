from typing import List
import ghidra.app.util.importer
import ghidra.program.model.address
import java.lang


class LoaderArgsOptionChooser(object, ghidra.app.util.importer.OptionChooser):
    """
    An option chooser that applies loader options that were passed in as command line arguments.
    """

    DEFAULT_OPTIONS: ghidra.app.util.importer.OptionChooser = ghidra.app.util.importer.OptionChooser$$Lambda$1109/0x00000008013af440@3a67a678



    def __init__(self, loaderFilter: ghidra.app.util.importer.SingleLoaderFilter): ...



    def choose(self, __a0: List[object], __a1: ghidra.program.model.address.AddressFactory) -> List[object]: ...

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
