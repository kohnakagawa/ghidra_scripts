import ghidra.framework.options
import ghidra.program.model.listing
import ghidra.program.util
import ghidra.util.classfinder
import java.lang


class DiscoverableAddressCorrelator(ghidra.program.util.AddressCorrelator, ghidra.util.classfinder.ExtensionPoint, object):
    """
    AddressCorrelators that want to be discovered by version tracking should implement this interface.
    """









    @overload
    def correlate(self, __a0: ghidra.program.model.listing.Data, __a1: ghidra.program.model.listing.Data) -> ghidra.program.util.AddressCorrelation: ...

    @overload
    def correlate(self, __a0: ghidra.program.model.listing.Function, __a1: ghidra.program.model.listing.Function) -> ghidra.program.util.AddressCorrelation: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDefaultOptions(self) -> ghidra.framework.options.Options: ...

    def getOptions(self) -> ghidra.framework.options.ToolOptions: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setOptions(self, __a0: ghidra.framework.options.ToolOptions) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def defaultOptions(self) -> ghidra.framework.options.Options: ...

    @property
    def options(self) -> ghidra.framework.options.ToolOptions: ...

    @options.setter
    def options(self, value: ghidra.framework.options.ToolOptions) -> None: ...
