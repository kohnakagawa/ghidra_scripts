import ghidra.framework.data
import ghidra.framework.model
import java.lang


class ToolAssociationInfo(object):
    """
    A class that describes a content types and the tool used to open it.
    """





    def __init__(self, contentHandler: ghidra.framework.data.ContentHandler, associatedToolName: unicode, currentToolTemplate: ghidra.framework.model.ToolTemplate, defaultTemplate: ghidra.framework.model.ToolTemplate): ...



    def equals(self, __a0: object) -> bool: ...

    def getAssociatedToolName(self) -> unicode: ...

    def getClass(self) -> java.lang.Class: ...

    def getContentHandler(self) -> ghidra.framework.data.ContentHandler: ...

    def getCurrentTemplate(self) -> ghidra.framework.model.ToolTemplate:
        """
        Returns the currently assigned tool used to open the content type of this association.
        """
        ...

    def getDefaultTemplate(self) -> ghidra.framework.model.ToolTemplate: ...

    def hashCode(self) -> int: ...

    def isDefault(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def restoreDefaultAssociation(self) -> None: ...

    def setCurrentTool(self, toolTemplate: ghidra.framework.model.ToolTemplate) -> None:
        """
        Sets the tool name that should be used to open files for the content type represented
         by this tool association.
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
    def associatedToolName(self) -> unicode: ...

    @property
    def contentHandler(self) -> ghidra.framework.data.ContentHandler: ...

    @property
    def currentTemplate(self) -> ghidra.framework.model.ToolTemplate: ...

    @property
    def currentTool(self) -> None: ...  # No getter available.

    @currentTool.setter
    def currentTool(self, value: ghidra.framework.model.ToolTemplate) -> None: ...

    @property
    def default(self) -> bool: ...

    @property
    def defaultTemplate(self) -> ghidra.framework.model.ToolTemplate: ...
