import ghidra.app.emulator.memory
import ghidra.app.emulator.state
import ghidra.program.model.address
import java.lang


class EmulatorLoadData(object):








    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getInitialRegisterState(self) -> ghidra.app.emulator.state.RegisterState: ...

    def getMemoryLoadImage(self) -> ghidra.app.emulator.memory.MemoryLoadImage: ...

    def getView(self) -> ghidra.program.model.address.AddressSetView: ...

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
    def initialRegisterState(self) -> ghidra.app.emulator.state.RegisterState: ...

    @property
    def memoryLoadImage(self) -> ghidra.app.emulator.memory.MemoryLoadImage: ...

    @property
    def view(self) -> ghidra.program.model.address.AddressSetView: ...
