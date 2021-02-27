import java.lang


class RefType(object):
    """
    Class to define reference types.
    """

    CALLOTHER_OVERRIDE_CALL: ghidra.program.model.symbol.FlowType = CALLOTHER_OVERRIDE_CALL
    CALLOTHER_OVERRIDE_JUMP: ghidra.program.model.symbol.FlowType = CALLOTHER_OVERRIDE_JUMP
    CALL_OVERRIDE_UNCONDITIONAL: ghidra.program.model.symbol.FlowType = CALL_OVERRIDE_UNCONDITIONAL
    CALL_TERMINATOR: ghidra.program.model.symbol.FlowType = CALL_TERMINATOR
    COMPUTED_CALL: ghidra.program.model.symbol.FlowType = COMPUTED_CALL
    COMPUTED_CALL_TERMINATOR: ghidra.program.model.symbol.FlowType = COMPUTED_CALL_TERMINATOR
    COMPUTED_JUMP: ghidra.program.model.symbol.FlowType = COMPUTED_JUMP
    CONDITIONAL_CALL: ghidra.program.model.symbol.FlowType = CONDITIONAL CALL
    CONDITIONAL_CALL_TERMINATOR: ghidra.program.model.symbol.FlowType = CONDITIONAL_CALL_TERMINATOR
    CONDITIONAL_COMPUTED_CALL: ghidra.program.model.symbol.FlowType = CONDITIONAL_COMPUTED_CALL
    CONDITIONAL_COMPUTED_JUMP: ghidra.program.model.symbol.FlowType = CONDITIONAL_COMPUTED_JUMP
    CONDITIONAL_JUMP: ghidra.program.model.symbol.FlowType = CONDITIONAL_JUMP
    CONDITIONAL_TERMINATOR: ghidra.program.model.symbol.FlowType = CONDITIONAL_TERMINATOR
    DATA: ghidra.program.model.symbol.RefType = DATA
    DATA_IND: ghidra.program.model.symbol.RefType = DATA_IND
    EXTERNAL_REF: ghidra.program.model.symbol.RefType = EXTERNAL
    FALL_THROUGH: ghidra.program.model.symbol.FlowType = FALL_THROUGH
    FLOW: ghidra.program.model.symbol.FlowType = FLOW
    INDIRECTION: ghidra.program.model.symbol.FlowType = INDIRECTION
    INVALID: ghidra.program.model.symbol.FlowType = INVALID
    JUMP_OVERRIDE_UNCONDITIONAL: ghidra.program.model.symbol.FlowType = JUMP_OVERRIDE_UNCONDITIONAL
    JUMP_TERMINATOR: ghidra.program.model.symbol.FlowType = JUMP_TERMINATOR
    PARAM: ghidra.program.model.symbol.RefType = PARAM
    READ: ghidra.program.model.symbol.RefType = READ
    READ_IND: ghidra.program.model.symbol.RefType = READ_IND
    READ_WRITE: ghidra.program.model.symbol.RefType = READ_WRITE
    READ_WRITE_IND: ghidra.program.model.symbol.RefType = READ_WRITE_IND
    STACK_READ: ghidra.program.model.symbol.RefType = STACK_READ
    STACK_WRITE: ghidra.program.model.symbol.RefType = STACK_WRITE
    TERMINATOR: ghidra.program.model.symbol.FlowType = TERMINATOR
    THUNK: ghidra.program.model.symbol.RefType = THUNK
    UNCONDITIONAL_CALL: ghidra.program.model.symbol.FlowType = UNCONDITIONAL_CALL
    UNCONDITIONAL_JUMP: ghidra.program.model.symbol.FlowType = UNCONDITIONAL_JUMP
    WRITE: ghidra.program.model.symbol.RefType = WRITE
    WRITE_IND: ghidra.program.model.symbol.RefType = WRITE_IND







    def equals(self, obj: object) -> bool:
        """
        @see java.lang.Object#equals(java.lang.Object)
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getName(self) -> unicode:
        """
        Returns name of ref-type
        """
        ...

    def getValue(self) -> int:
        """
        Get the int value for this RefType object.
        """
        ...

    def hasFallthrough(self) -> bool:
        """
        Returns true if this flow type can fall through.
        """
        ...

    def hashCode(self) -> int:
        """
        @see java.lang.Object#hashCode()
        """
        ...

    def isCall(self) -> bool:
        """
        Returns true if the flow is call
        """
        ...

    def isComputed(self) -> bool:
        """
        Returns true if the flow is a computed call or compute jump.
        """
        ...

    def isConditional(self) -> bool:
        """
        Returns true if the flow is a conditional call or jump.
        """
        ...

    def isData(self) -> bool:
        """
        Returns true if the reference is to data
        """
        ...

    def isFallthrough(self) -> bool:
        """
        Return true if this flow type is one that does not cause
         a break in control flow.
        """
        ...

    def isFlow(self) -> bool:
        """
        Returns true if the reference is an instruction flow reference.
        """
        ...

    def isIndirect(self) -> bool:
        """
        Returns true if the reference is indirect
        """
        ...

    def isJump(self) -> bool:
        """
        Returns true if the flow is jump
        """
        ...

    def isOverride(self) -> bool:
        """
        @return true precisely when the reference is an overriding reference
        """
        ...

    def isRead(self) -> bool:
        """
        Returns true if the reference is a read.
        """
        ...

    def isTerminal(self) -> bool:
        """
        returns true if this instruction terminates.
        """
        ...

    def isUnConditional(self) -> bool:
        """
        Returns true if the flow is an unconditional call or jump.
        """
        ...

    def isWrite(self) -> bool:
        """
        Returns true if the reference is a write.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def toString(self) -> unicode:
        """
        @see java.lang.Object#toString()
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def call(self) -> bool: ...

    @property
    def computed(self) -> bool: ...

    @property
    def conditional(self) -> bool: ...

    @property
    def data(self) -> bool: ...

    @property
    def fallthrough(self) -> bool: ...

    @property
    def flow(self) -> bool: ...

    @property
    def indirect(self) -> bool: ...

    @property
    def jump(self) -> bool: ...

    @property
    def name(self) -> unicode: ...

    @property
    def override(self) -> bool: ...

    @property
    def read(self) -> bool: ...

    @property
    def terminal(self) -> bool: ...

    @property
    def unConditional(self) -> bool: ...

    @property
    def value(self) -> int: ...

    @property
    def write(self) -> bool: ...
