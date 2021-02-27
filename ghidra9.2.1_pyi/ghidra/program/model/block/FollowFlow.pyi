import ghidra.program.model.address
import ghidra.util.task
import java.lang


class FollowFlow(object):
    """
    FollowFlow follows the program's code flow either forward or backward from an initial
     address set. It adds the flow addresses to the initial address set by flowing "from" the
     initial addresses in the forward direction or by flowing "to" the initial addresses when
     used in the backward direction.
     The flow can be limited by indicating the flow types (i.e. unconditional call,
     computed jump, etc.) that we do NOT want to follow.
    """





    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, addressSet: ghidra.program.model.address.AddressSet, doNotFollow: List[ghidra.program.model.symbol.FlowType]):
        """
        Constructor
        @param program the program whose flow we are following.
        @param addressSet the initial addresses that should be flowed from or flowed to.
        @param doNotFollow array of flow types that are not to be followed.
         null or empty array indicates follow all flows. The following are valid
         flow types for the doNotFollow array:
         <BR>FlowType.COMPUTED_CALL
         <BR>FlowType.CONDITIONAL_CALL
         <BR>FlowType.UNCONDITIONAL_CALL
         <BR>FlowType.COMPUTED_JUMP
         <BR>FlowType.CONDITIONAL_JUMP
         <BR>FlowType.UNCONDITIONAL_JUMP
         <BR>FlowType.INDIRECTION
        """
        ...

    @overload
    def __init__(self, program: ghidra.program.model.listing.Program, addressSet: ghidra.program.model.address.AddressSet, doNotFollow: List[ghidra.program.model.symbol.FlowType], followIntoFunctions: bool):
        """
        Constructor
        @param program the program whose flow we are following.
        @param addressSet the initial addresses that should be flowed from or flowed to.
        @param doNotFollow array of flow types that are not to be followed.
         null or empty array indicates follow all flows. The following are valid
         flow types for the doNotFollow array:
         <BR>FlowType.COMPUTED_CALL
         <BR>FlowType.CONDITIONAL_CALL
         <BR>FlowType.UNCONDITIONAL_CALL
         <BR>FlowType.COMPUTED_JUMP
         <BR>FlowType.CONDITIONAL_JUMP
         <BR>FlowType.UNCONDITIONAL_JUMP
         <BR>FlowType.INDIRECTION
        @param followIntoFunctions true if flows into (or back from) defined functions
         should be followed.
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getFlowAddressSet(self, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.address.AddressSet:
        """
        Determines the address set that flows from the addresses in this FollowFlow object's
         initialAddresses set. The address set is determined by what addresses were provided
         when the FollowFlow was constructed and the type of flow requested.
         This method follows flows in the forward direction.
        @param monitor a cancellable task monitor, may be null
        @return the resulting address set.
        """
        ...

    def getFlowToAddressSet(self, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.address.AddressSet:
        """
        Determines the address set that flows to the addresses in this FollowFlow object's
         initialAddresses set. The address set is determined by what addresses were provided
         when the FollowFlow was constructed and the type of flow requested. The constructor
         indicated the flow types not to be followed. All others will be traversed in the
         backwards direction to determine the addresses that are flowing to those in the initial
         set.
        @param monitor a cancellable task monitor, may be null
        @return the resulting address set.
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
