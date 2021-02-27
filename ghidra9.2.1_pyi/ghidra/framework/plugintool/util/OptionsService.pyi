from typing import List
import ghidra.framework.options
import java.lang


class OptionsService(object):
    """
    Provides a service interface that allows the user to get Options and to check for the
     existence of options.
    """









    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @overload
    def getOptions(self) -> List[ghidra.framework.options.Options]:
        """
        Get the list of options for all categories.
        @return the list of options for all categories.
        """
        ...

    @overload
    def getOptions(self, category: unicode) -> ghidra.framework.options.ToolOptions:
        """
        Get the options for the given category name.
        @param category name of category
        @return the options for the given category name.
        """
        ...

    def hasOptions(self, category: unicode) -> bool:
        """
        Return whether an Options object exists for the given category.
        @param category name of the category
        @return true if an Options object exists
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def showOptionsDialog(self, category: unicode, filterText: unicode) -> None:
        """
        Shows Options Dialog with the node denoted by "category" being displayed.  The value is
         expected to be the name of a node in the options tree, residing under the root node.  You
         may also provide the name of such a node, followed by the options delimiter, followed by
         the name of a child node under that node.  For example, suppose in the options tree exists
         a node {@literal Root->Foo}  You may pass the value "Foo" to get that node.  Or, suppose
         in the options tree exists a node {@literal Root->Foo->childNode1}  In this case, you may
         pass the value "Foo.childNode1", where the '.' character is the delimiter of the
         {@link ToolOptions} class (this is the value at the time of writing this documentation).

         <p>
         The filter text parameter is used to set the contents filter text of the options.  You may
         use this parameter to filter the tree; for example, to show only the node in the tree that
         you want the user to see.
        @param category The category of options to have displayed
        @param filterText An optional value used to filter the nodes visible in the options tree.
                           You may pass <code>null</code> or the empty string <code>""</code> here if you
                           do not desire filtering.
        @throws IllegalArgumentException if the given <code>category</code> value does not exist in
                                          the tree of options.
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
    def options(self) -> List[ghidra.framework.options.Options]: ...
