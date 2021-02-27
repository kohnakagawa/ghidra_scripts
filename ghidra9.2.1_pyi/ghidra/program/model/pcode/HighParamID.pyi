from typing import Iterator
from typing import List
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.program.model.pcode
import ghidra.program.model.symbol
import ghidra.xml
import java.lang
import java.util
import org.xml.sax


class HighParamID(ghidra.program.model.pcode.PcodeSyntaxTree):
    """
    High-level abstraction associated with a low level function made up of assembly instructions.
     Based on information the decompiler has produced after working on a function.
    """

    DECOMPILER_TAG_MAP: unicode = u'decompiler_tags'



    def __init__(self, function: ghidra.program.model.listing.Function, language: ghidra.program.model.lang.Language, compilerSpec: ghidra.program.model.lang.CompilerSpec, dtManager: ghidra.program.model.pcode.PcodeDataTypeManager):
        """
        @param function function associated with the higher level function abstraction.
        @param language language parser used to disassemble/get info on the language.
        @param compilerSpec the compiler spec.
        @param dtManager data type manager.
        """
        ...



    def buildStorage(self, vn: ghidra.program.model.pcode.Varnode) -> ghidra.program.model.listing.VariableStorage: ...

    def clear(self) -> None: ...

    def createFromStorage(self, addr: ghidra.program.model.address.Address, storage: ghidra.program.model.listing.VariableStorage, logicalSize: int) -> ghidra.program.model.pcode.Varnode: ...

    def delete(self, op: ghidra.program.model.pcode.PcodeOp) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def findInputVarnode(self, sz: int, addr: ghidra.program.model.address.Address) -> ghidra.program.model.pcode.Varnode:
        """
        return Varnode of given size and starting Address, which is also an input
        @param sz -- size of Varnode
        @param addr -- starting Address of Varnode
        @return -- the Varnode
        """
        ...

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

    def getDataTypeManager(self) -> ghidra.program.model.pcode.PcodeDataTypeManager: ...

    @staticmethod
    def getErrorHandler(errOriginator: object, targetName: unicode) -> org.xml.sax.ErrorHandler: ...

    def getFunction(self) -> ghidra.program.model.listing.Function:
        """
        @return get the associated low level function
        """
        ...

    def getFunctionAddress(self) -> ghidra.program.model.address.Address:
        """
        @return get the Address of the function
        """
        ...

    def getFunctionName(self) -> unicode:
        """
        @return get the name of the function
        """
        ...

    def getInput(self, i: int) -> ghidra.program.model.pcode.ParamMeasure:
        """
        @return the specific of input for functionparams
        """
        ...

    def getModelName(self) -> unicode:
        """
        @return get the name of the model
        """
        ...

    def getNumInputs(self) -> int:
        """
        @return the number of inputs for functionparams
        """
        ...

    def getNumOutputs(self) -> int:
        """
        @return the number of outputs for functionparams
        """
        ...

    def getNumVarnodes(self) -> int: ...

    def getOpRef(self, id: int) -> ghidra.program.model.pcode.PcodeOp: ...

    def getOutput(self, i: int) -> ghidra.program.model.pcode.ParamMeasure:
        """
        @return the specific of output for functionparams
        """
        ...

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

    def getProtoExtraPop(self) -> int:
        """
        @return get the prototype extrapop information
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

    def storeParametersToDatabase(self, storeDataTypes: bool, srctype: ghidra.program.model.symbol.SourceType) -> None:
        """
        Update any parameters for this Function from parameters defined in this map.
           Originally from LocalSymbolMap, but being modified.
        @param srctype function signature source
        """
        ...

    def storeReturnToDatabase(self, storeDataTypes: bool, srctype: ghidra.program.model.symbol.SourceType) -> None:
        """
        Update any parameters for this Function from parameters defined in this map.
        @param srctype function signature source
        """
        ...

    @staticmethod
    def stringTree(xml: unicode, handler: org.xml.sax.ErrorHandler) -> ghidra.xml.XmlPullParser:
        """
        Create and XML SAX parse tree from an input XML string

         TODO: this probably doesn't belong here.
        @param xml string to parse
        @return an XML tree element
        @throws PcodeXMLException
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
    def function(self) -> ghidra.program.model.listing.Function: ...

    @property
    def functionAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def functionName(self) -> unicode: ...

    @property
    def modelName(self) -> unicode: ...

    @property
    def numInputs(self) -> int: ...

    @property
    def numOutputs(self) -> int: ...

    @property
    def protoExtraPop(self) -> int: ...
