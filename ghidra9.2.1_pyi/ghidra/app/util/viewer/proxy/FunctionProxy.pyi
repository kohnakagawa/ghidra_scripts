import ghidra.app.util.viewer.listingpanel
import ghidra.app.util.viewer.proxy
import ghidra.program.model.address
import ghidra.program.model.listing
import java.lang


class FunctionProxy(ghidra.app.util.viewer.proxy.ProxyObj):
    """
    Stores information about a function in a program such that the function can
     be retrieved when needed.  The locationAddr and functionAddr may differ when the
     function object has been inferred via a reference at the locationAddr.
    """





    def __init__(self, model: ghidra.app.util.viewer.listingpanel.ListingModel, program: ghidra.program.model.listing.Program, locationAddr: ghidra.program.model.address.Address, function: ghidra.program.model.listing.Function):
        """
        Construct a proxy for a function
        @param model listing model
        @param program the program containing the function
        @param locationAddr the listing address at which the function exists or was inferred via reference
        @param function the function to proxy
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFunctionAddress(self) -> ghidra.program.model.address.Address: ...

    def getListingLayoutModel(self) -> ghidra.app.util.viewer.listingpanel.ListingModel:
        """
        Returns the layout model which corresponds to this field proxy.
        """
        ...

    def getLocationAddress(self) -> ghidra.program.model.address.Address: ...

    def getObject(self) -> ghidra.program.model.listing.Function:
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
    def functionAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def locationAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def object(self) -> ghidra.program.model.listing.Function: ...
