import ghidra.app.plugin.processors.sleigh
import java.lang


class OpTplWalker(object):
    """
    Class for walking pcode templates OpTpl in the correct order
     Supports walking the tree of an entire SleighInstructionPrototype or just a single ConstructTpl
    """





    @overload
    def __init__(self, tpl: ghidra.app.plugin.processors.sleigh.template.ConstructTpl):
        """
        Constructor for walking a single template
        @param tpl
        """
        ...

    @overload
    def __init__(self, root: ghidra.app.plugin.processors.sleigh.ConstructState, sectionnum: int):
        """
        Constructor for walking an entire parse tree
        @param root is the root ConstructState of the tree
        @param sectionnum is the named section to traverse (or -1 for main section)
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getState(self) -> ghidra.app.plugin.processors.sleigh.ConstructState: ...

    def hashCode(self) -> int: ...

    def isState(self) -> bool: ...

    def nextOpTpl(self) -> object: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def popBuild(self) -> None:
        """
        Move to the parent of the current node
        """
        ...

    def pushBuild(self, buildnum: int) -> None:
        """
        While walking the OpTpl's in order, follow a particular BUILD directive into its respective Constructor and ContructTpl
         Use popBuild to backtrack
        @param buildnum is the operand number of the BUILD directive to follow
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
    def state(self) -> bool: ...
