from typing import List
import docking.widgets.fieldpanel.support
import java.lang


class HighlightProvider(object):
    """
    Provider of Highlight objects appropriate for the text, object, and FieldFactory class.
    """

    EMPTY_HIGHLIGHT: List[docking.widgets.fieldpanel.support.Highlight] = array(docking.widgets.fieldpanel.support.Highlight)







    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getHighlights(self, text: unicode, obj: object, fieldFactoryClass: java.lang.Class, cursorTextOffset: int) -> List[docking.widgets.fieldpanel.support.Highlight]:
        """
        Get the highlights appropriate for the given text, object, and FieldFactory class.
        @param text the entire text contained in the field, regardless of layout.
        @param obj object that provides the information to be rendered (usually a code unit)
        @param fieldFactoryClass the class that indicates what type of field is being rendered.
         For Example, address fields would have the AddressFieldFactory class.
        @param cursorTextOffset the cursor position within the given text or -1 if no cursor in this field.
        @return an array of highlight objects that indicate the location within the text string to
         be highlighted.
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
