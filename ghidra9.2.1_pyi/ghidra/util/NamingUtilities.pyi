import java.lang


class NamingUtilities(object):
    """
    Utility class with static methods for validating project file names.
    """

    MAX_NAME_LENGTH: int = 60







    @staticmethod
    def demangle(mangledName: unicode) -> unicode:
        """
        Performs the inverse of the mangle method.  A string is returned such that
         all characters following a MANGLE_CHAR are converted to uppercase.  Two MANGLE
         chars in a row are replace by a single MANGLE_CHAR.
        @param mangledName mangled name string
        @return demangle name
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def findInvalidChar(name: unicode) -> int:
        """
        Find the invalid character in the given name.
         <p>
         This method should only be used with {@link #isValidName(String)}} and <b>not</b>
         {@link #isValidProjectName(String)}
        @param name the name with an invalid character
        @return the invalid character or 0 if no invalid character can be found
        @see #isValidName(String)
        @deprecated this method may be removed in a subsequent release due to
         limited use and applicability (project names and project file names have
         different naming restrictions).
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isValidMangledName(name: unicode) -> bool:
        """
        Performs a validity check on a mangled name
        @param name mangled name
        @return true if name can be demangled else false
        """
        ...

    @staticmethod
    def isValidName(name: unicode) -> bool:
        """
        Tests whether the given string is a valid.
         Rules:
         <ul>
         <li>All characters must be a letter, digit (0..9), period, hyphen, underscore or space</li>
         <li>May not exceed a length of 60 characters</li>
         </ul>
        @param name name to validate
        @return true if specified name is valid, else false
        @deprecated method has been deprecated due to improper and widespread use.
         New methods include {@link NamingUtilities#isValidProjectName(String)} and
         {@link LocalFileSystem#testValidName(String,boolean)}.
        """
        ...

    @staticmethod
    def isValidProjectName(name: unicode) -> bool:
        """
        Tests whether the given string is a valid project name.
         Rules:
         <ul>
         <li>Name may not start with period</li>
         <li>All characters must be a letter, digit (0..9), period, hyphen, underscore or space</li>
         <li>May not exceed a length of 60 characters</li>
         </ul>
        @param name name to validate
        @return true if specified name is valid, else false
        """
        ...

    @staticmethod
    def mangle(name: unicode) -> unicode:
        """
        Returns a string such that all uppercase characters in the given string are
         replaced by the MANGLE_CHAR followed by the lowercase version of the character.
         MANGLE_CHARs are replaced by 2 MANGLE_CHARs.

         This method is to get around the STUPID windows problem where filenames are
         not case sensitive.  Under Windows, Foo.exe and foo.exe represent
         the same filename.  To fix this we mangle names first such that Foo.exe becomes
         _foo.exe.
        @param name name string to be mangled
        @return mangled name
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
