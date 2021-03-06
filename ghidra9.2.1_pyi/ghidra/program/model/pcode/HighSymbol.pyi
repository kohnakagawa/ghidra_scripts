import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.program.model.pcode
import ghidra.program.model.symbol
import ghidra.xml
import java.lang


class HighSymbol(object):
    """
    A symbol within the decompiler's model of a particular function.  The symbol has a name and a data-type
     along with other properties. The symbol is mapped to one or more storage locations by attaching a
     SymbolEntry for each mapping.
    """

    ID_BASE: long = 0x4000000000000000L







    @staticmethod
    def buildMapSymXML(res: java.lang.StringBuilder, sym: ghidra.program.model.pcode.HighSymbol) -> None:
        """
        Write out the given symbol with all its mapping as a &lt;mapsym&gt; tag to the given XML stream.
        @param res is the given XML stream
        @param sym is the given symbol
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getCategoryIndex(self) -> int:
        """
        For parameters (category=0), this method returns the position of the parameter within the function prototype.
        @return the category index for this symbol
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDataType(self) -> ghidra.program.model.data.DataType:
        """
        @return the data-type associate with this symbol
        """
        ...

    def getFirstWholeMap(self) -> ghidra.program.model.pcode.SymbolEntry:
        """
        @return the first mapping object attached to this symbol
        """
        ...

    def getHighFunction(self) -> ghidra.program.model.pcode.HighFunction:
        """
        Get the function model of which this symbol is a part.
        @return the HighFunction owning this symbol
        """
        ...

    def getHighVariable(self) -> ghidra.program.model.pcode.HighVariable:
        """
        Get the HighVariable associate with this symbol if any.  This allows the user to go straight
         into the decompiler's function to see how the symbol gets manipulated.
        @return the associated HighVariable or null
        """
        ...

    def getId(self) -> long:
        """
        Get id associated with this symbol.
        @return the id
        """
        ...

    def getName(self) -> unicode:
        """
        Get the base name of this symbol
        @return the name
        """
        ...

    def getNamespace(self) -> ghidra.program.model.symbol.Namespace:
        """
        Fetch the namespace owning this symbol, if it exists.
        @return the Namespace object or null
        """
        ...

    def getPCAddress(self) -> ghidra.program.model.address.Address:
        """
        Get the first code Address, within the function, where this symbol's storage actually
         holds the value of the symbol.  If there is more than one mapping for the symbol, this
         returns the code Address for the first mapping.  A null value indicates that the storage
         is valid over the whole function (at least). If the value is non-null, the symbol storage
         may be used for other purposes at prior locations.
        @return the first use code Address or null
        """
        ...

    def getProgram(self) -> ghidra.program.model.listing.Program:
        """
        Get the Program object containing the function being modeled.
        @return the Program
        """
        ...

    def getSize(self) -> int:
        """
        @return the number of bytes consumed by the storage for this symbol
        """
        ...

    def getStorage(self) -> ghidra.program.model.listing.VariableStorage:
        """
        @return the storage associated with this symbol (associated with the first mapping)
        """
        ...

    def getSymbol(self) -> ghidra.program.model.symbol.Symbol:
        """
        Fetch the corresponding database Symbol if it exists.
        @return the matching Symbol object or null
        """
        ...

    def hashCode(self) -> int: ...

    def isGlobal(self) -> bool:
        """
        Is this symbol in the global scope or some other global namespace
        @return true if this is global
        """
        ...

    def isHiddenReturn(self) -> bool:
        """
        @return true is symbol holds a pointer to where a function's return value should be stored
        """
        ...

    def isIsolated(self) -> bool:
        """
        If this returns true, the decompiler will not speculatively merge this with
         other variables.
         Currently, being isolated is equivalent to being typelocked.
        @return true if this will not be merged with other variables
        """
        ...

    def isNameLocked(self) -> bool:
        """
        If this returns true, this symbol's name is "locked". meaning the decompiler
         is forced to use the name when labeling the storage described by this symbol.
        @return true if the name is considered "locked".
        """
        ...

    def isParameter(self) -> bool:
        """
        Is this symbol a parameter for a function
        @return true if this is a parameter
        """
        ...

    def isReadOnly(self) -> bool:
        """
        @return true if the symbol's value is considered read-only (by the decompiler)
        """
        ...

    def isThisPointer(self) -> bool:
        """
        @return true if symbol is a "this" pointer for a class method
        """
        ...

    def isTypeLocked(self) -> bool:
        """
        If this returns true, this symbol's data-type is "locked", meaning
         it is considered unchangeable during decompilation. The data-type
         will be forced into the decompiler's model of the function to the extent possible.
        @return true if the data-type is considered "locked".
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def restoreMapSymXML(parser: ghidra.xml.XmlPullParser, isGlobal: bool, high: ghidra.program.model.pcode.HighFunction) -> ghidra.program.model.pcode.HighSymbol:
        """
        Restore a full HighSymbol from the next &lt;mapsym&gt; tag in the given XML stream.
         This method acts as an XML based HighSymbol factory, instantiating the correct class
         based on the particular tags.
        @param parser is the given XML stream
        @param isGlobal is true if this symbol is being read into a global scope
        @param high is the function model that will own the new symbol
        @return the new symbol
        @throws PcodeXMLException if the XML description is invalid
        """
        ...

    def restoreXML(self, parser: ghidra.xml.XmlPullParser) -> None:
        """
        Restore this symbol object and its associated mappings from an XML description
         in the given stream.
        @param parser is the given XML stream
        @throws PcodeXMLException if the XML description is invalid
        """
        ...

    def saveXML(self, buf: java.lang.StringBuilder) -> None:
        """
        Save the symbol description as a tag to the XML stream.  This does NOT save the mappings.
        @param buf is the XML stream
        """
        ...

    def setHighVariable(self, high: ghidra.program.model.pcode.HighVariable) -> None:
        """
        Associate a particular HighVariable with this symbol. This is used to link the symbol
         into the decompiler's description of how a function manipulates a particular symbol.
        @param high is the associated HighVariable
        """
        ...

    def setNameLock(self, namelock: bool) -> None:
        """
        Set whether this symbol's name is considered "locked". If it is "locked", the decompiler
         will use the name when labeling the storage described by this symbol.
        @param namelock is true if the name should be considered "locked".
        """
        ...

    def setTypeLock(self, typelock: bool) -> None:
        """
        Set whether this symbol's data-type is considered "locked". If it is "locked",
         this symbol's data-type is considered unchangeable during decompilation. The data-type
         will be forced into the decompiler's model of the function to the extent possible.
        @param typelock is true if the data-type should be considered "locked".
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
    def PCAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def categoryIndex(self) -> int: ...

    @property
    def dataType(self) -> ghidra.program.model.data.DataType: ...

    @property
    def firstWholeMap(self) -> ghidra.program.model.pcode.SymbolEntry: ...

    @property
    def global(self) -> bool: ...

    @property
    def hiddenReturn(self) -> bool: ...

    @property
    def highFunction(self) -> ghidra.program.model.pcode.HighFunction: ...

    @property
    def highVariable(self) -> ghidra.program.model.pcode.HighVariable: ...

    @highVariable.setter
    def highVariable(self, value: ghidra.program.model.pcode.HighVariable) -> None: ...

    @property
    def id(self) -> long: ...

    @property
    def isolated(self) -> bool: ...

    @property
    def name(self) -> unicode: ...

    @property
    def nameLock(self) -> None: ...  # No getter available.

    @nameLock.setter
    def nameLock(self, value: bool) -> None: ...

    @property
    def nameLocked(self) -> bool: ...

    @property
    def namespace(self) -> ghidra.program.model.symbol.Namespace: ...

    @property
    def parameter(self) -> bool: ...

    @property
    def program(self) -> ghidra.program.model.listing.Program: ...

    @property
    def readOnly(self) -> bool: ...

    @property
    def size(self) -> int: ...

    @property
    def storage(self) -> ghidra.program.model.listing.VariableStorage: ...

    @property
    def symbol(self) -> ghidra.program.model.symbol.Symbol: ...

    @property
    def thisPointer(self) -> bool: ...

    @property
    def typeLock(self) -> None: ...  # No getter available.

    @typeLock.setter
    def typeLock(self, value: bool) -> None: ...

    @property
    def typeLocked(self) -> bool: ...
