from typing import List
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.model.symbol
import ghidra.util
import ghidra.util.prop
import ghidra.util.task
import java.lang
import java.util


class ProgramMerge(object, ghidra.util.prop.PropertyVisitor):
    """
    ProgramMerge is a class for merging the differences between two
     programs. The differences are merged from program2 into program1.
     Program1 is the program being modified by the merge. Program2 is source
     for obtaining differences to apply to program1.
     If name conflicts occur while merging, the item (for example, symbol) will
     be merged with a new name that consists of the original name followed by "_conflict"
     and a one up number.
    """

    SYMBOL_CONFLICT_SUFFIX: unicode



    @overload
    def __init__(self, originToResultTranslator: ghidra.program.util.AddressTranslator):
        """
        <CODE>ProgramMerge</CODE> allows the merging of differences from program2 (the origin program)
         into program1 (the result program).
         <br>If the address translator is not a "one for one translator" then certain methods within
         this class will throw an UnsupportedOperationException.
         The destination program from the address translator should be the result program into
         which changes are made.
         The source program from the translator is the origin program for obtaining the changes.
        @param originToResultTranslator converts addresses from the origin program into an
         equivalent address in the destination program.
        @see AddressTranslator
        """
        ...

    @overload
    def __init__(self, resultProgram: ghidra.program.model.listing.Program, originProgram: ghidra.program.model.listing.Program):
        """
        <CODE>ProgramMerge</CODE> allows the merging of differences from program2
         into program1 (the result program).
        @param resultProgram The result program that will get modified by merge.
        @param originProgram The program (used as read only) for obtaining
         differences to merge.
        """
        ...



    def addReference(self, originRef: ghidra.program.model.symbol.Reference, toSymbolID: long, replaceExtLoc: bool) -> ghidra.program.model.symbol.Reference:
        """
        <CODE>addReference</CODE> creates a reference in program1 that is equivalent
         to the one specified as a parameter. If a symbol ID is specified, the
         reference will refer to the symbol in program1 with that ID. If the reference
         is an external reference, then the external location associated with it can be replaced
         also by setting the replace external location flag.
        @param originRef the reference equivalent to the one to be created.
        @param toSymbolID ID of the symbol to referred to. null indicates don't
         refer directly to a symbol.
        @param replaceExtLoc the replace external location flag. true indicates to replace the
         external location, if applicable, with the one defined for the reference passed to this method.
        @return the reference that was created. null if none created.
        """
        ...

    def applyFunctionTagChanges(self, originAddressSet: ghidra.program.model.address.AddressSetView, setting: int, discardTags: java.util.Set, keepTags: java.util.Set, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Merges/replaces tags of program2 into program1. When merging, tags that are in
         conflict are replaced according to the user setting (ignore, replace, merge).
        @param originAddressSet the addresses to be merged.
        @param setting how to merge. IGNORE, REPLACE, MERGE
        @param discardTags tags to keep out of the final result
        @param keepTags tags to add to the final result
        @param monitor the task monitor for notifying the user of this merge's progress.
        @throws CancelledException if user cancels via the monitor.
        """
        ...

    def clearErrorMessage(self) -> None:
        """
        This method clears the current error message.
        """
        ...

    def clearInfoMessage(self) -> None:
        """
        This method clears the current informational message.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getErrorMessage(self) -> unicode:
        """
        Get the error messages that resulted from the last call to a merge or
         replace method. These are errors that prevented something from being merged.
         <br>Important: Call clearErrorMessage() to clear the current error message after this returns it.
        @return the error message string or an empty string if there were no problems with the merge.
        """
        ...

    def getInfoMessage(self) -> unicode:
        """
        Get the information messages that resulted from the last call to a merge or
         replace method. These messages are non-critical changes that were
         necessary during the merge. For example giving a symbol a name with a conflict
         extension because another symbol with that name existed elsewhere in the
         program already.
         <br>Important: Call clearInfoMessage() to clear the current info message after this returns it.
        @return the information message string or an empty string if there were no informational
         messages for the merge.
        """
        ...

    def getOriginProgram(self) -> ghidra.program.model.listing.Program:
        """
        Gets the origin program. This program is used for obtaining things to merge into program1.
        @return the program we are obtaining the changes from which we will merge.
        """
        ...

    def getResultProgram(self) -> ghidra.program.model.listing.Program:
        """
        Gets the result program. Merge changes are applied to this program.
        @return the program being changed by the merge.
        """
        ...

    @overload
    @staticmethod
    def getUniqueName(symbolTable: ghidra.program.model.symbol.SymbolTable, name: unicode, address: ghidra.program.model.address.Address, namespace: ghidra.program.model.symbol.Namespace, type: ghidra.program.model.symbol.SymbolType) -> unicode:
        """
        Create a name that is unique in the indicated namespace of the symbol table.
        @param symbolTable the symbolTable where the symbol will be created.
        @param name the desired name. This name will be given a conflict suffix if necessary
         to make it unique.
        @param address the address of the symbol.
        @param namespace the namespace where the new symbol would be created.
         This namespace must be from the same program as the symbol table.
        @param type the type of symbol.
        @return a unique name within the namespace.
        """
        ...

    @overload
    @staticmethod
    def getUniqueName(symbolTable: ghidra.program.model.symbol.SymbolTable, name: unicode, address: ghidra.program.model.address.Address, namespace1: ghidra.program.model.symbol.Namespace, namespace2: ghidra.program.model.symbol.Namespace, type: ghidra.program.model.symbol.SymbolType) -> unicode:
        """
        Create a name that is unique in both namespaces of the given symbolTable.
        @param symbolTable the symbolTable where the symbol will be created.
        @param name the desired name. This name will be given a conflict suffix if necessary
         to make it unique.
        @param address the address of the symbol.
        @param namespace1 the first namespace where the new symbol should be unique.
         This namespace must be from the same program as the symbol table.
        @param namespace2 the second namespace where the new symbol should be unique.
         This namespace must be from the same program as the symbol table.
        @param type the symbol type of the symbol.
        @return a unique name for both namespaces.
        """
        ...

    def hasErrorMessage(self) -> bool:
        """
        Determines if this ProgramMerge currently has an error message.
        @return true if there is an error message.
        """
        ...

    def hasInfoMessage(self) -> bool:
        """
        Determines if this ProgramMerge currently has an informational message.
        @return true if there is an information message.
        """
        ...

    def hashCode(self) -> int: ...

    def mergeBookmark(self, originAddress: ghidra.program.model.address.Address, type: unicode, category: unicode, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        <CODE>mergeBookmark</CODE> merges the indicated bookmark from the origin program into the
         result program at an address equivalent to the originAddress.
         Merging means replace any existing bookmark of the specified type for NOTEs
         or of the specified type and category for non-NOTE types.
         <p>Note: This method merges a single bookmark without affecting
         other bookmarks at the indicated address.
        @param originAddress the address in the origin program where the bookmark is to be merged.
        @param type indicates the type of bookmark to merge.
        @param category indicates the category of the bookmark.
        @param monitor a task monitor for providing feedback to the user.
        @throws CancelledException if the user cancels the bookmark merge from the monitor dialog.
        """
        ...

    def mergeBytes(self, originAddressSet: ghidra.program.model.address.AddressSetView, overwriteInstructions: bool, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        <CODE>mergeBytes</CODE> merges byte differences within the specified
          address set.
         <br>Note: Any instructions at the equivalent byte addresses in the result program will get cleared and
         re-created resulting in the existing references being dropped.
        @param originAddressSet the addresses to be merged.
         The addresses in this set are derived from the origin program.
        @param overwriteInstructions if true affected instructions will be cleared and
         re-disassmebled after bytes are modified
        @param monitor the task monitor for notifying the user of this merge's
         progress.
        @throws MemoryAccessException if bytes can't be merged.
        @throws CancelledException if user cancels via the monitor.
        @throws UnsupportedOperationException if the ProgramMerge translator is not a
         "one for one translator".
        """
        ...

    def mergeCodeUnits(self, originAddressSet: ghidra.program.model.address.AddressSetView, byteDiffs: ghidra.program.model.address.AddressSetView, mergeDataBytes: bool, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        <CODE>mergeCodeUnits</CODE> merges all instructions and/or data
         (as indicated) in the specified address set from the origin program.
         It merges them into the result program. When merging
         instructions, the bytes are also replaced if they differ.
         This assumes originToResultTranslator maps address spaces and does
         not do fine-grained mapping of addresses.
        @param originAddressSet the addresses to be merged.
         The addresses in this set should be derived from the origin program.
        @param byteDiffs address set indicating addresses where the bytes differ
         between the result program and the origin program.
         The addresses in this set should be derived from the origin program.
        @param mergeDataBytes true indicates bytes that differ should be copied when merging Data.
         false means don't copy any bytes for Data.
        @param monitor the task monitor for notifying the user of this merge's
         progress.
        @throws MemoryAccessException if bytes can't be copied.
        @throws CancelledException if user cancels via the monitor.
        @throws UnsupportedOperationException if the ProgramMerge translator is not a
         "one for one translator".
        """
        ...

    def mergeComment(self, originAddressSet: ghidra.program.model.address.AddressSet, type: int, both: bool, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        <CODE>mergeComment</CODE> merges/replaces comments of the indicated
         type wherever they occur in the specified address set.
        @param originAddressSet the addresses where comments should be merged/replaced.
         The addresses in this set should be from the origin program.
        @param type ProgramMergeFilter comment type.
         The comment type can be PLATE, PRE, EOL, REPEATABLE, POST.
        @param both true means merge both program1 and program2 comments.
         false means replace the program1 comment with the program2 comment.
        @param monitor the task monitor for notifying the user of this merge's progress.
        @throws CancelledException if user cancels via the monitor.
        """
        ...

    def mergeCommentType(self, originAddressSet: ghidra.program.model.address.AddressSetView, type: int, setting: int, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        <CODE>mergeCommentType</CODE> merges/replaces comments of the indicated
         type wherever they occur in the specified address set.
         It merges them from program2 into program1.
         This merges eol, pre, post, repeatable, and plate comments.
        @param originAddressSet the addresses to be merged.
         The addresses in this set should be derived from the origin program.
        @param type the comment type. PLATE, PRE, EOL, REPEATABLE, POST
        @param setting how to merge. IGNORE, REPLACE, MERGE
        @param monitor the task monitor for notifying the user of this merge's progress.
        @throws CancelledException if user cancels via the monitor.
        """
        ...

    def mergeComments(self, commentType: int, originAddress: ghidra.program.model.address.Address) -> None:
        """
        <CODE>mergeComments</CODE> merges the comment of the indicated
         type in program1 with the comment in program2 at the specified address.
        @param commentType comment type to merge (from CodeUnit class).
         <br>EOL_COMMENT, PRE_COMMENT, POST_COMMENT, REPEATABLE_COMMENT, OR PLATE_COMMENT.
        @param originAddress the address
         This address should be derived from the origin program.
        """
        ...

    def mergeEquate(self, originAddress: ghidra.program.model.address.Address, opIndex: int, value: long) -> None:
        """
        <CODE>mergeEquate</CODE> replaces the current equates in program1 with those in program2.
        @param originAddress the address where the equates should be merged.
         This address should be derived from the origin program.
        @param opIndex the operand index where the equates should be merged.
        @param value the scalar value where the equate is used.
        """
        ...

    def mergeEquates(self, originAddressSet: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        <CODE>mergeEquates</CODE> merges the equate differences in the specified
         address set.
        @param originAddressSet the addresses to be merged.
         The addresses in this set should be derived from the origin program.
        @param monitor the task monitor for notifying the user of this merge's
         progress.
        @throws CancelledException if user cancels via the monitor.
        @throws UnsupportedOperationException if the ProgramMerge translators are not
         "one for one translators".
        """
        ...

    def mergeFunction(self, entry: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.listing.Function:
        """
        <CODE>mergeFunction</CODE> completely replaces any function at the
         indicated address in program1 with the function, if any, in program2.
        @param entry the entry point address of the function to be merged.
         This address should be derived from program1.
        @param monitor the task monitor for notifying the user of this merge's progress.
        @throws CancelledException if user cancels via the monitor.
        """
        ...

    def mergeFunctionLocalSize(self, entry2: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        <CODE>mergeFunctionLocalSize</CODE> replaces the local size of the
         function in program1 with the local size of the function in program2
         at the specified entry point address.
        @param entry2 the entry point address of the function.
         This address should be derived from the origin program.
        @param monitor the task monitor for notifying the user of this merge's progress.
        """
        ...

    def mergeFunctionName(self, entry2: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        <CODE>mergeFunctionName</CODE> replaces the name of the
         function in program1 with the name of the function in program2
         at the specified entry point address.
        @param entry2 the entry point address of the function.
         This address should be derived from the origin program.
        @param monitor the task monitor for notifying the user of this merge's progress.
        """
        ...

    def mergeFunctionReturn(self, entry2: ghidra.program.model.address.Address) -> None:
        """
        <CODE>mergeFunctionReturn</CODE> replaces the return type/storage of the
         function in program1 with the return type/storage of the function in program2
         at the specified entry point address.
        @param entry2 the entry point address of the function.
         This address should be derived from the origin program.
        """
        ...

    def mergeFunctionReturnAddressOffset(self, entry2: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        <CODE>mergeFunctionReturnAddressOffset</CODE> replaces the return address offset of the
         function in program1 with the return address offset of the function in program2
         at the specified entry point address.
        @param entry2 the entry point address of the function.
         This address should be derived from the origin program.
        @param monitor the task monitor for notifying the user of this merge's progress.
        """
        ...

    def mergeFunctionStackPurgeSize(self, entry2: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        <CODE>mergeFunctionStackPurgeSize</CODE> replaces the stack purge size of the
         function in program1 with the stack purge size of the function in program2
         at the specified entry point address.
        @param entry2 the entry point address of the function.
         This address should be derived from the origin program.
        @param monitor the task monitor for notifying the user of this merge's progress.
        """
        ...

    def mergeFunctions(self, addrSet: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        <CODE>mergeFunctions</CODE> merges function differences within the specified
          address set.
        @param addrSet the addresses to be merged.
         The addresses in this set should be derived from program1.
        @param monitor the task monitor for notifying the user of this merge's
         progress.
        @throws CancelledException if user cancels via the monitor.
        """
        ...

    def mergeLabels(self, originAddressSet: ghidra.program.model.address.AddressSetView, setting: int, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        <CODE>mergeLabels</CODE> merges all symbols and aliases
         in the specified address set from the second program.
         It merges them into the merge program.
        @param originAddressSet the addresses to be merged.
         The addresses in this address set should be derived from program1.
        @param setting the current label setting.
        @param monitor the task monitor for notifying the user of this merge's
         progress.
        @throws CancelledException if user cancels via the monitor.
        """
        ...

    def mergeProperties(self, originAddressSet: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        <CODE>mergeProperties</CODE> merges user defined property differences
          within the specified address set.
        @param originAddressSet the addresses to be merged from the origin program.
        @param monitor the task monitor for notifying the user of this merge's progress.
        @throws CancelledException if user cancels via the monitor.
        @throws UnsupportedOperationException if the ProgramMerge translator is not a
         "one for one translator".
        """
        ...

    def mergeReferences(self, originAddressSet: ghidra.program.model.address.AddressSetView, onlyKeepDefaults: bool, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        <CODE>mergeReferences</CODE> merges the references in
         program1 for the specified address set with the references from program2.
         If an equivalent reference already exists then it is updated to match the
         new reference if possible. A merge of references prevents the loss of any
         non-default references already in the result program.
         <br> Important: Fallthrough references will not be merged by this method.
         Fallthroughs are handled by merging code units.
         <br> Note: All reference types (memory, stack, external) get replaced
         where possible. i.e. If a function or variable doesn't exist for a
         variable reference then it will not be able to replace the reference.
        @param originAddressSet the addresses to be merged.
         The addresses in this set should be derived from the origin program.
        @param onlyKeepDefaults true indicates to merge only the default references
         from the origin program into the result program. Non-default references will not be merged.
         false indicates merge all references except fallthroughs.
        @param monitor the task monitor for notifying the user of this merge's
         progress.
        @throws CancelledException if the user cancels the replace via the monitor.
        @throws UnsupportedOperationException if the ProgramMerge translators are not
         "one for one translators".
        """
        ...

    def mergeUserProperty(self, userPropertyName: unicode, originAddress: ghidra.program.model.address.Address) -> None:
        """
        Replaces the user defined properties from the specified origin address in the origin program
         to the equivalent result address in the result program.
         Note: To merge properties, there must be a code unit AT the equivalent address
         in the result program.
        @param originAddress the address of the code unit to get the properties from in the origin program.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def replaceComment(self, commentType: int, originAddress: ghidra.program.model.address.Address) -> None:
        """
        <CODE>replaceComment</CODE> replaces the comment of the indicated
         type in program1 with the comment in program2 at the specified address.
        @param commentType comment type to replace (from CodeUnit class).
         <br>EOL_COMMENT, PRE_COMMENT, POST_COMMENT, REPEATABLE_COMMENT, OR PLATE_COMMENT.
        @param originAddress the address
         This address should be derived from the origin program.
        """
        ...

    def replaceExternalFunction(self, toFunction: ghidra.program.model.listing.Function, fromFunction: ghidra.program.model.listing.Function, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.listing.Function:
        """
        Replaces the external result function with the origin Function.
         <br>Note: This method will replace the function, but does not create
         the parent namespace or put the function in the parent namespace.
         This must be done separately.
        @param toFunction the result function to replace.
        @param fromFunction the function to use as the model when replacing the result function.
        @param monitor the task monitor for notifying the user of this merge's progress.
        @return the new function that was created in the resultListing or null
         if no function was created. If null is returned you should call
         getErrorMessage() to see if an error occurred.
        @throws CancelledException if user cancels via the monitor.
        @throws UnsupportedOperationException if the ProgramMerge translators are not
         "one for one translators".
        """
        ...

    def replaceFallThroughs(self, originAddressSet: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        <CODE>replaceFallThroughs</CODE> replaces all fallthroughs in
         program1 for the specified address set with those in program2 where they differ.
        @param originAddressSet the addresses to be merged.
         The addresses in this set should be derived from the origin program.
        @param monitor the task monitor for notifying the user of this merge's
         progress.
        @throws CancelledException if the user cancels the replace via the monitor.
        """
        ...

    def replaceFunctionCallingConvention(self, originEntryPoint: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        <CODE>replaceFunctionCallingConvention</CODE> changes the function calling convention
         in program1 if it doesn't match the function calling convention in program2
         at the specified entry point address.
        @param originEntryPoint the entry point address of the function.
         This address should be derived from the origin program.
        @param monitor the task monitor for notifying the user of this merge's progress.
        """
        ...

    def replaceFunctionCustomStorageFlag(self, originEntryPoint: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        <CODE>replaceFunctionCustomStorageFlag</CODE> changes whether the flag is set indicating
         the function does not return
         in program1 if it doesn't match the "custom storage" flag in the function in program2
         at the specified entry point address.
        @param originEntryPoint the entry point address of the function.
         This address should be derived from the origin program.
        @param monitor the task monitor for notifying the user of this merge's progress.
        """
        ...

    def replaceFunctionInlineFlag(self, originEntryPoint: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        <CODE>replaceFunctionInlineFlag</CODE> changes whether the function is inline
         in program1 if it doesn't match whether the function is inline in program2
         at the specified entry point address.
        @param originEntryPoint the entry point address of the function.
         This address should be derived from the origin program.
        @param monitor the task monitor for notifying the user of this merge's progress.
        """
        ...

    def replaceFunctionNames(self, originAddressSet: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        <CODE>replaceFunctionNames</CODE> merges function name and namespace differences
         within the specified address set.
        @param originAddressSet the addresses to be merged.
         The addresses in this set should be derived from program1.
        @param monitor the task monitor for notifying the user of this merge's
         progress.
        @throws CancelledException if user cancels via the monitor.
        """
        ...

    def replaceFunctionNoReturnFlag(self, originEntryPoint: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        <CODE>replaceFunctionNoReturnFlag</CODE> changes whether the flag is set indicating
         the function does not return
         in program1 if it doesn't match the "does not return" flag in the function in program2
         at the specified entry point address.
        @param originEntryPoint the entry point address of the function.
         This address should be derived from the origin program.
        @param monitor the task monitor for notifying the user of this merge's progress.
        """
        ...

    def replaceFunctionParameterComment(self, originEntryPoint: ghidra.program.model.address.Address, ordinal: int, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        <CODE>replaceFunctionParameterComment</CODE> replaces the comment of the indicated
         function parameter in program1 with the comment from the origin program.
        @param originEntryPoint the entry point address of the function to modify.
         This address should be derived from the origin program.
        @param ordinal the index of the parameter to change.
        @param monitor the task monitor for notifying the user of progress.
        """
        ...

    def replaceFunctionParameterDataType(self, originEntryPoint: ghidra.program.model.address.Address, ordinal: int, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        <CODE>replaceFunctionParameterDataType</CODE> replaces the data type of the indicated
         function parameter in program1 with the data type from the origin program.
        @param originEntryPoint the entry point address of the function to modify.
         This address should be derived from the origin program.
        @param ordinal the index of the parameter to change.
        @param monitor the task monitor for notifying the user of progress.
        """
        ...

    def replaceFunctionParameterName(self, originEntryPoint: ghidra.program.model.address.Address, ordinal: int, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        <CODE>replaceFunctionParameterName</CODE> replaces the name of the indicated
         function parameter in program1 with the name from the origin program.
        @param originEntryPoint the entry point address of the function to modify.
         This address should be derived from the origin program.
        @param ordinal the index of the parameter to change.
        @param monitor the task monitor for notifying the user of progress.
        @throws InvalidInputException
        @throws DuplicateNameException
        """
        ...

    @overload
    def replaceFunctionParameters(self, originEntryPoint: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        <CODE>replaceFunctionParameters</CODE> replaces the parameters of the
         function in program1 with the parameters of the function in program2
         at the specified entry point address.  It also replaces the return
         type/storage as well as custom storage use.
        @param originEntryPoint the entry point address of the function.
         This address should be derived from the origin program.
        """
        ...

    @overload
    def replaceFunctionParameters(self, toFunc: ghidra.program.model.listing.Function, fromFunc: ghidra.program.model.listing.Function) -> None:
        """
        <CODE>replaceFunctionParameters</CODE> replaces the parameters of the
         function in program1 with the parameters of the function in program2
         at the specified entry point address.  It also replaces the return
         type/storage as well as custom storage use.
        @param toFunc target function
        @param fromFunc source function
        """
        ...

    def replaceFunctionSignatureSource(self, originEntryPoint: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        <CODE>replaceFunctionSignatureSource</CODE> changes the result function's signature source
         to match the origin program's signature source.
        @param originEntryPoint the entry point address of the function.
         This address should be derived from the origin program.
        @param monitor the task monitor for notifying the user of this merge's progress.
        """
        ...

    def replaceFunctionVarArgs(self, entry2: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        <CODE>replaceFunctionVarArgs</CODE> changes whether the function has VarArgs
         in program1 if it doesn't match the use of VarArgs in the function in program2
         at the specified entry point address.
        @param entry2 the entry point address of the function.
         This address should be derived from program1.
        @param monitor the task monitor for notifying the user of this merge's progress.
        """
        ...

    def replaceFunctionVariable(self, originEntryPoint: ghidra.program.model.address.Address, var: ghidra.program.model.listing.Variable, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        <CODE>replaceFunctionVariable</CODE> replaces the name of the indicated
         function variable in program1 with that from the origin program.
        @param originEntryPoint the entry point address of the function to modify.
         This address should be derived from program1.
        @param var a variable that is equivalent to the one in program1 to be replaced.
         The variable passed here could be from another program.
        @param monitor the task monitor for notifying the user of progress.
        """
        ...

    def replaceFunctionVariableComment(self, originEntryPoint: ghidra.program.model.address.Address, var: ghidra.program.model.listing.Variable, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        <CODE>replaceFunctionVariableComment</CODE> replaces the comment on the indicated
         function variable in program1 with the comment from the equivalent variable in program2.
        @param originEntryPoint entry point address of the function whose variable is getting the comment replaced.
         This address should be derived from the origin program.
        @param var a variable that is equivalent to the one in program1 to be changed.
         The variable passed here could be from another program.
        @param monitor the task monitor for notifying the user of progress.
        """
        ...

    def replaceFunctionVariableDataType(self, originEntryPoint: ghidra.program.model.address.Address, var: ghidra.program.model.listing.Variable, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        <CODE>replaceFunctionVariableDataType</CODE> replaces the data type on the indicated
         function variable in program1 with the data type from the equivalent variable in program2.
        @param originEntryPoint the entry point address of the function to modify.
         This address should be derived from the origin program.
        @param var a variable that is equivalent to the one in program1 to be changed.
         The variable passed here could be from another program.
        @param monitor the task monitor for notifying the user of progress.
        """
        ...

    def replaceFunctionVariableName(self, originEntryPoint: ghidra.program.model.address.Address, var: ghidra.program.model.listing.Variable, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        <CODE>replaceFunctionVariableName</CODE> replaces the name on the indicated
         function variable in program1 with the name from the equivalent variable in program2.
        @param originEntryPoint the entry point address of the function to modify.
         This address should be derived from the origin program.
        @param var a variable that is equivalent to the one in program1 to be changed.
         The variable passed here could be from another program.
        @param monitor the task monitor for notifying the user of progress.
        @throws InvalidInputException
        @throws DuplicateNameException
        """
        ...

    def replaceLabels(self, originAddressSet: ghidra.program.model.address.AddressSet, replaceFunction: bool, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        <CODE>replaceLabels</CODE> replaces all symbols and aliases
         in the specified address set from the second program.
        @param originAddressSet the addresses to be replaced
         The addresses in this address set should be derived from program1.
        @param replaceFunction true indicates the function symbol should be replaced
        @param monitor the task monitor for notifying the user of this merge's progress
        @throws CancelledException if user cancels via the monitor.
        """
        ...

    @overload
    def replaceReference(self, resultRef: ghidra.program.model.symbol.Reference, originRef: ghidra.program.model.symbol.Reference) -> ghidra.program.model.symbol.Reference:
        """
        Replaces the reference in program1 with the reference from the origin program.
        @param resultRef the program1 reference to be replaced.
        @param originRef the program2 reference used to replace what's in program1.
        @return the resulting reference in program1. null if reference is removed
         by the replace.
        """
        ...

    @overload
    def replaceReference(self, resultRef: ghidra.program.model.symbol.Reference, originRef: ghidra.program.model.symbol.Reference, toSymbolID: long) -> ghidra.program.model.symbol.Reference:
        """
        Replaces the reference in program1 with the reference from the origin program.
        @param resultRef the program1 reference to be replaced.
        @param originRef the program2 reference used to replace what's in program1.
        @param toSymbolID ID of the symbol in program1 the resulting reference is to.
        @return the resulting reference in program1. null if reference is removed
         by the replace.
        """
        ...

    @overload
    def replaceReferences(self, originAddress: ghidra.program.model.address.Address, operandIndex: int) -> None:
        """
        <CODE>replaceReferences</CODE> replaces all references in
         program1 for the specified address and operand index with those in program2.
         If an equivalent reference already exists then it is updated to match the
         new reference.
         <br> Note: All reference types (memory, stack, external) get replaced
         where possible. i.e. If a function or variable doesn't exist for a
         variable reference then it will not be able to replace the reference.
        @param originAddress the "from" address where references are to be replaced
        @param operandIndex the operand of the code unit at the address where
         references are to be replaced.
        """
        ...

    @overload
    def replaceReferences(self, originAddressSet: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        <CODE>replaceReferences</CODE> replaces all references in
         program1 for the specified address set with those in program2.
         If an equivalent reference already exists then it is updated to match the
         new reference.
         <br> Note: All reference types (memory, stack, external) get replaced
         where possible. i.e. If a function or variable doesn't exist for a
         variable reference then it will not be able to replace the reference.
        @param originAddressSet the addresses to be merged.
         The addresses in this set should be derived from the origin program.
        @param monitor the task monitor for notifying the user of this merge's
         progress.
        @throws CancelledException if the user cancels the replace via the monitor.
        @throws UnsupportedOperationException if the ProgramMerge translators are not
         "one for one translators".
        """
        ...

    @overload
    def replaceReferences(self, originAddressSet: ghidra.program.model.address.AddressSetView, onlyKeepDefaults: bool, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        <CODE>replaceReferences</CODE> replaces all references in
         program1 for the specified address set with the references from program2.
         If an equivalent reference already exists then it is updated to match the
         new reference.
         <br> Note: All reference types (memory, stack, external) get replaced
         where possible. i.e. If a function or variable doesn't exist for a
         variable reference then it will not be able to replace the reference.
        @param originAddressSet the addresses to be merged.
         The addresses in this set should be derived from the origin program.
        @param onlyKeepDefaults true indicates to replace all references with only
         the default references from the origin program.
        @param monitor the task monitor for notifying the user of this merge's
         progress.
        @throws CancelledException if the user cancels the replace via the monitor.
        @throws UnsupportedOperationException if the ProgramMerge translators are not
         "one for one translators".
        """
        ...

    def replaceVariables(self, __a0: ghidra.program.model.address.Address, __a1: List[object], __a2: ghidra.util.task.TaskMonitor) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def visit(self) -> None:
        """
        Set the property on the merge program's code unit if the named property
          is a void property type.
        """
        ...

    @overload
    def visit(self, value: int) -> None:
        """
        Set the property on the merge program's code unit if the named property
          is an int property type.
        @param value the value for the named property.
        """
        ...

    @overload
    def visit(self, value: unicode) -> None:
        """
        Set the property on the merge program's code unit if the named property
          is a String property type.
        @param value the value for the named property.
        """
        ...

    @overload
    def visit(self, value: ghidra.util.Saveable) -> None:
        """
        Set the property on the merge program's code unit if the named property
          is an Object property type.
        @param value the value for the named property.
        """
        ...

    @overload
    def visit(self, value: object) -> None:
        """
        Set the property on the merge program's code unit if the named property
          is an Object property type.
        @param value the value for the named property.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def errorMessage(self) -> unicode: ...

    @property
    def infoMessage(self) -> unicode: ...

    @property
    def originProgram(self) -> ghidra.program.model.listing.Program: ...

    @property
    def resultProgram(self) -> ghidra.program.model.listing.Program: ...
