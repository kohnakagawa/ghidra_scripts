import ghidra.feature.vt.api.main
import ghidra.program.model.address
import ghidra.util.task
import java.lang
import java.util


class VTAssociation(object):








    def clearStatus(self) -> None: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getDestinationAddress(self) -> ghidra.program.model.address.Address: ...

    def getMarkupItems(self, __a0: ghidra.util.task.TaskMonitor) -> java.util.Collection: ...

    def getMarkupStatus(self) -> ghidra.feature.vt.api.main.VTAssociationMarkupStatus: ...

    def getRelatedAssociations(self) -> java.util.Collection: ...

    def getSession(self) -> ghidra.feature.vt.api.main.VTSession: ...

    def getSourceAddress(self) -> ghidra.program.model.address.Address: ...

    def getStatus(self) -> ghidra.feature.vt.api.main.VTAssociationStatus: ...

    def getType(self) -> ghidra.feature.vt.api.main.VTAssociationType: ...

    def getVoteCount(self) -> int: ...

    def hasAppliedMarkupItems(self) -> bool: ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def setAccepted(self) -> None: ...

    def setMarkupStatus(self, __a0: ghidra.feature.vt.api.main.VTAssociationMarkupStatus) -> None: ...

    def setRejected(self) -> None: ...

    def setVoteCount(self, __a0: int) -> None: ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def destinationAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def markupStatus(self) -> ghidra.feature.vt.api.main.VTAssociationMarkupStatus: ...

    @markupStatus.setter
    def markupStatus(self, value: ghidra.feature.vt.api.main.VTAssociationMarkupStatus) -> None: ...

    @property
    def relatedAssociations(self) -> java.util.Collection: ...

    @property
    def session(self) -> ghidra.feature.vt.api.main.VTSession: ...

    @property
    def sourceAddress(self) -> ghidra.program.model.address.Address: ...

    @property
    def status(self) -> ghidra.feature.vt.api.main.VTAssociationStatus: ...

    @property
    def type(self) -> ghidra.feature.vt.api.main.VTAssociationType: ...

    @property
    def voteCount(self) -> int: ...

    @voteCount.setter
    def voteCount(self, value: int) -> None: ...
