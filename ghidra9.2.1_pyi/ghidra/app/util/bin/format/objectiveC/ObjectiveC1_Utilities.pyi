from typing import List
import ghidra.app.util.bin
import ghidra.app.util.bin.format.objc2
import ghidra.app.util.bin.format.objectiveC
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.program.model.mem
import ghidra.program.model.symbol
import java.lang


class ObjectiveC1_Utilities(object):




    def __init__(self): ...



    @staticmethod
    def applyData(program: ghidra.program.model.listing.Program, dt: ghidra.program.model.data.DataType, address: ghidra.program.model.address.Address) -> None:
        """
        Applies the data type at the specified address.
        """
        ...

    @staticmethod
    def clear(state: ghidra.app.util.bin.format.objc2.ObjectiveC2_State, block: ghidra.program.model.mem.MemoryBlock) -> None:
        """
        Clears the code units defined in the given memory block.
        """
        ...

    @staticmethod
    def createInstanceVariablesC2_OBJC2(state: ghidra.app.util.bin.format.objc2.ObjectiveC2_State) -> None: ...

    @staticmethod
    def createMethods(state: ghidra.app.util.bin.format.objectiveC.ObjectiveC1_State) -> None: ...

    @staticmethod
    def createNamespace(program: ghidra.program.model.listing.Program, namespacePath: List[unicode]) -> ghidra.program.model.symbol.Namespace:
        """
        Creates a namespace hierarchy using the list of strings specified in namespacePath.
        """
        ...

    @staticmethod
    def createPointer(program: ghidra.program.model.listing.Program, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        Applies a pointer data type at the specified address and returns the newly created data object.
        """
        ...

    @staticmethod
    def createPointerAndReturnAddressBeingReferenced(program: ghidra.program.model.listing.Program, address: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address:
        """
        Applies a pointer data type at the specified address and returns the address being referenced.
        """
        ...

    @staticmethod
    def createString(program: ghidra.program.model.listing.Program, address: ghidra.program.model.address.Address) -> unicode:
        """
        Applies a string data type at the specified address and returns the string object.
        """
        ...

    @staticmethod
    def createSymbol(program: ghidra.program.model.listing.Program, parentNamespace: ghidra.program.model.symbol.Namespace, symbolName: unicode, symbolAddress: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.Symbol:
        """
        Creates a symbol.

         TODO - make symbols primary?
        """
        ...

    @staticmethod
    def dereferenceAsciiString(reader: ghidra.app.util.bin.BinaryReader, is32bit: bool) -> unicode:
        """
        Dereferences a string pointer and returns the string.
         If 32-bit only reads a 32-bit pointer.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def fixupReferences(state: ghidra.app.util.bin.format.objectiveC.ObjectiveC1_State) -> None:
        """
        This method will remove references to the NULL address
         and it will adjust THUMB references to no longer be offcut.
        """
        ...

    @overload
    @staticmethod
    def formatAsObjectiveC(function: ghidra.program.model.listing.Function, methodType: ghidra.app.util.bin.format.objectiveC.ObjectiveC_MethodType) -> unicode: ...

    @overload
    @staticmethod
    def formatAsObjectiveC(signature: ghidra.program.model.listing.FunctionSignature, methodType: ghidra.app.util.bin.format.objectiveC.ObjectiveC_MethodType, appendSemicolon: bool) -> unicode: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getClassNamespace(program: ghidra.program.model.listing.Program, parentNamespace: ghidra.program.model.symbol.Namespace, namespaceName: unicode) -> ghidra.program.model.symbol.Namespace:
        """
        Returns the class inside the given parent name space.
         If it does not exist, then create it and return it.
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isNull(address: ghidra.program.model.address.Address) -> bool:
        """
        Returns true if the given address is zero.
        """
        ...

    @overload
    @staticmethod
    def isThumb(program: ghidra.program.model.listing.Program, address: long) -> bool:
        """
        Returns true if the address is THUMB code.
        """
        ...

    @overload
    @staticmethod
    def isThumb(program: ghidra.program.model.listing.Program, address: ghidra.program.model.address.Address) -> bool:
        """
        Returns true if the address is THUMB code.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def readNextIndex(reader: ghidra.app.util.bin.BinaryReader, is32bit: bool) -> long:
        """
        Reads the next index value. If is32bit is true, then 4 bytes
         will be read to form index. Otherwise, 8 bytes will be read to form index.
        """
        ...

    @staticmethod
    def setThumbBit(state: ghidra.app.util.bin.format.objectiveC.ObjectiveC1_State, address: ghidra.program.model.address.Address) -> None:
        """
        If needed, sets the TMode bit at the specified address.
        """
        ...

    @staticmethod
    def toAddress(program: ghidra.program.model.listing.Program, offset: long) -> ghidra.program.model.address.Address:
        """
        Manufactures an address from the given long.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
