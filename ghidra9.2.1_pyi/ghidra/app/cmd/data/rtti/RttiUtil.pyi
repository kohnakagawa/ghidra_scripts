import ghidra.app.cmd.data
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.util.task
import java.lang


class RttiUtil(object):
    TYPE_INFO_LABEL: unicode = u'class_type_info_RTTI_Type_Descriptor'
    TYPE_INFO_STRING: unicode = u'.?AVtype_info@@'







    @staticmethod
    def createTypeInfoVftableSymbol(__a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.Address) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def findTypeInfoVftableAddress(__a0: ghidra.program.model.listing.Program, __a1: ghidra.util.task.TaskMonitor) -> ghidra.program.model.address.Address: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getDescriptorTypeNamespace(__a0: ghidra.app.cmd.data.TypeDescriptorModel) -> unicode: ...

    @staticmethod
    def getVfTableCount(__a0: ghidra.program.model.listing.Program, __a1: ghidra.program.model.address.Address) -> int: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
