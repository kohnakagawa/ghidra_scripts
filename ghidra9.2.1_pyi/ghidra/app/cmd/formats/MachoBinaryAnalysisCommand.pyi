from typing import List
import ghidra.app.plugin.core.analysis
import ghidra.app.util.importer
import ghidra.framework.cmd
import ghidra.framework.model
import ghidra.program.flatapi
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.program.model.mem
import ghidra.program.model.symbol
import ghidra.program.util.string
import ghidra.util.task
import java.io
import java.lang


class MachoBinaryAnalysisCommand(ghidra.program.flatapi.FlatProgramAPI, ghidra.framework.cmd.BinaryAnalysisCommand, ghidra.app.plugin.core.analysis.AnalysisWorker):




    @overload
    def __init__(self): ...

    @overload
    def __init__(self, address: ghidra.program.model.address.Address, module: ghidra.program.model.listing.ProgramModule): ...

    @overload
    def __init__(self, address: ghidra.program.model.address.Address, isRelativeToAddress: bool, module: ghidra.program.model.listing.ProgramModule): ...



    def addEntryPoint(self, address: ghidra.program.model.address.Address) -> None:
        """
        Adds an entry point at the specified address.
        @param address address to create entry point
        """
        ...

    def addInstructionXref(self, from_: ghidra.program.model.address.Address, to: ghidra.program.model.address.Address, opIndex: int, type: ghidra.program.model.symbol.FlowType) -> ghidra.program.model.symbol.Reference:
        """
        Adds a cross reference (XREF).
        @param from the source address of the reference
        @param to the destination address of the reference
        @param opIndex the operand index (-1 indicates the mnemonic)
        @param type the flow type
        @return the newly created reference
        @see ghidra.program.model.symbol.FlowType
        @see ghidra.program.model.symbol.Reference
        """
        ...

    def analysisWorkerCallback(self, program: ghidra.program.model.listing.Program, workerContext: object, monitor: ghidra.util.task.TaskMonitor) -> bool: ...

    def analyze(self, program: ghidra.program.model.listing.Program) -> None:
        """
        Starts auto-analysis on the specified program and performs complete analysis
         of the entire program.  This is usually only necessary if full analysis was never
         performed. This method will block until analysis completes.
        @param program the program to analyze
        @deprecated the method {@link #analyzeAll} or {@link #analyzeChanges} should be invoked.
         These separate methods were created to clarify their true behavior since many times it is
         only necessary to analyze changes and not the entire program which can take much
         longer and affect more of the program than is necessary.
        """
        ...

    def analyzeAll(self, program: ghidra.program.model.listing.Program) -> None:
        """
        Starts auto-analysis on the specified program and performs complete analysis
         of the entire program.  This is usually only necessary if full analysis was never
         performed. This method will block until analysis completes.
        @param program the program to analyze
        """
        ...

    def analyzeChanges(self, program: ghidra.program.model.listing.Program) -> None:
        """
        Starts auto-analysis if not started and waits for pending analysis to complete.
         Only pending analysis on program changes is performed, including changes resulting
         from any analysis activity.  This method will block until analysis completes.
         NOTE: The auto-analysis manager will only detect program changes once it has been
         instantiated for a program (i.e, AutoAnalysisManager.getAnalysisManager(program) ).
         This is automatically done for the initial currentProgram, however, if a script is
         opening/instantiating its own programs it may be necessary to do this prior to
         making changes to the program.
        @param program the program to analyze
        """
        ...

    def applyTo(self, program: ghidra.program.model.listing.Program, monitor: ghidra.util.task.TaskMonitor) -> bool: ...

    def canApply(self, program: ghidra.program.model.listing.Program) -> bool: ...

    @overload
    def clearListing(self, address: ghidra.program.model.address.Address) -> None:
        """
        Clears the code unit (instruction or data) defined at the address.
        @param address the address to clear the code unit
        @throws CancelledException
        """
        ...

    @overload
    def clearListing(self, set: ghidra.program.model.address.AddressSetView) -> None:
        """
        Clears the code units (instructions or data) in the specified set
        @param set the set to clear
        @throws CancelledException
        """
        ...

    @overload
    def clearListing(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> None:
        """
        Clears the code units (instructions or data) in the specified range.
        @param start the start address
        @param end the end address
        @throws CancelledException
        """
        ...

    @overload
    def clearListing(self, set: ghidra.program.model.address.AddressSetView, code: bool, symbols: bool, comments: bool, properties: bool, functions: bool, registers: bool, equates: bool, userReferences: bool, analysisReferences: bool, importReferences: bool, defaultReferences: bool, bookmarks: bool) -> bool:
        """
        Clears the listing in the specified address set.
        @param set the address set where to clear
        @param code true if code units should be cleared (instructions and defined data)
        @param symbols true if symbols should be cleared
        @param comments true if comments should be cleared
        @param properties true if properties should be cleared
        @param functions true if functions should be cleared
        @param registers true if registers should be cleared
        @param equates true if equates should be cleared
        @param userReferences true if user references should be cleared
        @param analysisReferences true if analysis references should be cleared
        @param importReferences true if import references should be cleared
        @param defaultReferences true if default references should be cleared
        @param bookmarks true if bookmarks should be cleared
        @return true if the address set was successfully cleared
        """
        ...

    def createAddressSet(self) -> ghidra.program.model.address.AddressSet:
        """
        Creates a new mutable address set.
        @return a new mutable address set
        """
        ...

    @overload
    def createAsciiString(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        Creates a null terminated ascii string starting
         at the specified address.
        @param address the address to create the string
        @return the newly created Data object
        """
        ...

    @overload
    def createAsciiString(self, address: ghidra.program.model.address.Address, length: int) -> ghidra.program.model.listing.Data:
        """
        Create an ASCII string at the specified address.
        @param address
        @param length length of string (a value of 0 or negative will force use
         of dynamic null terminated string)
        @return string data created
        @throws CodeUnitInsertionException
        @throws DataTypeConflictException
        """
        ...

    def createBookmark(self, address: ghidra.program.model.address.Address, category: unicode, note: unicode) -> ghidra.program.model.listing.Bookmark:
        """
        Creates a <code>NOTE</code> bookmark at the specified address
         <br>
         NOTE: if a <code>NOTE</code> bookmark already exists at the address, it will be replaced.
         This is intentional and is done to match the behavior of setting bookmarks from the UI.
        @param address the address to create the bookmark
        @param category the bookmark category (it may be null)
        @param note the bookmark text
        @return the newly created bookmark
        """
        ...

    def createByte(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        Creates a byte datatype at the given address.
        @param address the address to create the byte
        @return the newly created Data object
        """
        ...

    def createChar(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        Creates a char datatype at the given address.
        @param address the address to create the char
        @return the newly created Data object
        """
        ...

    def createDWord(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        Creates a dword datatype at the given address.
        @param address the address to create the dword
        @return the newly created Data object
        """
        ...

    def createData(self, address: ghidra.program.model.address.Address, datatype: ghidra.program.model.data.DataType) -> ghidra.program.model.listing.Data:
        """
        Creates a new defined Data object at the given address.
        @param address the address at which to create a new Data object.
        @param datatype the Data Type that describes the type of Data object to create.
        @return the newly created Data object
        """
        ...

    def createDouble(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        Creates a double datatype at the given address.
        @param address the address to create the double
        @return the newly created Data object
        """
        ...

    def createDwords(self, start: ghidra.program.model.address.Address, count: int) -> None:
        """
        Creates a list of dword datatypes starting at the given address.
        @param start the start address to create the dwords
        @param count the number of dwords to create
        """
        ...

    @overload
    def createEquate(self, data: ghidra.program.model.listing.Data, equateName: unicode) -> ghidra.program.model.symbol.Equate:
        """
        Creates a new equate on the scalar value
         at the value of the data.
        @param data the data
        @param equateName the name of the equate
        @return the newly created equate
        @throws InvalidInputException if a scalar does not exist on the data
        """
        ...

    @overload
    def createEquate(self, instruction: ghidra.program.model.listing.Instruction, operandIndex: int, equateName: unicode) -> ghidra.program.model.symbol.Equate:
        """
        Creates a new equate on the scalar value
         at the operand index of the instruction.
        @param instruction the instruction
        @param operandIndex the operand index on the instruction
        @param equateName the name of the equate
        @return the newly created equate
        @throws Exception if a scalar does not exist of the specified
         operand index of the instruction
        """
        ...

    @overload
    def createExternalReference(self, data: ghidra.program.model.listing.Data, libraryName: unicode, externalLabel: unicode, externalAddr: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.Reference:
        """
        Creates an external reference from the given data.  The reference type {@link RefType#DATA}
         will be used.
        @param data the data
        @param libraryName the name of the library being referred
        @param externalLabel the name of function in the library being referred
        @param externalAddr the address of the function in the library being referred
        @return the newly created external reference
        @throws Exception if an exception occurs
        """
        ...

    @overload
    def createExternalReference(self, instruction: ghidra.program.model.listing.Instruction, operandIndex: int, libraryName: unicode, externalLabel: unicode, externalAddr: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.Reference:
        """
        Creates an external reference from the given instruction.
         For instructions with flow, the FlowType will be assumed, otherwise
         {@link RefType#DATA} will be assumed.  To specify the appropriate
         RefType use the alternate form of this method.
        @param instruction the instruction
        @param operandIndex the operand index on the instruction
        @param libraryName the name of the library being referred
        @param externalLabel the name of function in the library being referred
        @param externalAddr the address of the function in the library being referred
        @return the newly created external reference
        @throws Exception if an exception occurs
        """
        ...

    @overload
    def createExternalReference(self, instruction: ghidra.program.model.listing.Instruction, operandIndex: int, libraryName: unicode, externalLabel: unicode, externalAddr: ghidra.program.model.address.Address, refType: ghidra.program.model.symbol.RefType) -> ghidra.program.model.symbol.Reference:
        """
        Creates an external reference from the given instruction.
        @param instruction the instruction
        @param operandIndex the operand index on the instruction
        @param libraryName the name of the library being referred
        @param externalLabel the name of function in the library being referred
        @param externalAddr the address of the function in the library being referred
        @param refType the appropriate external reference type (e.g., DATA, COMPUTED_CALL, etc.)
        @return the newly created external reference
        @throws Exception if an exception occurs
        """
        ...

    def createFloat(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        Creates a float datatype at the given address.
        @param address the address to create the float
        @return the newly created Data object
        """
        ...

    @overload
    def createFragment(self, fragmentName: unicode, start: ghidra.program.model.address.Address, length: long) -> ghidra.program.model.listing.ProgramFragment:
        """
        Creates a fragment in the root folder of the default program tree.
        @param fragmentName the name of the fragment
        @param start the start address
        @param length the length of the fragment
        @return the newly created fragment
        @throws DuplicateNameException if the given fragment name already exists
        @throws NotFoundException if any address in the fragment would be outside of the program
        """
        ...

    @overload
    def createFragment(self, fragmentName: unicode, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> ghidra.program.model.listing.ProgramFragment:
        """
        Creates a fragment in the root folder of the default program tree.
        @param fragmentName the name of the fragment
        @param start the start address
        @param end the end address (NOT INCLUSIVE)
        @return the newly created fragment
        @throws DuplicateNameException if the given fragment name already exists
        @throws NotFoundException if any address in the fragment would be outside of the program
        @deprecated This method is deprecated because it did not allow you to include the
         largest possible address.  Instead use the one that takes a start address and a length.
        """
        ...

    @overload
    def createFragment(self, module: ghidra.program.model.listing.ProgramModule, fragmentName: unicode, start: ghidra.program.model.address.Address, length: long) -> ghidra.program.model.listing.ProgramFragment:
        """
        Creates a fragment in the given folder of the default program tree.
        @param module the parent module (or folder)
        @param fragmentName the name of the fragment
        @param start the start address
        @param length the length of the fragment
        @return the newly created fragment
        @throws DuplicateNameException if the given fragment name already exists
        @throws NotFoundException if any address in the fragment would be outside of the program
        """
        ...

    @overload
    def createFragment(self, module: ghidra.program.model.listing.ProgramModule, fragmentName: unicode, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> ghidra.program.model.listing.ProgramFragment:
        """
        Creates a fragment in the given folder of the default program tree.
        @param module the parent module (or folder)
        @param fragmentName the name of the fragment
        @param start the start address
        @param end the end address (NOT INCLUSIVE)
        @return the newly created fragment
        @throws DuplicateNameException if the given fragment name already exists
        @throws NotFoundException if any address in the fragment would be outside of the program
        @deprecated This method is deprecated because it did not allow you to include the
         largest possible address.  Instead use the one that takes a start address and a length.
        """
        ...

    def createFunction(self, entryPoint: ghidra.program.model.address.Address, name: unicode) -> ghidra.program.model.listing.Function:
        """
        Creates a function at entry point with the specified name
        @param entryPoint the entry point of the function
        @param name the name of the function or null for a default function
        @return the new function or null if the function was not created
        """
        ...

    @overload
    def createLabel(self, address: ghidra.program.model.address.Address, name: unicode, makePrimary: bool) -> ghidra.program.model.symbol.Symbol:
        """
        Creates a label at the specified address in the global namespace.
         If makePrimary==true, then the new label is made primary.
        @param address the address to create the symbol
        @param name the name of the symbol
        @param makePrimary true if the symbol should be made primary
        @return the newly created code or function symbol
        """
        ...

    @overload
    def createLabel(self, address: ghidra.program.model.address.Address, name: unicode, makePrimary: bool, sourceType: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.symbol.Symbol:
        """
        Creates a label at the specified address in the global namespace.
         If makePrimary==true, then the new label is made primary.
         If makeUnique==true, then if the name is a duplicate, the address
         will be concatenated to name to make it unique.
        @param address the address to create the symbol
        @param name the name of the symbol
        @param makePrimary true if the symbol should be made primary
        @param sourceType the source type.
        @return the newly created code or function symbol
        """
        ...

    @overload
    def createLabel(self, address: ghidra.program.model.address.Address, name: unicode, namespace: ghidra.program.model.symbol.Namespace, makePrimary: bool, sourceType: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.symbol.Symbol:
        """
        Creates a label at the specified address in the specified namespace.
         If makePrimary==true, then the new label is made primary if permitted.
         If makeUnique==true, then if the name is a duplicate, the address
         will be concatenated to name to make it unique.
        @param address the address to create the symbol
        @param name the name of the symbol
        @param namespace label's parent namespace
        @param makePrimary true if the symbol should be made primary
        @param sourceType the source type.
        @return the newly created code or function symbol
        """
        ...

    @overload
    def createMemoryBlock(self, name: unicode, start: ghidra.program.model.address.Address, bytes: List[int], overlay: bool) -> ghidra.program.model.mem.MemoryBlock:
        """
        Create a new memory block.
        @param name the name of the block
        @param start start address of the block
        @param bytes the bytes of the memory block
        @param overlay true will create an overlay, false will not
        @return the newly created memory block
        """
        ...

    @overload
    def createMemoryBlock(self, name: unicode, start: ghidra.program.model.address.Address, input: java.io.InputStream, length: long, overlay: bool) -> ghidra.program.model.mem.MemoryBlock:
        """
        Create a new memory block.
         If the input stream is null, then an uninitialized block will be created.
        @param name the name of the block
        @param start start address of the block
        @param input source of the data used to fill the block.
        @param length the size of the block
        @param overlay true will create an overlay, false will not
        @return the newly created memory block
        """
        ...

    @overload
    def createMemoryReference(self, data: ghidra.program.model.listing.Data, toAddress: ghidra.program.model.address.Address, dataRefType: ghidra.program.model.symbol.RefType) -> ghidra.program.model.symbol.Reference:
        """
        Creates a memory reference from the given data.
        @param data the data
        @param toAddress the TO address
        @param dataRefType the type of the reference
        @return the newly created memory reference
        """
        ...

    @overload
    def createMemoryReference(self, instruction: ghidra.program.model.listing.Instruction, operandIndex: int, toAddress: ghidra.program.model.address.Address, flowType: ghidra.program.model.symbol.RefType) -> ghidra.program.model.symbol.Reference:
        """
        Creates a memory reference from the given instruction.
        @param instruction the instruction
        @param operandIndex the operand index on the instruction
        @param toAddress the TO address
        @param flowType the flow type of the reference
        @return the newly created memory reference
        """
        ...

    def createQWord(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        Creates a qword datatype at the given address.
        @param address the address to create the qword
        @return the newly created Data object
        """
        ...

    def createStackReference(self, instruction: ghidra.program.model.listing.Instruction, operandIndex: int, stackOffset: int, isWrite: bool) -> ghidra.program.model.symbol.Reference:
        """
        Create a stack reference from the given instruction
        @param instruction the instruction
        @param operandIndex the operand index on the instruction
        @param stackOffset the stack offset of the reference
        @param isWrite true if the reference is WRITE access or false if the
         reference is READ access
        @return the newly created stack reference
        """
        ...

    @overload
    def createSymbol(self, address: ghidra.program.model.address.Address, name: unicode, makePrimary: bool) -> ghidra.program.model.symbol.Symbol:
        """
        @deprecated use {@link #createLabel(Address, String, boolean)} instead.
         Deprecated in Ghidra 7.4
        """
        ...

    @overload
    def createSymbol(self, address: ghidra.program.model.address.Address, name: unicode, makePrimary: bool, makeUnique: bool, sourceType: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.symbol.Symbol:
        """
        @deprecated use {@link #createLabel(Address, String, boolean, SourceType)} instead. Deprecated in Ghidra 7.4
        """
        ...

    def createUnicodeString(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        Creates a null terminated unicode string starting
         at the specified address.
        @param address the address to create the string
        @return the newly created Data object
        @throws Exception
        """
        ...

    def createWord(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        Creates a word datatype at the given address.
        @param address the address to create the word
        @return the newly created Data object
        """
        ...

    def disassemble(self, address: ghidra.program.model.address.Address) -> bool:
        """
        Start disassembling at the specified address.
         The disassembler will follow code flows.
        @param address the address to begin disassembling
        @return true if the program was successfully disassembled
        """
        ...

    def end(self, commit: bool) -> None:
        """
        Ends the transactions on the current program.
        @param commit true if changes should be committed
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @overload
    def find(self, text: unicode) -> ghidra.program.model.address.Address:
        """
        Finds the first occurrence of 'text' in the program listing.
         The search order is defined as:
         <ol>
         <li>PLATE comments</li>
         <li>PRE comments</li>
         <li>labels</li>
         <li>code unit mnemonics and operands</li>
         <li>EOL comments</li>
         <li>repeatable comments</li>
         <li>POST comments</li>
         </ol>
        @param text the text to search for
        @return the first address where the 'text' was found, or null
          if the text was not found
        """
        ...

    @overload
    def find(self, start: ghidra.program.model.address.Address, value: int) -> ghidra.program.model.address.Address:
        """
        Finds the first occurrence of the byte
         starting from the address. If the start address
         is null, then the find will start from the minimum address
         of the program.
        @param start the address to start searching
        @param value the byte to search for
        @return the first address where the byte was found
        """
        ...

    @overload
    def find(self, start: ghidra.program.model.address.Address, values: List[int]) -> ghidra.program.model.address.Address:
        """
        Finds the first occurrence of the byte array sequence
         starting from the address. If the start address
         is null, then the find will start from the minimum address
         of the program.
        @param start the address to start searching
        @param values the byte array sequence to search for
        @return the first address where the byte was found, or
         null if the bytes were not found
        """
        ...

    @overload
    def findBytes(self, start: ghidra.program.model.address.Address, byteString: unicode) -> ghidra.program.model.address.Address:
        """
        Finds the first occurrence of the byte array sequence that matches the given byte string,
         starting from the address. If the start address is null, then the find will start
         from the minimum address of the program.
         <p>
         The <code>byteString</code> may contain regular expressions.  The following
         highlights some example search strings (note the use of double backslashes ("\\")):
         <pre>
                     "\\x80" - A basic search pattern for a byte value of 0x80
         "\\x50.{0,10}\\x55" - A regular expression string that searches for the byte 0x50
                               followed by 0-10 occurrences of any byte value, followed
                               by the byte 0x55
         </pre>
        @param start the address to start searching.  If null, then the start of the program
                will be used.
        @param byteString the byte pattern for which to search
        @return the first address where the byte was found, or null if the bytes were not found
        @throws IllegalArgumentException if the byteString is not a valid regular expression
        @see #findBytes(Address, String, int)
        """
        ...

    @overload
    def findBytes(self, start: ghidra.program.model.address.Address, byteString: unicode, matchLimit: int) -> List[ghidra.program.model.address.Address]:
        """
        Finds the first {@code <matchLimit>} occurrences of the byte array sequence that matches
         the given byte string, starting from the address. If the start address is null, then the
         find will start from the minimum address of the program.
         <p>
         The <code>byteString</code> may contain regular expressions.  The following
         highlights some example search strings (note the use of double backslashes ("\\")):
         <pre>
                     "\\x80" - A basic search pattern for a byte value of 0x80
         "\\x50.{0,10}\\x55" - A regular expression string that searches for the byte 0x50
                               followed by 0-10 occurrences of any byte value, followed
                               by the byte 0x55
         </pre>
        @param start the address to start searching.  If null, then the start of the program
                will be used.
        @param byteString the byte pattern for which to search
        @param matchLimit The number of matches to which the search should be restricted
        @return the start addresses that contain byte patterns that match the given byteString
        @throws IllegalArgumentException if the byteString is not a valid regular expression
        @see #findBytes(Address, String)
        """
        ...

    @overload
    def findBytes(self, start: ghidra.program.model.address.Address, byteString: unicode, matchLimit: int, alignment: int) -> List[ghidra.program.model.address.Address]:
        """
        Finds the first {@code <matchLimit>} occurrences of the byte array sequence that matches
         the given byte string, starting from the address. If the start address is null, then the
         find will start from the minimum address of the program.
         <p>
         The <code>byteString</code> may contain regular expressions.  The following
         highlights some example search strings (note the use of double backslashes ("\\")):
         <pre>
                     "\\x80" - A basic search pattern for a byte value of 0x80
         "\\x50.{0,10}\\x55" - A regular expression string that searches for the byte 0x50
                               followed by 0-10 occurrences of any byte value, followed
                               by the byte 0x55
         </pre>
        @param start the address to start searching.  If null, then the start of the program
                will be used.
        @param byteString the byte pattern for which to search
        @param matchLimit The number of matches to which the search should be restricted
        @param alignment byte alignment to use for search starts. For example, a value of
            1 searches from every byte.  A value of 2 only matches runs that begin on a even
            address boundary.
        @return the start addresses that contain byte patterns that match the given byteString
        @throws IllegalArgumentException if the byteString is not a valid regular expression
        @see #findBytes(Address, String)
        """
        ...

    @overload
    def findBytes(self, set: ghidra.program.model.address.AddressSetView, byteString: unicode, matchLimit: int, alignment: int) -> List[ghidra.program.model.address.Address]:
        """
        Finds a byte pattern within an addressSet.

         Note: The ranges within the addressSet are NOT treated as a contiguous set when searching
         <p>
         The <code>byteString</code> may contain regular expressions.  The following
         highlights some example search strings (note the use of double backslashes ("\\")):
         <pre>
                     "\\x80" - A basic search pattern for a byte value of 0x80
         "\\x50.{0,10}\\x55" - A regular expression string that searches for the byte 0x50
                               followed by 0-10 occurrences of any byte value, followed
                               by the byte 0x55
         </pre>
        @param set the addressSet specifying which addresses to search.
        @param byteString the byte pattern for which to search
        @param matchLimit The number of matches to which the search should be restricted
        @param alignment byte alignment to use for search starts. For example, a value of
            1 searches from every byte.  A value of 2 only matches runs that begin on a even
            address boundary.
        @return the start addresses that contain byte patterns that match the given byteString
        @throws IllegalArgumentException if the byteString is not a valid regular expression
        @see #findBytes(Address, String)
        """
        ...

    @overload
    def findBytes(self, set: ghidra.program.model.address.AddressSetView, byteString: unicode, matchLimit: int, alignment: int, searchAcrossAddressGaps: bool) -> List[ghidra.program.model.address.Address]:
        """
        Finds a byte pattern within an addressSet.

         Note: When searchAcrossAddressGaps is set to true, the ranges within the addressSet are
         treated as a contiguous set when searching.

         <p>
         The <code>byteString</code> may contain regular expressions.  The following
         highlights some example search strings (note the use of double backslashes ("\\")):
         <pre>
                     "\\x80" - A basic search pattern for a byte value of 0x80
         "\\x50.{0,10}\\x55" - A regular expression string that searches for the byte 0x50
                               followed by 0-10 occurrences of any byte value, followed
                               by the byte 0x55
         </pre>
        @param set the addressSet specifying which addresses to search.
        @param byteString the byte pattern for which to search
        @param matchLimit The number of matches to which the search should be restricted
        @param alignment byte alignment to use for search starts. For example, a value of
                1 searches from every byte.  A value of 2 only matches runs that begin on a even
                address boundary.
        @param searchAcrossAddressGaps when set to 'true' searches for matches across the gaps
                of each addressRange contained in the addresSet.
        @return the start addresses that contain byte patterns that match the given byteString
        @throws IllegalArgumentException if the byteString is not a valid regular expression
        @see #findBytes(Address, String)
        """
        ...

    def findPascalStrings(self, addressSet: ghidra.program.model.address.AddressSetView, minimumStringLength: int, alignment: int, includePascalUnicode: bool) -> List[ghidra.program.util.string.FoundString]:
        """
        Search for sequences of Pascal Ascii strings in program memory.  See {@link AsciiCharSetRecognizer}
         to see exactly what chars are considered ASCII for purposes of this search.
        @param addressSet The address set to search. Use null to search all memory;
        @param minimumStringLength The smallest number of chars in a sequence to be considered a "string".
        @param alignment specifies any alignment requirements for the start of the string.  An alignment
         of 1, means the string can start at any address.  An alignment of 2 means the string must
         start on an even address and so on.  Only allowed values are 1,2, and 4.
        @param includePascalUnicode if true, UTF16 size strings will be included in addition to UTF8.
        @return a list of "FoundString" objects which contain the addresses, length, and type of possible strings.
        """
        ...

    def findStrings(self, addressSet: ghidra.program.model.address.AddressSetView, minimumStringLength: int, alignment: int, requireNullTermination: bool, includeAllCharWidths: bool) -> List[ghidra.program.util.string.FoundString]:
        """
        Search for sequences of Ascii strings in program memory.  See {@link AsciiCharSetRecognizer}
         to see exactly what chars are considered ASCII for purposes of this search.
        @param addressSet The address set to search. Use null to search all memory;
        @param minimumStringLength The smallest number of chars in a sequence to be considered a "string".
        @param alignment specifies any alignment requirements for the start of the string.  An alignment
         of 1, means the string can start at any address.  An alignment of 2 means the string must
         start on an even address and so on.  Only allowed values are 1,2, and 4.
        @param requireNullTermination If true, only strings that end in a null will be returned.
        @param includeAllCharWidths if true, UTF16 and UTF32 size strings will be included in addition to UTF8.
        @return a list of "FoundString" objects which contain the addresses, length, and type of possible strings.
        """
        ...

    def getAddressFactory(self) -> ghidra.program.model.address.AddressFactory: ...

    def getBookmarks(self, address: ghidra.program.model.address.Address) -> List[ghidra.program.model.listing.Bookmark]:
        """
        Returns all of the NOTE bookmarks defined at the specified address
        @param address the address to retrieve the bookmark
        @return the bookmarks at the specified address
        """
        ...

    def getByte(self, address: ghidra.program.model.address.Address) -> int:
        """
        Returns the 'byte' value at the specified address in memory.
        @param address the address
        @return the 'byte' value at the specified address in memory
        @throws MemoryAccessException if the memory is not readable
        """
        ...

    def getBytes(self, address: ghidra.program.model.address.Address, length: int) -> List[int]:
        """
        Reads length number of bytes starting at the specified address.
         Note: this could be inefficient if length is large
        @param address the address to start reading
        @param length the number of bytes to read
        @return an array of bytes
        @throws MemoryAccessException if memory does not exist or is uninitialized
        @see ghidra.program.model.mem.Memory
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getCurrentProgram(self) -> ghidra.program.model.listing.Program:
        """
        Gets the current program.
        @return the program
        """
        ...

    @overload
    def getDataAfter(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        Returns the defined data after the specified address or null if no data exists.
        @param address the data address
        @return the defined data after the specified address or null if no data exists
        """
        ...

    @overload
    def getDataAfter(self, data: ghidra.program.model.listing.Data) -> ghidra.program.model.listing.Data:
        """
        Returns the defined data after the specified data or null if no data exists.
        @param data preceeding data
        @return the defined data after the specified data or null if no data exists
        """
        ...

    def getDataAt(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        Returns the defined data at the specified address or null if no data exists.
        @param address the data address
        @return the data at the specified address or null if no data exists
        """
        ...

    @overload
    def getDataBefore(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        Returns the defined data before the specified address or null if no data exists.
        @param address the data address
        @return the defined data before the specified address or null if no data exists
        """
        ...

    @overload
    def getDataBefore(self, data: ghidra.program.model.listing.Data) -> ghidra.program.model.listing.Data:
        """
        Returns the defined data before the specified data or null if no data exists.
        @param data the succeeding data
        @return the defined data before the specified data or null if no data exists
        """
        ...

    def getDataContaining(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        Returns the defined data containing the specified address or null if no data exists.
        @param address the data address
        @return the defined data containing the specified address or null if no data exists
        """
        ...

    def getDataTypes(self, name: unicode) -> List[ghidra.program.model.data.DataType]:
        """
        Searches through the datatype manager of the current program and
         returns an array of datatypes that match the specified name.
         The datatype manager supports datatypes of the same name in different categories.
         A zero-length array indicates that no datatypes with the specified name exist.
        @param name the name of the desired datatype
        @return an array of datatypes that match the specified name
        """
        ...

    def getDouble(self, address: ghidra.program.model.address.Address) -> float:
        """
        Returns the 'double' value at the specified address in memory.
        @param address the address
        @return the 'double' value at the specified address in memory
        @throws MemoryAccessException if the memory is not readable
        """
        ...

    def getEOLComment(self, address: ghidra.program.model.address.Address) -> unicode:
        """
        Returns the EOL comment at the specified address.  The comment returned is the raw text
         of the comment.  Contrastingly, calling {@link GhidraScript#getEOLCommentAsRendered(Address)} will
         return the text of the comment as it is rendered in the display.
        @param address the address to get the comment
        @return the EOL comment at the specified address or null
         if one does not exist
        @see GhidraScript#getEOLCommentAsRendered(Address)
        """
        ...

    @overload
    def getEquate(self, data: ghidra.program.model.listing.Data) -> ghidra.program.model.symbol.Equate:
        """
        Returns the equate defined on the data.
        @param data the data
        @return the equate defined on the data
        """
        ...

    @overload
    def getEquate(self, instruction: ghidra.program.model.listing.Instruction, operandIndex: int) -> ghidra.program.model.symbol.Equate:
        """
        Returns the equate defined at the operand index of the instruction.
        @param instruction the instruction
        @param operandIndex the operand index
        @return the equate defined at the operand index of the instruction
        @deprecated this form of getEquate is not supported and will throw a UnsupportedOperationException
        """
        ...

    @overload
    def getEquate(self, instruction: ghidra.program.model.listing.Instruction, operandIndex: int, value: long) -> ghidra.program.model.symbol.Equate:
        """
        Returns the equate defined at the operand index of the instruction with the given value.
        @param instruction the instruction
        @param operandIndex the operand index
        @param value scalar equate value
        @return the equate defined at the operand index of the instruction
        """
        ...

    def getEquates(self, instruction: ghidra.program.model.listing.Instruction, operandIndex: int) -> List[ghidra.program.model.symbol.Equate]:
        """
        Returns the equates defined at the operand index of the instruction.
        @param instruction the instruction
        @param operandIndex the operand index
        @return the equate defined at the operand index of the instruction
        """
        ...

    def getFirstData(self) -> ghidra.program.model.listing.Data:
        """
        Returns the first defined data in the current program.
        @return the first defined data in the current program
        """
        ...

    def getFirstFunction(self) -> ghidra.program.model.listing.Function:
        """
        Returns the first function in the current program.
        @return the first function in the current program
        """
        ...

    @overload
    def getFirstInstruction(self) -> ghidra.program.model.listing.Instruction:
        """
        Returns the first instruction in the current program.
        @return the first instruction in the current program
        """
        ...

    @overload
    def getFirstInstruction(self, function: ghidra.program.model.listing.Function) -> ghidra.program.model.listing.Instruction:
        """
        Returns the first instruction in the function.
        @return the first instruction in the function
        """
        ...

    def getFloat(self, address: ghidra.program.model.address.Address) -> float:
        """
        Returns the 'float' value at the specified address in memory.
        @param address the address
        @return the 'float' value at the specified address in memory
        @throws MemoryAccessException if the memory is not readable
        """
        ...

    def getFragment(self, module: ghidra.program.model.listing.ProgramModule, fragmentName: unicode) -> ghidra.program.model.listing.ProgramFragment:
        """
        Returns the fragment with the specified name
         defined in the given module.
        @param module the parent module
        @param fragmentName the fragment name
        @return the fragment or null if one does not exist
        """
        ...

    def getFunction(self, name: unicode) -> ghidra.program.model.listing.Function:
        """
        Returns the function with the specified name, or
         null if no function exists. (Now returns the first one it finds with that name)
        @param name the name of the function
        @return the function with the specified name, or
         null if no function exists
        @deprecated this method makes no sense in the new world order where function  names
         			   no longer have to be unique. Use {@link #getGlobalFunctions(String)}
         			   Deprecated in Ghidra 7.4
        """
        ...

    @overload
    def getFunctionAfter(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Function:
        """
        Returns the function defined after the specified address.
        @param address the address
        @return the function defined after the specified address
        """
        ...

    @overload
    def getFunctionAfter(self, function: ghidra.program.model.listing.Function) -> ghidra.program.model.listing.Function:
        """
        Returns the function defined before the specified function in address order.
        @param function the function
        @return the function defined before the specified function
        """
        ...

    def getFunctionAt(self, entryPoint: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Function:
        """
        Returns the function with the specified entry point, or
         null if no function exists.
        @param entryPoint the function entry point address
        @return the function with the specified entry point, or
         null if no function exists
        """
        ...

    @overload
    def getFunctionBefore(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Function:
        """
        Returns the function defined before the specified address.
        @param address the address
        @return the function defined before the specified address
        """
        ...

    @overload
    def getFunctionBefore(self, function: ghidra.program.model.listing.Function) -> ghidra.program.model.listing.Function:
        """
        Returns the function defined before the specified function in address order.
        @param function the function
        @return the function defined before the specified function
        """
        ...

    def getFunctionContaining(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Function:
        """
        Returns the function containing the specified address.
        @param address the address
        @return the function containing the specified address
        """
        ...

    def getGlobalFunctions(self, name: unicode) -> List[ghidra.program.model.listing.Function]:
        """
        Returns a list of all functions in the global namespace with the given name.
        @param name the name of the function
        @return the function with the specified name, or
        """
        ...

    @overload
    def getInstructionAfter(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Instruction:
        """
        Returns the instruction defined after the specified address or null
         if no instruction exists.
         The instruction that is returned does not have to be contiguous.
        @param address the address of the prior instruction
        @return the instruction defined after the specified address or null if no instruction exists
        """
        ...

    @overload
    def getInstructionAfter(self, instruction: ghidra.program.model.listing.Instruction) -> ghidra.program.model.listing.Instruction:
        """
        Returns the instruction defined after the specified instruction or null
         if no instruction exists.
         The instruction that is returned does not have to be contiguous.
        @param instruction the instruction
        @return the instruction defined after the specified instruction or null if no instruction exists
        """
        ...

    def getInstructionAt(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Instruction:
        """
        Returns the instruction at the specified address or null if no instruction exists.
        @param address the instruction address
        @return the instruction at the specified address or null if no instruction exists
        """
        ...

    @overload
    def getInstructionBefore(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Instruction:
        """
        Returns the instruction defined before the specified address or null
         if no instruction exists.
         The instruction that is returned does not have to be contiguous.
        @param address the address of the instruction
        @return the instruction defined before the specified address or null if no instruction exists
        """
        ...

    @overload
    def getInstructionBefore(self, instruction: ghidra.program.model.listing.Instruction) -> ghidra.program.model.listing.Instruction:
        """
        Returns the instruction defined before the specified instruction or null
         if no instruction exists.
         The instruction that is returned does not have to be contiguous.
        @param instruction the instruction
        @return the instruction defined before the specified instruction or null if no instruction exists
        """
        ...

    def getInstructionContaining(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Instruction:
        """
        Returns the instruction containing the specified address or null if no instruction exists.
        @param address the instruction address
        @return the instruction containing the specified address or null if no instruction exists
        """
        ...

    def getInt(self, address: ghidra.program.model.address.Address) -> int:
        """
        Returns the 'integer' value at the specified address in memory.
        @param address the address
        @return the 'integer' value at the specified address in memory
        @throws MemoryAccessException if the memory is not readable
        """
        ...

    def getLastData(self) -> ghidra.program.model.listing.Data:
        """
        Returns the last defined data in the current program.
        @return the last defined data in the current program
        """
        ...

    def getLastFunction(self) -> ghidra.program.model.listing.Function:
        """
        Returns the last function in the current program.
        @return the last function in the current program
        """
        ...

    def getLastInstruction(self) -> ghidra.program.model.listing.Instruction:
        """
        Returns the last instruction in the current program.
        @return the last instruction in the current program
        """
        ...

    def getLong(self, address: ghidra.program.model.address.Address) -> long:
        """
        Returns the 'long' value at the specified address in memory.
        @param address the address
        @return the 'long' value at the specified address in memory
        @throws MemoryAccessException if the memory is not readable
        """
        ...

    @overload
    def getMemoryBlock(self, name: unicode) -> ghidra.program.model.mem.MemoryBlock:
        """
        Returns the first memory block with the specified name.
         NOTE: if more than block exists with the same name, the first
         block with that name will be returned.
        @param name the name of the requested block
        @return the the memory block with the specified name
        """
        ...

    @overload
    def getMemoryBlock(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.mem.MemoryBlock:
        """
        Returns the memory block containing the specified address,
         or null if no memory block contains the address.
        @param address the address
        @return the memory block containing the specified address
        """
        ...

    def getMemoryBlocks(self) -> List[ghidra.program.model.mem.MemoryBlock]:
        """
        Returns an array containing all the memory blocks
         in the current program.
        @return an array containing all the memory blocks
        """
        ...

    def getMessages(self) -> ghidra.app.util.importer.MessageLog: ...

    def getMonitor(self) -> ghidra.util.task.TaskMonitor:
        """
        Gets the current task monitor.
        @return the task monitor
        """
        ...

    def getName(self) -> unicode: ...

    def getNamespace(self, parent: ghidra.program.model.symbol.Namespace, namespaceName: unicode) -> ghidra.program.model.symbol.Namespace:
        """
        Returns the non-function namespace with the given name contained inside the
         specified parent namespace.
         Pass <code>null</code> for namespace to indicate the global namespace.
        @param parent the parent namespace, or null for global namespace
        @param namespaceName the requested namespace's name
        @return the namespace with the given name or null if not found
        """
        ...

    def getPlateComment(self, address: ghidra.program.model.address.Address) -> unicode:
        """
        Returns the PLATE comment at the specified address.  The comment returned is the raw text
         of the comment.  Contrastingly, calling {@link GhidraScript#getPlateCommentAsRendered(Address)} will
         return the text of the comment as it is rendered in the display.
        @param address the address to get the comment
        @return the PLATE comment at the specified address or null
         if one does not exist
        @see GhidraScript#getPlateCommentAsRendered(Address)
        """
        ...

    def getPostComment(self, address: ghidra.program.model.address.Address) -> unicode:
        """
        Returns the POST comment at the specified address.  The comment returned is the raw text
         of the comment.  Contrastingly, calling {@link GhidraScript#getPostCommentAsRendered(Address)} will
         return the text of the comment as it is rendered in the display.
        @param address the address to get the comment
        @return the POST comment at the specified address or null
         if one does not exist
        @see GhidraScript#getPostCommentAsRendered(Address)
        """
        ...

    def getPreComment(self, address: ghidra.program.model.address.Address) -> unicode:
        """
        Returns the PRE comment at the specified address.  The comment returned is the raw text
         of the comment.  Contrastingly, calling {@link GhidraScript#getPreCommentAsRendered(Address)} will
         return the text of the comment as it is rendered in the display.
        @param address the address to get the comment
        @return the PRE comment at the specified address or null
         if one does not exist
        @see GhidraScript#getPreCommentAsRendered(Address)
        """
        ...

    def getProgramFile(self) -> java.io.File:
        """
        Returns the path to the program's executable file.
         For example, <code>c:\temp\test.exe</code>.
        @return path to program's executable file
        """
        ...

    def getProjectRootFolder(self) -> ghidra.framework.model.DomainFolder:
        """
        This method looks up the current project and returns
         the root domain folder.
        @return the root domain folder of the current project
        """
        ...

    @overload
    def getReference(self, data: ghidra.program.model.listing.Data, toAddress: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.Reference:
        """
        Returns the reference from the data to the given address.
        @param data the data
        @param toAddress the destination address
        @return the reference from the data to the given address
        """
        ...

    @overload
    def getReference(self, instruction: ghidra.program.model.listing.Instruction, toAddress: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.Reference:
        """
        Returns the reference from the instruction to the given address.
        @param instruction the instruction
        @param toAddress the destination address
        @return the reference from the instruction to the given address
        """
        ...

    def getReferencesFrom(self, address: ghidra.program.model.address.Address) -> List[ghidra.program.model.symbol.Reference]:
        """
        Returns an array of the references FROM the given address.
        @param address the from address of the references
        @return an array of the references FROM the given address
        """
        ...

    def getReferencesTo(self, address: ghidra.program.model.address.Address) -> List[ghidra.program.model.symbol.Reference]:
        """
        Returns an array of the references TO the given address.
         Note: If more than 4096 references exists to this address,
         only the first 4096 will be returned.
         If you need to access all the references, please
         refer to the method <code>ReferenceManager::getReferencesTo(Address)</code>.
        @param address the from address of the references
        @return an array of the references TO the given address
        """
        ...

    def getRepeatableComment(self, address: ghidra.program.model.address.Address) -> unicode:
        """
        Returns the repeatable comment at the specified address.  The comment returned is the raw text
         of the comment.  Contrastingly, calling {@link GhidraScript#getRepeatableCommentAsRendered(Address)} will
         return the text of the comment as it is rendered in the display.
        @param address the address to get the comment
        @return the repeatable comment at the specified address or null
         if one does not exist
        @see GhidraScript#getRepeatableCommentAsRendered(Address)
        """
        ...

    def getShort(self, address: ghidra.program.model.address.Address) -> int:
        """
        Returns the 'short' value at the specified address in memory.
        @param address the address
        @return the 'short' value at the specified address in memory
        @throws MemoryAccessException if the memory is not readable
        """
        ...

    def getSymbol(self, name: unicode, namespace: ghidra.program.model.symbol.Namespace) -> ghidra.program.model.symbol.Symbol:
        """
        Returns the symbol with the given name in the given namespace if there is only one.
         Pass <code>null</code> for namespace to indicate the global namespace.
        @param name the name of the symbol
        @param namespace the parent namespace, or null for global namespace
        @return the symbol with the given name in the given namespace
        @throws IllegalStateException if there is more than one symbol with that name.
        @deprecated use {@link #getSymbols(String, Namespace)}
        """
        ...

    @overload
    def getSymbolAfter(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.Symbol:
        """
        Returns the next non-default primary symbol defined
         after the given address.
        @param address the address to use as a starting point
        @return the next non-default primary symbol
        """
        ...

    @overload
    def getSymbolAfter(self, symbol: ghidra.program.model.symbol.Symbol) -> ghidra.program.model.symbol.Symbol:
        """
        Returns the next non-default primary symbol defined
         after the given symbol.
        @param symbol the symbol to use as a starting point
        @return the next non-default primary symbol
        """
        ...

    @overload
    def getSymbolAt(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.Symbol:
        """
        Returns the PRIMARY symbol at the specified address, or
         null if no symbol exists.
        @param address the symbol address
        @return the PRIMARY symbol at the specified address, or
         null if no symbol exists
        """
        ...

    @overload
    def getSymbolAt(self, address: ghidra.program.model.address.Address, name: unicode) -> ghidra.program.model.symbol.Symbol:
        """
        Returns the symbol with the specified address and name, or
         null if no symbol exists.
        @param address the symbol address
        @param name the symbol name
        @return the symbol with the specified address and name, or
         null if no symbol exists
        @deprecated Since the same label name can be at the same address if in a different namespace,
         this method is ambiguous. Use {@link #getSymbolAt(Address, String, Namespace)} instead.
        """
        ...

    @overload
    def getSymbolAt(self, address: ghidra.program.model.address.Address, name: unicode, namespace: ghidra.program.model.symbol.Namespace) -> ghidra.program.model.symbol.Symbol:
        """
        Returns the symbol with the specified address, name, and namespace
        @param address the symbol address
        @param name the symbol name
        @param namespace the parent namespace for the symbol.
        @return the symbol with the specified address, name, and namespace, or
         null if no symbol exists
        """
        ...

    @overload
    def getSymbolBefore(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.Symbol:
        """
        Returns the previous non-default primary symbol defined
         after the previous address.
        @param address the address to use as a starting point
        @return the next non-default primary symbol
        """
        ...

    @overload
    def getSymbolBefore(self, symbol: ghidra.program.model.symbol.Symbol) -> ghidra.program.model.symbol.Symbol:
        """
        Returns the previous non-default primary symbol defined
         before the given symbol.
        @param symbol the symbol to use as a starting point
        @return the previous non-default primary symbol
        """
        ...

    def getSymbols(self, name: unicode, namespace: ghidra.program.model.symbol.Namespace) -> List[ghidra.program.model.symbol.Symbol]:
        """
        Returns a list of all the symbols with the given name in the given namespace.
        @param name the name of the symbols to retrieve.
        @param namespace the namespace containing the symbols, or null for the global namespace.
        @return a list of all the symbols with the given name in the given namespace.
        """
        ...

    def getUndefinedDataAfter(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        Returns the undefined data after the specified address or null if no undefined data exists.
        @param address the undefined data address
        @return the undefined data after the specified address or null if no undefined data exists
        """
        ...

    def getUndefinedDataAt(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        Returns the undefined data at the specified address or null if no undefined data exists.
        @param address the undefined data address
        @return the undefined data at the specified address or null if no undefined data exists
        """
        ...

    def getUndefinedDataBefore(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        Returns the undefined data before the specified address or null if no undefined data exists.
        @param address the undefined data address
        @return the undefined data before the specified address or null if no undefined data exists
        """
        ...

    def getWorkerName(self) -> unicode: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def openDataTypeArchive(self, archiveFile: java.io.File, readOnly: bool) -> ghidra.program.model.data.FileDataTypeManager:
        """
        Opens a Data Type Archive
        @param archiveFile the archive file to open
        @param readOnly should file be opened read only
        """
        ...

    def removeBookmark(self, bookmark: ghidra.program.model.listing.Bookmark) -> None:
        """
        Removes the specified bookmark.
        @param bookmark the bookmark to remove
        """
        ...

    def removeData(self, data: ghidra.program.model.listing.Data) -> None:
        """
        Removes the given data from the current program.
        @param data the data to remove
        """
        ...

    def removeDataAt(self, address: ghidra.program.model.address.Address) -> None:
        """
        Removes the data containing the given address from the current program.
        @param address the address to remove data
        """
        ...

    def removeEntryPoint(self, address: ghidra.program.model.address.Address) -> None:
        """
        Removes the entry point at the specified address.
        @param address address of entry point to remove
        """
        ...

    @overload
    def removeEquate(self, data: ghidra.program.model.listing.Data) -> None:
        """
        Removes the equate defined on the data.
        @param data the data
        """
        ...

    @overload
    def removeEquate(self, instruction: ghidra.program.model.listing.Instruction, operandIndex: int) -> None:
        """
        Removes the equate defined at the operand index of the instruction.
        @param instruction the instruction
        @param operandIndex the operand index
        @deprecated this form of getEquate is not supported and will throw a UnsupportedOperationException
        """
        ...

    @overload
    def removeEquate(self, instruction: ghidra.program.model.listing.Instruction, operandIndex: int, value: long) -> None:
        """
        Removes the equate defined at the operand index of the instruction with the given value.
        @param instruction the instruction
        @param operandIndex the operand index
        @param value scalar value corresponding to equate
        """
        ...

    def removeEquates(self, instruction: ghidra.program.model.listing.Instruction, operandIndex: int) -> None:
        """
        Removes the equates defined at the operand index of the instruction.
        @param instruction the instruction
        @param operandIndex the operand index
        """
        ...

    def removeFunction(self, function: ghidra.program.model.listing.Function) -> None:
        """
        Removes the function from the current program.
        @param function the function to remove
        """
        ...

    def removeFunctionAt(self, entryPoint: ghidra.program.model.address.Address) -> None:
        """
        Removes the function with the given entry point.
        @param entryPoint the entry point of the function to remove
        """
        ...

    def removeInstruction(self, instruction: ghidra.program.model.listing.Instruction) -> None:
        """
        Removes the given instruction from the current program.
        @param instruction the instruction to remove
        """
        ...

    def removeInstructionAt(self, address: ghidra.program.model.address.Address) -> None:
        """
        Removes the instruction containing the given address from the current program.
        @param address the address to remove instruction
        """
        ...

    def removeMemoryBlock(self, block: ghidra.program.model.mem.MemoryBlock) -> None:
        """
        Remove the memory block.
         NOTE: ALL ANNOTATION (disassembly, comments, etc) defined in this
         memory block will also be removed!
        @param block the block to be removed
        """
        ...

    def removeReference(self, reference: ghidra.program.model.symbol.Reference) -> None:
        """
        Removes the given reference.
        @param reference the reference to remove
        """
        ...

    def removeSymbol(self, address: ghidra.program.model.address.Address, name: unicode) -> bool:
        """
        Deletes the symbol with the specified name at the specified address.
        @param address the address of the symbol to delete
        @param name the name of the symbol to delete
        @return true if the symbol was deleted
        """
        ...

    @overload
    def saveProgram(self, program: ghidra.program.model.listing.Program) -> None:
        """
        Saves the changes to the specified program.
         If the program does not already exist in the current project
         then it will be saved into the root folder.
         If a program already exists with the specified
         name, then a time stamp will be appended to the name to make it unique.
        @param program the program to save
        @throws Exception
        """
        ...

    @overload
    def saveProgram(self, __a0: ghidra.program.model.listing.Program, __a1: List[object]) -> None: ...

    def setByte(self, address: ghidra.program.model.address.Address, value: int) -> None:
        """
        Sets the 'byte' value at the specified address.
        @param address the address to set the 'byte'
        @param value the value to set
        @throws MemoryAccessException if memory does not exist or is uninitialized
        """
        ...

    def setBytes(self, address: ghidra.program.model.address.Address, values: List[int]) -> None:
        """
        Sets the 'byte' values starting at the specified address.
        @param address the address to set the bytes
        @param values the values to set
        @throws MemoryAccessException if memory does not exist or is uninitialized
        """
        ...

    def setDouble(self, address: ghidra.program.model.address.Address, value: float) -> None:
        """
        Sets the 'double' value at the specified address.
        @param address the address to set the 'double'
        @param value the value to set
        @throws MemoryAccessException if memory does not exist or is uninitialized
        """
        ...

    def setEOLComment(self, address: ghidra.program.model.address.Address, comment: unicode) -> bool:
        """
        Sets an EOL comment at the specified address
        @param address the address to set the EOL comment
        @param comment the EOL comment
        @return true if the EOL comment was successfully set
        """
        ...

    def setFloat(self, address: ghidra.program.model.address.Address, value: float) -> None:
        """
        Sets the 'float' value at the specified address.
        @param address the address to set the 'float'
        @param value the value to set
        @throws MemoryAccessException if memory does not exist or is uninitialized
        """
        ...

    def setInt(self, address: ghidra.program.model.address.Address, value: int) -> None:
        """
        Sets the 'integer' value at the specified address.
        @param address the address to set the 'integer'
        @param value the value to set
        @throws MemoryAccessException if memory does not exist or is uninitialized
        """
        ...

    def setLong(self, address: ghidra.program.model.address.Address, value: long) -> None:
        """
        Sets the 'long' value at the specified address.
        @param address the address to set the 'long'
        @param value the value to set
        @throws MemoryAccessException if memory does not exist or is uninitialized
        """
        ...

    def setPlateComment(self, address: ghidra.program.model.address.Address, comment: unicode) -> bool:
        """
        Sets a PLATE comment at the specified address
        @param address the address to set the PLATE comment
        @param comment the PLATE comment
        @return true if the PLATE comment was successfully set
        """
        ...

    def setPostComment(self, address: ghidra.program.model.address.Address, comment: unicode) -> bool:
        """
        Sets a POST comment at the specified address
        @param address the address to set the POST comment
        @param comment the POST comment
        @return true if the POST comment was successfully set
        """
        ...

    def setPreComment(self, address: ghidra.program.model.address.Address, comment: unicode) -> bool:
        """
        Sets a PRE comment at the specified address
        @param address the address to set the PRE comment
        @param comment the PRE comment
        @return true if the PRE comment was successfully set
        """
        ...

    @overload
    def setReferencePrimary(self, reference: ghidra.program.model.symbol.Reference) -> None:
        """
        Sets the given reference as primary.
        @param reference the reference to mark as primary
        """
        ...

    @overload
    def setReferencePrimary(self, reference: ghidra.program.model.symbol.Reference, primary: bool) -> None:
        """
        Sets the given reference as primary.
        @param reference the reference
        @param primary true if primary, false not primary
        """
        ...

    def setRepeatableComment(self, address: ghidra.program.model.address.Address, comment: unicode) -> bool:
        """
        Sets a repeatable comment at the specified address
        @param address the address to set the repeatable comment
        @param comment the repeatable comment
        @return true if the repeatable comment was successfully set
        """
        ...

    def setShort(self, address: ghidra.program.model.address.Address, value: int) -> None:
        """
        Sets the 'short' value at the specified address.
        @param address the address to set the 'short'
        @param value the value to set
        @throws MemoryAccessException if memory does not exist or is uninitialized
        """
        ...

    def start(self) -> None:
        """
        Starts a transaction on the current program.
        """
        ...

    @overload
    def toAddr(self, offset: long) -> ghidra.program.model.address.Address:
        """
        Returns a new address with the specified offset in the default address space.
        @param offset the offset for the new address
        @return a new address with the specified offset in the default address space
        """
        ...

    @overload
    def toAddr(self, offset: int) -> ghidra.program.model.address.Address:
        """
        Returns a new address with the specified offset in the default address space.
        @param offset the offset for the new address
        @return a new address with the specified offset in the default address space
        """
        ...

    @overload
    def toAddr(self, addressString: unicode) -> ghidra.program.model.address.Address:
        """
        Returns a new address inside the specified program as indicated by the string.
        @param addressString string representation of the address desired
        @return the address. Otherwise, return null if the string fails to evaluate
         to a legitimate address
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
    def messages(self) -> ghidra.app.util.importer.MessageLog: ...

    @property
    def name(self) -> unicode: ...

    @property
    def workerName(self) -> unicode: ...
