from typing import List
import generic.jar
import java.lang
import javax.swing


class ScriptInfo(object):
    """
    This class parses the meta-data about a script.
    """

    DELIMITTER: unicode = u'.'
    METADATA: List[unicode] = array(java.lang.String, [u'@author', u'@category', u'@keybinding', u'@menupath', u'@toolbar'])







    def equals(self, __a0: object) -> bool: ...

    def getAuthor(self) -> unicode:
        """
        Returns the script author information.
        @return the script author information.
        """
        ...

    def getCategory(self) -> List[unicode]:
        """
        Returns the script category path.
        @return the script category path
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getDescription(self) -> unicode:
        """
        Returns the script description.
        @return the script description
        """
        ...

    def getErrorMessage(self) -> unicode:
        """
        @return a generic error message
        """
        ...

    def getImportPackage(self) -> unicode:
        """
        Returns the script imports
        @return the script imports
        """
        ...

    def getKeyBinding(self) -> javax.swing.KeyStroke:
        """
        Returns the script key binding.
        @return the script key binding
        """
        ...

    def getKeyBindingErrorMessage(self) -> unicode:
        """
        @return an error resulting from parsing keybinding metadata
        """
        ...

    def getMenuPath(self) -> List[unicode]:
        """
        Returns the script menu path.
        @return the script menu path
        """
        ...

    def getMenuPathAsString(self) -> unicode:
        """
        Returns the script menu path as a string.
         For example,{@literal "Path1->Path2->Path3"}.
        @return the script menu path as a string
        """
        ...

    def getName(self) -> unicode:
        """
        Returns the name of the script.
         The name of the script is the file name.
        @return the name of the script
        """
        ...

    def getSourceFile(self) -> generic.jar.ResourceFile:
        """
        Returns the script source file.
        @return the script source file
        """
        ...

    def getToolBarImage(self, scaled: bool) -> javax.swing.ImageIcon:
        """
        Returns the script tool bar icon.
        @param scaled true if the icon should be scaled to 16x16.
        @return the script tool bar icon
        """
        ...

    def getToolTipText(self) -> unicode:
        """
        Returns a string designed to be used as a tool tip for describing this script
        @return a string designed to be used as a tool tip
        """
        ...

    def hasErrors(self) -> bool:
        """
        @return true if the script either has compiler errors, or is a duplicate
        """
        ...

    def hashCode(self) -> int: ...

    def isCategory(self, otherCategory: List[unicode]) -> bool:
        """
        Returns true if 'cat' is a category.
        @param otherCategory the script category
        @return true if 'cat' is a category
        """
        ...

    def isCompileErrors(self) -> bool:
        """
        Returns true if the script has compile errors.
        @return true if the script has compile errors
        """
        ...

    def isDuplicate(self) -> bool:
        """
        Returns true if this script is a duplicate.
         When two or more scripts exists with the same name, this
         is considered a duplicate script.
        @return true if this script is a duplicate
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def refresh(self) -> None:
        """
        Setting the toolbar image to null forces it to be reloaded on the next request.
        """
        ...

    def setCompileErrors(self, b: bool) -> None:
        """
        Sets whether the script has compile errors.
        @param b true if the script has compile errors
        """
        ...

    def setDuplicate(self, isDuplicate: bool) -> None:
        """
        Sets whether the script is a duplicate.
        @param isDuplicate true if the script is a duplicate
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
    def author(self) -> unicode: ...

    @property
    def category(self) -> List[unicode]: ...

    @property
    def compileErrors(self) -> bool: ...

    @compileErrors.setter
    def compileErrors(self, value: bool) -> None: ...

    @property
    def description(self) -> unicode: ...

    @property
    def duplicate(self) -> bool: ...

    @duplicate.setter
    def duplicate(self, value: bool) -> None: ...

    @property
    def errorMessage(self) -> unicode: ...

    @property
    def importPackage(self) -> unicode: ...

    @property
    def keyBinding(self) -> javax.swing.KeyStroke: ...

    @property
    def keyBindingErrorMessage(self) -> unicode: ...

    @property
    def menuPath(self) -> List[unicode]: ...

    @property
    def menuPathAsString(self) -> unicode: ...

    @property
    def name(self) -> unicode: ...

    @property
    def sourceFile(self) -> generic.jar.ResourceFile: ...

    @property
    def toolTipText(self) -> unicode: ...
