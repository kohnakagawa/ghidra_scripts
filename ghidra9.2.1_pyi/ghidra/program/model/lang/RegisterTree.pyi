from typing import List
import ghidra.program.model.lang
import java.lang


class RegisterTree(object, java.lang.Comparable):
    """
    The RegisterTree class builds and represents relationships between registers. Any
     register that "breaks down" into smaller registers can be represent by a
     RegisterTree.  The largest register will be at the root and the registers that
     make it up will be its children trees.  The children are RegisterTrees as well
     and can have children trees of thier own.  The root of a RegisterTree may not
     have an associated Register which means that its children are unrelated.  This
     way all the registers of a processor can be represented as a single RegisterTree.
    """





    @overload
    def __init__(self, reg: ghidra.program.model.lang.Register): ...

    @overload
    def __init__(self, name: unicode, regs: List[ghidra.program.model.lang.Register]):
        """
        Constructs a RegisterTree with the given name and set of registers
        @param name the name of the tree
        @param regs the array of registers to form into a tree
        """
        ...

    @overload
    def __init__(self, name: unicode, tree: ghidra.program.model.lang.RegisterTree):
        """
        Constructs a RegisterTree with one RegisterTree child
        @param name the name of this tree
        @param tree the child tree.
        """
        ...



    def add(self, tree: ghidra.program.model.lang.RegisterTree) -> None:
        """
        Adds a Register Tree to this tree.
        @param tree the register tree to add
        """
        ...

    @overload
    def compareTo(self, other: ghidra.program.model.lang.RegisterTree) -> int:
        """
        @see java.lang.Comparable#compareTo(java.lang.Object)
        """
        ...

    @overload
    def compareTo(self, __a0: object) -> int: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getComponents(self) -> List[ghidra.program.model.lang.RegisterTree]:
        """
        Get the RegisterTrees that are the children of this RegisterTree
        @return a array of RegisterTrees
        """
        ...

    def getName(self) -> unicode:
        """
        Returns the name of this register tree.
        """
        ...

    def getParent(self) -> ghidra.program.model.lang.RegisterTree:
        """
        Returns the parent RegisterTree.
        """
        ...

    def getParentRegisterPath(self) -> unicode:
        """
        The parent path of this RegisterTree if it exists or null if this tree has no parent or
         no parent with a register.
        @return The parent path of this RegisterTree.
        """
        ...

    def getRegister(self) -> ghidra.program.model.lang.Register:
        """
        Returns the Register associated with this tree. This may be null which
         indicates the children RegisterTrees are unrelated to each other.
        """
        ...

    def getRegisterPath(self) -> unicode:
        """
        The path of this register, which includes the parent path of this RegisterTree if this
         RegisterTree has a parent.
        @return the path of this register.
        """
        ...

    def getRegisterTree(self, register1: ghidra.program.model.lang.Register) -> ghidra.program.model.lang.RegisterTree:
        """
        Returns the RegisterTree for the given register if one exists in this RegisterTree object.
        @param register1 The register for which to get a RegisterTree.
        @return The RegisterTree for the given register if one exists in this RegisterTree object.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def remove(self, reg: ghidra.program.model.lang.Register) -> None:
        """
        Removes the register from the children
        @param reg the register to remove.
        """
        ...

    def toString(self) -> unicode:
        """
        @see java.lang.Object#toString()
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def components(self) -> List[ghidra.program.model.lang.RegisterTree]: ...

    @property
    def name(self) -> unicode: ...

    @property
    def parent(self) -> ghidra.program.model.lang.RegisterTree: ...

    @property
    def parentRegisterPath(self) -> unicode: ...

    @property
    def register(self) -> ghidra.program.model.lang.Register: ...

    @property
    def registerPath(self) -> unicode: ...
