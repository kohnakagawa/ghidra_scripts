from typing import List
import docking.widgets.fieldpanel.field
import ghidra.app.nav
import ghidra.framework.plugintool
import ghidra.program.model.listing
import ghidra.util.classfinder
import java.lang


class AnnotatedStringHandler(ghidra.util.classfinder.ExtensionPoint, object):
    """
    NOTE:  ALL AnnotatedStringHandler CLASSES MUST END IN "StringHandler".  If not,
     the ClassSearcher will not find them.

     An interface that describes a string that has been annotated, which allows for adding
     rendering and functionality to strings.
    """

    DUMMY_MOUSE_HANDLER: ghidra.app.util.viewer.field.AnnotatedMouseHandler = ghidra.app.util.viewer.field.AnnotatedStringHandler$1@202d0e44







    def createAnnotatedString(self, prototypeString: docking.widgets.fieldpanel.field.AttributedString, text: List[unicode], program: ghidra.program.model.listing.Program) -> docking.widgets.fieldpanel.field.AttributedString:
        """
        Creates an {@link FieldElement} based upon the give array of Strings.  The first String
         in the list is expected to be the annotation tag used to create the annotation.  At the
         very least the array is expected to be comprised of two elements, the annotation and some
         data.  Extra data may be provided as needed by implementing classes.
        @param prototypeString The prototype {@link FieldElement} that dictates the
                 attributes for the newly created string.  Implementations may change attributes
                 as needed.
        @param text An array of Strings used to create the {@link FieldElement} being
                 returned.
        @param program The program with which the returned string is associated.
        @return An {@link AnnotatedTextFieldElement} that will be used to render the given text.
        @throws AnnotationException if the given text data does not fit the expected format for
                 the given handler implementation.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDisplayString(self) -> unicode:
        """
        Returns the String that represents the GUI presence of this option
        @return the String to display in GUI components.
        """
        ...

    def getPrototypeString(self) -> unicode:
        """
        Returns an example string of how the annotation is used
        @return the example of how this is used.
        """
        ...

    def getSupportedAnnotations(self) -> List[unicode]:
        """
        Returns the annotation string names that this AnnotatedStringHandler supports (e.g., "symbol",
         "address", etc...).
        @return the annotation string names that this AnnotatedStringHandler supports.
        """
        ...

    def handleMouseClick(self, annotationParts: List[unicode], sourceNavigatable: ghidra.app.nav.Navigatable, serviceProvider: ghidra.framework.plugintool.ServiceProvider) -> bool:
        """
        A method that is notified when an annotation is clicked.  Returns true if this annotation
         handles the click; return false if this annotation does not do anything with the click.
        @param annotationParts The constituent parts of the annotation
        @param sourceNavigatable The location in the program that was clicked.
        @param serviceProvider A service provider for needed services.
        @return true if this annotation handles the click; return false if this annotation does
                 not do anything with the click.
        """
        ...

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

    @property
    def displayString(self) -> unicode: ...

    @property
    def prototypeString(self) -> unicode: ...

    @property
    def supportedAnnotations(self) -> List[unicode]: ...
