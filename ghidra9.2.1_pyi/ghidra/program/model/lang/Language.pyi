from typing import List
import ghidra.app.plugin.processors.generic
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.program.model.mem
import ghidra.program.model.util
import ghidra.util
import ghidra.util.task
import java.lang
import java.util


class Language(object):








    def applyContextSettings(self, ctx: ghidra.program.model.listing.DefaultProgramContext) -> None:
        """
        Apply context settings to the ProgramContext as specified by the
         configuration
        @param ctx is the default program context
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getAddressFactory(self) -> ghidra.program.model.address.AddressFactory:
        """
        Get the AddressFactory for this language. The returned Address factory will allow
         addresses associated with physical, constant and unique spaces to be instantiated.
         NOTE! this factory does not know about compiler or program specified spaces.
         Spaces such as stack and overlay spaces are not defined by the language -
         if these are needed, Program.getAddressFactory() should be used instead.
        @return the AddressFactory for this language.
        @see Program#getAddressFactory()
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getCompatibleCompilerSpecDescriptions(self) -> List[ghidra.program.model.lang.CompilerSpecDescription]:
        """
        Returns a list of all compatible compiler spec descriptions.
         The first item in the list is the default.
        @return list of all compatible compiler specifications descriptions
        """
        ...

    def getCompilerSpecByID(self, compilerSpecID: ghidra.program.model.lang.CompilerSpecID) -> ghidra.program.model.lang.CompilerSpec:
        """
        Returns the compiler spec associated with a given CompilerSpecID.
        @param compilerSpecID the compiler spec id
        @return the compiler spec associated with the given id
        @throws CompilerSpecNotFoundException if no such compiler spec exists
        """
        ...

    def getContextBaseRegister(self) -> ghidra.program.model.lang.Register:
        """
        Returns processor context base register or null if one has not been defined by the
         language.
        @return base context register or null if not defined
        """
        ...

    def getContextRegisters(self) -> List[ghidra.program.model.lang.Register]:
        """
        Get an unsorted unmodifiable list of processor context registers that this language defines
         (includes context base register and its context field registers).
        @return unmodifiable list of processor registers.
        """
        ...

    def getDefaultCompilerSpec(self) -> ghidra.program.model.lang.CompilerSpec:
        """
        Returns the default compiler spec for this language, which is used
         when a loader cannot determine the compiler spec or for upgrades when a
         program had no compiler spec registered (seriously old program, like
         Ghidra 4.1 or earlier).  NOTE: this has NOTHING to do with the
         compiler spec registered for a program.  Use Program.getCompilerSpec()
         for that!
        @return the default compiler spec for this language
        """
        ...

    def getDefaultDataSpace(self) -> ghidra.program.model.address.AddressSpace:
        """
        Get the preferred data space used by loaders for data sections.
        @return default data address space
        """
        ...

    def getDefaultMemoryBlocks(self) -> List[ghidra.app.plugin.processors.generic.MemoryBlockDefinition]:
        """
        Returns the default memory blocks for this language.
        @return the default memory blocks for this language
        """
        ...

    def getDefaultSpace(self) -> ghidra.program.model.address.AddressSpace:
        """
        Get the default memory/code space.
        @return default address space
        """
        ...

    def getDefaultSymbols(self) -> List[ghidra.program.model.util.AddressLabelInfo]:
        """
        Returns the default symbols for this language.  This list does not
         contain registers.
        @return the default symbols for this language
        """
        ...

    def getInstructionAlignment(self) -> int:
        """
        Get instruction alignment in terms of bytes.
        @return instruction alignment
        """
        ...

    def getLanguageDescription(self) -> ghidra.program.model.lang.LanguageDescription:
        """
        Returns the LanguageDescription of this language, which contains useful
         information about the characteristics of the language.
        @return the LanguageDescription of this language
        """
        ...

    def getLanguageID(self) -> ghidra.program.model.lang.LanguageID:
        """
        Returns the LanguageID of this language, which is used as a primary key to
         find the language when Ghidra loads it.
        @return the LanguageID of this language
        """
        ...

    def getManualEntry(self, instructionMnemonic: unicode) -> ghidra.util.ManualEntry:
        """
        Get the ManualEntry for the given instruction mnemonic.
        @param instructionMnemonic the instruction mnemonic
        @return the ManualEntry or null.  A default manual entry will be returned if
         an instruction can not be found within the index and a manual exists.
        """
        ...

    def getManualException(self) -> java.lang.Exception:
        """
        Returns the exception generated trying to load the manual, or null if it succeeded.
        @return the exception generated trying to load the manual, or null if it succeeded
        """
        ...

    def getManualInstructionMnemonicKeys(self) -> java.util.Set:
        """
        Returns a read-only set view of the instruction mnemonic keys defined on
         this language.
        @return read-only set of instruction mnemonic keys
        """
        ...

    def getMinorVersion(self) -> int:
        """
        Returns the minor version for this language. Returning a minor version
         number different than before could cause the program to try and "update"
         itself. Those languages which do not support this feature may always
         return a constant value of 0.
        @return the language minor version number
        """
        ...

    def getNumberOfUserDefinedOpNames(self) -> int:
        """
        Get the total number of user defined pcode names.

         Note: only works for Pcode based languages
        @return number of user defined pcodeops
        """
        ...

    def getParallelInstructionHelper(self) -> ghidra.program.model.lang.ParallelInstructionLanguageHelper:
        """
        Returns a parallel instruction helper for this language or null
         if one has not been defined.
        @return parallel instruction helper or null if not applicable
        """
        ...

    def getProcessor(self) -> ghidra.program.model.lang.Processor:
        """
        Returns the processor name on which this language is based.

         For example, 30386, Pentium, 68010, etc.
        @return the processor name
        """
        ...

    def getProgramCounter(self) -> ghidra.program.model.lang.Register:
        """
        Get the default program counter register for this language if there is
         one.
        @return default program counter register.
        """
        ...

    @overload
    def getProperty(self, key: unicode) -> unicode:
        """
        Gets a property defined for this language, or null if that property isn't defined.
        @param key the property key
        @return the property value, or null if not defined
        """
        ...

    @overload
    def getProperty(self, key: unicode, defaultString: unicode) -> unicode:
        """
        Gets the value of a property as a String, returning defaultString if undefined.
        @param key the property key
        @param defaultString the default value to return if property is undefined
        @return the property value as a String, or the default value if undefined
        """
        ...

    def getPropertyAsBoolean(self, key: unicode, defaultBoolean: bool) -> bool:
        """
        Gets the value of a property as a boolean, returning defaultBoolean if undefined.
        @param key the property key
        @param defaultBoolean the default value to return if property is undefined
        @return the property value as a boolean, or the default value if undefined
        """
        ...

    def getPropertyAsInt(self, key: unicode, defaultInt: int) -> int:
        """
        Gets the value of a property as an int, returning defaultInt if undefined.
        @param key the property key
        @param defaultInt the default value to return if property is undefined
        @return the property value as an int, or the default value if undefined
        """
        ...

    def getPropertyKeys(self) -> java.util.Set:
        """
        Returns a read-only set view of the property keys defined on this language.
        @return read-only set of property keys
        """
        ...

    @overload
    def getRegister(self, name: unicode) -> ghidra.program.model.lang.Register:
        """
        Get a register given the name of the register
        @param name Register name
        @return the register
        """
        ...

    @overload
    def getRegister(self, addr: ghidra.program.model.address.Address, size: int) -> ghidra.program.model.lang.Register:
        """
        Get a register given it's underlying address location and size.
        @param addr location of the register in its address space
        @param size the size of the register (in bytes).  A value of 0 will return the
                    largest register at the specified addr
        @return the register
        """
        ...

    @overload
    def getRegister(self, addrspc: ghidra.program.model.address.AddressSpace, offset: long, size: int) -> ghidra.program.model.lang.Register:
        """
        Get a register given the address space it is in, its offset in the space
         and its size.
        @param addrspc address space the register is in
        @param offset offset of the register in the space
        @param size size of the register in bytes
        @return the register
        """
        ...

    def getRegisterNames(self) -> List[unicode]:
        """
        Get an alphabetical sorted unmodifiable list of original register names
         (including context registers).  Names correspond to orignal register
         name and not aliases which may be defined.
        @return alphabetical sorted unmodifiable list of original register names.
        """
        ...

    @overload
    def getRegisters(self) -> List[ghidra.program.model.lang.Register]:
        """
        Get an unsorted unmodifiable list of Register objects that this language defines
         (including context registers).
        @return unmodifiable list of processor registers.
        """
        ...

    @overload
    def getRegisters(self, address: ghidra.program.model.address.Address) -> List[ghidra.program.model.lang.Register]:
        """
        Returns all the registers (each different size is a different register)
         for an address.
        @param address the register address for which to return all registers.
        @return all the registers (each different size is a different register)
                 for an address.
        """
        ...

    def getSegmentedSpace(self) -> unicode:
        """
        Returns the name of the segmented space for this language, or the
         empty string if the memory model for this language is not
         segmented.
        @return the name of the segmented space or ""
        """
        ...

    def getSortedVectorRegisters(self) -> List[ghidra.program.model.lang.Register]:
        """
        Returns an unmodifiable list of vector registers, sorted first by size and then by name.
        @return unmodifiable list of vector registers.
        """
        ...

    def getUserDefinedOpName(self, index: int) -> unicode:
        """
        Get the user define name for a given index. Certain pcode has operations
         defined only by name that when the pcode returns, only the index is
         known.

         Note: only works for Pcode based languages
        @param index user defined pcodeop index
        @return pcodeop name or null if not defined
        """
        ...

    def getVersion(self) -> int:
        """
        Returns the major version for this language. Returning a version number
         different than before could cause the program to try and "update" itself.
         Those languages which do not support this feature may always return a
         constant value of 1.
        @return the language version number
        """
        ...

    def getVolatileAddresses(self) -> ghidra.program.model.address.AddressSetView:
        """
        Returns an AddressSetView of the volatile addresses for this language
        @return an AddressSetView of the volatile addresses for this language
        """
        ...

    def hasManual(self) -> bool:
        """
        Returns whether the language has a valid manual defined.
        @return if the language has a manual
        """
        ...

    def hasProperty(self, key: unicode) -> bool:
        """
        Returns whether this lanugage has a property defined.
        @param key the property key
        @return if the property is defined
        """
        ...

    def hashCode(self) -> int: ...

    def isBigEndian(self) -> bool:
        """
        get the Endian type for this language. (If a language supports both, then
         this returns an initial or default value.)
        @return true for BigEndian, false for LittleEndian.
        """
        ...

    def isVolatile(self, addr: ghidra.program.model.address.Address) -> bool:
        """
        Returns true if the language has defined the specified location as
         volatile.
        @param addr location address
        @return true if specified address is within a volatile range
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def parse(self, buf: ghidra.program.model.mem.MemBuffer, context: ghidra.program.model.lang.ProcessorContext, inDelaySlot: bool) -> ghidra.program.model.lang.InstructionPrototype:
        """
        Get the InstructionPrototype that matches the bytes presented by the
         MemBuffer object.
        @param buf the MemBuffer that presents the bytes in Memory at some
                    address as if they were an array of bytes starting at index 0.
        @param context the processor context at the address to be disassembled
        @param inDelaySlot true if this instruction should be parsed as if it were in a
                    delay slot
        @return the InstructionPrototype that matches the bytes in buf.
        @exception InsufficientBytesException thrown if there are not enough bytes in memory to satisfy
                        a legal instruction.
        @exception UnknownInstructionException thrown if the byte pattern does not match any legal
                        instruction.
        """
        ...

    def reloadLanguage(self, taskMonitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Refreshes the definition of this language if possible.  Use of this method is
         intended for development purpose only since stale references to prior
         language resources (e.g., registers) may persist.
        @param taskMonitor monitor for progress back to the user
        @throws IOException if error occurs while reloading language spec file(s)
        """
        ...

    def supportsPcode(self) -> bool:
        """
        Return true if the instructions in this language support Pcode.
        @return true if language supports the use of pcode
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
    def addressFactory(self) -> ghidra.program.model.address.AddressFactory: ...

    @property
    def bigEndian(self) -> bool: ...

    @property
    def compatibleCompilerSpecDescriptions(self) -> List[object]: ...

    @property
    def contextBaseRegister(self) -> ghidra.program.model.lang.Register: ...

    @property
    def contextRegisters(self) -> List[object]: ...

    @property
    def defaultCompilerSpec(self) -> ghidra.program.model.lang.CompilerSpec: ...

    @property
    def defaultDataSpace(self) -> ghidra.program.model.address.AddressSpace: ...

    @property
    def defaultMemoryBlocks(self) -> List[ghidra.app.plugin.processors.generic.MemoryBlockDefinition]: ...

    @property
    def defaultSpace(self) -> ghidra.program.model.address.AddressSpace: ...

    @property
    def defaultSymbols(self) -> List[object]: ...

    @property
    def instructionAlignment(self) -> int: ...

    @property
    def languageDescription(self) -> ghidra.program.model.lang.LanguageDescription: ...

    @property
    def languageID(self) -> ghidra.program.model.lang.LanguageID: ...

    @property
    def manualException(self) -> java.lang.Exception: ...

    @property
    def manualInstructionMnemonicKeys(self) -> java.util.Set: ...

    @property
    def minorVersion(self) -> int: ...

    @property
    def numberOfUserDefinedOpNames(self) -> int: ...

    @property
    def parallelInstructionHelper(self) -> ghidra.program.model.lang.ParallelInstructionLanguageHelper: ...

    @property
    def processor(self) -> ghidra.program.model.lang.Processor: ...

    @property
    def programCounter(self) -> ghidra.program.model.lang.Register: ...

    @property
    def propertyKeys(self) -> java.util.Set: ...

    @property
    def registerNames(self) -> List[object]: ...

    @property
    def registers(self) -> List[object]: ...

    @property
    def segmentedSpace(self) -> unicode: ...

    @property
    def sortedVectorRegisters(self) -> List[object]: ...

    @property
    def version(self) -> int: ...

    @property
    def volatileAddresses(self) -> ghidra.program.model.address.AddressSetView: ...
