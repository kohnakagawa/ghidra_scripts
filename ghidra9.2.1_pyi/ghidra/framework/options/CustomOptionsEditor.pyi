from typing import List
import java.lang


class CustomOptionsEditor(object):
    """
    Marker interface to signal that the implementing PropertyEditor component desires to handle
     display editing of an option or options.  This allows options to create custom property
     editors that can paint and edit a group of interrelated options.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getOptionDescriptions(self) -> List[unicode]:
        """
        Gets the descriptions of the options that this editor is editing.
        @return the descriptions of the options that this editor is editing.
        """
        ...

    def getOptionNames(self) -> List[unicode]:
        """
        Gets the names of the options that this editor is editing.
        @return the names of the options that this editor is editing.
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
    def optionDescriptions(self) -> List[unicode]: ...

    @property
    def optionNames(self) -> List[unicode]: ...
