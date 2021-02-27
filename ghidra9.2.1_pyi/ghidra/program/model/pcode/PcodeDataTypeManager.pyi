import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.xml
import java.lang


class PcodeDataTypeManager(object):
    """
    Class for making Ghidra DataTypes suitable for use with pcode
    """





    def __init__(self, prog: ghidra.program.model.listing.Program): ...



    def buildCoreTypes(self) -> unicode:
        """
        Build the coretypes xml element
        @return coretypes xml element
        """
        ...

    def buildStructTypeZeroSizeOveride(self, type: ghidra.program.model.data.DataType) -> java.lang.StringBuilder:
        """
        Build an XML document string representing the Structure or Typedef to Structure that has
          its size reported as zero.
        @param type data type to build XML for
        @return XML string document
        """
        ...

    def buildType(self, type: ghidra.program.model.data.DataType, size: int) -> java.lang.StringBuilder:
        """
        Build an XML document string representing the type information for a data type
        @param type data type to build XML for
        @param size size of the data type
        @return XML string document
        """
        ...

    def buildTypeRef(self, type: ghidra.program.model.data.DataType, size: int) -> java.lang.StringBuilder:
        """
        Generate an XML tag describing the given data-type. Most data-types produce a {@code <type>} tag,
         fully describing the data-type. Where possible a {@code <typeref>} tag is produced, which just gives
         the name of the data-type, deferring a full description of the data-type. For certain simple or
         nameless data-types, a {@code <type>} tag is emitted giving a full description.
        @param type is the data-type to be converted
        @param size is the size in bytes of the specific instance of the data-type
        @return a StringBuilder containing the XML tag
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def findBaseType(self, nm: unicode, idstr: unicode) -> ghidra.program.model.data.DataType:
        """
        Find a base/built-in data-type with the given name and/or id.  If an id is provided and
         a corresponding data-type exists, this data-type is returned. Otherwise the first
         built-in data-type with a matching name is returned
        @param nm name of data-type
        @param idstr is an optional string containing a data-type id number
        @return the data-type object or null if no matching data-type exists
        """
        ...

    def findUndefined(self, size: int) -> ghidra.program.model.data.DataType: ...

    def getClass(self) -> java.lang.Class: ...

    def getProgram(self) -> ghidra.program.model.listing.Program: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def readXMLDataType(self, parser: ghidra.xml.XmlPullParser) -> ghidra.program.model.data.DataType:
        """
        Get the data type that corresponds to the given XML element.
        @param parser the xml parser
        @return the read data type
        @throws PcodeXMLException if the data type could be resolved from the
         element
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
    def program(self) -> ghidra.program.model.listing.Program: ...
