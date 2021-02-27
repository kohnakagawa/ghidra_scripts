import ghidra.framework.cmd
import ghidra.framework.model
import ghidra.program.model.symbol
import java.lang


class CreateExternalFunctionCmd(object, ghidra.framework.cmd.Command):




    @overload
    def __init__(self, extSymbol: ghidra.program.model.symbol.Symbol):
        """
        Create an external function
        @param extSymbol a non-function external symbol
        """
        ...

    @overload
    def __init__(self, libraryName: unicode, name: unicode, address: ghidra.program.model.address.Address, source: ghidra.program.model.symbol.SourceType):
        """
        Create an external function
        @param libraryName library name, if null the UNKNOWN library will be used
        @param name function name (required)
        @param address the address of the function's entry point in the external library (optional)
        """
        ...

    @overload
    def __init__(self, externalParentNamespace: ghidra.program.model.symbol.Namespace, name: unicode, address: ghidra.program.model.address.Address, source: ghidra.program.model.symbol.SourceType):
        """
        Create an external function in the specified external namespace.
        @param externalParentNamespace the external parent namespace where the named function should be created (required)
        @param name function name (required)
        @param address the address of the function's entry point in the external library (optional)
        @param source the source type for this external function
        """
        ...



    def applyTo(self, obj: ghidra.framework.model.DomainObject) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getExtSymbol(self) -> ghidra.program.model.symbol.Symbol: ...

    def getName(self) -> unicode: ...

    def getStatusMsg(self) -> unicode: ...

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
    def extSymbol(self) -> ghidra.program.model.symbol.Symbol: ...

    @property
    def name(self) -> unicode: ...

    @property
    def statusMsg(self) -> unicode: ...
