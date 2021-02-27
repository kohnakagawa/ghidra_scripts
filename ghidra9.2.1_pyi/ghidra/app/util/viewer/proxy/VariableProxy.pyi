import ghidra.app.util.viewer.listingpanel
import ghidra.app.util.viewer.proxy
import ghidra.program.model.address
import ghidra.program.model.listing
import java.lang


class VariableProxy(ghidra.app.util.viewer.proxy.ProxyObj):
    """
    Stores information about a variable in a program such that the variable can
     be retrieved when needed.
    """





    def __init__(self, model: ghidra.app.util.viewer.listingpanel.ListingModel, program: ghidra.program.model.listing.Program, locationAddr: ghidra.program.model.address.Address, fun: ghidra.program.model.listing.Function, var: ghidra.program.model.listing.Variable):
        """
        Constructs a proxy for a variable.
        @param model listing model
        @param program the program containing the variable.
        @param locationAddr the listing address at which the function exists or was inferred via reference
        @param fun the function containing the variable.
        @param var the variable to proxy.
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

    def getObject(self) -> ghidra.program.model.listing.Variable:
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
    def object(self) -> ghidra.program.model.listing.Variable: ...
