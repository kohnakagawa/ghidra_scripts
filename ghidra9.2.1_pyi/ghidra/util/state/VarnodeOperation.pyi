from typing import Iterator
from typing import List
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.pcode
import ghidra.xml
import java.lang
import org.xml.sax


class VarnodeOperation(ghidra.program.model.pcode.Varnode):




    def __init__(self, pcodeOp: ghidra.program.model.pcode.PcodeOp, inputValues: List[ghidra.program.model.pcode.Varnode]): ...



    @staticmethod
    def appendSpaceOffset(buf: java.lang.StringBuilder, addr: ghidra.program.model.address.Address) -> None: ...

    def buildXML(self, buf: java.lang.StringBuilder) -> None:
        """
        @param buf is the builder to which to append XML
        """
        ...

    @overload
    @staticmethod
    def buildXMLAddress(addr: ghidra.program.model.address.Address) -> unicode:
        """
        Convert an address into an XML document.
        @param addr -- Address to convert to XML
        @return XML string
        """
        ...

    @overload
    @staticmethod
    def buildXMLAddress(varnodes: List[ghidra.program.model.pcode.Varnode], logicalsize: int) -> unicode:
        """
        Convert a varnode array into an XML document.
        @param varnodes sequence of storage varnodes
        @param logicalsize the logical size value of the varnode
        @return XML string
        """
        ...

    @overload
    @staticmethod
    def buildXMLAddress(resBuf: java.lang.StringBuilder, addr: ghidra.program.model.address.Address, size: int) -> None:
        """
        Build an XML document representation of a varnode with the given address and size.
        @param resBuf is the builder to which to append the XML
        @param addr location varnode is defined at
        @param size size of the varnode.
        """
        ...

    def contains(self, address: ghidra.program.model.address.Address) -> bool:
        """
        Determine if this varnode contains the specified address
        @param address the address for which to check
        @return true if this varnode contains the specified address
        """
        ...

    def equals(self, o: object) -> bool: ...

    def getAddress(self) -> ghidra.program.model.address.Address:
        """
        @return the address this varnode is attached to
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDef(self) -> ghidra.program.model.pcode.PcodeOp:
        """
        @return get the pcode op this varnode belongs to
        """
        ...

    def getDescendants(self) -> Iterator[ghidra.program.model.pcode.PcodeOp]:
        """
        @return iterator to all PcodeOp s that take this as input
        """
        ...

    def getHigh(self) -> ghidra.program.model.pcode.HighVariable:
        """
        @return the high level variable this varnode represents
        """
        ...

    def getInputValues(self) -> List[ghidra.program.model.pcode.Varnode]: ...

    def getLoneDescend(self) -> ghidra.program.model.pcode.PcodeOp:
        """
        If there is only one PcodeOp taking this varnode as input, return it. Otherwise return null
        @return the lone descendant PcodeOp
        """
        ...

    def getMergeGroup(self) -> int:
        """
        @return the index of the group, within the high containing this, that are forced merged with this
        """
        ...

    def getOffset(self) -> long:
        """
        @return the offset into the address space varnode is defined within
        """
        ...

    def getPCAddress(self) -> ghidra.program.model.address.Address:
        """
        Get the address where this varnode is defined or
         NO_ADDRESS if this varnode is an input
        @return the address
        """
        ...

    def getPCodeOp(self) -> ghidra.program.model.pcode.PcodeOp: ...

    def getSize(self) -> int:
        """
        @return size of the varnode in bytes
        """
        ...

    def getSpace(self) -> int:
        """
        @return the space this varnode belongs to (ram, register, ...)
        """
        ...

    def getWordOffset(self) -> long:
        """
        Returns the word offset into the address space this is defined within

         The word size is defined in the Language's .slaspec file with the
         "WORDSIZE" argument when DEFINEing a memory SPACE (capitalization is
         for emphasis; the directives are actually lowercase).
        @return the word offset into the address space this is defined within
        """
        ...

    def hashCode(self) -> int: ...

    @overload
    def intersects(self, set: ghidra.program.model.address.AddressSetView) -> bool:
        """
        Determine if this varnode intersects the specified address set
        @param set address set
        @return true if this varnode intersects the specified address set
        """
        ...

    @overload
    def intersects(self, varnode: ghidra.program.model.pcode.Varnode) -> bool:
        """
        Determine if this varnode intersects another varnode.
        @param varnode other varnode
        @return true if this varnode intersects the specified varnode
        """
        ...

    def isAddrTied(self) -> bool: ...

    def isAddress(self) -> bool: ...

    def isConstant(self) -> bool: ...

    def isFree(self) -> bool: ...

    def isHash(self) -> bool: ...

    def isInput(self) -> bool: ...

    def isPersistant(self) -> bool: ...

    def isRegister(self) -> bool: ...

    def isSimplified(self) -> bool: ...

    def isUnaffected(self) -> bool: ...

    def isUnique(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def readXML(parser: ghidra.xml.XmlPullParser, factory: ghidra.program.model.pcode.PcodeFactory) -> ghidra.program.model.pcode.Varnode:
        """
        Build a varnode from a SAX parse tree node
        @param parser the parser
        @param factory pcode factory used to create valid pcode
        @return new varnode element based on info in the XML.
        @throws PcodeXMLException
        """
        ...

    @overload
    @staticmethod
    def readXMLAddress(el: ghidra.xml.XmlElement, addrFactory: ghidra.program.model.address.AddressFactory) -> ghidra.program.model.address.Address:
        """
        Create an address from a SAX parse tree node.
        @param el SAX parse tree element
        @param addrFactory address factory used to create valid addresses
        @return Address created from XML info
        """
        ...

    @overload
    @staticmethod
    def readXMLAddress(addrstring: unicode, addrfactory: ghidra.program.model.address.AddressFactory, refSpace: ghidra.program.model.address.AddressSpace) -> ghidra.program.model.address.Address:
        """
        Parse an XML containing an address.  The format options are simple enough that we don't try to invoke
         an actual XML parser but just walk the string
        @param addrstring is the string containing the XML tag
        @param addrfactory is the factory that can produce addresses
        @param refSpace can be null but is otherwise the reference AddressSpace from which the request is sent.
        @return the created Address or Address.NO_ADDRESS in some special cases
        @throws PcodeXMLException
        """
        ...

    @overload
    @staticmethod
    def readXMLAddress(localName: unicode, attr: org.xml.sax.Attributes, addrFactory: ghidra.program.model.address.AddressFactory) -> ghidra.program.model.address.Address: ...

    def setSimplified(self, simplified: bool) -> None: ...

    @overload
    def toString(self) -> unicode: ...

    @overload
    def toString(self, language: ghidra.program.model.lang.Language) -> unicode: ...

    def trim(self) -> None: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def PCodeOp(self) -> ghidra.program.model.pcode.PcodeOp: ...

    @property
    def addrTied(self) -> bool: ...

    @property
    def address(self) -> bool: ...

    @property
    def constant(self) -> bool: ...

    @property
    def free(self) -> bool: ...

    @property
    def input(self) -> bool: ...

    @property
    def inputValues(self) -> List[ghidra.program.model.pcode.Varnode]: ...

    @property
    def persistant(self) -> bool: ...

    @property
    def register(self) -> bool: ...

    @property
    def simplified(self) -> bool: ...

    @simplified.setter
    def simplified(self, value: bool) -> None: ...

    @property
    def unaffected(self) -> bool: ...

    @property
    def unique(self) -> bool: ...
