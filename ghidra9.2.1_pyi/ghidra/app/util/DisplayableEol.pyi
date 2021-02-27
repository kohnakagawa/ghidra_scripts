from typing import List
import docking.widgets.fieldpanel.support
import ghidra.app.util
import ghidra.program.model.address
import ghidra.program.util
import java.lang


class DisplayableEol(object):
    """
    Utility class with methods to get comment information that can be displayed in the
     end of line comment field. A DisplayableEol is associated with a code unit.
     The DisplayableEol gets information for the EOL comment field, which can show the
     End of Line comment for the code unit, the Repeatable comment for the code unit,
     any repeatable comments for the code units that this code unit has references to, and
     possibly a comment indicating the data at a code unit that is referenced by this code unit.
    """

    MY_AUTOMATIC: int = 3
    MY_EOLS: int = 0
    MY_REPEATABLES: int = 1
    REF_REPEATABLES: int = 2



    def __init__(self, cu: ghidra.program.model.listing.CodeUnit, alwaysShowRepeatable: bool, alwaysShowRefRepeats: bool, alwaysShowAutomatic: bool, operandsFollowPointerRefs: bool, maxDisplayLines: int, useAbbreviatedAutomatic: bool):
        """
        Construct a new DisplayableEol.
        @param cu code unit that may have end of line or repeatable comments.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getAutomaticComment(self) -> List[unicode]:
        """
        Gets the automatic comment as an array.
        @return the automatic comment
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getCommentLineCount(self, subType: int) -> int: ...

    def getComments(self) -> List[unicode]:
        """
        Return all the comments (End of Line, Repeatable, Referenced Repeatables, and Referenced Data).
        """
        ...

    def getEOLComments(self) -> List[unicode]:
        """
        Gets the end of line comment as an array.
        @return the EOL comment
        """
        ...

    def getLocation(self, eolRow: int, eolColumn: int) -> ghidra.program.util.ProgramLocation: ...

    def getRefRepeatableCommentLineCount(self, refAddress: ghidra.program.model.address.Address) -> int: ...

    @overload
    def getReferencedRepeatableComments(self) -> List[unicode]: ...

    @overload
    def getReferencedRepeatableComments(self, index: int) -> ghidra.app.util.RefRepeatComment:
        """
        Gets a referenced repeatable comment as a RefRepeatComment object.
        @param index indicator of which referenced repeatable comment is desired.
         The value is 0 thru one less than the number of referenced repeatable comments.
        @return the RefRepeatComment containing the referenced address and its referenced repeatable comment
        """
        ...

    @overload
    def getReferencedRepeatableComments(self, refAddress: ghidra.program.model.address.Address) -> List[unicode]:
        """
        Gets a referenced repeatable comment as a RefRepeatComment object.
        @param refAddress the reference address whose repeatable comment is desired.
         Note: there must be a reference from the address for this displayableEol to the refAddress.
        @return the comment lines for the referenced address's repeatable comment or null.
        """
        ...

    def getReferencedRepeatableCommentsCount(self) -> int:
        """
        Gets the number of repeatable comments at the "to reference"s
        @return the number of reference repeatable comments
        """
        ...

    def getRepeatableComments(self) -> List[unicode]:
        """
        Gets the repeatable comment as an array.
        @return the repeatable comment.
        """
        ...

    def getRowCol(self, cloc: ghidra.program.util.CommentFieldLocation) -> docking.widgets.fieldpanel.support.RowColLocation: ...

    def hasAutomatic(self) -> bool:
        """
        Return whether this code unit has an automatic comment.
         (i.e. any memory reference from this code unit has a
         function defined at the reference's to address, or if the to
         address is a pointer.)
        """
        ...

    def hasEOL(self) -> bool:
        """
        Return whether the associated code unit has an end of line comment.
        """
        ...

    def hasReferencedRepeatable(self) -> bool:
        """
        Return whether any memory reference from this code unit has a repeatable
         comment at the reference's to address.
        """
        ...

    def hasRepeatable(self) -> bool:
        """
        Return whether the associated code unit has a repeatable comment.
        """
        ...

    def hashCode(self) -> int: ...

    def isRefRepeatRow(self, eolRow: int) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def EOLComments(self) -> List[unicode]: ...

    @property
    def automaticComment(self) -> List[unicode]: ...

    @property
    def comments(self) -> List[unicode]: ...

    @property
    def referencedRepeatableComments(self) -> List[unicode]: ...

    @property
    def referencedRepeatableCommentsCount(self) -> int: ...

    @property
    def repeatableComments(self) -> List[unicode]: ...
