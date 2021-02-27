from typing import Iterator
from typing import List
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.program.model.pcode
import ghidra.program.model.symbol
import ghidra.xml
import java.io
import java.lang
import java.util
import org.xml.sax


class HighFunction(ghidra.program.model.pcode.PcodeSyntaxTree):
    """
    High-level abstraction associated with a low level function made up of assembly instructions.
     Based on information the decompiler has produced after working on a function.
    """

    DECOMPILER_TAG_MAP: unicode = u'decompiler_tags'



    def __init__(self, function: ghidra.program.model.listing.Function, language: ghidra.program.model.lang.Language, compilerSpec: ghidra.program.model.lang.CompilerSpec, dtManager: ghidra.program.model.pcode.PcodeDataTypeManager):
        """
        @param function function associated with the higher level function abstraction.
        @param language description of the processor language of the function
        @param compilerSpec description of the compiler that produced the function
        @param dtManager data type manager
        """
        ...



    def buildFunctionXML(self, id: long, namespace: ghidra.program.model.symbol.Namespace, entryPoint: ghidra.program.model.address.Address, size: int) -> unicode:
        """
        Build an XML string that represents all the information about this HighFunction. The
         size describes how many bytes starting from the entry point are used by the function, but
         this doesn't need to be strictly accurate as it is only used to associate the function with
         addresses near its entry point.
        @param id is the id associated with the function symbol
        @param namespace is the namespace containing the function symbol
        @param entryPoint pass null to use the function entryPoint, pass an address to force an entry point
        @param size describes how many bytes the function occupies as code
        @return the XML string
        """
        ...

    def buildStorage(self, vn: ghidra.program.model.pcode.Varnode) -> ghidra.program.model.listing.VariableStorage: ...

    def clear(self) -> None: ...

    @staticmethod
    def clearNamespace(symtab: ghidra.program.model.symbol.SymbolTable, space: ghidra.program.model.symbol.Namespace) -> bool: ...

    @staticmethod
    def collapseToGlobal(namespace: ghidra.program.model.symbol.Namespace) -> bool:
        """
        The decompiler treats some namespaces as equivalent to the "global" namespace.
         Return true if the given namespace is treated as equivalent.
        @param namespace is the namespace
        @return true if equivalent
        """
        ...

    def createFromStorage(self, addr: ghidra.program.model.address.Address, storage: ghidra.program.model.listing.VariableStorage, logicalSize: int) -> ghidra.program.model.pcode.Varnode: ...

    @staticmethod
    def createLabelSymbol(symtab: ghidra.program.model.symbol.SymbolTable, addr: ghidra.program.model.address.Address, name: unicode, namespace: ghidra.program.model.symbol.Namespace, source: ghidra.program.model.symbol.SourceType, useLocalNamespace: bool) -> None: ...

    @staticmethod
    def createNamespaceTag(buf: java.lang.StringBuilder, namespace: ghidra.program.model.symbol.Namespace) -> None:
        """
        Append an XML &lt;parent&gt; tag to the buffer describing the formal path elements
         from the root (global) namespace up to the given namespace
        @param buf is the buffer to write to
        @param namespace is the namespace being described
        """
        ...

    def delete(self, op: ghidra.program.model.pcode.PcodeOp) -> None: ...

    @staticmethod
    def deleteSymbol(symtab: ghidra.program.model.symbol.SymbolTable, addr: ghidra.program.model.address.Address, name: unicode, space: ghidra.program.model.symbol.Namespace) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def findCreateNamespace(symtab: ghidra.program.model.symbol.SymbolTable, parentspace: ghidra.program.model.symbol.Namespace, name: unicode) -> ghidra.program.model.symbol.Namespace: ...

    @staticmethod
    def findCreateOverrideSpace(func: ghidra.program.model.listing.Function) -> ghidra.program.model.symbol.Namespace: ...

    def findInputVarnode(self, sz: int, addr: ghidra.program.model.address.Address) -> ghidra.program.model.pcode.Varnode:
        """
        return Varnode of given size and starting Address, which is also an input
        @param sz -- size of Varnode
        @param addr -- starting Address of Varnode
        @return -- the Varnode
        """
        ...

    @staticmethod
    def findNamespace(symtab: ghidra.program.model.symbol.SymbolTable, parent: ghidra.program.model.symbol.Namespace, name: unicode) -> ghidra.program.model.symbol.Namespace: ...

    @staticmethod
    def findOverrideSpace(func: ghidra.program.model.listing.Function) -> ghidra.program.model.symbol.Namespace: ...

    @overload
    def findVarnode(self, sz: int, addr: ghidra.program.model.address.Address, pc: ghidra.program.model.address.Address) -> ghidra.program.model.pcode.Varnode:
        """
        return first instance of a Varnode with given size, starting Address,
         and bound to an instruction at the given Address
        @param sz -- size of Varnode
        @param addr -- starting Address of Varnode
        @param pc -- Address of instruction writing to Varnode
        @return -- the Varnode
        """
        ...

    @overload
    def findVarnode(self, sz: int, addr: ghidra.program.model.address.Address, sq: ghidra.program.model.pcode.SequenceNumber) -> ghidra.program.model.pcode.Varnode:
        """
        return Varnode of given size and starting Address defined by a PcodeOp
         with a given SequenceNumber
        @param sz -- size of Varnode
        @param addr -- starting Address of Varnode
        @param sq -- SequenceNumber of PcodeOp defining the Varnode
        @return -- the Varnode
        """
        ...

    def getAddressFactory(self) -> ghidra.program.model.address.AddressFactory: ...

    def getBasicBlocks(self) -> List[ghidra.program.model.pcode.PcodeBlockBasic]: ...

    def getClass(self) -> java.lang.Class: ...

    def getCompilerSpec(self) -> ghidra.program.model.lang.CompilerSpec: ...

    def getDataTypeManager(self) -> ghidra.program.model.pcode.PcodeDataTypeManager: ...

    @staticmethod
    def getErrorHandler(errOriginator: object, targetName: unicode) -> org.xml.sax.ErrorHandler: ...

    def getFunction(self) -> ghidra.program.model.listing.Function:
        """
        @return get the associated low level function
        """
        ...

    def getFunctionPrototype(self) -> ghidra.program.model.pcode.FunctionPrototype:
        """
        @return the function prototype for the function (how things are passed/returned)
        """
        ...

    def getGlobalSymbolMap(self) -> ghidra.program.model.pcode.GlobalSymbolMap:
        """
        @return a map describing global variables accessed by this function
        """
        ...

    def getID(self) -> long:
        """
        Get the id with the associated function symbol, if it exists.
         Otherwise return a dynamic id based on the entry point.
        @return the symbol id, or possibly a dynamic id
        """
        ...

    def getJumpTables(self) -> List[ghidra.program.model.pcode.JumpTable]:
        """
        @return an array of jump table definitions found for this function decompilation
        """
        ...

    def getLanguage(self) -> ghidra.program.model.lang.Language:
        """
        @return get the language parser used to disassemble
        """
        ...

    def getLocalSymbolMap(self) -> ghidra.program.model.pcode.LocalSymbolMap:
        """
        @return the local variable map describing the defined local variables
        """
        ...

    def getMappedSymbol(self, addr: ghidra.program.model.address.Address, pcaddr: ghidra.program.model.address.Address) -> ghidra.program.model.pcode.HighSymbol: ...

    def getNumVarnodes(self) -> int: ...

    def getOpRef(self, id: int) -> ghidra.program.model.pcode.PcodeOp: ...

    def getPcodeOp(self, sq: ghidra.program.model.pcode.SequenceNumber) -> ghidra.program.model.pcode.PcodeOp: ...

    @overload
    def getPcodeOps(self) -> Iterator[ghidra.program.model.pcode.PcodeOpAST]:
        """
        return all PcodeOps (alive or dead) ordered by SequenceNumber
        @return -- Iterator to PcodeOps
        """
        ...

    @overload
    def getPcodeOps(self, addr: ghidra.program.model.address.Address) -> Iterator[ghidra.program.model.pcode.PcodeOpAST]:
        """
        return all PcodeOps associated with a particular instruction Address
        @param addr -- Address of instruction generating PcodeOps
        @return -- Iterator to PcodeOps
        """
        ...

    def getRef(self, id: int) -> ghidra.program.model.pcode.Varnode: ...

    def getSymbol(self, symbolId: long) -> ghidra.program.model.pcode.HighSymbol: ...

    @overload
    def getVarnodes(self, addr: ghidra.program.model.address.Address) -> Iterator[ghidra.program.model.pcode.VarnodeAST]:
        """
        return all Varnodes that start at a given Address
        @param addr -- Address of Varnodes
        @return -- Iterator to Varnodes
        """
        ...

    @overload
    def getVarnodes(self, spc: ghidra.program.model.address.AddressSpace) -> Iterator[ghidra.program.model.pcode.VarnodeAST]:
        """
        return Iterator to all Varnodes in the indicated AddressSpace
        @param spc -- AddressSpace to restrict Iterator to
        @return -- Iterator to Varnodes
        """
        ...

    @overload
    def getVarnodes(self, sz: int, addr: ghidra.program.model.address.Address) -> Iterator[ghidra.program.model.pcode.VarnodeAST]:
        """
        return all Varnodes of a given size that start at a given Address
        @param sz -- Size of Varnodes
        @param addr -- Starting Address of Varnodes
        @return -- Iterator to Varnodes
        """
        ...

    def getVbank(self) -> ghidra.program.model.pcode.VarnodeBank:
        """
        @deprecated
        @return the varnode bank for this syntax tree
        """
        ...

    def grabFromFunction(self, overrideExtrapop: int, includeDefaultNames: bool, doOverride: bool) -> None:
        """
        Populate the information for the HighFunction from the information in the
         Function object.
        @param overrideExtrapop is the value to use if extrapop is overridden
        @param includeDefaultNames is true if default symbol names should be considered locked
        @param doOverride is true if extrapop is overridden
        """
        ...

    def hashCode(self) -> int: ...

    def insertAfter(self, newop: ghidra.program.model.pcode.PcodeOp, prev: ghidra.program.model.pcode.PcodeOp) -> None: ...

    def insertBefore(self, newop: ghidra.program.model.pcode.PcodeOp, follow: ghidra.program.model.pcode.PcodeOp) -> None: ...

    def locRange(self) -> Iterator[ghidra.program.model.pcode.VarnodeAST]:
        """
        Returns an iterator for all Varnodes in the tree ordered by Address
        """
        ...

    def newOp(self, __a0: ghidra.program.model.pcode.SequenceNumber, __a1: int, __a2: java.util.ArrayList, __a3: ghidra.program.model.pcode.Varnode) -> ghidra.program.model.pcode.PcodeOp: ...

    @overload
    def newVarnode(self, sz: int, addr: ghidra.program.model.address.Address) -> ghidra.program.model.pcode.Varnode: ...

    @overload
    def newVarnode(self, sz: int, addr: ghidra.program.model.address.Address, id: int) -> ghidra.program.model.pcode.Varnode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def readXML(self, parser: ghidra.xml.XmlPullParser) -> None: ...

    def readXMLVarnodePieces(self, el: ghidra.xml.XmlElement, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.VariableStorage:
        """
        Read an XML join address with "piece" attributes
        @param el SAX parse tree element
        @param addr join address associated with pieces
        @return the VariableStorage associated with xml
        @throws PcodeXMLException
        @throws InvalidInputException
        """
        ...

    def setAddrTied(self, vn: ghidra.program.model.pcode.Varnode, val: bool) -> None: ...

    def setDataType(self, vn: ghidra.program.model.pcode.Varnode, type: ghidra.program.model.data.DataType) -> None: ...

    @overload
    def setInput(self, vn: ghidra.program.model.pcode.Varnode, val: bool) -> ghidra.program.model.pcode.Varnode: ...

    @overload
    def setInput(self, op: ghidra.program.model.pcode.PcodeOp, vn: ghidra.program.model.pcode.Varnode, slot: int) -> None: ...

    def setMergeGroup(self, vn: ghidra.program.model.pcode.Varnode, val: int) -> None: ...

    def setOpcode(self, op: ghidra.program.model.pcode.PcodeOp, opc: int) -> None: ...

    def setOutput(self, op: ghidra.program.model.pcode.PcodeOp, vn: ghidra.program.model.pcode.Varnode) -> None: ...

    def setPersistant(self, vn: ghidra.program.model.pcode.Varnode, val: bool) -> None: ...

    def setUnaffected(self, vn: ghidra.program.model.pcode.Varnode, val: bool) -> None: ...

    def splitOutMergeGroup(self, high: ghidra.program.model.pcode.HighVariable, vn: ghidra.program.model.pcode.Varnode) -> ghidra.program.model.pcode.HighVariable:
        """
        If a HighVariable consists of more than one (forced) merge group, split out the group
         that contains vn as a separate HighVariable. Otherwise just return the original high.
        @param high is the HighVariable to split
        @param vn is a representative of the merge group to split out
        @return a HighVariable containing just the forced merge group of vn
        @throws PcodeException if the split can't be performed
        """
        ...

    @staticmethod
    def stringTree(xml: java.io.InputStream, handler: org.xml.sax.ErrorHandler) -> ghidra.xml.XmlPullParser:
        """
        Create XML parse tree from an input XML string

         TODO: this probably doesn't belong here.
        @param xml is the XML string to parse
        @param handler is the handler to use for parsing errors
        @return the XML tree
        @throws PcodeXMLException for format errors in the XML
        """
        ...

    @staticmethod
    def tagFindExclude(tagname: unicode, doc: unicode) -> unicode:
        """
        @param tagname -- Name of tag to search for
        @param doc -- String through which to search for tags
        @return all characters between beginning and ending XML tags, excluding tags themselves
        """
        ...

    def toString(self) -> unicode: ...

    def unInsert(self, op: ghidra.program.model.pcode.PcodeOp) -> None: ...

    def unSetInput(self, op: ghidra.program.model.pcode.PcodeOp, slot: int) -> None: ...

    def unSetOutput(self, op: ghidra.program.model.pcode.PcodeOp) -> None: ...

    def unlink(self, op: ghidra.program.model.pcode.PcodeOpAST) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def ID(self) -> long: ...

    @property
    def compilerSpec(self) -> ghidra.program.model.lang.CompilerSpec: ...

    @property
    def function(self) -> ghidra.program.model.listing.Function: ...

    @property
    def functionPrototype(self) -> ghidra.program.model.pcode.FunctionPrototype: ...

    @property
    def globalSymbolMap(self) -> ghidra.program.model.pcode.GlobalSymbolMap: ...

    @property
    def jumpTables(self) -> List[ghidra.program.model.pcode.JumpTable]: ...

    @property
    def language(self) -> ghidra.program.model.lang.Language: ...

    @property
    def localSymbolMap(self) -> ghidra.program.model.pcode.LocalSymbolMap: ...
