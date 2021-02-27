import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.program.model.pcode
import ghidra.xml
import java.lang
import java.util


class PcodeFactory(object):
    """
    Interface for classes that build PcodeOps and Varnodes
    """









    def buildStorage(self, vn: ghidra.program.model.pcode.Varnode) -> ghidra.program.model.listing.VariableStorage: ...

    def createFromStorage(self, addr: ghidra.program.model.address.Address, storage: ghidra.program.model.listing.VariableStorage, logicalSize: int) -> ghidra.program.model.pcode.Varnode: ...

    def equals(self, __a0: object) -> bool: ...

    def getAddressFactory(self) -> ghidra.program.model.address.AddressFactory:
        """
        @return Address factory
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDataTypeManager(self) -> ghidra.program.model.pcode.PcodeDataTypeManager:
        """
        @return pcode data type manager used to convert strings to Ghidra data types
        """
        ...

    def getOpRef(self, refid: int) -> ghidra.program.model.pcode.PcodeOp: ...

    def getRef(self, refid: int) -> ghidra.program.model.pcode.Varnode: ...

    def getSymbol(self, symbolId: long) -> ghidra.program.model.pcode.HighSymbol: ...

    def hashCode(self) -> int: ...

    def newOp(self, __a0: ghidra.program.model.pcode.SequenceNumber, __a1: int, __a2: java.util.ArrayList, __a3: ghidra.program.model.pcode.Varnode) -> ghidra.program.model.pcode.PcodeOp: ...

    @overload
    def newVarnode(self, sz: int, addr: ghidra.program.model.address.Address) -> ghidra.program.model.pcode.Varnode:
        """
        Create a new Varnode with the given size an location
        @param sz size of varnode
        @param addr location of varnode
        @return a new varnode
        """
        ...

    @overload
    def newVarnode(self, sz: int, addr: ghidra.program.model.address.Address, refId: int) -> ghidra.program.model.pcode.Varnode: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def readXMLVarnodePieces(self, el: ghidra.xml.XmlElement, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.VariableStorage: ...

    def setAddrTied(self, vn: ghidra.program.model.pcode.Varnode, val: bool) -> None: ...

    def setDataType(self, vn: ghidra.program.model.pcode.Varnode, type: ghidra.program.model.data.DataType) -> None: ...

    def setInput(self, vn: ghidra.program.model.pcode.Varnode, val: bool) -> ghidra.program.model.pcode.Varnode: ...

    def setMergeGroup(self, vn: ghidra.program.model.pcode.Varnode, val: int) -> None: ...

    def setPersistant(self, vn: ghidra.program.model.pcode.Varnode, val: bool) -> None: ...

    def setUnaffected(self, vn: ghidra.program.model.pcode.Varnode, val: bool) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def addressFactory(self) -> ghidra.program.model.address.AddressFactory: ...

    @property
    def dataTypeManager(self) -> ghidra.program.model.pcode.PcodeDataTypeManager: ...
