import java.lang


class DebugStateMachineOpCodes(object):
    DBG_ADVANCE_LINE: int = 2
    DBG_ADVANCE_PC: int = 1
    DBG_END_LOCAL: int = 5
    DBG_END_SEQUENCE: int = 0
    DBG_RESTART_LOCAL: int = 6
    DBG_SET_EPILOGUE_BEGIN: int = 8
    DBG_SET_FILE: int = 9
    DBG_SET_PROLOGUE_END: int = 7
    DBG_START_LOCAL: int = 3
    DBG_START_LOCAL_EXTENDED: int = 4



    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isSpecialOpCode(__a0: int) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
