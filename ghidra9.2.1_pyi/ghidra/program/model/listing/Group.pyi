from typing import List
import ghidra.program.model.listing
import java.lang


class Group(object):
    """
    The interface for groupings of code units that may have attributes such
     as names and comments.
    """









    def contains(self, codeUnit: ghidra.program.model.listing.CodeUnit) -> bool:
        """
        Returns whether this fragment contains the given code unit.<P>
        @param codeUnit the code unit being tested.
        @return true if the code unit is in the fragment, false otherwise.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getComment(self) -> unicode:
        """
        Obtains the comment that has been associated with this fragment or module.
        @return may be null.
        """
        ...

    def getName(self) -> unicode:
        """
        Obtains the name that has been associated with this fragment. A fragment will
         always have a name and it will be unique within the set of all fragment and
         module names.
        """
        ...

    def getNumParents(self) -> int:
        """
        Obtains the number of parent's of this fragment. If a fragment is in a module
         then the module is a <I>parent</I> of the fragment and the fragment is a
         <I>child</I> of the module. A fragment must have at least one parent and it
         may have multiple parents.
        @return the number of parents of this fragment.
        """
        ...

    def getParentNames(self) -> List[unicode]:
        """
        Returns the names of the modules which are parents to this
         fragment.
        """
        ...

    def getParents(self) -> List[ghidra.program.model.listing.ProgramModule]:
        """
        Returns a list of the modules which are parents for this group.
        """
        ...

    def getTreeName(self) -> unicode:
        """
        Returns the name of the tree that this group belongs to.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setComment(self, comment: unicode) -> None:
        """
        Sets the comment to associate with this fragment.
        @param comment the comment.
        """
        ...

    def setName(self, name: unicode) -> None:
        """
        Sets the name of this fragment.
        @param name the string to use for the fragment's name.
        @exception DuplicateNameException thrown if the name being set is already in use by another fragment or a
                           module.
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
    def comment(self) -> unicode: ...

    @comment.setter
    def comment(self, value: unicode) -> None: ...

    @property
    def name(self) -> unicode: ...

    @name.setter
    def name(self, value: unicode) -> None: ...

    @property
    def numParents(self) -> int: ...

    @property
    def parentNames(self) -> List[unicode]: ...

    @property
    def parents(self) -> List[ghidra.program.model.listing.ProgramModule]: ...

    @property
    def treeName(self) -> unicode: ...
