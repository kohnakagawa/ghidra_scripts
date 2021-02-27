import docking.action
import ghidra.app.plugin.core.comments
import ghidra.program.util
import java.lang


class DecompilerCommentsActionFactory(ghidra.app.plugin.core.comments.CommentsActionFactory):




    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getEditCommentsAction(__a0: ghidra.app.plugin.core.comments.CommentsDialog, __a1: unicode) -> docking.action.DockingAction: ...

    @staticmethod
    def getSetCommentsAction(__a0: ghidra.app.plugin.core.comments.CommentsDialog, __a1: unicode, __a2: unicode, __a3: int) -> docking.action.DockingAction: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isCommentSupported(__a0: ghidra.program.util.ProgramLocation) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
