import ghidra.framework.cmd
import ghidra.framework.model
import java.lang


class RenameLabelCmd(object, ghidra.framework.cmd.Command):
    """
    Command for renaming labels. Handles converting back and forth between
     default and named labels as well.
    """





    @overload
    def __init__(self, addr: ghidra.program.model.address.Address, oldName: unicode, newName: unicode, source: ghidra.program.model.symbol.SourceType):
        """
        Constructs a new command for renaming global labels.
        @param addr Address of label to be renamed.
        @param oldName the name of the label to be renamed; may be null
         of the existing label is a dynamic label
        @param newName the new name for the label
        @param source the source of this symbol
        """
        ...

    @overload
    def __init__(self, addr: ghidra.program.model.address.Address, oldName: unicode, newName: unicode, currentNamespace: ghidra.program.model.symbol.Namespace, source: ghidra.program.model.symbol.SourceType):
        """
        Constructs a new command for renaming a label within a specified namespace.
        @param addr Address of label to be renamed.
        @param oldName the current name of the label to be renamed.
        @param newName the new name for the label. (null for default)
        @param currentNamespace the symbol's current name space. (The namespace to associate this label with)
        @param source the source of this symbol
        """
        ...

    @overload
    def __init__(self, addr: ghidra.program.model.address.Address, oldName: unicode, newName: unicode, currentNamespace: ghidra.program.model.symbol.Namespace, newNamespace: ghidra.program.model.symbol.Namespace, source: ghidra.program.model.symbol.SourceType):
        """
        Constructs a new command for renaming a label within currentNamespace and changing the
         namespace to newNamespace.
        @param addr Address of label to be renamed.
        @param oldName the current name of the label to be renamed.
        @param newName the new name for the label. (null for default)
        @param currentNamespace the symbol's current parent name space (null indicates global namespace)
        @param newNamespace final namespace (null indicates global namespace)
        @param source the source of this symbol
        """
        ...



    def applyTo(self, obj: ghidra.framework.model.DomainObject) -> bool:
        """
        @see ghidra.framework.cmd.Command#applyTo(ghidra.framework.model.DomainObject)
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode:
        """
        @see ghidra.framework.cmd.Command#getName()
        """
        ...

    def getStatusMsg(self) -> unicode:
        """
        @see ghidra.framework.cmd.Command#getStatusMsg()
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
    def name(self) -> unicode: ...

    @property
    def statusMsg(self) -> unicode: ...
