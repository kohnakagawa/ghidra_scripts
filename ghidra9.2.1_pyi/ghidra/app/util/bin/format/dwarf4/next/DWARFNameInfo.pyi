from typing import List
import ghidra.app.util.bin.format.dwarf4.next
import ghidra.program.model.data
import ghidra.program.model.listing
import ghidra.program.model.symbol
import java.lang


class DWARFNameInfo(object):
    """
    A immutable hierarchical path based name implementation that can be viewed as either
     Namespace or CategoryPath.

    """









    def asCategoryPath(self) -> ghidra.program.model.data.CategoryPath:
        """
        Converts this object into an equiv {@link CategoryPath}.
        @return {@link CategoryPath}: "/organizational_cat_path/namespace1/namespace2/obj_name"
        """
        ...

    def asDataTypePath(self) -> ghidra.program.model.data.DataTypePath:
        """
        Converts this object into an equiv {@link DataTypePath}.
        @return {@link DataTypePath}: { "/organizational_cat_path/namespace1/namespace2", "obj_name" }
        """
        ...

    def asNamespace(self, program: ghidra.program.model.listing.Program) -> ghidra.program.model.symbol.Namespace:
        """
        Converts this object into an equiv Ghidra {@link Namespace}, omitting the organizational
         category path (which only applies to DataTypes).
        @param program {@link Program} where the namespace lives.
        @return {@link Namespace}: "ROOT::namespace1::namespace2::obj_name"
        """
        ...

    def createChild(self, childOriginalName: unicode, childName: unicode, childType: ghidra.program.model.symbol.SymbolType) -> ghidra.app.util.bin.format.dwarf4.next.DWARFNameInfo: ...

    @staticmethod
    def createRoot(rootCategory: ghidra.program.model.data.CategoryPath) -> ghidra.app.util.bin.format.dwarf4.next.DWARFNameInfo: ...

    def equals(self, obj: object) -> bool: ...

    @staticmethod
    def fromDataType(dataType: ghidra.program.model.data.DataType) -> ghidra.app.util.bin.format.dwarf4.next.DWARFNameInfo: ...

    @staticmethod
    def fromList(__a0: ghidra.app.util.bin.format.dwarf4.next.DWARFNameInfo, __a1: List[object]) -> ghidra.app.util.bin.format.dwarf4.next.DWARFNameInfo: ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode: ...

    def getNamespacePath(self) -> ghidra.app.util.bin.format.dwarf4.next.NamespacePath: ...

    def getOrganizationalCategoryPath(self) -> ghidra.program.model.data.CategoryPath: ...

    def getOriginalName(self) -> unicode: ...

    def getParent(self) -> ghidra.app.util.bin.format.dwarf4.next.DWARFNameInfo: ...

    def getParentCP(self) -> ghidra.program.model.data.CategoryPath: ...

    def getParentNamespace(self, program: ghidra.program.model.listing.Program) -> ghidra.program.model.symbol.Namespace: ...

    def getType(self) -> ghidra.program.model.symbol.SymbolType: ...

    def hashCode(self) -> int: ...

    def isAnon(self) -> bool: ...

    def isNameModified(self) -> bool:
        """
        Returns true if this instance's {@link #getName() name} value is different
         than its {@link #getOriginalName() original} form.
         <p>
        @return
        """
        ...

    def isRoot(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def replaceName(self, newName: unicode, newOriginalName: unicode) -> ghidra.app.util.bin.format.dwarf4.next.DWARFNameInfo: ...

    def replaceType(self, newType: ghidra.program.model.symbol.SymbolType) -> ghidra.app.util.bin.format.dwarf4.next.DWARFNameInfo: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def anon(self) -> bool: ...

    @property
    def name(self) -> unicode: ...

    @property
    def nameModified(self) -> bool: ...

    @property
    def namespacePath(self) -> ghidra.app.util.bin.format.dwarf4.next.NamespacePath: ...

    @property
    def organizationalCategoryPath(self) -> ghidra.program.model.data.CategoryPath: ...

    @property
    def originalName(self) -> unicode: ...

    @property
    def parent(self) -> ghidra.app.util.bin.format.dwarf4.next.DWARFNameInfo: ...

    @property
    def parentCP(self) -> ghidra.program.model.data.CategoryPath: ...

    @property
    def root(self) -> bool: ...

    @property
    def type(self) -> ghidra.program.model.symbol.SymbolType: ...
