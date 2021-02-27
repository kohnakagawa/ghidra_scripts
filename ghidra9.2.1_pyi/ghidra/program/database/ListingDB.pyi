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


class ListingDB(object, ghidra.program.model.listing.Listing):
    """
    Database implementation of Listing.
    """









    def addInstructions(self, instructionSet: ghidra.program.model.lang.InstructionSet, overwrite: bool) -> ghidra.program.model.address.AddressSetView:
        """
        @see ghidra.program.model.listing.Listing#addInstructions(ghidra.program.model.lang.InstructionSet, boolean)
        """
        ...

    def clearAll(self, clearContext: bool, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        @see ghidra.program.model.listing.Listing#clearAll(boolean, TaskMonitor)
        """
        ...

    @overload
    def clearCodeUnits(self, startAddr: ghidra.program.model.address.Address, endAddr: ghidra.program.model.address.Address, clearContext: bool) -> None:
        """
        @see ghidra.program.model.listing.Listing#clearCodeUnits(ghidra.program.model.address.Address, ghidra.program.model.address.Address, boolean)
        """
        ...

    @overload
    def clearCodeUnits(self, startAddr: ghidra.program.model.address.Address, endAddr: ghidra.program.model.address.Address, clearContext: bool, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        @see ghidra.program.model.listing.Listing#clearCodeUnits(ghidra.program.model.address.Address, ghidra.program.model.address.Address, boolean, ghidra.util.task.TaskMonitor)
        """
        ...

    def clearComments(self, startAddr: ghidra.program.model.address.Address, endAddr: ghidra.program.model.address.Address) -> None:
        """
        @see ghidra.program.model.listing.Listing#clearComments(ghidra.program.model.address.Address, ghidra.program.model.address.Address)
        """
        ...

    def clearProperties(self, startAddr: ghidra.program.model.address.Address, endAddr: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        @see ghidra.program.model.listing.Listing#clearProperties(ghidra.program.model.address.Address, ghidra.program.model.address.Address)
        """
        ...

    @overload
    def createData(self, addr: ghidra.program.model.address.Address, dataType: ghidra.program.model.data.DataType) -> ghidra.program.model.listing.Data:
        """
        @see ghidra.program.model.listing.Listing#createData(ghidra.program.model.address.Address, ghidra.program.model.data.DataType)
        """
        ...

    @overload
    def createData(self, addr: ghidra.program.model.address.Address, dataType: ghidra.program.model.data.DataType, length: int) -> ghidra.program.model.listing.Data:
        """
        @see ghidra.program.model.listing.Listing#createData(ghidra.program.model.address.Address, ghidra.program.model.data.DataType)
        """
        ...

    @overload
    def createFunction(self, name: unicode, entryPoint: ghidra.program.model.address.Address, body: ghidra.program.model.address.AddressSetView, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.listing.Function: ...

    @overload
    def createFunction(self, name: unicode, nameSpace: ghidra.program.model.symbol.Namespace, entryPoint: ghidra.program.model.address.Address, body: ghidra.program.model.address.AddressSetView, source: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.listing.Function: ...

    def createInstruction(self, addr: ghidra.program.model.address.Address, prototype: ghidra.program.model.lang.InstructionPrototype, memBuf: ghidra.program.model.mem.MemBuffer, context: ghidra.program.model.lang.ProcessorContextView) -> ghidra.program.model.listing.Instruction:
        """
        @see ghidra.program.model.listing.Listing#createInstruction(ghidra.program.model.address.Address, ghidra.program.model.lang.InstructionPrototype, ghidra.program.model.mem.MemBuffer, ghidra.program.model.lang.ProcessorContext)
        """
        ...

    def createRootModule(self, treeName: unicode) -> ghidra.program.model.listing.ProgramModule:
        """
        @see ghidra.program.model.listing.Listing#createRootModule(java.lang.String)
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getCodeUnitAfter(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.CodeUnit:
        """
        @see ghidra.program.model.listing.Listing#getCodeUnitAfter(ghidra.program.model.address.Address)
        """
        ...

    def getCodeUnitAt(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.CodeUnit:
        """
        @see ghidra.program.model.listing.Listing#getCodeUnitAt(ghidra.program.model.address.Address)
        """
        ...

    def getCodeUnitBefore(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.CodeUnit:
        """
        @see ghidra.program.model.listing.Listing#getCodeUnitBefore(ghidra.program.model.address.Address)
        """
        ...

    def getCodeUnitContaining(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.CodeUnit:
        """
        @see ghidra.program.model.listing.Listing#getCodeUnitContaining(ghidra.program.model.address.Address)
        """
        ...

    @overload
    def getCodeUnitIterator(self, property: unicode, forward: bool) -> ghidra.program.model.listing.CodeUnitIterator:
        """
        @see ghidra.program.model.listing.Listing#getCodeUnitIterator(java.lang.String)
        """
        ...

    @overload
    def getCodeUnitIterator(self, property: unicode, addr: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.listing.CodeUnitIterator:
        """
        @see ghidra.program.model.listing.Listing#getCodeUnitIterator(java.lang.String, ghidra.program.model.address.Address)
        """
        ...

    @overload
    def getCodeUnitIterator(self, property: unicode, addrSet: ghidra.program.model.address.AddressSetView, forward: bool) -> ghidra.program.model.listing.CodeUnitIterator:
        """
        @see ghidra.program.model.listing.Listing#getCodeUnitIterator(java.lang.String, ghidra.program.model.address.AddressSetView)
        """
        ...

    @overload
    def getCodeUnits(self, forward: bool) -> ghidra.program.model.listing.CodeUnitIterator:
        """
        @see ghidra.program.model.listing.Listing#getCodeUnits()
        """
        ...

    @overload
    def getCodeUnits(self, addr: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.listing.CodeUnitIterator:
        """
        @see ghidra.program.model.listing.Listing#getCodeUnits(ghidra.program.model.address.Address)
        """
        ...

    @overload
    def getCodeUnits(self, addrSet: ghidra.program.model.address.AddressSetView, forward: bool) -> ghidra.program.model.listing.CodeUnitIterator:
        """
        @see ghidra.program.model.listing.Listing#getCodeUnits(ghidra.program.model.address.AddressSetView)
        """
        ...

    def getComment(self, commentType: int, address: ghidra.program.model.address.Address) -> unicode:
        """
        @see ghidra.program.model.listing.Listing#getComment(int, ghidra.program.model.address.Address)
        """
        ...

    @overload
    def getCommentAddressIterator(self, addrSet: ghidra.program.model.address.AddressSetView, forward: bool) -> ghidra.program.model.address.AddressIterator:
        """
        @see ghidra.program.model.listing.Listing#getCommentAddressIterator(ghidra.program.model.address.AddressSetView, boolean)
        """
        ...

    @overload
    def getCommentAddressIterator(self, commentType: int, addrSet: ghidra.program.model.address.AddressSetView, forward: bool) -> ghidra.program.model.address.AddressIterator:
        """
        @see ghidra.program.model.listing.Listing#getCommentAddressIterator(int, ghidra.program.model.address.AddressSetView, boolean)
        """
        ...

    def getCommentCodeUnitIterator(self, commentType: int, addrSet: ghidra.program.model.address.AddressSetView) -> ghidra.program.model.listing.CodeUnitIterator:
        """
        @see ghidra.program.model.listing.Listing#getCommentCodeUnitIterator(int, ghidra.program.model.address.AddressSetView)
        """
        ...

    def getCommentHistory(self, addr: ghidra.program.model.address.Address, commentType: int) -> List[ghidra.program.model.listing.CommentHistory]:
        """
        @see ghidra.program.model.listing.Listing#getCommentHistory(ghidra.program.model.address.Address, int)
        """
        ...

    @overload
    def getCompositeData(self, forward: bool) -> ghidra.program.model.listing.DataIterator:
        """
        @see ghidra.program.model.listing.Listing#getCompositeData()
        """
        ...

    @overload
    def getCompositeData(self, start: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.listing.DataIterator:
        """
        @see ghidra.program.model.listing.Listing#getCompositeData(ghidra.program.model.address.Address)
        """
        ...

    @overload
    def getCompositeData(self, addrSet: ghidra.program.model.address.AddressSetView, forward: bool) -> ghidra.program.model.listing.DataIterator:
        """
        @see ghidra.program.model.listing.Listing#getCompositeData(ghidra.program.model.address.AddressSetView)
        """
        ...

    @overload
    def getData(self, forward: bool) -> ghidra.program.model.listing.DataIterator:
        """
        @see ghidra.program.model.listing.Listing#getData()
        """
        ...

    @overload
    def getData(self, addr: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.listing.DataIterator:
        """
        @see ghidra.program.model.listing.Listing#getData(ghidra.program.model.address.Address)
        """
        ...

    @overload
    def getData(self, addrSet: ghidra.program.model.address.AddressSetView, forward: bool) -> ghidra.program.model.listing.DataIterator:
        """
        @see ghidra.program.model.listing.Listing#getData(ghidra.program.model.address.AddressSetView)
        """
        ...

    def getDataAfter(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        @see ghidra.program.model.listing.Listing#getDataAfter(ghidra.program.model.address.Address)
        """
        ...

    def getDataAt(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        @see ghidra.program.model.listing.Listing#getDataAt(ghidra.program.model.address.Address)
        """
        ...

    def getDataBefore(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        @see ghidra.program.model.listing.Listing#getDataBefore(ghidra.program.model.address.Address)
        """
        ...

    def getDataContaining(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        @see ghidra.program.model.listing.Listing#getDataContaining(ghidra.program.model.address.Address)
        """
        ...

    def getDataTypeManager(self) -> ghidra.program.model.data.DataTypeManager:
        """
        @see ghidra.program.model.listing.Listing#getDataTypeManager()
        """
        ...

    def getDefaultRootModule(self) -> ghidra.program.model.listing.ProgramModule:
        """
        @see ghidra.program.model.listing.Listing#getRootModule(long)
        """
        ...

    def getDefinedCodeUnitAfter(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.CodeUnit:
        """
        @see ghidra.program.model.listing.Listing#getDefinedCodeUnitAfter(ghidra.program.model.address.Address)
        """
        ...

    def getDefinedCodeUnitBefore(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.CodeUnit:
        """
        @see ghidra.program.model.listing.Listing#getDefinedCodeUnitBefore(ghidra.program.model.address.Address)
        """
        ...

    @overload
    def getDefinedData(self, forward: bool) -> ghidra.program.model.listing.DataIterator:
        """
        @see ghidra.program.model.listing.Listing#getDefinedData()
        """
        ...

    @overload
    def getDefinedData(self, addr: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.listing.DataIterator:
        """
        @see ghidra.program.model.listing.Listing#getDefinedData(ghidra.program.model.address.Address)
        """
        ...

    @overload
    def getDefinedData(self, addrSet: ghidra.program.model.address.AddressSetView, forward: bool) -> ghidra.program.model.listing.DataIterator:
        """
        @see ghidra.program.model.listing.Listing#getDefinedData(ghidra.program.model.address.AddressSetView)
        """
        ...

    def getDefinedDataAfter(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        @see ghidra.program.model.listing.Listing#getDefinedDataAfter(ghidra.program.model.address.Address)
        """
        ...

    def getDefinedDataAt(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        @see ghidra.program.model.listing.Listing#getDefinedDataAt(ghidra.program.model.address.Address)
        """
        ...

    def getDefinedDataBefore(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        @see ghidra.program.model.listing.Listing#getDefinedDataBefore(ghidra.program.model.address.Address)
        """
        ...

    def getDefinedDataContaining(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        @see ghidra.program.model.listing.Listing#getDefinedDataContaining(ghidra.program.model.address.Address)
        """
        ...

    def getExternalFunctions(self) -> ghidra.program.model.listing.FunctionIterator: ...

    def getFirstUndefinedData(self, set: ghidra.program.model.address.AddressSetView, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.listing.Data:
        """
        @see ghidra.program.model.listing.Listing#getFirstUndefinedData(ghidra.program.model.address.AddressSetView)
        """
        ...

    @overload
    def getFragment(self, treeName: unicode, name: unicode) -> ghidra.program.model.listing.ProgramFragment:
        """
        @see ghidra.program.model.listing.Listing#getFragment(java.lang.String, java.lang.String)
        """
        ...

    @overload
    def getFragment(self, treeName: unicode, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.ProgramFragment:
        """
        @see ghidra.program.model.listing.Listing#getFragment(java.lang.String, ghidra.program.model.address.Address)
        """
        ...

    def getFunctionAt(self, entryPoint: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Function:
        """
        @see ghidra.program.model.listing.Listing#getFunctionAt(ghidra.program.model.address.Address)
        """
        ...

    def getFunctionContaining(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Function:
        """
        @see ghidra.program.model.listing.Listing#getFirstFunctionContaining(ghidra.program.model.address.Address)
        """
        ...

    @overload
    def getFunctions(self, forward: bool) -> ghidra.program.model.listing.FunctionIterator:
        """
        @see ghidra.program.model.listing.Listing#getFunctions(boolean)
        """
        ...

    @overload
    def getFunctions(self, start: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.listing.FunctionIterator:
        """
        @see ghidra.program.model.listing.Listing#getFunctions(ghidra.program.model.address.Address, boolean)
        """
        ...

    @overload
    def getFunctions(self, asv: ghidra.program.model.address.AddressSetView, forward: bool) -> ghidra.program.model.listing.FunctionIterator:
        """
        @see ghidra.program.model.listing.Listing#getFunctions(ghidra.program.model.address.AddressSetView, boolean)
        """
        ...

    @overload
    def getFunctions(self, namespacePath: unicode, name: unicode) -> List[ghidra.program.model.listing.Function]: ...

    def getGlobalFunctions(self, name: unicode) -> List[ghidra.program.model.listing.Function]: ...

    def getInstructionAfter(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Instruction:
        """
        @see ghidra.program.model.listing.Listing#getInstructionAfter(ghidra.program.model.address.Address)
        """
        ...

    def getInstructionAt(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Instruction:
        """
        @see ghidra.program.model.listing.Listing#getInstructionAt(ghidra.program.model.address.Address)
        """
        ...

    def getInstructionBefore(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Instruction:
        """
        @see ghidra.program.model.listing.Listing#getInstructionBefore(ghidra.program.model.address.Address)
        """
        ...

    def getInstructionContaining(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Instruction:
        """
        @see ghidra.program.model.listing.Listing#getInstructionContaining(ghidra.program.model.address.Address)
        """
        ...

    @overload
    def getInstructions(self, forward: bool) -> ghidra.program.model.listing.InstructionIterator:
        """
        @see ghidra.program.model.listing.Listing#getInstructions()
        """
        ...

    @overload
    def getInstructions(self, addr: ghidra.program.model.address.Address, forward: bool) -> ghidra.program.model.listing.InstructionIterator:
        """
        @see ghidra.program.model.listing.Listing#getInstructions(ghidra.program.model.address.Address)
        """
        ...

    @overload
    def getInstructions(self, addrSet: ghidra.program.model.address.AddressSetView, forward: bool) -> ghidra.program.model.listing.InstructionIterator:
        """
        @see ghidra.program.model.listing.Listing#getInstructions(ghidra.program.model.address.AddressSetView)
        """
        ...

    def getModule(self, treeName: unicode, name: unicode) -> ghidra.program.model.listing.ProgramModule:
        """
        @see ghidra.program.model.listing.Listing#getModule(java.lang.String, java.lang.String)
        """
        ...

    def getNumCodeUnits(self) -> long:
        """
        @see ghidra.program.model.listing.Listing#getNumCodeUnits()
        """
        ...

    def getNumDefinedData(self) -> long:
        """
        @see ghidra.program.model.listing.Listing#getNumDefinedData()
        """
        ...

    def getNumInstructions(self) -> long:
        """
        @see ghidra.program.model.listing.Listing#getNumInstructions()
        """
        ...

    def getPropertyMap(self, propertyName: unicode) -> ghidra.program.model.util.PropertyMap:
        """
        @see ghidra.program.model.listing.Listing#getPropertyMap(java.lang.String)
        """
        ...

    @overload
    def getRootModule(self, treeID: long) -> ghidra.program.model.listing.ProgramModule:
        """
        @see ghidra.program.model.listing.Listing#getRootModule(long)
        """
        ...

    @overload
    def getRootModule(self, treeName: unicode) -> ghidra.program.model.listing.ProgramModule:
        """
        @see ghidra.program.model.listing.Listing#getRootModule(java.lang.String)
        """
        ...

    def getTreeNames(self) -> List[unicode]:
        """
        @see ghidra.program.model.listing.Listing#getTreeNames()
        """
        ...

    def getUndefinedDataAfter(self, addr: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.listing.Data:
        """
        @see ghidra.program.model.listing.Listing#getUndefinedDataAfter(ghidra.program.model.address.Address)
        """
        ...

    def getUndefinedDataAt(self, addr: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        @see ghidra.program.model.listing.Listing#getUndefinedDataAt(ghidra.program.model.address.Address)
        """
        ...

    def getUndefinedDataBefore(self, addr: ghidra.program.model.address.Address, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.listing.Data:
        """
        @see ghidra.program.model.listing.Listing#getUndefinedDataBefore(ghidra.program.model.address.Address)
        """
        ...

    def getUndefinedRanges(self, set: ghidra.program.model.address.AddressSetView, initializedMemoryOnly: bool, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.address.AddressSetView: ...

    def getUserDefinedProperties(self) -> Iterator[unicode]:
        """
        @see ghidra.program.model.listing.Listing#getUserDefinedProperties()
        """
        ...

    def hashCode(self) -> int: ...

    def isInFunction(self, addr: ghidra.program.model.address.Address) -> bool:
        """
        @see ghidra.program.model.listing.Listing#isInFunction(ghidra.program.model.address.Address)
        """
        ...

    def isUndefined(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> bool:
        """
        @see ghidra.program.model.listing.Listing#isUndefined(ghidra.program.model.address.Address, ghidra.program.model.address.Address)
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeFunction(self, entryPoint: ghidra.program.model.address.Address) -> None:
        """
        @see ghidra.program.model.listing.Listing#removeFunction(ghidra.program.model.address.Address)
        """
        ...

    def removeTree(self, treeName: unicode) -> bool:
        """
        @see ghidra.program.model.listing.Listing#removeTree(java.lang.String)
        """
        ...

    def removeUserDefinedProperty(self, propertyName: unicode) -> None:
        """
        @see ghidra.program.model.listing.Listing#removeUserDefinedProperty(java.lang.String)
        """
        ...

    def renameTree(self, oldName: unicode, newName: unicode) -> None:
        """
        @see ghidra.program.model.listing.Listing#renameTree(java.lang.String, java.lang.String)
        """
        ...

    def setComment(self, address: ghidra.program.model.address.Address, commentType: int, comment: unicode) -> None:
        """
        @see ghidra.program.model.listing.Listing#setComment(ghidra.program.model.address.Address, int, java.lang.String)
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
