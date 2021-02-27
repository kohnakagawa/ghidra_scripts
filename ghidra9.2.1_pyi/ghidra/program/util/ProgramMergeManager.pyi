import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.util
import ghidra.util.task
import java.lang


class ProgramMergeManager(object):
    """
    ProgramMergeManager is a class for merging the differences between two
     programs as specified by a ProgramMergeFilter and the address
     ranges to be merged.
     Program1 is the program being modified by the merge. Program2 is source
     for obtaining differences to apply to program1.

     ProgramDiff is being used to determine the differences between
     the two programs.
     If name conflicts occur while merging, the item (for example, symbol) will
     be merged with a new name that consists of the original name followed by "_conflict"
     and a one up number.
    """





    @overload
    def __init__(self, program1: ghidra.program.model.listing.Program, program2: ghidra.program.model.listing.Program, monitor: ghidra.util.task.TaskMonitor):
        """
        <CODE>ProgramMergeManager</CODE> allows the merging of differences from program1
         or program2 into the merged program.
        @param program1 the first program (read only) for the merge.
        @param program2 the second program (read only) for the merge.
        @param monitor the task monitor for indicating progress at determining
          the differences. This also allows the user to cancel the merge.
        @throws ProgramConflictException if the memory blocks, that overlap
         between the two programs, do not match. This indicates that programs
         couldn't be compared to determine the differences.
        """
        ...

    @overload
    def __init__(self, program1: ghidra.program.model.listing.Program, program2: ghidra.program.model.listing.Program, p1LimitedAddressSet: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor):
        """
        <CODE>ProgramMergeManager</CODE> allows the merging of differences from program1
         or program2 into the merged program.
        @param program1 the first program for the merge. This program will get
         modified by merge.
        @param program2 the second program (read only) for the merge.
        @param p1LimitedAddressSet the limited address set. program differences
         can only be merged if they overlap this address set. null means find
         differences in each of the entire programs.
         The addresses in this set should be derived from program1.
        @param monitor the task monitor for indicating progress at determining
          the differences. This also allows the user to cancel the merge.
        @throws ProgramConflictException if the memory blocks, that overlap
         between the two programs, do not match. This indicates that programs
         couldn't be compared to determine the differences.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getAddressesInCommon(self) -> ghidra.program.model.address.AddressSetView:
        """
        Returns the addresses in common between program1 and program2
        @return the addresses in common between program1 and program2.
         The addresses in this address set are derived from program1.
        """
        ...

    def getAddressesOnlyInOne(self) -> ghidra.program.model.address.AddressSetView:
        """
        Returns the addresses that are in program1, but not in program2
        @return the addresses that are in program1, but not in program2.
         The addresses in this address set are derived from program1.
        """
        ...

    def getAddressesOnlyInTwo(self) -> ghidra.program.model.address.AddressSetView:
        """
        Returns the addresses that are in program2, but not in program1
        @return the addresses that are in program2, but not in program1.
         The addresses in this address set are derived from program2.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getCombinedAddresses(self) -> ghidra.program.model.address.AddressSetView:
        """
        Returns the addresses from combining the address sets in program1 and program2
        @return the addresses for both program1 and program2.
         The addresses in this address set are derived from program1.
        """
        ...

    def getDiffFilter(self) -> ghidra.program.util.ProgramDiffFilter:
        """
        Get a copy of the diff filter that the merge is using.
        """
        ...

    def getErrorMessage(self) -> unicode:
        """
        Get the error messages that resulted from doing the merge.
        @return String empty string if there were no problems with the merge.
        """
        ...

    @overload
    def getFilteredDifferences(self) -> ghidra.program.model.address.AddressSetView:
        """
        Gets the filtered program differences for this merge. Only differences are
         indicated for merge filter categories that are enabled and for address
         that have not been marked as ignored.
        @return the program differences.
         The addresses in this address set are derived from program2.
        """
        ...

    @overload
    def getFilteredDifferences(self, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.address.AddressSetView:
        """
        Gets the filtered program differences for this merge. Only differences are
         indicated for merge filter categories that are enabled and for address
         that have not been marked as ignored.
        @param monitor the task monitor for indicating the progress of
         determining differences. This monitor also allows the user to cancel if
         the diff takes too long. If no monitor is desired, use null.
        @return the program differences.
         The addresses in this address set are derived from program2.
        """
        ...

    def getIgnoreAddressSet(self) -> ghidra.program.model.address.AddressSetView:
        """
        Get the address set indicating the addresses to be ignored (not checked) when determining
         differences between the two programs.
        @return the set of addresses to ignore.
         The addresses in this address set are derived from program1.
        """
        ...

    def getInfoMessage(self) -> unicode:
        """
        Get the informational messages that resulted from doing the merge.
        @return String empty string if there were no information messages
         generated during the merge.
        """
        ...

    def getLimitedAddressSet(self) -> ghidra.program.model.address.AddressSetView:
        """
        Get the address set that the process of determining differences is limited to.
         In other words, only addresses in this set will be checked by the Diff.
        @return the address set
         The addresses in this address set are derived from program1.
        """
        ...

    def getMergeFilter(self) -> ghidra.program.util.ProgramMergeFilter:
        """
        Get a copy of the filter that indicates which parts of the Program
         should be merged.
        """
        ...

    def getProgramOne(self) -> ghidra.program.model.listing.Program:
        """
        Gets the first program being compared by the ProgramDiff.
        @return program1. This is the program being modified by the merge.
         The addresses in this address set are derived from program1.
        """
        ...

    def getProgramTwo(self) -> ghidra.program.model.listing.Program:
        """
        Gets the second program being compared by the ProgramDiff.
        @return program2. This is the program for obtaining the program information to merge.
        """
        ...

    def getRestrictedAddressSet(self) -> ghidra.program.model.address.AddressSetView:
        """
        Return the address set that is currently being used to restrict the
         differences that get returned.
        @return the address set being used to restrict the Diff results.
         The addresses in this set are derived from program1.
        """
        ...

    def getWarnings(self) -> unicode:
        """
        Gets a string indicating warnings that occurred during the initial Diff
         of the two programs.
        @return the warnings
        """
        ...

    def hashCode(self) -> int: ...

    def ignore(self, p1AddressSet: ghidra.program.model.address.AddressSetView) -> None:
        """
        Ignore the differences for the indicated address set.
        @param p1AddressSet the address set to be merged.
         The addresses in this set should be derived from program1.
        """
        ...

    def memoryMatches(self) -> bool:
        """
        Determine whether memory between the two programs matches.
         For example, if one program has more memory than the other then it
         doesn't match or if the address ranges for memory are different for
         the two programs then they don't match.
        @return whether the memory matches between the two programs.
        """
        ...

    @overload
    def merge(self, p2Address: ghidra.program.model.address.Address, filter: ghidra.program.util.ProgramMergeFilter) -> bool:
        """
        Merge the differences from the indicated program at the specified
          address with the indicated filtering.
        @param p2Address the address to be merged.
         This address should be derived from program2.
        @param filter the filter indicating what types of differences to merge.
        @return true if merge succeeds
        @throws MemoryAccessException if bytes can't be copied.
        @throws CancelledException if user cancels via the monitor.
        """
        ...

    @overload
    def merge(self, p2Address: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        Merge the differences from the indicated program at the specified
          address with the current filtering.
        @param p2Address the address to be merged.
         This address should be derived from program2.
        @param monitor monitor for reporting merge status to the user.
        @return true if merge succeeds
        @throws MemoryAccessException if bytes can't be copied.
        @throws CancelledException if user cancels via the monitor.
        """
        ...

    @overload
    def merge(self, p1MergeSet: ghidra.program.model.address.AddressSetView, filter: ghidra.program.util.ProgramMergeFilter) -> bool:
        """
        Merge the differences from the indicated program on the specified
          address set with the indicated filtering.
        @param p1MergeSet the address set to be merged.
         The addresses in this set should be derived from program1.
        @param filter the filter indicating what types of differences to merge.
        @return true if merge succeeds
        @throws MemoryAccessException if bytes can't be copied.
        @throws CancelledException if user cancels via the monitor.
        """
        ...

    @overload
    def merge(self, p1MergeSet: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        Merge the differences from the indicated program on the specified
          address set with the filtering that is currently set.
        @param p1MergeSet the address set to be merged
         The addresses in this set should be derived from program1.
        @param monitor task monitor for reporting merge status to the user.
        @return true if merge succeeds
        @throws MemoryAccessException if bytes can't be copied.
        @throws CancelledException if user cancels via the monitor.
        """
        ...

    @overload
    def merge(self, p2Address: ghidra.program.model.address.Address, filter: ghidra.program.util.ProgramMergeFilter, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        Merge the differences from the indicated program at the specified
          address with the indicated filtering.
        @param p2Address the address to be merged.
         This address should be derived from program2.
        @param filter the filter indicating what types of differences to merge.
        @param monitor monitor for reporting merge status to the user.
        @return true if merge succeeds
        @throws MemoryAccessException if bytes can't be copied.
        @throws CancelledException if user cancels via the monitor.
        """
        ...

    @overload
    def merge(self, p1MergeSet: ghidra.program.model.address.AddressSetView, filter: ghidra.program.util.ProgramMergeFilter, monitor: ghidra.util.task.TaskMonitor) -> bool:
        """
        Merge the differences from the indicated program on the specified
          address set with the indicated filtering.
        @param p1MergeSet the address set to be merged
         The addresses in this set should be derived from program1.
        @param filter the filter indicating what types of differences to merge.
        @param monitor task monitor for reporting merge status to the user.
        @return true if merge succeeds
        @throws MemoryAccessException if bytes can't be copied.
        @throws CancelledException if user cancels via the monitor.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeResultRestrictions(self) -> None:
        """
        Remove the restriction for the resulting differences to the indicated address set.
        """
        ...

    def restrictResults(self, p1AddressSet: ghidra.program.model.address.AddressSetView) -> None:
        """
        Restrict the resulting differences to the indicated address set.
         Although the Diff will check for differences based on the limited set, the resulting
         differences from calls to getDifferences() will only return addresses contained in
         this restricted address set.
        @param p1AddressSet the address set to restrict the getFilteredDifferences() to.
         The addresses in this set are derived from program1.
        """
        ...

    def setDiffFilter(self, filter: ghidra.program.util.ProgramDiffFilter) -> None:
        """
        Set the filter that indicates which parts of the Program should be
         diffed.
        @param filter the filter indicating the types of differences to be
         determined by this ProgramMerge.
        """
        ...

    def setMergeFilter(self, filter: ghidra.program.util.ProgramMergeFilter) -> None:
        """
        Set the filter that indicates which parts of the Program should be
         applied from the second program to the first program.
        @param filter the filter indicating the types of differences to apply.
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
    def addressesInCommon(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def addressesOnlyInOne(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def addressesOnlyInTwo(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def combinedAddresses(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def diffFilter(self) -> ghidra.program.util.ProgramDiffFilter: ...

    @diffFilter.setter
    def diffFilter(self, value: ghidra.program.util.ProgramDiffFilter) -> None: ...

    @property
    def errorMessage(self) -> unicode: ...

    @property
    def filteredDifferences(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def ignoreAddressSet(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def infoMessage(self) -> unicode: ...

    @property
    def limitedAddressSet(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def mergeFilter(self) -> ghidra.program.util.ProgramMergeFilter: ...

    @mergeFilter.setter
    def mergeFilter(self, value: ghidra.program.util.ProgramMergeFilter) -> None: ...

    @property
    def programOne(self) -> ghidra.program.model.listing.Program: ...

    @property
    def programTwo(self) -> ghidra.program.model.listing.Program: ...

    @property
    def restrictedAddressSet(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def warnings(self) -> unicode: ...
