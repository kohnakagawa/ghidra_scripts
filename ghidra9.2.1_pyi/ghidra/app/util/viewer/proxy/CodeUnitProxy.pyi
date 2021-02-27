import ghidra.app.util.viewer.listingpanel
import ghidra.app.util.viewer.proxy
import ghidra.program.model.listing
import java.lang


class CodeUnitProxy(ghidra.app.util.viewer.proxy.ProxyObj):
    """
    Stores information about a code unti in a program such that the code unit can
     be retrieved when needed.
    """





    def __init__(self, model: ghidra.app.util.viewer.listingpanel.ListingModel, program: ghidra.program.model.listing.Program, cu: ghidra.program.model.listing.CodeUnit):
        """
        Construct a proxy for a code unit
        @param program the program containing the code unit
        @param cu the code unit to proxy.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getListingLayoutModel(self) -> ghidra.app.util.viewer.listingpanel.ListingModel:
        """
        Returns the layout model which corresponds to this field proxy.
        """
        ...

    def getObject(self) -> ghidra.program.model.listing.CodeUnit:
        """
        @see ghidra.app.util.viewer.proxy.ProxyObj#getObject()
        """
        ...

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
    def object(self) -> ghidra.program.model.listing.CodeUnit: ...
