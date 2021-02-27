import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.program.model.symbol
import java.lang
import java.util
import java.util.function


class SymbolUtilities(object):
    """
    Class with static methods to deal with symbol strings.
    """

    DAT_LEVEL: int = 1
    EXT_LEVEL: int = 5
    FUN_LEVEL: int = 6
    INVALIDCHARS: List[int] = array('c', ' ')
    LAB_LEVEL: int = 2
    MAX_SYMBOL_NAME_LENGTH: int = 2000
    ORDINAL_PREFIX: unicode = u'Ordinal_'
    SUB_LEVEL: int = 3
    UNK_LEVEL: int = 0



    def __init__(self): ...



    @staticmethod
    def containsInvalidChars(str: unicode) -> bool:
        """
        Check for invalid characters
         (space, colon, asterisk, plus, bracket)
         in labels.
        @param str the string to be checked for invalid characters.
        @return boolean true if no invalid chars
        """
        ...

    @staticmethod
    def createPreferredLabelOrFunctionSymbol(program: ghidra.program.model.listing.Program, address: ghidra.program.model.address.Address, namespace: ghidra.program.model.symbol.Namespace, name: unicode, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.symbol.Symbol:
        """
        Create label symbol giving preference to non-global symbols.  An existing function symbol
         may be returned.  If attempting to create a global symbol and the name already exists
         at the address no symbol will be created and null will be returned.
         If attempting to create a non-global symbol, which does not exist,
         and a global symbol does exist with same name its namespace will be changed.
        @param program program within which the symbol should be created
        @param address memory address where symbol should be created
        @param namespace symbol namespace or null for global
        @param name symbol name
        @param source symbol source type
        @return new or existing label or function symbol or null if creating a global symbol
         whose name already exists at address
        @throws InvalidInputException if invalid symbol name provided
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def getAddressAppendedName(name: unicode, address: ghidra.program.model.address.Address) -> unicode:
        """
        Creates the standard symbol name for symbols that have the addresses appended to the
         name following an "@" character in order to make it unique.
        @param name the "true" name of the symbol
        @param address the address to be appended
        @return the name with the address appended.
        """
        ...

    @staticmethod
    def getAddressString(addr: ghidra.program.model.address.Address) -> unicode: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    @staticmethod
    def getCleanSymbolName(symbol: ghidra.program.model.symbol.Symbol) -> unicode:
        """
        Gets the base symbol name regardless of whether or not the address has been appended.
        @param symbol the symbol to get the clean name for.
        @return the base symbol name where the {@literal "@<address>"} has been stripped away if it exists.
        """
        ...

    @overload
    @staticmethod
    def getCleanSymbolName(symbolName: unicode, address: ghidra.program.model.address.Address) -> unicode:
        """
        Gets the base symbol name regardless of whether or not the address has been appended
         using either the standard "@" separator, or the less preferred "_" separator.  The
         address string extension must match that which is produced by the
         {@link #getAddressString(Address)} method for it to be recognized.
        @param symbolName a symbol name to get the clean name for.
        @param address the symbol's address
        @return the base symbol name where the {@literal "@<address>"} has been stripped away if it exists.
        """
        ...

    @staticmethod
    def getDefaultExternalFunctionName(addr: ghidra.program.model.address.Address) -> unicode:
        """
        Generates a default external name for an external function
        @param addr the memory address referred to by the external.
        @return the default generated name for the external.
        """
        ...

    @staticmethod
    def getDefaultExternalName(addr: ghidra.program.model.address.Address, dt: ghidra.program.model.data.DataType) -> unicode:
        """
        Generates a default external name for a given external data/code location.
        @param addr the memory address referred to by the external.
        @param dt data type associated with the specified external memory address
        @return the default generated name for the external.
        """
        ...

    @staticmethod
    def getDefaultFunctionName(addr: ghidra.program.model.address.Address) -> unicode:
        """
        Generates a default function name for a given address.
        @param addr the entry point of the function.
        @return the default generated name for the function.
        """
        ...

    @overload
    @staticmethod
    def getDefaultLocalName(program: ghidra.program.model.listing.Program, stackOffset: int, firstUseOffset: int) -> unicode: ...

    @overload
    @staticmethod
    def getDefaultLocalName(program: ghidra.program.model.listing.Program, storage: ghidra.program.model.listing.VariableStorage, firstUseOffset: int) -> unicode: ...

    @staticmethod
    def getDefaultParamName(ordinal: int) -> unicode: ...

    @overload
    @staticmethod
    def getDynamicName(referenceLevel: int, addr: ghidra.program.model.address.Address) -> unicode:
        """
        Create a name for a dynamic symbol with a 3-letter prefix based upon reference level
         and an address.  Acceptable referenceLevel's are:
         {@link #UNK_LEVEL}, {@link #DAT_LEVEL}, {@link #LAB_LEVEL}, {@link #SUB_LEVEL},
         {@link #EXT_LEVEL}, {@link #FUN_LEVEL}.
        @param referenceLevel the type of reference for which to create a dynamic name.
        @param addr the address at which to create a dynamic name.
        @return dynamic symbol name
        """
        ...

    @overload
    @staticmethod
    def getDynamicName(program: ghidra.program.model.listing.Program, addr: ghidra.program.model.address.Address) -> unicode:
        """
        Create a name for a dynamic symbol.
        @param program the current program
        @param addr the address of the symbol for which to generate a name
        @return a name for the symbol at the given address
        """
        ...

    @staticmethod
    def getDynamicOffcutName(addr: ghidra.program.model.address.Address) -> unicode:
        """
        Create a dynamic label name for an offcut reference.
        @param addr the address at which to create an offcut reference name.
        @return dynamic offcut label name
        """
        ...

    @staticmethod
    def getExpectedLabelOrFunctionSymbol(program: ghidra.program.model.listing.Program, symbolName: unicode, errorConsumer: java.util.function.Consumer) -> ghidra.program.model.symbol.Symbol:
        """
        Returns the unique global label or function symbol with the given name. Also, logs if there
         is not exactly one symbol with that name.
        @param program the program to search.
        @param symbolName the name of the global label or function symbol to search.
        @param errorConsumer the object to use for reporting errors via it's accept() method.
        @return symbol if a unique label/function symbol with name is found or null
        """
        ...

    @staticmethod
    def getLabelOrFunctionSymbol(program: ghidra.program.model.listing.Program, symbolName: unicode, errorConsumer: java.util.function.Consumer) -> ghidra.program.model.symbol.Symbol:
        """
        Returns the unique global label or function symbol with the given name. Also, logs if there
         is more than one symbol with that name.
        @param program the program to search.
        @param symbolName the name of the global label or function symbol to search.
        @param errorConsumer the object to use for reporting errors via it's accept() method.
        @return symbol if a unique label/function symbol with name is found or null
        """
        ...

    @staticmethod
    def getOrdinalValue(symbolName: unicode) -> int: ...

    @staticmethod
    def getSymbolNameComparator() -> java.util.Comparator:
        """
        Returns a comparator for symbols.  The comparison is based upon the name.  This call
         replaces the former <code>compareTo</code> method on Symbol.  This comparator returned here
         is case-insensitive.
        @return the comparator
        """
        ...

    @staticmethod
    def getSymbolTypeDisplayName(symbol: ghidra.program.model.symbol.Symbol) -> unicode:
        """
        Returns display text suitable for describing in the GUI the {@link SymbolType} of the
         given symbol
        @param symbol The symbol from which to get the SymbolType
        @return a display string for the SymbolType
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isDefaultLocalName(program: ghidra.program.model.listing.Program, name: unicode, storage: ghidra.program.model.listing.VariableStorage) -> bool: ...

    @staticmethod
    def isDefaultLocalStackName(name: unicode) -> bool: ...

    @staticmethod
    def isDefaultParameterName(name: unicode) -> bool: ...

    @staticmethod
    def isDynamicSymbolPattern(name: unicode, caseSensitive: bool) -> bool:
        """
        Tests if the given name is a possible dynamic symbol name.
         WARNING! This method should be used carefully since it will return true for
         any name which starts with a known dynamic label prefix or ends with an '_'
         followed by a valid hex value.
        @param name the name to test
        @param caseSensitive true if case matters.
        @return true if name is a possible dynamic symbol name, else false
        """
        ...

    @staticmethod
    def isInvalidChar(c: int) -> bool:
        """
        Returns true if the specified char
         is not valid for use in a symbol name
        @param c the character to be tested as a valid symbol character.
        @return return true if c is an invalid char within a symbol name, else false
        """
        ...

    @staticmethod
    def isReservedDynamicLabelName(name: unicode, addrFactory: ghidra.program.model.address.AddressFactory) -> bool:
        """
        Returns true if the given name could match a default dynamic label (EXT, LAB, SUB, FUN, DAT)
         at some address.
         WARNING! Does not handle dynamic labels which use data-type prefixes -
         see {@link #isDynamicSymbolPattern(String, boolean)} for more liberal check
        """
        ...

    @staticmethod
    def isReservedExternalDefaultName(name: unicode, addrFactory: ghidra.program.model.address.AddressFactory) -> bool:
        """
        Returns true if the specified name is reserved as a default external name.
        @param name
        @param addrFactory
        @return true if the specified name is reserved as a default external name.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def parseDynamicName(factory: ghidra.program.model.address.AddressFactory, name: unicode) -> ghidra.program.model.address.Address:
        """
        Parse a dynamic name and return its address or null if unable to parse.
        @param factory address factory
        @param name the dynamic label name to parse into an address.
        @return address corresponding to symbol name if it satisfies possible dynamic naming
         or null if unable to parse address fro name
        """
        ...

    @staticmethod
    def replaceInvalidChars(str: unicode, replaceWithUnderscore: bool) -> unicode:
        """
        Removes from the given string any invalid characters or replaces
         them with underscores.

         For example:
         given "a:b*c", the return value would be "a_b_c"
        @param str the string to have invalid chars converted to underscores or removed.
        @param replaceWithUnderscore - true means replace the invalid
         chars with underscore. if false, then just drop the invalid chars
        @return modified string
        """
        ...

    @staticmethod
    def startsWithDefaultDynamicPrefix(name: unicode) -> bool:
        """
        Returns true if the given name starts with a possible default symbol prefix.
        @param name the name string to test.
        @return true if name starts with a know dynamic prefix
        """
        ...

    def toString(self) -> unicode: ...

    @staticmethod
    def validateName(name: unicode) -> None:
        """
        Validate the given symbol name: cannot be null, cannot be an empty string, cannot contain blank
         characters, cannot be a reserved name.
        @param name symbol name to be validated
        @throws InvalidInputException invalid or reserved name has been specified
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
