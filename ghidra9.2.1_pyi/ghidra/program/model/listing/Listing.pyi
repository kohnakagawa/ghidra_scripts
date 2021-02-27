from typing import Iterator
from typing import List
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.program.model.mem
import ghidra.program.model.symbol
import ghidra.program.model.util
import ghidra.util.task
import java.lang


class Listing(object):
    """
    This interface provides all the methods needed to create,delete, retrieve,
     modify code level constructs (CodeUnits, Macros, Fragments, and Modules).
    """









    def addInstructions(self, instructionSet: ghidra.program.model.lang.InstructionSet, overwrite: bool) -> ghidra.program.model.address.AddressSetView:
        """
        Creates a complete set of instructions. A preliminary pass will be made
         checking for code unit conflicts which will be marked within the
         instructionSet causing dependent blocks to get pruned.
        @param instructionSet the set of instructions to be added. All code unit
                    conflicts will be marked within the instructionSet and
                    associated blocks.
        @param overwrite if true, overwrites existing code units.
        @throws CodeUnitInsertionException if the instruction set is incompatible
                     with the program memory
        @return the set of addresses over which instructions were actually added
                 to the program. This may differ from the InstructionSet address
                 set if conflict errors occurred. Such conflict errors will be
                 recorded within the InstructionSet and its InstructionBlocks.
        """
        ...

    def clearAll(self, clearContext: bool, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Removes all CodeUnits, comments, properties, and references from the
         listing.
        @param clearContext if true, also clear any instruction context that has
                    been laid down from previous disassembly.
        @param monitor used for tracking progress and cancelling the clear
                    operation.
        """
        ...

    @overload
    def clearCodeUnits(self, startAddr: ghidra.program.model.address.Address, endAddr: ghidra.program.model.address.Address, clearContext: bool) -> None:
        """
        Clears any code units in the given range returning everything to "db"s,
         and removing any references in the affected area. Note that the module
         and fragment structure is unaffected. If part of a code unit is contained
         in the given address range then the whole code unit will be cleared.
        @param startAddr the start address of the area to be cleared.
        @param endAddr the end address of the area to be cleared.
        @param clearContext clear context register values if true
        """
        ...

    @overload
    def clearCodeUnits(self, startAddr: ghidra.program.model.address.Address, endAddr: ghidra.program.model.address.Address, clearContext: bool, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Clears any code units in the given range returning everything to "db"s,
         and removing any references in the affected area. Note that the module
         and fragment structure is unaffected. If part of a code unit is contained
         in the given address range then the whole code unit will be cleared.
        @param startAddr the start address of the area to be cleared.
        @param endAddr the end address of the area to be cleared.
        @param clearContext clear context register values if true
        @param monitor monitor that can be used to cancel the clear operation
        @throws CancelledException if the operation was cancelled.
        """
        ...

    def clearComments(self, startAddr: ghidra.program.model.address.Address, endAddr: ghidra.program.model.address.Address) -> None:
        """
        Clears the comments in the given range.
        @param startAddr the start address of the range to be cleared
        @param endAddr the end address of the range to be cleard
        """
        ...

    def clearProperties(self, startAddr: ghidra.program.model.address.Address, endAddr: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Clears the properties in the given range.
        @param startAddr the start address of the range to be cleared
        @param endAddr the end address of the range to be cleard
        @param monitor task monitor for cancelling operation.
        @throws CancelledException if the operation was cancelled.
        """
        ...

    @overload
    def createData(self, addr: ghidra.program.model.address.Address, dataType: ghidra.program.model.data.DataType) -> ghidra.program.model.listing.Data:
        """
        Creates a new defined Data object at the given address. This ignores the
         bytes that are present
        @param addr the address at which to create a new Data object.
        @param dataType the Data Type that describes the type of Data object to
                    create.
        @return newly created data unit
        @exception CodeUnitInsertionException thrown if the new Instruction would
                        overlap and existing Instruction or defined data.
        @throws DataTypeConflictException if the given datatype conflicts (same
                     name, but not equal) with an existing datatype.
        """
        ...

    @overload
    def createData(self, addr: ghidra.program.model.address.Address, dataType: ghidra.program.model.data.DataType, length: int) -> ghidra.program.model.listing.Data:
        """
        Creates a new defined Data object of a given length at the given address.
         This ignores the bytes that are present
        @param addr the address at which to create a new Data object.
        @param dataType the Data Type that describes the type of Data object to
                    create.
        @param length the length of the datatype.
        @return newly created data unit
        @exception CodeUnitInsertionException thrown if the new Instruction would
                        overlap and existing Instruction or defined data.
        @throws DataTypeConflictException if the given datatype conflicts (same
                     name, but not equal) with an existing datatype.
        """
        ...

    @overload
    def createFunction(self, name: unicode, entryPoint: ghidra.program.model.address.Address, body: ghidra.program.model.address.AddressSetView, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.listing.Function:
        """
        Create a function with an entry point and a body of addresses.
        @param name the name of the function to create
        @param entryPoint the entry point for the function
        @param body the address set that makes up the functions body
        @param source the source of this function
        @return the created function
        @throws InvalidInputException if the name contains invalid characters
        @throws OverlappingFunctionException if the given body overlaps with an
                     existing function.
        """
        ...

    @overload
    def createFunction(self, name: unicode, nameSpace: ghidra.program.model.symbol.Namespace, entryPoint: ghidra.program.model.address.Address, body: ghidra.program.model.address.AddressSetView, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.listing.Function:
        """
        Create a function in the specified namespace with an entry point and a
         body of addresses.
        @param name the name of the function to create
        @param nameSpace the namespace in which to create the function
        @param entryPoint the entry point for the function
        @param body the address set that makes up the functions body
        @param source the source of this function
        @return the created function
        @throws InvalidInputException if the name contains invalid characters
        @throws OverlappingFunctionException if the given body overlaps with an
                     existing function.
        """
        ...

    def createInstruction(self, addr: ghidra.program.model.address.Address, prototype: ghidra.program.model.lang.InstructionPrototype, memBuf: ghidra.program.model.mem.MemBuffer, context: ghidra.program.model.lang.ProcessorContextView) -> ghidra.program.model.listing.Instruction:
        """
        Creates a new Instruction object at the given address. The specified
         context is only used to create the associated prototype. It is critical
         that the context be written immediately after creation of the instruction
         and must be done with a single set operation on the program context. Once
         a set context is done on the instruction address, any subsequent context
         changes will result in a <code>ContextChangeException</code>
        @param addr the address at which to create an instruction
        @param prototype the InstructionPrototype the describes the type of
                    instruction to create.
        @param memBuf buffer that provides the bytes that make up the
                    instruction.
        @param context the processor context at this location.
        @return the newly created instruction.
        @exception CodeUnitInsertionException thrown if the new Instruction would
                        overlap and existing Instruction or defined data.
        """
        ...

    def createRootModule(self, treeName: unicode) -> ghidra.program.model.listing.ProgramModule:
        """
        Create a new tree that will be identified by the given name. By default,
         the new root module is populated with fragments based on memory blocks.
         Note that the root module's name is not the same as its tree name. The
         root module name defaults to the name of the program.
        @param treeName name of the tree to search
        @return root module
        @throws DuplicateNameException if a tree with the given name already
                     exists
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getCodeUnitAfter(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.CodeUnit:
        """
        get the next code unit that starts an an address that is greater than the
         given address. The search will include instructions, defined data, and
         undefined data.
        @param addr the address from which to search forward.
        @return the next CodeUnit found while searching forward from addr or null
                 if none found.
        """
        ...

    def getCodeUnitAt(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.CodeUnit:
        """
        get the code unit that starts at the given address.
        @param addr the address to look for a codeUnit.
        @return the codeUnit that begins at the given address
        """
        ...

    def getCodeUnitBefore(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.CodeUnit:
        """
        get the next code unit that starts at an address that is less than the
         given address. The search will include instructions, defined data, and
         undefined data.
        @param addr the address from which to search backwards.
        @return The first codeUnit found while searching backwards from addr or
                 null if none found.
        """
        ...

    def getCodeUnitContaining(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.CodeUnit:
        """
        get the code unit that contains the given address.
        @param addr the address to look for a codeUnit.
        @return the codeUnit that contains the given address
        """
        ...

    @overload
    def getCodeUnitIterator(self, property: unicode, forward: bool) -> ghidra.program.model.listing.CodeUnitIterator:
        """
        Get an iterator that contains all code units in the program which have
         the specified property type defined. Standard property types are defined
         in the CodeUnit class. The property types are: EOL_COMMENT, PRE_COMMENT,
         POST_COMMENT, USER_REFERENCE, MNEMONIC_REFERENCE, VALUE_REFERENCE.
         Property types can also be user defined.
        @param property the name of the property type.
        @param forward true means get iterator in forward direction
        @return a CodeUnitIterator that returns all code units from the indicated
                 start address that have the specified property type defined.
        """
        ...

    @overload
    def getCodeUnitIterator(self, property: unicode, addr: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.listing.CodeUnitIterator:
        """
        Get an iterator that contains the code units which have the specified
         property type defined. Only code units at an address greater than or
         equal to the specified start address will be returned by the iterator. If
         the start address is null then check the entire program. Standard
         property types are defined in the CodeUnit class. The property types are:
         EOL_COMMENT, PRE_COMMENT, POST_COMMENT, USER_REFERENCE,
         MNEMONIC_REFERENCE, VALUE_REFERENCE. Property types can also be user
         defined.
        @param property the name of the property type. (EOL_COMMENT, PRE_COMMENT,
                    POST_COMMENT, USER_REFERENCE, MNEMONIC_REFERENCE,
                    VALUE_REFERENCE)
        @param addr the start address
        @param forward true means get iterator in forward direction
        @return a CodeUnitIterator that returns all code units from the indicated
                 start address that have the specified property type defined.
        """
        ...

    @overload
    def getCodeUnitIterator(self, property: unicode, addrSet: ghidra.program.model.address.AddressSetView, forward: bool) -> ghidra.program.model.listing.CodeUnitIterator:
        """
        Get an iterator that contains the code units which have the specified
         property type defined. Only code units starting within the address set
         will be returned by the iterator. If the address set is null then check
         the entire program. Standard property types are defined in the CodeUnit
         class.
        @param property the name of the property type.
        @param addrSet the address set
        @param forward true means get iterator in forward direction
        @return a CodeUnitIterator that returns all code units from the indicated
                 address set that have the specified property type defined.
        """
        ...

    @overload
    def getCodeUnits(self, forward: bool) -> ghidra.program.model.listing.CodeUnitIterator:
        """
        get a CodeUnit iterator that will iterate over the entire address space.
        @param forward true means get iterator in forward direction
        @return a CodeUnitIterator in forward direction
        """
        ...

    @overload
    def getCodeUnits(self, addr: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.listing.CodeUnitIterator:
        """
        Returns an iterator of the code units in this listing (in proper
         sequence), starting at the specified address. The specified address
         indicates the first code unit that would be returned by an initial call
         to the <code>next</code> method. An initial call to the <code>previous</code>
         method would return the code unit with an address less than the specified
         address.
         <p>
        @param addr the start address of the iterator.
        @param forward true means get iterator in forward direction
        @return a CodeUnitIterator positioned just before addr.
        """
        ...

    @overload
    def getCodeUnits(self, addrSet: ghidra.program.model.address.AddressSetView, forward: bool) -> ghidra.program.model.listing.CodeUnitIterator:
        """
        Get an iterator over the address range(s). Only code units whose start
         addresses are contained in the given address set will be returned by the
         iterator.
        @param addrSet the AddressRangeSet to iterate over.
        @param forward true means get iterator in forward direction
        @return a CodeUnitIterator that is restricted to the give
                 AddressRangeSet.
        """
        ...

    def getComment(self, commentType: int, address: ghidra.program.model.address.Address) -> unicode:
        """
        Get the comment for the given type at the specified address.
        @param commentType either EOL_COMMENT, PRE_COMMENT, POST_COMMENT,
                    PLATE_COMMENT, or REPEATABLE_COMMENT
        @param address the address of the comment.
        @return the comment string of the appropriate type or null if no comment
                 of that type exists for this codeunit
        @throws IllegalArgumentException if type is not one of the types of
                     comments supported
        """
        ...

    @overload
    def getCommentAddressIterator(self, addrSet: ghidra.program.model.address.AddressSetView, forward: bool) -> ghidra.program.model.address.AddressIterator:
        """
        Get a forward iterator over addresses that have any type of comment.
        @param addrSet address set
        @param forward true to iterator from lowest address to highest, false
                    highest to lowest
        @return an AddressIterator that returns all addresses from the indicated
                 address set that have any type of comment.
        """
        ...

    @overload
    def getCommentAddressIterator(self, commentType: int, addrSet: ghidra.program.model.address.AddressSetView, forward: bool) -> ghidra.program.model.address.AddressIterator:
        """
        Get a forward iterator over addresses that have the specified comment
         type.
        @param commentType type defined in CodeUnit
        @param addrSet address set
        @param forward true to iterator from lowest address to highest, false
                    highest to lowest
        @return an AddressIterator that returns all addresses from the indicated
                 address set that have the specified comment type defined
        """
        ...

    def getCommentCodeUnitIterator(self, commentType: int, addrSet: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.listing.CodeUnitIterator:
        """
        Get a forward code unit iterator over code units that have the specified
         comment type.
        @param commentType type defined in CodeUnit
        @param addrSet address set
        @return a CodeUnitIterator that returns all code units from the indicated
                 address set that have the specified comment type defined
        """
        ...

    def getCommentHistory(self, addr: ghidra.program.model.address.Address, commentType: int) -> List[ghidra.program.model.listing.CommentHistory]:
        """
        Get the comment history for comments at the given address.
        @param addr address for comments
        @param commentType comment type defined in CodeUnit
        @return array of comment history records
        """
        ...

    @overload
    def getCompositeData(self, forward: bool) -> ghidra.program.model.listing.DataIterator:
        """
        Get an iterator over all the composite data objects (Arrays, Structures,
         and Union) in the program.
        @param forward true means get iterator that starts at the minimum address
                    and iterates forward. Otherwise it starts at the maximum
                    address and iterates backwards.
        @return an iterator over all the composite data objects.
        """
        ...

    @overload
    def getCompositeData(self, start: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.listing.DataIterator:
        """
        Get an iterator over all the composite data objects (Arrays, Structures,
         and Union) in the program at or after the given Address.
        @param start start of the iterator
        @param forward true means get iterator in forward direction
        @return an iterator over all the composite data objects starting with the
                 given address.
        """
        ...

    @overload
    def getCompositeData(self, addrSet: ghidra.program.model.address.AddressSetView, forward: bool) -> ghidra.program.model.listing.DataIterator:
        """
        Get an iterator over all the composite data objects (Arrays, Structures,
         and Union) within the specified address set in the program.
        @param addrSet the address set
        @param forward true means get iterator in forward direction
        @return an iterator over all the composite data objects in the given
                 address set.
        """
        ...

    @overload
    def getData(self, forward: bool) -> ghidra.program.model.listing.DataIterator:
        """
        get a Data iterator that will iterate over the entire address space;
         returning both defined and undefined Data objects.
        @param forward true means get iterator in forward direction
        @return a DataIterator that iterates over all defined and undefined Data
                 object in the program.
        """
        ...

    @overload
    def getData(self, addr: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.listing.DataIterator:
        """
        Returns an iterator of the data in this listing (in proper sequence),
         starting at the specified address. The specified address indicates the
         first Data that would be returned by an initial call to the <code>next</code>
         method. An initial call to the <code>previous</code> method would return the
         Data with an address less than the specified address.
         <p>
        @param addr the initial position of the iterator
        @param forward true means get iterator in forward direction
        @return a DataIterator that iterates over all Data objects in the given
                 address range set.
        """
        ...

    @overload
    def getData(self, addrSet: ghidra.program.model.address.AddressSetView, forward: bool) -> ghidra.program.model.listing.DataIterator:
        """
        Get an iterator over the address range(s). Only data whose start
         addresses are contained in the given address set will be returned by the
         iterator.
        @param addrSet the address range set to iterate over.
        @param forward true means get iterator in forward direction
        @return a DataIterator that iterates over all defined and undefined Data
                 objects in the given address range set.
        """
        ...

    def getDataAfter(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        get the closest Data object that starts at an address that is greater
         than the given address.
        @param addr the address at which to begin the forward search.
        @return the next Data object whose starting address is greater than addr.
        """
        ...

    def getDataAt(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        get the Data (Defined or Undefined) that starts at the given address.
        @param addr the address to check for a Data object.
        @return the Data object that starts at addr; or null if no Data
                 objects(defined or undefined) start at addr.
        """
        ...

    def getDataBefore(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        get the closest Data object that starts at an address that is less than
         the given address.
        @param addr The address at which to begin the backward search.
        @return the closest Data object whose starting address is less than addr.
        """
        ...

    def getDataContaining(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        Gets the data object that is at or contains the given address or null if
         the address in not in memory or is in an instruction.
        @param addr the address for which to find its containing data element.
        @return the Data object containing the given address or null if there is
                 no data that contains the address.
        """
        ...

    def getDataTypeManager(self) -> ghidra.program.model.data.DataTypeManager:
        """
        Get the data type manager for the program.
        @return the datatype manager for the program.
        """
        ...

    def getDefaultRootModule(self) -> ghidra.program.model.listing.ProgramModule:
        """
        Returns the root module for the default program tree. This would be the
         program tree that has existed the longest.
        @return the root module for the oldest existing program tree.
        """
        ...

    def getDefinedCodeUnitAfter(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.CodeUnit:
        """
        Returns the next instruction or defined data after the given address;
        @param addr the address at which to begin the search
        @return the next instruction or defined data at an address higher than
                 the given address.
        """
        ...

    def getDefinedCodeUnitBefore(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.CodeUnit:
        """
        Returns the closest instruction or defined data that starts before the
         given address.
        @param addr the address at which to begin the search
        @return the closest instruction or defined data at an address below the
                 given address.
        """
        ...

    @overload
    def getDefinedData(self, forward: bool) -> ghidra.program.model.listing.DataIterator:
        """
        get a Data iterator that will iterate over the entire address space;
         returning only defined Data objects.
        @param forward true means get iterator in forward direction
        @return a DataIterator that iterates over all defined Data objects in the
                 program.
        """
        ...

    @overload
    def getDefinedData(self, addr: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.listing.DataIterator:
        """
        Returns an iterator of the defined data in this listing (in proper
         sequence), starting at the specified address. The specified address
         indicates the first defined Data that would be returned by an initial
         call to the <code>next</code> method. An initial call to the
         <code>previous</code> method would return the defined Data with an address
         less than the specified address.
         <p>
        @param addr the initial position of the iterator
        @param forward true means get iterator in forward direction
        @return a DataIterator that iterates over all defined Data objects in the
                 given address range set.
        """
        ...

    @overload
    def getDefinedData(self, addrSet: ghidra.program.model.address.AddressSetView, forward: bool) -> ghidra.program.model.listing.DataIterator:
        """
        Get an iterator over the address range(s). Only defined data whose start
         addresses are contained in the given address set will be returned by the
         iterator.
        @param addrSet the address range set to iterate over.
        @param forward true means get iterator in forward direction
        @return a DataIterator that iterates over all defined Data objects in the
                 given address range set.
        """
        ...

    def getDefinedDataAfter(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        get the defined Data object that starts at an address that is greater
         than the given address.
        @param addr the address at which to begin the forward search.
        @return the next defined Data object whose starting address is greater
                 than addr.
        """
        ...

    def getDefinedDataAt(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        get the Data (defined) object that starts at the given address. If no
         Data object is defined at that address, then return null.
        @param addr The address to check for defined Data.
        @return a Data object that starts at addr, or null if no Data object has
                 been defined to start at addr.
        """
        ...

    def getDefinedDataBefore(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        get the closest defined Data object that starts at an address that is
         less than the given address.
        @param addr The address at which to begin the backward search.
        @return the closest defined Data object whose starting address is less
                 than addr.
        """
        ...

    def getDefinedDataContaining(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        get the Data object that starts at the given address. If no Data objects
         have been defined that contain that address, then return null.
        @param addr the address to check for containment in a defined Data
                    object.
        @return the defined Data object containing addr.
        """
        ...

    def getExternalFunctions(self) -> ghidra.program.model.listing.FunctionIterator:
        """
        Get an iterator over all external functions
        @return an iterator over all currently defined external functions.
        """
        ...

    def getFirstUndefinedData(self, set: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.listing.Data:
        """
        Get the undefined Data object that falls within the set. This operation
         can be slow for large programs so a TaskMonitor is required.
        @param set the addressSet at which to find the first undefined address.
        @param monitor a task monitor allowing this operation to be cancelled
        @return the next undefined Data object whose starting address falls
                 within the addresSet.
        """
        ...

    @overload
    def getFragment(self, treeName: unicode, name: unicode) -> ghidra.program.model.listing.ProgramFragment:
        """
        Returns the fragment with the given name.
         <P>
        @param treeName name of the tree to search
        @param name the name of the fragment to find.
        @return will return null if there is no fragment with the given name.
        """
        ...

    @overload
    def getFragment(self, treeName: unicode, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.ProgramFragment:
        """
        Returns the fragment containing the given address.
         <P>
        @param treeName name of the tree to search
        @param addr the address that is contained within a fragment.
        @return will return null if the address is not in the program.
        """
        ...

    def getFunctionAt(self, entryPoint: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Function:
        """
        Get a function with a given entry point.
        @param entryPoint entry point of the function
        @return function at the entry point
        """
        ...

    def getFunctionContaining(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Function:
        """
        Get a function containing an address.
        @param addr the address to search.
        @return function containing this address, null otherwise
        """
        ...

    @overload
    def getFunctions(self, forward: bool) -> ghidra.program.model.listing.FunctionIterator:
        """
        Get an iterator over all functions
        @param forward if true functions are return in address order, otherwise
                    backwards address order
        @return an iterator over all currently defined functions.
        """
        ...

    @overload
    def getFunctions(self, start: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.listing.FunctionIterator:
        """
        Get an iterator over all functions starting at address
        @param start the address to start iterating at.
        @param forward if true functions are return in address order, otherwise
                    backwards address order
        @return an iterator over functions
        """
        ...

    @overload
    def getFunctions(self, asv: ghidra.program.model.address.AddressSetView, forward: bool) -> ghidra.program.model.listing.FunctionIterator:
        """
        Get an iterator over all functions with entry points in the address set.
        @param asv the set of addresses to iterator function entry points over.
        @param forward if true functions are return in address order, otherwise
                    backwards address order
        @return an iterator over functions
        """
        ...

    @overload
    def getFunctions(self, namespace: unicode, name: unicode) -> List[ghidra.program.model.listing.Function]:
        """
        Returns a list of all functions with the given name in the given
         namespace.
        @param namespace the namespace to search for functions of the given name.
                    Can be null, in which case it will search the global
                    namespace.
        @param name the name of the functions to retrieve.
        @return a list of all global functions with the given name.
        """
        ...

    def getGlobalFunctions(self, name: unicode) -> List[ghidra.program.model.listing.Function]:
        """
        Returns a list of all global functions with the given name.
        @param name the name of the functions to retrieve.
        @return a list of all global functions with the given name.
        """
        ...

    def getInstructionAfter(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Instruction:
        """
        get the closest Instruction that starts at an address that is greater
         than the given address.
        @param addr The address at which to begin the forward search.
        @return the next Instruction whose starting address is greater than addr.
        """
        ...

    def getInstructionAt(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Instruction:
        """
        get the Instruction that starts at the given address. If no Instruction
         has been defined to start at that address, return null.
        @param addr the address to check for the start of an instruction
        @return the Instruction object that starts at addr; or null if no
                 Instructions starts at addr.
        """
        ...

    def getInstructionBefore(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Instruction:
        """
        get the closest Instruction that starts at an address that is less than
         the given address.
        @param addr The address at which to begin the backward search.
        @return the closest Instruction whose starting address is less than addr.
        """
        ...

    def getInstructionContaining(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Instruction:
        """
        get the Instruction that contains the given address. If an Instruction is
         defined that contains that address, it will be returned. Otherwise, null
         will be returned.
        @param addr the address to check for containment in an Instruction.
        @return the Instruction object that contains addr; or null if no
                 Instructions contain addr.
        """
        ...

    @overload
    def getInstructions(self, forward: bool) -> ghidra.program.model.listing.InstructionIterator:
        """
        get an Instruction iterator that will iterate over the entire address
         space.
        @param forward true means get iterator in forward direction
        @return an InstructionIterator that iterates over all instructions in the
                 program.
        """
        ...

    @overload
    def getInstructions(self, addr: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.listing.InstructionIterator:
        """
        Returns an iterator of the instructions in this listing (in proper
         sequence), starting at the specified address. The specified address
         indicates the first instruction that would be returned by an initial call
         to the <code>next</code> method. An initial call to the <code>previous</code>
         method would return the instruction with an address less than the
         specified address.
         <p>
        @param addr the initial position of the iterator
        @param forward true means get iterator in forward direction
        @return an InstructionIterator that iterates over all Instruction objects
                 in the given address range set.
        """
        ...

    @overload
    def getInstructions(self, addrSet: ghidra.program.model.address.AddressSetView, forward: bool) -> ghidra.program.model.listing.InstructionIterator:
        """
        Get an Instruction iterator over the address range(s). Only instructions
         whose start addresses are contained in the given address set will be
         returned by the iterator.
        @param addrSet the address range set to iterate over.
        @param forward true means get iterator in forward direction
        @return a DataIterator that iterates over all defined and undefined Data
                 objects in the given address range set.
        """
        ...

    def getModule(self, treeName: unicode, name: unicode) -> ghidra.program.model.listing.ProgramModule:
        """
        Returns the module with the given name.
         <P>
        @param treeName name of the tree to search
        @param name the name of the module to find.
        @return will return null if there is no module with the given name.
        """
        ...

    def getNumCodeUnits(self) -> long:
        """
        gets the total number of CodeUnits (Instructions, defined Data, and
         undefined Data)
        @return the total number of CodeUnits in the listing.
        """
        ...

    def getNumDefinedData(self) -> long:
        """
        gets the total number of defined Data objects in the listing.
        @return the total number of defined Data objects in the listing.
        """
        ...

    def getNumInstructions(self) -> long:
        """
        gets the total number of Instructions in the listing.
        @return number of Instructions
        """
        ...

    def getPropertyMap(self, propertyName: unicode) -> ghidra.program.model.util.PropertyMap:
        """
        Returns the PropertyMap associated with the given name
        @param propertyName the property name
        @return PropertyMap the propertyMap object.
        """
        ...

    @overload
    def getRootModule(self, treeID: long) -> ghidra.program.model.listing.ProgramModule:
        """
        Returns the root module of the program tree with the given name;
        @param treeID id of the program tree
        @return the root module of the specified tree.
        """
        ...

    @overload
    def getRootModule(self, treeName: unicode) -> ghidra.program.model.listing.ProgramModule:
        """
        Gets the root module for a tree in this listing.
        @param treeName name of tree
        @return the root module for the listing; returns null if there is no tree
                 rooted at a module with the given name.
        """
        ...

    def getTreeNames(self) -> List[unicode]:
        """
        Get the names of all the trees defined in this listing.
        @return the names of all program trees defined in the program.
        """
        ...

    def getUndefinedDataAfter(self, addr: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.listing.Data:
        """
        Get the undefined Data object that starts at an address that is greater
         than the given address. This operation can be slow for large programs so
         a TaskMonitor is required.
        @param addr the address at which to begin the forward search.
        @param monitor a task monitor allowing this operation to be cancelled
        @return the next undefined Data object whose starting address is greater
                 than addr.
        """
        ...

    def getUndefinedDataAt(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        get the Data (undefined) object that starts at the given address.
        @param addr The address to check for undefined data.
        @return a default DataObject if bytes exist at addr and nothing has been
                 defined to exist there. Otherwise returns null.
        """
        ...

    def getUndefinedDataBefore(self, addr: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.listing.Data:
        """
        get the closest undefined Data object that starts at an address that is
         less than the given address. This operation can be slow for large
         programs so a TaskMonitor is required.
        @param addr The address at which to begin the backward search.
        @param monitor a task monitor allowing this operation to be cancelled
        @return the closest undefined Data object whose starting address is less
                 than addr.
        """
        ...

    def getUndefinedRanges(self, set: ghidra.program.model.address.AddressSetView, initializedMemoryOnly: bool, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.address.AddressSetView:
        """
        Get the address set which corresponds to all undefined code units within
         the specified set of address.
        @param set set of addresses to search
        @param initializedMemoryOnly if true set will be constrained to
                    initialized memory areas, if false set will be constrained to
                    all defined memory blocks.
        @param monitor task monitor
        @return address set corresponding to undefined code units
        @throws CancelledException if monitor cancelled
        """
        ...

    def getUserDefinedProperties(self) -> Iterator[unicode]:
        """
        Returns an iterator over all user defined property names.
        @return an iterator over all user defined property names.
        """
        ...

    def hashCode(self) -> int: ...

    def isInFunction(self, addr: ghidra.program.model.address.Address) -> bool:
        """
        Check if an address is contained in a function
        @param addr address to test
        @return true if this address is in one or more functions
        """
        ...

    def isUndefined(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> bool:
        """
        Checks if the given ranges consists entirely of undefined data.
        @param start The start address of the range to check.
        @param end The end address of the range to check.
        @return boolean true if the given range is in memory and has no
                 instructions or defined data.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeFunction(self, entryPoint: ghidra.program.model.address.Address) -> None:
        """
        Remove a function a given entry point.
        @param entryPoint entry point of function to be removed.
        """
        ...

    def removeTree(self, treeName: unicode) -> bool:
        """
        Remove the tree rooted at the given name.
        @param treeName the name of the tree to remove.
        @return true if the tree was removed; return false if this is the last
                 tree for the program; cannot delete the last tree.
        """
        ...

    def removeUserDefinedProperty(self, propertyName: unicode) -> None:
        """
        Removes the entire property from the program
        @param propertyName the name of the property to remove.
        """
        ...

    def renameTree(self, oldName: unicode, newName: unicode) -> None:
        """
        Rename the tree. This method does not change the root module's name only
         the identifier for the tree.
        @param oldName old name of the tree
        @param newName new name of the tree.
        @throws DuplicateNameException if newName already exists for a root
                     module
        """
        ...

    def setComment(self, address: ghidra.program.model.address.Address, commentType: int, comment: unicode) -> None:
        """
        Set the comment for the given comment type at the specified address.
        @param address the address of the comment.
        @param commentType either EOL_COMMENT, PRE_COMMENT, POST_COMMENT,
                    PLATE_COMMENT, or REPEATABLE_COMMENT
        @param comment comment to set at the address
        @throws IllegalArgumentException if type is not one of the types of
                     comments supported
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
    def dataTypeManager(self) -> ghidra.program.model.data.DataTypeManager: ...

    @property
    def defaultRootModule(self) -> ghidra.program.model.listing.ProgramModule: ...

    @property
    def externalFunctions(self) -> ghidra.program.model.listing.FunctionIterator: ...

    @property
    def numCodeUnits(self) -> long: ...

    @property
    def numDefinedData(self) -> long: ...

    @property
    def numInstructions(self) -> long: ...

    @property
    def treeNames(self) -> List[unicode]: ...

    @property
    def userDefinedProperties(self) -> java.util.Iterator: ...
