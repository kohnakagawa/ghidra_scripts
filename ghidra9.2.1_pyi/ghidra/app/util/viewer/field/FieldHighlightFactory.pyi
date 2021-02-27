from typing import List
import docking.widgets.fieldpanel.field
import docking.widgets.fieldpanel.support
import java.lang


class FieldHighlightFactory(object, docking.widgets.fieldpanel.support.HighlightFactory):
    """
    Wrapper class to hold field factory information in the text field to be provided to the
     highlightProvider to get highlights just before the field is painted.
    """





    def __init__(self, provider: ghidra.app.util.HighlightProvider, fieldFactoryClass: java.lang.Class, obj: object):
        """
        Constructs a new FieldHighlightFactory.
        @param provider the HighlightProvider that will actually compute the highlights.
        @param fieldFactoryClass the class of the field factory that generated the field to be rendered.
        @param obj the object that holds the information that will be rendered (usually a code unit)
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getHighlights(self, field: docking.widgets.fieldpanel.field.Field, text: unicode, cursorTextOffset: int) -> List[docking.widgets.fieldpanel.support.Highlight]: ...

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
