import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.util.classfinder
import ghidra.util.task
import java.lang


class LanguageTranslator(ghidra.util.classfinder.ExtensionPoint, object):
    """
    NOTE:  ALL LanguageTranslator CLASSES MUST END IN "LanguageTranslator".  If not,
     the ClassSearcher will not find them.

     LanguageTranslator provides translation capabilities used by Program.setLanguage
     when converting a program from one language to another or from one version to another.

     Explicit translator implementations must implement the default constructor and should not
     instantiate Language, AddressSpace, AddressFactory or Register objects until isValid() is invoked.
    """









    def equals(self, __a0: object) -> bool: ...

    def fixupInstructions(self, program: ghidra.program.model.listing.Program, oldLanguage: ghidra.program.model.lang.Language, monitor: ghidra.util.task.TaskMonitor) -> None:
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
        @param program
        @param oldLanguage the oldest language involved in the current upgrade translation
         (this is passed since this is the only fixup invocation which must handle the any
         relevant fixup complexities when transitioning from the specified oldLanguage).
        @param monitor task monitor
        @throws Exception if a bad exception occurs with the post upgrade fixup
        @throws CancelledException if upgrade cancelled
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getNewAddressSpace(self, oldSpaceName: unicode) -> ghidra.program.model.address.AddressSpace:
        """
        Translate BASE address spaces (Overlay spaces are not handled)
        @param oldSpaceName old space name
        @return corresponding address space in new language
        """
        ...

    def getNewCompilerSpecID(self, oldCompilerSpecID: ghidra.program.model.lang.CompilerSpecID) -> ghidra.program.model.lang.CompilerSpecID:
        """
        Obtain the new compiler specification ID given the old compiler spec ID.
        @param oldCompilerSpecID old compiler spec ID.
        @return new compiler spec ID.
        """
        ...

    def getNewContextRegister(self) -> ghidra.program.model.lang.Register:
        """
        Returns the new processor context register or null if not defined
        """
        ...

    def getNewLanguage(self) -> ghidra.program.model.lang.Language:
        """
        Returns new language
        """
        ...

    def getNewLanguageID(self) -> ghidra.program.model.lang.LanguageID:
        """
        Returns new language name
        """
        ...

    def getNewRegister(self, oldReg: ghidra.program.model.lang.Register) -> ghidra.program.model.lang.Register:
        """
        Find new register which corresponds to the specified old register.
        @param oldReg old register
        @return new register or null if corresponding register not found.
        """
        ...

    def getNewRegisterValue(self, oldValue: ghidra.program.model.lang.RegisterValue) -> ghidra.program.model.lang.RegisterValue:
        """
        Get the translated register value
        @param oldValue old register value (may not be null)
        @return new register value or null if register not mapped
        @see #isValueTranslationRequired(Register)
        """
        ...

    def getNewVersion(self) -> int:
        """
        Returns new language version
        """
        ...

    def getOldCompilerSpec(self, oldCompilerSpecID: ghidra.program.model.lang.CompilerSpecID) -> ghidra.program.model.lang.CompilerSpec:
        """
        Get a compiler spec suitable for use with the old language.  The compiler
         spec returned is intended for upgrade use only prior to the setLanguage
         and may be based upon compiler conventions specified in the new compiler
         spec returned by getNewCompilerSpec given the same compilerSpecID.
        @param oldCompilerSpecID old compiler spec ID.
        @return compiler spec for use with old language
        @throws CompilerSpecNotFoundException if new compiler spec not found based upon
         translator mappings.
        """
        ...

    def getOldContextRegister(self) -> ghidra.program.model.lang.Register:
        """
        Returns the old processor context register or null if not defined
        """
        ...

    def getOldLanguage(self) -> ghidra.program.model.lang.Language:
        """
        Returns old language
        @throws IllegalStateException if instance has not been validated
        @see #isValid()
        """
        ...

    def getOldLanguageID(self) -> ghidra.program.model.lang.LanguageID:
        """
        Returns old language name
        """
        ...

    def getOldRegister(self, oldAddr: ghidra.program.model.address.Address, size: int) -> ghidra.program.model.lang.Register:
        """
        Get the old register at the specified oldAddr.  This will null if the specified
         address is offcut within the register.
         The smallest register will be returned which is greater than or equal to the specified size.
        @param oldAddr old register address.
        @param size minimum register size
        @return old register or null if suitable register can not be found.
        @see #getOldRegisterContaining(Address)
        """
        ...

    def getOldRegisterContaining(self, oldAddr: ghidra.program.model.address.Address) -> ghidra.program.model.lang.Register:
        """
        Get the largest old register which contains the specified oldAddr
        @param oldAddr old register address which may be offcut
        @return old register or null if suitable register can not be found.
        """
        ...

    def getOldVersion(self) -> int:
        """
        Returns old language version
        """
        ...

    def hashCode(self) -> int: ...

    def isValid(self) -> bool:
        """
        Validate translator to complete initialization and ensure language compatibility.
         This method will be invoked by the LanguageTranslatorFactory before handing out this
         translator.
        @return true if translator successfully validated
        """
        ...

    def isValueTranslationRequired(self, oldReg: ghidra.program.model.lang.Register) -> bool:
        """
        Returns true if register value translation required for
         program context.
        @param oldReg
        @see #getNewRegisterValue(RegisterValue)
        """
        ...

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
    def newContextRegister(self) -> ghidra.program.model.lang.Register: ...

    @property
    def newLanguage(self) -> ghidra.program.model.lang.Language: ...

    @property
    def newLanguageID(self) -> ghidra.program.model.lang.LanguageID: ...

    @property
    def newVersion(self) -> int: ...

    @property
    def oldContextRegister(self) -> ghidra.program.model.lang.Register: ...

    @property
    def oldLanguage(self) -> ghidra.program.model.lang.Language: ...

    @property
    def oldLanguageID(self) -> ghidra.program.model.lang.LanguageID: ...

    @property
    def oldVersion(self) -> int: ...

    @property
    def valid(self) -> bool: ...
