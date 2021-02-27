import java.lang


class DialogManager(object):
    """
    Helper class to manage actions for saving and exporting the tool
    """





    def __init__(self, tool: ghidra.framework.plugintool.PluginTool): ...



    def equals(self, __a0: object) -> bool: ...

    def exportDefaultTool(self) -> None:
        """
        Exports a version of our tool without any config settings.  This is useful for making a
         new 'default' tool to be shared with others, which will not contain any user settings.
        """
        ...

    def exportTool(self) -> None:
        """
        Write our tool to a filename; the user is prompted for a filename
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def saveToolAs(self) -> bool:
        """
        Show the "Save Tool" dialog.  Returns true if the user performed a 'save as'; returns false
         if the user cancelled.
        @return false if the user cancelled
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
