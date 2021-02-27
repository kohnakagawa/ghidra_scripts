from typing import List
import docking.widgets.fieldpanel.field
import ghidra.app.nav
import ghidra.app.util.viewer.field
import ghidra.framework.plugintool
import java.lang


class Annotation(object):




    def __init__(self, annotationText: unicode, prototypeString: docking.widgets.fieldpanel.field.AttributedString, program: ghidra.program.model.listing.Program):
        """
        Constructor
         <b>Note</b>: This constructor assumes that the string starts with "{<pre>@</pre>" and ends with '}'
        @param annotationText The complete annotation text.
        @param prototypeString An AttributedString that provides the attributes for the display
         text this Annotation can create
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def getAnnotatedStringHandlers() -> List[ghidra.app.util.viewer.field.AnnotatedStringHandler]: ...

    def getAnnotationText(self) -> unicode: ...

    def getClass(self) -> java.lang.Class: ...

    def getDisplayString(self) -> docking.widgets.fieldpanel.field.AttributedString: ...

    def handleMouseClick(self, sourceNavigatable: ghidra.app.nav.Navigatable, serviceProvider: ghidra.framework.plugintool.ServiceProvider) -> bool:
        """
        Called when a mouse click occurs on a FieldElement containing this Annotation.
        @param sourceNavigatable The source navigatable associated with the mouse click.
        @param serviceProvider The service provider to be used when creating
         {@link AnnotatedStringHandler} instances.
        @return true if the handler desires to handle the mouse click.
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
    def annotationText(self) -> unicode: ...

    @property
    def displayString(self) -> docking.widgets.fieldpanel.field.AttributedString: ...
