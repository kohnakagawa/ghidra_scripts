import ghidra.program.model.lang
import ghidra.util.task
import java.lang


class LanguagePostUpgradeInstructionHandler(object):
    """
    LanguagePostUpgradeInstructionHandler provides an abstract implementation
     of a post language-upgrade instruction modification handler.  The Simple Language Translator
     facilitates the specification of such a handler implementation within a language
     translator specification file using the post_upgrade_handler element.
     Following a major-version language upgrade, the last translator invoked is given an
     opportunity to perform additional instruction modifications on the entire program.
    """





    def __init__(self, program: ghidra.program.model.listing.Program):
        """
        Constructor
        @param program
        """
        ...



    def equals(self, __a0: object) -> bool: ...

    def fixupInstructions(self, oldLanguage: ghidra.program.model.lang.Language, monitor: ghidra.util.task.TaskMonitor) -> None:
        """
        Invoked after Program language upgrade has completed.
         Implementation of this method permits the final re-disassembled program to be
         examined/modified to address more complex language upgrades.  This method will only be
         invoked on the latest translator, which means all complex multi-version post-upgrade
         concerns must factor in the complete language transition.  The program's language
         information will still reflect the original pre-upgrade state, and if the program is
         undergoing a schema version upgrade as well, certain complex upgrades may not
         have been completed (e.g., Function and Variable changes).  Program modifications should
         be restricted to instruction and instruction context changes only.
        @param oldLanguage the oldest language involved in the current upgrade translation
         (this is passed since this is the only fixup invocation which must handle the any
         relevant fixup complexities when transitioning from the specified oldLanguage).
        @param monitor task monitor
        @throws CancelledException if upgrade cancelled
        """
        ...

    def getClass(self) -> java.lang.Class: ...

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
