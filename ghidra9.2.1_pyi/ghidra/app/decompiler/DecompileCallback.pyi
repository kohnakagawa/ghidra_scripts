from typing import List
import ghidra.app.decompiler
import ghidra.app.decompiler.DecompileCallback
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.program.model.pcode
import java.lang


class DecompileCallback(object):
    """
    Routines that the decompiler invokes to gather info during decompilation of a
     function.
    """

    MAX_SYMBOL_COUNT: int = 16




    class StringData(object):
        byteData: List[int]



        def __init__(self): ...



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



    def __init__(self, prog: ghidra.program.model.listing.Program, language: ghidra.program.model.lang.Language, compilerSpec: ghidra.program.model.lang.CompilerSpec, dt: ghidra.program.model.pcode.PcodeDataTypeManager): ...



    @staticmethod
    def buildInstruction(ops: List[ghidra.program.model.pcode.PcodeOp], fallthruoffset: int, paramshift: int, addrFactory: ghidra.program.model.address.AddressFactory) -> unicode:
        """
        Build an XML representation of all the pcode op's a given Instruction is
         defined to perform.
        @param ops pcode ops
        @param fallthruoffset number of bytes after instruction start that pcode
                    flow falls into
        @param paramshift special instructions for injection use
        @param addrFactory is the address factory for recovering address space names
        @return XML document as string representing all the p-code
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getBytes(self, addrxml: unicode) -> List[int]: ...

    def getCPoolRef(self, refs: List[long]) -> unicode: ...

    def getClass(self) -> java.lang.Class: ...

    def getComments(self, addrstring: unicode, types: unicode) -> unicode:
        """
        Collect any/all comments for the function starting at the indicated
         address
        @param addrstring is the XML rep of function address
        @param types is the string encoding of the comment type flags
        @return XML document describing comments
        """
        ...

    def getExternalRefXML(self, addrstring: unicode) -> unicode: ...

    def getMappedSymbolsXML(self, addrstring: unicode) -> unicode:
        """
        Called by the native decompiler to query the GHIDRA database about any
         symbols at the given address.
        @param addrstring XML encoded address to query
        @return XML encoded result. Either function, reference, datatype, or hole
        """
        ...

    def getNamespacePath(self, id: long) -> unicode:
        """
        Return an XML description of the formal namespace path to the given namespace
        @param id is the ID of the given namespace
        @return a parent XML tag
        """
        ...

    def getNativeMessage(self) -> unicode:
        """
        @return the last message from the decompiler
        """
        ...

    def getPcodeInject(self, nm: unicode, context: unicode, type: int) -> unicode: ...

    def getPcodePacked(self, addrstring: unicode) -> ghidra.program.model.lang.PackedBytes: ...

    def getRegister(self, name: unicode) -> unicode: ...

    def getRegisterName(self, addrstring: unicode) -> unicode: ...

    def getStringData(self, addrString: unicode, dtName: unicode, dtId: unicode) -> ghidra.app.decompiler.DecompileCallback.StringData:
        """
        Check for a string at an address and return a UTF8 encoded byte array.
         If there is already data present at the address, use this to determine the
         string encoding. Otherwise use the data-type info passed in to determine the encoding.
         Check that the bytes at the address represent a valid string encoding that doesn't
         exceed the maximum character limit passed in.  Return null if the string is invalid.
         Return the string translated into a UTF8 byte array otherwise.  A (valid) empty
         string is returned as a zero length array.
        @param addrString is the XML encoded address and maximum byte limit
        @param dtName is the name of a character data-type
        @param dtId is the id associated with the character data-type
        @return the UTF8 encoded byte array or null
        """
        ...

    def getSymbol(self, addrstring: unicode) -> unicode: ...

    def getTrackedRegisters(self, addrstring: unicode) -> unicode: ...

    def getType(self, name: unicode, idstr: unicode) -> unicode: ...

    def getUserOpName(self, indexStr: unicode) -> unicode: ...

    def hashCode(self) -> int: ...

    def isNameUsed(self, name: unicode, startId: long, stopId: long) -> bool:
        """
        Decide if a given name is used by any namespace between a starting namespace
         and a stopping namespace.  I.e. check for a name collision along a specific namespace path.
         Currently, Ghidra is inefficient at calculating this perfectly, so this routine calculates
         an approximation that can occasionally indicate a collision when there isn't.
        @param name is the given name to check for collisions
        @param startId is the id specifying the starting namespace
        @param stopId is the id specifying the stopping namespace
        @return true if the name (likely) occurs in one of the namespaces on the path
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def readXMLNameList(self, xml: unicode) -> List[unicode]: ...

    def readXMLSize(self, addrxml: unicode) -> int: ...

    def setFunction(self, func: ghidra.program.model.listing.Function, entry: ghidra.program.model.address.Address, dbg: ghidra.app.decompiler.DecompileDebug) -> None:
        """
        Establish function and debug context for next decompilation
        @param func is the function to be decompiled
        @param entry is the function's entry address
        @param dbg is the debugging context (or null)
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
    def nativeMessage(self) -> unicode: ...
