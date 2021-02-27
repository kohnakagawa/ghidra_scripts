import generic.jar
import ghidra.app.util.bin.format.dwarf4.next
import ghidra.program.model.lang
import java.lang
import org.jdom


class DWARFRegisterMappingsManager(object):
    """
    Factory class to instantiate and cache DWARFRegisterMappings objects.

    """





    def __init__(self): ...



    def equals(self, __a0: object) -> bool: ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getDWARFRegisterMappingFileFor(lang: ghidra.program.model.lang.Language) -> generic.jar.ResourceFile:
        """
        Returns {@link ResourceFile} that should contain the specified language's
         DWARF register mapping, never null.
        @param lang {@link Language} to find the mapping file for.
        @return {@link ResourceFile} of where the mapping file should be, never
                 null.
        @throws IOException if not a Sleigh language or no mapping specified or
                     multiple mappings specified.
        """
        ...

    @staticmethod
    def getMappingForLang(lang: ghidra.program.model.lang.Language) -> ghidra.app.util.bin.format.dwarf4.next.DWARFRegisterMappings:
        """
        Returns a possibly cached {@link DWARFRegisterMappings} object for the
         specified language,
         <p>
        @param lang {@link Language} to get the matching DWARF register mappings
                    for
        @return {@link DWARFRegisterMappings} instance, never null
        @throws IOException if mapping not found or invalid
        """
        ...

    @overload
    @staticmethod
    def hasDWARFRegisterMapping(lang: ghidra.program.model.lang.Language) -> bool:
        """
        Returns true if the specified {@link Language} has DWARF register
         mappings.
        @param lang The {@link Language} to test
        @return true if the language has a DWARF register mapping specified
        @throws IOException if there was an error in the language LDEF file.
        """
        ...

    @overload
    @staticmethod
    def hasDWARFRegisterMapping(langDesc: ghidra.program.model.lang.LanguageDescription) -> bool:
        """
        Returns true if the specified {@link LanguageDescription} has DWARF
         register mappings.
        @param langDesc The {@link LanguageDescription} to test
        @return true if the language has a DWARF register mapping specified
        @throws IOException if there was an error in the language LDEF file.
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def readMappingForLang(lang: ghidra.program.model.lang.Language) -> ghidra.app.util.bin.format.dwarf4.next.DWARFRegisterMappings:
        """
        Finds the DWARF register mapping information file specified in the
         specified language's LDEF file and returns a new
         {@link DWARFRegisterMappings} object containing the data read from that
         file.
         <p>
         Throws {@link IOException} if the lang does not have a mapping or it is
         invalid.
         <p>
        @param lang {@link Language} to read the matching DWARF register mappings
                    for
        @return a new {@link DWARFRegisterMappings} instance, created from
                 information read from the {@link #DWARF_REGISTER_MAPPING_NAME}
                 xml file referenced in the language's LDEF, never null.
        @throws IOException if there is no DWARF register mapping file associated
                     with the specified {@link Language} or if there was an error
                     in the register mapping data.
        """
        ...

    @staticmethod
    def readMappingFrom(rootElem: org.jdom.Element, lang: ghidra.program.model.lang.Language) -> ghidra.app.util.bin.format.dwarf4.next.DWARFRegisterMappings:
        """
        Creates a new {@link DWARFRegisterMappings} from the data present in the
         xml element.
         <p>
        @param rootElem JDom XML element containing the &lt;dwarf&gt; root
                    element of the mapping file.
        @param lang The Ghidra {@link Language} that the DWARF register mapping
                    applies to
        @return a new {@link DWARFRegisterMappings} instance, never null.
        @throws IOException if missing or invalid data found in xml
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
