from typing import Iterator
from typing import List
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.program.model.pcode
import ghidra.xml
import java.lang
import java.util


class PcodeSyntaxTree(object, ghidra.program.model.pcode.PcodeFactory):
    """
    Varnodes and PcodeOps in a coherent graph structure
    """





    def __init__(self, afact: ghidra.program.model.address.AddressFactory, dtmanage: ghidra.program.model.pcode.PcodeDataTypeManager): ...



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
    def addressFactory(self) -> ghidra.program.model.address.AddressFactory: ...

    @property
    def basicBlocks(self) -> java.util.ArrayList: ...

    @property
    def dataTypeManager(self) -> ghidra.program.model.pcode.PcodeDataTypeManager: ...

    @property
    def numVarnodes(self) -> int: ...

    @property
    def pcodeOps(self) -> java.util.Iterator: ...

    @property
    def vbank(self) -> ghidra.program.model.pcode.VarnodeBank: ...
