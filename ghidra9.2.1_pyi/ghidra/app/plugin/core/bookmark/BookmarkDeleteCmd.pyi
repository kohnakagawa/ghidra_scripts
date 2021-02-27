import ghidra.framework.cmd
import ghidra.framework.model
import java.lang


class BookmarkDeleteCmd(object, ghidra.framework.cmd.Command):




    @overload
    def __init__(self, __a0: unicode): ...

    @overload
    def __init__(self, __a0: ghidra.program.model.address.Address): ...

    @overload
    def __init__(self, __a0: ghidra.program.model.address.AddressSetView): ...

    @overload
    def __init__(self, __a0: ghidra.program.model.listing.Bookmark): ...

    @overload
    def __init__(self, __a0: List[object]): ...

    @overload
    def __init__(self, __a0: unicode, __a1: unicode): ...

    @overload
    def __init__(self, __a0: ghidra.program.model.address.Address, __a1: unicode): ...

    @overload
    def __init__(self, __a0: ghidra.program.model.address.AddressSetView, __a1: unicode): ...

    @overload
    def __init__(self, __a0: ghidra.program.model.address.Address, __a1: unicode, __a2: unicode): ...

    @overload
    def __init__(self, __a0: ghidra.program.model.address.AddressSetView, __a1: unicode, __a2: unicode): ...



    def applyTo(self, __a0: ghidra.framework.model.DomainObject) -> bool: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode: ...

    def getPresentationName(self) -> unicode: ...

    def getStatusMsg(self) -> unicode: ...

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
    def name(self) -> unicode: ...

    @property
    def presentationName(self) -> unicode: ...

    @property
    def statusMsg(self) -> unicode: ...
