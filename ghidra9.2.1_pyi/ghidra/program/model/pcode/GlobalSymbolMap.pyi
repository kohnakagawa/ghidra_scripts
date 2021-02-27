from typing import Iterator
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.pcode
import java.lang


class GlobalSymbolMap(object):
    """
    A container for global symbols in the decompiler's model of a function. It contains
     HighSymbol objects for any symbol accessed by the particular function that is in either
     the global scope or some other global namespace. Currently the container is populated
     indirectly from the HighGlobal objects marshaled back from the decompiler, using either
     the populateSymbol() or newSymbol() methods. HighSymbols are stored by Address and by id,
     which matches the formal SymbolDB id when it exists.
    """





    def __init__(self, f: ghidra.program.model.pcode.HighFunction):
        """
        Construct a global symbol map attached to a particular function model.
        @param f is the decompiler function model
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def getSymbol(self, id: long) -> ghidra.program.model.pcode.HighSymbol:
        """
        Retrieve a HighSymbol based on an id
        @param id is the id
        @return the matching HighSymbol or null
        """
        ...

    @overload
    def getSymbol(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.pcode.HighSymbol:
        """
        Retrieve a HighSymbol based on an Address
        @param addr is the given Address
        @return the matching HighSymbol or null
        """
        ...

    def getSymbols(self) -> Iterator[ghidra.program.model.pcode.HighSymbol]:
        """
        Get an iterator over all HighSymbols in this container
        @return the iterator
        """
        ...

    def hashCode(self) -> int: ...

    def newSymbol(self, id: long, addr: ghidra.program.model.address.Address, dataType: ghidra.program.model.data.DataType, sz: int) -> ghidra.program.model.pcode.HighCodeSymbol:
        """
        Create a HighSymbol corresponding to an underlying Data object. The name of the symbol is
         generated dynamically. A symbol is always returned unless the address is invalid,
         in which case null is returned.
        @param id is the id to associate with the new symbol
        @param addr is the address of the Data object
        @param dataType is the recovered data-type of the symbol
        @param sz is the size in bytes of the symbol
        @return the new HighSymbol or null
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def populateSymbol(self, id: long, dataType: ghidra.program.model.data.DataType, sz: int) -> ghidra.program.model.pcode.HighSymbol:
        """
        Create a HighSymbol based on the id of the underlying Ghidra Symbol. The Symbol
         is looked up in the SymbolTable and then a HighSymbol is created with the name and
         dataType associated with the Symbol. If a Symbol cannot be found, null is returned.
        @param id is the database id of the CodeSymbol
        @param dataType is the recovered data-type of the symbol
        @param sz is the size in bytes of the desired symbol
        @return the CodeSymbol wrapped as a HighSymbol or null
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
    def symbols(self) -> java.util.Iterator: ...
