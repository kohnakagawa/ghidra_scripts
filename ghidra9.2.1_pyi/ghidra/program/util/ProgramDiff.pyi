from typing import List
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.symbol
import ghidra.program.util
import ghidra.util.task
import java.lang


class ProgramDiff(object):
    """
    ProgramDiff is a class for comparing two programs and
     determining where there are differences between them.

     Currently, the differences can be determined if the two programs have
     equivalent address spaces. If the programs have different program context
     registers, the Diff can still occur but will not determine program context
     differences.

    """





    @overload
    def __init__(self, program1: ghidra.program.model.listing.Program, program2: ghidra.program.model.listing.Program):
        """
        <CODE>ProgramDiff</CODE> is used to determine the addresses where
         there are differences between two programs.
         Possible differences are:
         the actual bytes at an address, comments, labels, mnemonics,
         references, equates, properties, functions, program context.
         <P>Currently, the differences can be determined only if the address
         spaces match between the programs.
        @param program1 the first program
        @param program2 the second program
        @throws ProgramConflictException indicates that programs
         couldn't be compared to determine the differences.
         <P>For example,
         <P>the two programs have different address spaces.
        @throws IllegalArgumentException if one of the programs is null.
        """
        ...

    @overload
    def __init__(self, program1: ghidra.program.model.listing.Program, program2: ghidra.program.model.listing.Program, checkAddressSet: ghidra.program.model.address.AddressSetView):
        """
        <CODE>ProgramDiff</CODE> is used to determine the addresses where
         there are differences between two programs.
         Possible differences are:
         the actual bytes at an address, comments, labels, mnemonics,
         references, equates, properties, functions, program context.
         <P>Currently, the differences can be determined only if the address
         spaces match between the programs.
        @param program1 the first program
        @param program2 the second program
        @param checkAddressSet the address set to be used to constrain where
         differences are found.
         The addresses in this address set should be derived from program1.
        @throws ProgramConflictException indicates that programs
         couldn't be compared to determine the differences.
         <P>For example,
         <P>the two programs have different address spaces.
         between the two programs, do not match.
        @throws IllegalArgumentException if one of the programs is null.
        """
        ...



    def checkCancelled(self, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Checks the task associated with the indicated monitor to determine if it has
         been canceled.
        @param monitor the task monitor, associated with getting differences from this Diff,
         to be checked
        @throws CancelledException if the getDifferences() task has been canceled by the user.
        """
        ...

    def equalRefArrays(self, refs1: List[ghidra.program.model.symbol.Reference], refs2: List[ghidra.program.model.symbol.Reference]) -> bool:
        """
        Compares an array of references from program1 with an array of references from program2 to see if they are equivalent.
        @param refs1 program1 array of references
        @param refs2 program2 array of references
        @return true if the arrays of references are equal.
        """
        ...

    def equalRefs(self, ref1: ghidra.program.model.symbol.Reference, ref2: ghidra.program.model.symbol.Reference) -> bool:
        """
        Compares reference from program1 with reference from program2 to see if they are equivalent.
        @param ref1 program1 reference
        @param ref2 program2 reference
        @return true if they are equivalent
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @overload
    @staticmethod
    def equivalentFunctions(f1: ghidra.program.model.listing.Function, f2: ghidra.program.model.listing.Function) -> bool: ...

    @overload
    @staticmethod
    def equivalentFunctions(f1: ghidra.program.model.listing.Function, f2: ghidra.program.model.listing.Function, ignoreName: bool) -> bool: ...

    def getAddressesInCommon(self) -> ghidra.program.model.address.AddressSet:
        """
        Returns the addresses in common between program1 and program2.
        @return the addresses in common between program1 and program2.
         The addresses in this address set are derived from program1.
        """
        ...

    def getAddressesOnlyInOne(self) -> ghidra.program.model.address.AddressSet:
        """
        Returns the addresses that are in program1, but not in program2.
        @return the addresses that are in program1, but not in program2.
         The addresses in this address set are derived from program1.
        """
        ...

    def getAddressesOnlyInTwo(self) -> ghidra.program.model.address.AddressSet:
        """
        Returns the addresses that are in program2, but not in program1.
        @return the addresses that are in program2, but not in program1.
         The addresses in this address set are derived from program2.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getCombinedAddresses(self) -> ghidra.program.model.address.AddressSetView:
        """
        Returns the addresses from combining the address sets in program1 and program2.
        @return the addresses for both program1 and program2.
         The addresses in this address set are derived from program1.
        """
        ...

    @staticmethod
    def getDiffRefs(refs: List[ghidra.program.model.symbol.Reference]) -> List[ghidra.program.model.symbol.Reference]:
        """
        Gets the references that need to be checked for differences from those that are handed
         to it via the refs parameter.
        @param refs the references before removing those that we don't want to diff.
        @return only the references that should be part of the diff.
        """
        ...

    @overload
    def getDifferences(self, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.address.AddressSetView:
        """
        <CODE>getDifferences</CODE> is used to determine
         the addresses where there are differences between two programs using
         the current filter. This
         method only indicates that there is a difference at the address, not what
         type of difference it is. Possible differences are:
         the actual bytes at an address, comments, labels, code units,
         references, equates, properties, and program context register values.
        @param monitor the task monitor for indicating the progress of
         determining differences. This monitor also allows the user to cancel if
         the diff takes too long. If no monitor is desired, use null.
        @return an address set of where differences were found between the two
         programs based on the current filter setting.
         The addresses in this address set are derived from program1.
        @throws CancelledException if the user cancelled the Diff.
        """
        ...

    @overload
    def getDifferences(self, filter: ghidra.program.util.ProgramDiffFilter, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.address.AddressSetView:
        """
        <CODE>getDifferences</CODE> is used to determine
         the addresses where there are differences between two programs. This
         method only indicates that there is a difference at the address, not what
         type of difference it is. Possible differences are:
         the actual bytes at an address, comments, labels, code units,
         references, equates, properties, tags and program context register values.
         <P>The specified filter will become the new current filter.
        @param filter the filter to use instead of the current filter defined for
         this ProgramDiff.
        @param monitor the task monitor for indicating the progress of
         determining differences. This monitor also allows the user to cancel if
         the diff takes too long. If no monitor is desired, use null.
        @return an address set of where differences were found between the two
         programs based on the specified filter setting.
         The addresses in this address set are derived from program1.
        @throws CancelledException if the user cancelled the Diff.
        """
        ...

    def getFilter(self) -> ghidra.program.util.ProgramDiffFilter:
        """
        Returns a new ProgramDiffFilter equal to the one in this program diff.
         The filter indicates which types of differences are to be determined.
        @return a copy of the program diff filter currently in use.
        """
        ...

    def getIgnoreAddressSet(self) -> ghidra.program.model.address.AddressSetView:
        """
        Get the address set that contains addresses that should not be indicated as
         having any differences.
         The addresses in this address set are derived from program1.
        """
        ...

    def getInitializedInCommon(self) -> ghidra.program.model.address.AddressSet:
        """
        Returns the initialized memory addresses in common between
         program1 and program2.
        @return the initialized memory addresses in common between
         program1 and program2.
         The addresses in the this set are derived from program1.
        """
        ...

    def getLimitedAddressSet(self) -> ghidra.program.model.address.AddressSetView:
        """
        Get the address set that the diff process is limited to when checking for differences.
         Returns null if the diff is not limited (i.e. the entire program is being diffed).
         The addresses in the returned address set are derived from program1.
        """
        ...

    def getProgramOne(self) -> ghidra.program.model.listing.Program:
        """
        Gets the first program being compared by the ProgramDiff.
        @return program1.
        """
        ...

    def getProgramTwo(self) -> ghidra.program.model.listing.Program:
        """
        Gets the second program being compared by the ProgramDiff.
        @return program2.
        """
        ...

    def getRestrictedAddressSet(self) -> ghidra.program.model.address.AddressSetView:
        """
        Get the address set that the getDifferences method results are restricted to.
         null indicates no current restrictions.
         The addresses in the returned address set are derived from program1.
        """
        ...

    def getTypeDiffs(self, diffType: int, addrs: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.address.AddressSetView:
        """
        Creates an address set indicating the differences between program1 and
         program2 of the specified type.
        @param diffType the type of difference to look for between the programs.
        @param addrs the addresses to check for differences.
         The addresses in this address set should be derived from program1.
        @param monitor the task monitor for indicating the progress of
         determining differences. This monitor reports the progress to the user.
        @return the address set indicating the differences.
         The addresses in this address set are derived from program1.
        @throws CancelledException if the user cancelled the Diff.
        """
        ...

    def getUserDefinedDiffs(self, property: unicode, addrs: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.address.AddressSetView:
        """
        Returns an address set indicating where the user defined property differs
         between the Diff's two programs within the specified address set.
        @param property the user defined property
        @param addrs the address set for limiting checking.
         The addresses in this address set should be derived from program1.
        @param monitor the progress monitor.
        @return the address set indicating where the property differs.
         The addresses in this address set are derived from program1.
        @throws CancelledException if the user cancelled the Diff.
        """
        ...

    def getWarnings(self) -> unicode:
        """
        Get a message indicating any warnings about this PRogramDiff. For example,
         if the program context registers don't match between the programs, the
         string is a message indicating this.
        @return the warning message string. null if no warnings.
        """
        ...

    def hashCode(self) -> int: ...

    def ignore(self, addrs: ghidra.program.model.address.AddressSetView) -> None:
        """
        Set the indicated additional addresses that should not report any
         differences that are found at them.
        @param addrs the set of addresses to add to the current ignore set.
         The addresses in this address set should be derived from program1.
        """
        ...

    def isCancelled(self) -> bool:
        """
        Returns whether the last <CODE>getDifferences</CODE> call was cancelled.
         If a TaskMonitor displays a progress dialog to the user, then the cancel
         button could have been pressed.
        @return true if the last <CODE>getDifferences</CODE> call was cancelled.
        """
        ...

    @staticmethod
    def isEquivalentThunk(thunkFunction1: ghidra.program.model.listing.Function, thunkFunction2: ghidra.program.model.listing.Function) -> bool:
        """
        Compares two thunk functions from different programs to determine if they are
         equivalent to each other (effectively the same thunk function in the other program).
        @param thunkFunction1 the first thunk function
        @param thunkFunction2 the second thunk function
        @return true if the functions are equivalent thunk functions.
        """
        ...

    def isSameOperandEquates(self, address: ghidra.program.model.address.Address, opIndex: int) -> bool:
        """
        Determines if the two programs have the same equates specified at
         the indicated address and operand
        @param address the address
         This address should be derived from program1.
        @param opIndex the operand index
        @return true if both programs have the same operands.
        """
        ...

    def memoryMatches(self) -> bool:
        """
        Return true if the programs to compare have matching memory maps.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def printDifferences(self) -> None:
        """
        Print the differences that have been found so far by calls to
         <CODE>getDifferences</CODE>.
        """
        ...

    def printKnownDifferences(self, type: int) -> None:
        """
        Print the differences matching the types indicated that were found thus
         far by all calls to <CODE>getDifferences</CODE>.
        @param type the type(s) of differences we want to see.
         Valid types are: BYTE_DIFFS, CODE_UNIT_DIFFS,
         COMMENT_DIFFS, REFERENCE_DIFFS, USER_DEFINED_DIFFS,
         SYMBOL_DIFFS, EQUATE_DIFFS, PROGRAM_CONTEXT_DIFFS.
        """
        ...

    def printKnownDifferencesByType(self, type: int) -> None:
        """
        Print the differences matching the types indicated that were found thus
         far by all calls to getDifferences. The differences are grouped by
         each of the primary difference types.
        @param type the type(s) of differences we want to see.
         Valid types are: BYTE_DIFFS, CODE_UNIT_DIFFS,
         COMMENT_DIFFS, REFERENCE_DIFFS, USER_DEFINED_DIFFS,
         SYMBOL_DIFFS, EQUATE_DIFFS, PROGRAM_CONTEXT_DIFFS.
        """
        ...

    @staticmethod
    def sameFunctionNames(f1: ghidra.program.model.listing.Function, f2: ghidra.program.model.listing.Function) -> bool: ...

    def setFilter(self, filter: ghidra.program.util.ProgramDiffFilter) -> None:
        """
        Sets the ProgramDiffFilter for this program diff. The filter indicates
         which types of differences are to be determined.
        @param filter the program diff filter
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
    def addressesInCommon(self) -> ghidra.program.model.address.AddressSet: ...

    @property
    def addressesOnlyInOne(self) -> ghidra.program.model.address.AddressSet: ...

    @property
    def addressesOnlyInTwo(self) -> ghidra.program.model.address.AddressSet: ...

    @property
    def cancelled(self) -> bool: ...

    @property
    def combinedAddresses(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def filter(self) -> ghidra.program.util.ProgramDiffFilter: ...

    @filter.setter
    def filter(self, value: ghidra.program.util.ProgramDiffFilter) -> None: ...

    @property
    def ignoreAddressSet(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def initializedInCommon(self) -> ghidra.program.model.address.AddressSet: ...

    @property
    def limitedAddressSet(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def programOne(self) -> ghidra.program.model.listing.Program: ...

    @property
    def programTwo(self) -> ghidra.program.model.listing.Program: ...

    @property
    def restrictedAddressSet(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def warnings(self) -> unicode: ...
