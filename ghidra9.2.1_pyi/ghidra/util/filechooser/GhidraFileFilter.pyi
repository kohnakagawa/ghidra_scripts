import ghidra.util.filechooser
import java.io
import java.lang


class GhidraFileFilter(object):
    """
    A interface that filters out all files
     except for those type extensions that it knows about.
     Extensions are of the type ".foo", which is typically found on
     Windows and Unix boxes, but not on Macinthosh. Case is ignored.
    """

    ALL: ghidra.util.filechooser.GhidraFileFilter = ghidra.util.filechooser.GhidraFileFilter$1@25becf17







    def accept(self, pathname: java.io.File, model: ghidra.util.filechooser.GhidraFileChooserModel) -> bool:
        """
        Tests whether or not the specified abstract pathname should be
         included in a pathname list.
        @param pathname The abstract pathname to be tested
        @param model The underlying file chooser model
        @return <code>true</code> if and only if <code>pathname</code>
                  should be included
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode:
        """
        Returns the description of this filter.
        @return the description of this filter
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
    def description(self) -> unicode: ...
