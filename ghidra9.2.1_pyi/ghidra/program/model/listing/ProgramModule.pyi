from typing import List
import ghidra.program.model.address
import ghidra.program.model.listing
import java.lang


class ProgramModule(ghidra.program.model.listing.Group, object):
    """
    A ProgramModule is a group of ProgramFragments
     and/or other ProgramModules together with some related
     information such as a name, comment, and alias. Users create modules to
     overlay the program with a hierarchical structure. A child of a module
     is a fragment or module which it directly contains. A parent of a module
     is a module which has this module as a child. A module may be contained in more
     than one module. A Program always has at least one module, the root module.
     The root module cannot be removed and is the ancestor for all other modules and
     fragments in the program.
    """









    @overload
    def add(self, fragment: ghidra.program.model.listing.ProgramFragment) -> None:
        """
        Adds the given fragment as a child of this module.
         <P>
        @exception DuplicateGroupException thrown if the fragment being
         added is already a child of this module.
        """
        ...

    @overload
    def add(self, module: ghidra.program.model.listing.ProgramModule) -> None:
        """
        Adds the given module as a child of this module.
         <P>
        @param module the module to be added.
        @throws CircularDependencyException thrown if the module being
         added is an ancestor of this module. The module structure of
         a program does not allow "cycles" of this sort to be created.
        @exception DuplicateGroupException thrown if the module being
         added is already a child of this module.
        """
        ...

    @overload
    def contains(self, __a0: ghidra.program.model.listing.CodeUnit) -> bool: ...

    @overload
    def contains(self, fragment: ghidra.program.model.listing.ProgramFragment) -> bool:
        """
        Returns whether this module directly contains the
         given fragment as a child.
        @param fragment the fragment to check.
        """
        ...

    @overload
    def contains(self, module: ghidra.program.model.listing.ProgramModule) -> bool:
        """
        Returns whether this module directly contains the
         given module as a child.
        @param module the module to check.
        @return true if module is the same as this module, or if module
         is a child of this module.
        """
        ...

    def createFragment(self, fragmentName: unicode) -> ghidra.program.model.listing.ProgramFragment:
        """
        Creates a new fragment and makes it a child of this module.<P>
        @param fragmentName the name to use for the new fragment.
        @return the newly created fragment.
        @exception DuplicateNameException thrown if the given
         name is already used by an existing module or fragment.
        """
        ...

    def createModule(self, moduleName: unicode) -> ghidra.program.model.listing.ProgramModule:
        """
        Creates a new module and makes it a child of this
         module.<P>
        @param moduleName the name to use for the new module.
        @return the newly created module.
        @exception DuplicateNameException thrown if the given
         name is already used by an existing module or fragment.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getAddressSet(self) -> ghidra.program.model.address.AddressSetView:
        """
        Returns the set of addresses for this module which will be the combined
         set of addresses from the set of all fragments which are descendants of this
         module.
        @return the complete address set for this module.
        """
        ...

    def getChildren(self) -> List[ghidra.program.model.listing.Group]:
        """
        Returns an array containing this module's children.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getComment(self) -> unicode: ...

    def getFirstAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the first address of this module which will be the minimum
         address of the first descendant fragment which is non-empty. In other
         words this returns the first address for this module as defined by
         the user ordering of the module's children.
         <P>
        @return the first address, this will be null if all of the module's
         descendant fragments are empty.
        """
        ...

    def getIndex(self, name: unicode) -> int:
        """
        Get the index of the child with the given name.
        @param name name of child
        @return int index or -1 if this Module does not have a child
         with the given name
        """
        ...

    def getLastAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the last address of this module which will be the maximum address
         of the last descendant fragment which is non-empty. In other words this
         returns the last address for this module as defined by the user
         ordering of the module's children.
         <P>
        @return the last address, this will be null if all of the module's
         descendant fragments are empty.
        """
        ...

    def getMaxAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the maximum address of this module which will be the maximum
         address from the set of all fragments which are descendants of this
         module.
         <P>
        @return the maximum address, this will be null if all of the module's
         descendant fragments are empty.
        """
        ...

    def getMinAddress(self) -> ghidra.program.model.address.Address:
        """
        Returns the minimum address of this module which will be the minimum
         address from the set of all fragments which are descendants of this
         module.
         <P>
        @return the minimum address, this will be null if all of the module's
         descendant fragments are empty.
        """
        ...

    def getModificationNumber(self) -> long:
        """
        Get the current modification number of the module tree; the number
         is updated when ever a change is made to any module or fragment
         that is part of this module's root tree.
        """
        ...

    def getName(self) -> unicode: ...

    def getNumChildren(self) -> int:
        """
        Returns the number of children of this module.
        """
        ...

    def getNumParents(self) -> int: ...

    def getParentNames(self) -> List[unicode]: ...

    def getParents(self) -> List[ghidra.program.model.listing.ProgramModule]: ...

    def getTreeID(self) -> long:
        """
        Get the ID for the tree that this module belongs to.
        @return ID for the tree
        """
        ...

    def getTreeName(self) -> unicode: ...

    def getVersionTag(self) -> object:
        """
        Returns an object that can be used to detect when the module tree has been affected
         by an undo or redo. After an undo/redo, if this module was affected, then a new
         verionTag object is created.
        """
        ...

    def hashCode(self) -> int: ...

    @overload
    def isDescendant(self, fragment: ghidra.program.model.listing.ProgramFragment) -> bool:
        """
        Returns whether the given fragment is a descendant of this
         module.<P>
        @param fragment the fragment to check.
        @return true if the fragment is a descendant, false otherwise.
        """
        ...

    @overload
    def isDescendant(self, module: ghidra.program.model.listing.ProgramModule) -> bool:
        """
        Returns whether the given module is a descendant of this
         module.<P>
        @param module the module to check.
        @return true if the module is a descendant, false otherwise.
        """
        ...

    def moveChild(self, name: unicode, index: int) -> None:
        """
        Changes the ordering of this module's children by moving
         the child with the given name to position given by index.<P>
        @param name the name of the child to move.
        @param index the index to move it to.
        @exception NotFoundException thrown if a child with the given
         name cannot be found in this module.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def removeChild(self, name: unicode) -> bool:
        """
        Removes a child module or fragment from this Module.
        @return true if successful, false if no child in this module has the given name.
        @exception NotEmptyException thrown if the module appears in no other
         modules and it is not empty.
        """
        ...

    def reparent(self, name: unicode, oldParent: ghidra.program.model.listing.ProgramModule) -> None:
        """
        Reparents child with the given name to this Module; removes the
         child from oldParent.
        @param name name of child to reparent
        @param oldParent old parent
        @exception NotFoundException if name is not the name of a child
         in oldParent
        """
        ...

    def setComment(self, __a0: unicode) -> None: ...

    def setName(self, __a0: unicode) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def addressSet(self) -> ghidra.program.model.address.AddressSetView: ...

    @property
    def children(self) -> List[ghidra.program.model.listing.Group]: ...

    @property
    def comment(self) -> unicode: ...

    @comment.setter
    def comment(self, value: unicode) -> None: ...

    @property
    def firstAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def lastAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def maxAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def minAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def modificationNumber(self) -> long: ...

    @property
    def name(self) -> unicode: ...

    @name.setter
    def name(self, value: unicode) -> None: ...

    @property
    def numChildren(self) -> int: ...

    @property
    def numParents(self) -> int: ...

    @property
    def parentNames(self) -> List[unicode]: ...

    @property
    def parents(self) -> List[ghidra.program.model.listing.ProgramModule]: ...

    @property
    def treeID(self) -> long: ...

    @property
    def treeName(self) -> unicode: ...

    @property
    def versionTag(self) -> object: ...
