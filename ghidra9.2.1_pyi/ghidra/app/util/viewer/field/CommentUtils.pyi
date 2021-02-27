import docking.widgets.fieldpanel.field
import ghidra.program.model.listing
import java.lang


class CommentUtils(object):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def fixupAnnoations(rawCommentText: unicode, program: ghidra.program.model.listing.Program) -> unicode:
        """
        Makes adjustments as necessary to any annotations in the given text.
        @param rawCommentText the text to be updated
        @param program the program associated with the comment
        @return the updated string
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getDisplayString(rawCommentText: unicode, program: ghidra.program.model.listing.Program) -> unicode:
        """
        Returns the display string for the given raw annotation text.  Annotations are
         encoded strings that fit this pattern: <code>{@literal {@name text}}</code>.  This method
         will parse the given text, converting any annotations into their display version.
        @param rawCommentText text that may include annotations
        @param program the program
        @return the display string
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def parseTextForAnnotations(text: unicode, program: ghidra.program.model.listing.Program, prototypeString: docking.widgets.fieldpanel.field.AttributedString, row: int) -> docking.widgets.fieldpanel.field.FieldElement:
        """
        Parses the given text looking for annotations.
        @param text The text to parse.
        @param program the program from which to get information
        @param prototypeString The reference string used to determine the attributes of any
                 newly created AttributedString.
        @param row the row of the newly created FieldElement
        @return A field element containing {@link AttributedString}s
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
