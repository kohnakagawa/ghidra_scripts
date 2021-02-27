import ghidra.app.plugin.core.searchtext.databasesearcher
import ghidra.program.model.address
import ghidra.program.model.listing
import ghidra.program.util
import java.lang
import java.util.regex


class InstructionMnemonicOperandFieldSearcher(ghidra.app.plugin.core.searchtext.databasesearcher.ProgramDatabaseFieldSearcher):








    @staticmethod
    def createInstructionMnemonicAndOperandFieldSearcher(__a0: ghidra.program.model.listing.Program, __a1: ghidra.program.util.ProgramLocation, __a2: ghidra.program.model.address.AddressSetView, __a3: bool, __a4: java.util.regex.Pattern, __a5: ghidra.program.model.listing.CodeUnitFormat) -> ghidra.app.plugin.core.searchtext.databasesearcher.InstructionMnemonicOperandFieldSearcher: ...

    @staticmethod
    def createInstructionMnemonicOnlyFieldSearcher(__a0: ghidra.program.model.listing.Program, __a1: ghidra.program.util.ProgramLocation, __a2: ghidra.program.model.address.AddressSetView, __a3: bool, __a4: java.util.regex.Pattern, __a5: ghidra.program.model.listing.CodeUnitFormat) -> ghidra.app.plugin.core.searchtext.databasesearcher.InstructionMnemonicOperandFieldSearcher: ...

    @staticmethod
    def createInstructionOperandOnlyFieldSearcher(__a0: ghidra.program.model.listing.Program, __a1: ghidra.program.util.ProgramLocation, __a2: ghidra.program.model.address.AddressSetView, __a3: bool, __a4: java.util.regex.Pattern, __a5: ghidra.program.model.listing.CodeUnitFormat) -> ghidra.app.plugin.core.searchtext.databasesearcher.InstructionMnemonicOperandFieldSearcher: ...

    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    def getMatch(self) -> ghidra.program.util.ProgramLocation: ...

    def getNextSignificantAddress(self, __a0: ghidra.program.model.address.Address) -> ghidra.program.model.address.Address: ...

    def hasMatch(self, __a0: ghidra.program.model.address.Address) -> bool: ...

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
