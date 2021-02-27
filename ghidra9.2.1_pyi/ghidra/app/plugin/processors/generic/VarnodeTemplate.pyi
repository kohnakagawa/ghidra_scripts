import ghidra.app.plugin.processors.generic
import ghidra.program.model.pcode
import java.io
import java.lang
import java.util


class VarnodeTemplate(object, java.io.Serializable):
    """
    To change this generated comment edit the template variable "typecomment":

     To enable and disable the creation of type comments go to

    """





    def __init__(self, space: ghidra.app.plugin.processors.generic.ConstantTemplate, offset: ghidra.app.plugin.processors.generic.ConstantTemplate, size: ghidra.app.plugin.processors.generic.ConstantTemplate, addressFactory: ghidra.program.model.address.AddressFactory, ou: bool): ...



    def equals(self, o: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    def loadomit(self) -> bool: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def offset(self) -> ghidra.app.plugin.processors.generic.ConstantTemplate: ...

    def oneuse(self) -> bool: ...

    @overload
    def resolve(self, position: ghidra.app.plugin.processors.generic.Position, bufoff: int) -> ghidra.program.model.pcode.Varnode:
        """
        Resolves a varnode at the given position and buffer offset
        @param position the position
        @param bufoff the buffer offset
        @return the resolved {@link Varnode raw varnode}. (<b>Only</b> contains an address and size)
        @throws Exception if an error occurs resolving the varnode
        """
        ...

    @overload
    def resolve(self, handles: java.util.HashMap, position: ghidra.app.plugin.processors.generic.Position, bufoff: int) -> ghidra.program.model.pcode.Varnode:
        """
        Method resolve.
        @param handles
        @return Varnode
        """
        ...

    def setDef(self, opTemplate: ghidra.app.plugin.processors.generic.OpTemplate) -> None:
        """
        Method setDef.
        @param opTemplate
        """
        ...

    def setReplace(self, op: ghidra.app.plugin.processors.generic.Operand, load: bool) -> None: ...

    def size(self) -> ghidra.app.plugin.processors.generic.ConstantTemplate: ...

    def space(self) -> ghidra.app.plugin.processors.generic.ConstantTemplate: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def def(self) -> None: ...  # No getter available.

    @def.setter
    def def(self, value: ghidra.app.plugin.processors.generic.OpTemplate) -> None: ...
