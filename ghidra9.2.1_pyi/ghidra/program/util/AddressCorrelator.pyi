import ghidra.framework.options
import ghidra.program.model.listing
import ghidra.program.util
import java.lang


class AddressCorrelator(object):
    """
    Interface for address correlation algorithms that can generate an address mapping from one
     set of program addresses to another.
    """









    @overload
    def correlate(self, sourceData: ghidra.program.model.listing.Data, destinationData: ghidra.program.model.listing.Data) -> ghidra.program.util.AddressCorrelation:
        """
        Returns an address mapping from one piece of data to another.
        @param sourceData the source data.
        @param destinationData the destination data.
        @return an AddressCorrelation that represents a mapping of the addresses from the
         source data to the destination data.
        """
        ...

    @overload
    def correlate(self, sourceFunction: ghidra.program.model.listing.Function, destinationFunction: ghidra.program.model.listing.Function) -> ghidra.program.util.AddressCorrelation:
        """
        Returns an address mapping from one function to another.
        @param sourceFunction the source function.
        @param destinationFunction the destination function.
        @return an AddressCorrelation that represents a mapping of the addresses from the
         source function to the destination function.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDefaultOptions(self) -> ghidra.framework.options.Options:
        """
        Returns the options with the default settings for this correlator.
        @return the options with the default settings for this correlator.
        """
        ...

    def getOptions(self) -> ghidra.framework.options.ToolOptions:
        """
        Returns the current Option settings for this correlator.
        @return the current Option settings for this correlator.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setOptions(self, options: ghidra.framework.options.ToolOptions) -> None:
        """
        Sets the options to use for this correlator.
        @param options the options to use for this correlator.
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
    def defaultOptions(self) -> ghidra.framework.options.Options: ...

    @property
    def options(self) -> ghidra.framework.options.ToolOptions: ...

    @options.setter
    def options(self, value: ghidra.framework.options.ToolOptions) -> None: ...
