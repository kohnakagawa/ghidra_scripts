from typing import List
import ghidra.framework.model
import ghidra.framework.plugintool
import java.lang


class WorkspaceImpl(object, ghidra.framework.model.Workspace):
    """
    WorkspaceImpl

     Implementation of a Workspace.
    """









    def createTool(self) -> ghidra.framework.plugintool.PluginTool: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode: ...

    def getTools(self) -> List[ghidra.framework.plugintool.PluginTool]: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def runTool(self, template: ghidra.framework.model.ToolTemplate) -> ghidra.framework.plugintool.PluginTool: ...

    def setActive(self) -> None: ...

    def setName(self, newName: unicode) -> None: ...

    def toString(self) -> unicode:
        """
        Returns a string representation of the object. In general, the
         <code>toString</code> method returns a string that
         "textually represents" this object. The result should
         be a concise but informative representation that is easy for a
         person to read.
        @return a string representation of the object.
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
