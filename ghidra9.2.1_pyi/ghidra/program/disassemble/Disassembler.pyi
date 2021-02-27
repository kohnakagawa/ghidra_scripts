import ghidra.program.disassemble
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.program.model.mem
import ghidra.util.task
import java.lang


class Disassembler(object, ghidra.program.disassemble.DisassemblerConflictHandler):
    """
    Class to perform disassembly.  Contains the logic to follow instruction
     flows to continue the disassembly.
     17-Nov-2008: moved to ghidra.program.disassemble package since this is now used during
     					      language upgrades which may occur during construction of ProgramDB.
     12-Dec-2012: major refactor of disassembly to perform bulk add of instructions to
     program to avoid context related conflicts
    """

    ERROR_BOOKMARK_CATEGORY: unicode = u'Bad Instruction'
    MARK_BAD_INSTRUCTION_PROPERTY: unicode = u'Mark Bad Disassembly'
    MARK_UNIMPL_PCODE_PROPERTY: unicode = u'Mark Unimplemented Pcode'
    MAX_REPEAT_PATTERN_LENGTH: int = 16
    RESTRICT_DISASSEMBLY_TO_EXECUTE_MEMORY_PROPERTY: unicode = u'Restrict Disassembly to Executable Memory'
    UNIMPL_BOOKMARK_CATEGORY: unicode = u'Unimplemented Pcode'







    @staticmethod
    def clearBadInstructionErrors(program: ghidra.program.model.listing.Program, addressSet: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Clear all bookmarks which indicate Bad Instruction within the specified address set.
        @param program program to clear bookmarks
        @param addressSet restricted address set or null for entire program
        @param monitor allow canceling
        @throws CancelledException if monitor canceled
        """
        ...

    @staticmethod
    def clearUnimplementedPcodeWarnings(program: ghidra.program.model.listing.Program, addressSet: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Clear all bookmarks which indicate unimplemented pcode within the specified address set.
        @param program program to clear bookmarks
        @param addressSet restricted address set or null for entire program
        @param monitor allow canceling
        @throws CancelledException if monitor canceled
        """
        ...

    @overload
    def disassemble(self, startAddr: ghidra.program.model.address.Address, restrictedSet: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.address.AddressSet:
        """
        Disassembles code starting at startAddr and restricted to addrSet.
         NOTE: A single instance of this Disassembler does not support concurrent
         invocations of the various disassemble methods.
         Disassembler must be instantiated with a Program object.
        @param startAddr the address to begin disassembling.
        @param restrictedSet the set of addresses that disassembling is restricted to.
        @return AddressSet the set of addresses that were disassembled.
        """
        ...

    @overload
    def disassemble(self, startAddr: ghidra.program.model.address.Address, restrictedSet: ghidra.program.model.address.AddressSetView, doFollowFlow: bool) -> ghidra.program.model.address.AddressSet:
        """
        Disassembles code starting at startAddr and restricted to addrSet.
         NOTE: A single instance of this Disassembler does not support concurrent
         invocations of the various disassemble methods.
         Disassembler must be instantiated with a Program object.
        @param startAddr the address to begin disassembling.
        @param restrictedSet the set of addresses that disassembling is restricted to.
        @param doFollowFlow flag to follow references while disassembling.
        @return AddressSet the set of addresses that were disassembled.
        """
        ...

    @overload
    def disassemble(self, startSet: ghidra.program.model.address.AddressSetView, restrictedSet: ghidra.program.model.address.AddressSetView, doFollowFlow: bool) -> ghidra.program.model.address.AddressSet:
        """
        Attempt disassembly of all undefined code units within the specified set of addresses.
         NOTE: A single instance of this Disassembler does not support concurrent
         invocations of the various disassemble methods.
         Disassembler must be instantiated with a Program object.
        @param startSet the minimum set of addresses to disassemble
        @param restrictedSet the set of addresses that disassembling is restricted to (may be null)
        @param doFollowFlow flag to follow references while disassembling.
        @return the set of addresses that were disassembled.
        """
        ...

    @overload
    def disassemble(self, startAddr: ghidra.program.model.address.Address, restrictedSet: ghidra.program.model.address.AddressSetView, initialContextValue: ghidra.program.model.lang.RegisterValue, doFollowFlow: bool) -> ghidra.program.model.address.AddressSet:
        """
        Disassembles code starting at startAddr and restricted to addrSet.
         NOTE: A single instance of this Disassembler does not support concurrent
         invocations of the various disassemble methods.
         Disassembler must be instantiated with a Program object.
        @param startAddr the address to begin disassembling.
        @param restrictedSet the set of addresses that disassembling is restricted to.
        @param initialContextValue initial context value to be applied at the
         startAddr.  If not null this value will take precedence when combined with
         any seed value or program context.
        @param doFollowFlow flag to follow references while disassembling.
        @return AddressSet the set of addresses that were disassembled.
        """
        ...

    @overload
    def disassemble(self, startSet: ghidra.program.model.address.AddressSetView, restrictedSet: ghidra.program.model.address.AddressSetView, initialContextValue: ghidra.program.model.lang.RegisterValue, doFollowFlow: bool) -> ghidra.program.model.address.AddressSet:
        """
        Attempt disassembly of all undefined code units within the specified set of addresses.
         NOTE: A single instance of this Disassembler does not support concurrent
         invocations of the various disassemble methods.
         Disassembler must be instantiated with a Program object.
        @param startSet the minimum set of addresses to disassemble
        @param restrictedSet the set of addresses that disassembling is restricted to (may be null)
        @param initialContextValue initial context value to be applied at the
         startAddr.  If not null this value will take precedence when combined with
         any seed value or program context.
        @param doFollowFlow flag to follow references while disassembling.
        @return the set of addresses that were disassembled.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    @staticmethod
    def getDisassembler(program: ghidra.program.model.listing.Program, monitor: ghidra.util.task.TaskMonitor, listener: ghidra.program.disassemble.DisassemblerMessageListener) -> ghidra.program.disassemble.Disassembler:
        """
        Get a suitable disassembler instance.
         Marking of bad instructions honors "Mark Bad Disassembly"
         program Disassembler option.
        @param program the program to be disassembled.
        @param monitor progress monitor
        @param listener object to notify of disassembly messages.
        @return a disassembler ready to disassemble
        """
        ...

    @overload
    @staticmethod
    def getDisassembler(language: ghidra.program.model.lang.Language, addrFactory: ghidra.program.model.address.AddressFactory, monitor: ghidra.util.task.TaskMonitor, listener: ghidra.program.disassemble.DisassemblerMessageListener) -> ghidra.program.disassemble.Disassembler:
        """
        Get a suitable disassembler instance.
         Intended for block pseudo-disassembly use only when the method
         {@link Disassembler#pseudoDisassembleBlock(MemBuffer, RegisterValue, int)}
         is used.
        @param language processor language
        @param addrFactory address factory
        @param monitor progress monitor
        @param listener object to notify of disassembly messages.
        @return a disassembler ready to disassemble
        """
        ...

    @overload
    @staticmethod
    def getDisassembler(program: ghidra.program.model.listing.Program, markBadInstructions: bool, markUnimplementedPcode: bool, restrictToExecuteMemory: bool, monitor: ghidra.util.task.TaskMonitor, listener: ghidra.program.disassemble.DisassemblerMessageListener) -> ghidra.program.disassemble.Disassembler:
        """
        Get a suitable disassembler instance.
        @param program the program to be disassembled.
        @param markBadInstructions if true bad instructions will be marked
        @param markUnimplementedPcode if true instructions with unimplemented pcode will be marked
        @param restrictToExecuteMemory if true disassembly will only be permitted with executable memory blocks
        @param monitor progress monitor
        @param listener object to notify of disassembly messages.
        @return a disassembler ready to disassemble
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isMarkBadDisassemblyOptionEnabled(program: ghidra.program.model.listing.Program) -> bool:
        """
        @param program the program to check
        @return true if program MARK_BAD_INSTRUCTION_PROPERTY has been enabled
        """
        ...

    @staticmethod
    def isMarkUnimplementedPcodeOptionEnabled(program: ghidra.program.model.listing.Program) -> bool:
        """
        @param program the program to check
        @return true if program MARK_UNIMPL_PCODE_PROPERTY has been enabled
        """
        ...

    @staticmethod
    def isRestrictToExecuteMemory(program: ghidra.program.model.listing.Program) -> bool:
        """
        @param program the program to check
        @return true if program RESTRICT_DISASSEMBLY_TO_EXECUTE_MEMORY_PROPERTY has been enabled
        """
        ...

    def markInstructionError(self, conflict: ghidra.program.model.lang.InstructionError) -> None: ...

    @staticmethod
    def markUnimplementedPcode(program: ghidra.program.model.listing.Program, addressSet: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Mark all instructions with unimplemented pcode over the specified address set
        @param program to mark unimplemented in
        @param addressSet restricted address set or null for entire program
        @param monitor allow canceling
        @throws CancelledException if monitor canceled
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @overload
    def pseudoDisassembleBlock(self, addr: ghidra.program.model.address.Address, defaultContextValue: ghidra.program.model.lang.RegisterValue, limit: int) -> ghidra.program.model.lang.InstructionBlock:
        """
        Perform a psuedo-disassembly of an single instruction block only following fall-throughs.
         WARNING! This method should not be used in conjunction with other disassembly methods
         on the this Disassembler instance.  Disassembler must be instantiated with a Program object.
        @param addr start of block
        @param defaultContextValue starting context to use if no context has previously been established
         for the specified startAddr
        @param limit maximum number of instructions to disassemble
        @return instruction block of pseudo-instructions
        """
        ...

    @overload
    def pseudoDisassembleBlock(self, blockMemBuffer: ghidra.program.model.mem.MemBuffer, defaultContextValue: ghidra.program.model.lang.RegisterValue, limit: int) -> ghidra.program.model.lang.InstructionBlock:
        """
        Perform a psuedo-disassembly of an single instruction block only following fall-throughs.
         WARNING! This method should not be used in conjunction with other disassembly methods
         on the this Disassembler instance.
        @param blockMemBuffer block memory buffer
        @param defaultContextValue starting context to use if no context has previously been established
         for the specified startAddr
        @param limit maximum number of instructions to disassemble
        @return instruction block of pseudo-instructions or null if minimum address of blockMemBuffer
         is not properly aligned for instruction parsing.
        """
        ...

    def resetDisassemblerContext(self) -> None:
        """
        Clear any retained context state which may have been accumulated.
         Use of this method is only needed when using the pseudoDisassembleBlock
         method over an extended code range to avoid excessive in-memory state accumulation.
        """
        ...

    def setRepeatPatternLimit(self, maxInstructions: int) -> None:
        """
        Set the maximum number of instructions in a single run which contain the same byte values.
         Disassembly flow will stop and be flagged when this threshold is encountered.
         This check is set to MAX_REPEAT_PATTERN_LENGTH by default, and can be disabled by setting a value of -1
         NOTE: This restriction will only work for those cases where a given repeated byte
         results in an instruction which has a fall-through.
        @param maxInstructions limit on the number of consecutive instructions with the same
         byte values
        """
        ...

    def setRepeatPatternLimitIgnored(self, set: ghidra.program.model.address.AddressSetView) -> None:
        """
        Set the region over which the repeat pattern limit will be ignored.
         This allows areas which have been explicitly disassembled to be
         free of bad bookmarks caused by the repeat pattern limit being exceeded.
        @param set region over which the repeat pattern limit will be ignored
        """
        ...

    def setSeedContext(self, seedContext: ghidra.program.disassemble.DisassemblerContextImpl) -> None:
        """
        Set seed context which will be used to establish initial context at starting points
         which are not arrived at via a natural disassembly flow.  A null value will disable
         use of any previously set seed context
        @param seedContext initial context for disassembly
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
    def repeatPatternLimit(self) -> None: ...  # No getter available.

    @repeatPatternLimit.setter
    def repeatPatternLimit(self, value: int) -> None: ...

    @property
    def repeatPatternLimitIgnored(self) -> None: ...  # No getter available.

    @repeatPatternLimitIgnored.setter
    def repeatPatternLimitIgnored(self, value: ghidra.program.model.address.AddressSetView) -> None: ...

    @property
    def seedContext(self) -> None: ...  # No getter available.

    @seedContext.setter
    def seedContext(self, value: ghidra.program.disassemble.DisassemblerContextImpl) -> None: ...
