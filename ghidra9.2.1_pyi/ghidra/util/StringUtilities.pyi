from typing import List
import ghidra.util
import java.lang


class StringUtilities(object):
    """
    Class with static methods that deal with string manipulation.
    """

    DEFAULT_TAB_SIZE: int = 8
    DOUBLE_QUOTED_STRING_PATTERN: java.util.regex.Pattern = ^"((?:[^\\"]|\\.)*)"$
    LINE_SEPARATOR: unicode = u'\n'
    UNICODE_BE_BYTE_ORDER_MARK: int = 65279
    UNICODE_LE16_BYTE_ORDER_MARK: int = 65534
    UNICODE_LE32_BYTE_ORDER_MARK: int = -131072
    UNICODE_REPLACEMENT: int = 65533







    @staticmethod
    def characterToString(c: int) -> unicode:
        """
        Converts the character into a string.
         If the character is special, it will actually render the character.
         For example, given '\n' the output would be "\\n".
        @param c the character to convert into a string
        @return the converted character
        """
        ...

    @staticmethod
    def containsAll(toSearch: java.lang.CharSequence, searches: List[java.lang.CharSequence]) -> bool:
        """
        Returns true if all the given <code>searches</code> are contained in the given string.
        @param toSearch the string to search
        @param searches the strings to find
        @return true if all the given <code>searches</code> are contained in the given string.
        """
        ...

    @staticmethod
    def containsAllIgnoreCase(toSearch: java.lang.CharSequence, searches: List[java.lang.CharSequence]) -> bool:
        """
        Returns true if all the given <code>searches</code> are contained in the given string,
         ignoring case.
        @param toSearch the string to search
        @param searches the strings to find
        @return true if all the given <code>searches</code> are contained in the given string.
        """
        ...

    @staticmethod
    def containsAnyIgnoreCase(toSearch: java.lang.CharSequence, searches: List[java.lang.CharSequence]) -> bool:
        """
        Returns true if any of the given <code>searches</code> are contained in the given string,
         ignoring case.
        @param toSearch the string to search
        @param searches the strings to find
        @return true if any of the given <code>searches</code> are contained in the given string.
        """
        ...

    @staticmethod
    def convertCodePointToEscapeSequence(codePoint: int) -> unicode:
        """
        Maps known control characters to corresponding escape sequences.  For example
         a line feed character would be converted to backslash '\\' character
         followed by an 'n' character.  One use for this is to display strings in a manner to
         easily see the embedded control characters.
        @param codePoint The character to convert to escape sequence string
        @return a new string with equivalent to escape sequence, or original character (as
         a string) if not in the control character mapping.
        """
        ...

    @staticmethod
    def convertControlCharsToEscapeSequences(str: unicode) -> unicode:
        """
        Replaces known control characters in a string to corresponding escape sequences.  For example
         a string containing a line feed character would be converted to backslash character
         followed by an 'n' character.  One use for this is to display strings in a manner to
         easily see the embedded control characters.

         The string that contains 'a','b','c',0x0a,'d', 0x01, 'e'  would become
         'a','b','c', '\', 'n', 'd', 0x01, 'e'
        @param str The string to convert control characters to escape sequences
        @return a new string with all the control characters converted to escape sequences.
        """
        ...

    @staticmethod
    def convertEscapeSequences(str: unicode) -> unicode:
        """
        Replaces escaped characters in a string to corresponding control characters.  For example
         a string containing a backslash character followed by a 'n' character would be replaced
         with a single line feed (0x0a) character.  One use for this is to to allow users to
         type strings in a text field and include control characters such as line feeds and tabs.

         The string that contains 'a','b','c', '\', 'n', 'd', '\', 'u', '0', '0', '0', '1', 'e'  would become
           'a','b','c',0x0a,'d', 0x01, e"
        @param str The string to convert escape sequences to control characters.
        @return a new string with escape sequences converted to control characters.
        @see #convertEscapeSequences(String string)
        """
        ...

    @overload
    @staticmethod
    def convertTabsToSpaces(str: unicode) -> unicode:
        """
        Convert tabs in the given string to spaces using
         a default tab width of 8 spaces.
        @param str string containing tabs
        @return string that has spaces for tabs
        """
        ...

    @overload
    @staticmethod
    def convertTabsToSpaces(str: unicode, tabSize: int) -> unicode:
        """
        Convert tabs in the given string to spaces.
        @param str string containing tabs
        @param tabSize length of the tab
        @return string that has spaces for tabs
        """
        ...

    @staticmethod
    def countOccurrences(string: unicode, occur: int) -> int:
        """
        Returns a count of how many times the 'occur' char appears in the strings.
        @param string the string to look inside
        @param occur the character to look for/
        @return a count of how many times the 'occur' char appears in the strings
        """
        ...

    @staticmethod
    def endsWithIgnoreCase(string: unicode, postfix: unicode) -> bool:
        """
        Returns true if the given string ends with <code>postfix</code>, ignoring case.
         <p>
         Note: This method is equivalent to calling:
         <pre>
          int startIndex = string.length() - postfix.length();
         	string.regionMatches( true, startOffset, postfix, 0, postfix.length() );
         </pre>
        @param string the string which may end with <code>postfix</code>
        @param postfix the string for which to test existence
        @return true if the given string ends with <code>postfix</code>, ignoring case.
        """
        ...

    @staticmethod
    def endsWithWhiteSpace(string: unicode) -> bool: ...

    @overload
    def equals(self, __a0: object) -> bool: ...

    @overload
    @staticmethod
    def equals(s1: unicode, s2: unicode, caseSensitive: bool) -> bool: ...

    @staticmethod
    def extractFromDoubleQuotes(str: unicode) -> unicode:
        """
        If the given string is enclosed in double quotes, extract the inner text.
         Otherwise, return the given string unmodified.
        @param str String to match and extract from
        @return The inner text of a doubly-quoted string, or the original string if not
         double-quoted.
        """
        ...

    @staticmethod
    def findLastWordPosition(s: unicode) -> int:
        """
        Finds the starting position of the last word in the given string.
        @param s the string to search
        @return int the starting position of the last word, -1 if not found
        """
        ...

    @overload
    @staticmethod
    def findWord(s: unicode, index: int) -> unicode:
        """
        Finds the word at the given index in the given string. For example, the
         string "The tree is green" and the index of 5, the result would be
         "tree".
        @param s the string to search
        @param index the index into the string to "seed" the word.
        @return String the word contained at the given index.
        """
        ...

    @overload
    @staticmethod
    def findWord(s: unicode, index: int, charsToAllow: List[int]) -> unicode:
        """
        Finds the word at the given index in the given string; if the word
         contains the given charToAllow, then allow it in the string. For example,
         the string "The tree* is green" and the index of 5, charToAllow is '*',
         then the result would be "tree*".
         <p>
         If the search yields only whitespace, then the empty string will be returned.
        @param s the string to search
        @param index the index into the string to "seed" the word.
        @param charsToAllow chars that normally would be considered invalid, e.g., '*' so
                that the word can be returned with the charToAllow
        @return String the word contained at the given index.
        """
        ...

    @staticmethod
    def findWordLocation(s: unicode, index: int, charsToAllow: List[int]) -> ghidra.util.WordLocation: ...

    @staticmethod
    def fixMultipleAsterisks(value: unicode) -> unicode:
        """
        This method looks for all occurrences of successive asterisks (i.e.,
         "**") and replace with a single asterisk, which is an equivalent usage in
         Ghidra. This is necessary due to some symbol names which cause the
         pattern matching process to become unusable. An example string that
         causes this problem is
         "s_CLSID\{ADB880A6-D8FF-11CF-9377-00AA003B7A11}\InprocServer3_01001400".
        @param value The string to be checked.
        @return The updated string.
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    @staticmethod
    def getLastWord(s: unicode, separator: unicode) -> unicode:
        """
        Takes a path-like string and retrieves the last non-empty item.  Examples:
         <ul>
         		<li>StringUtilities.getLastWord("/This/is/my/last/word/", "/") returns word</li>
         		<li>StringUtilities.getLastWord("/This/is/my/last/word/", "/") returns word</li>
         		<li>StringUtilities.getLastWord("This.is.my.last.word", ".") returns word</li>
         		<li>StringUtilities.getLastWord("/This/is/my/last/word/MyFile.java", ".") returns java</li>
         		<li>StringUtilities.getLastWord("/This/is/my/last/word/MyFile.java", "/") returns MyFile.java</li>
         </ul>
        @param s the string from which to get the last word
        @param separator the separator of words
        @return the last word
        """
        ...

    def hashCode(self) -> int: ...

    @staticmethod
    def indentLines(s: unicode, indent: unicode) -> unicode:
        """
        Splits the given string into lines using <code>\n</code> and then pads each string
         with the given pad string.  Finally, the updated lines are formed into a single string.
         <p>
         This is useful for constructing complicated <code>toString()</code> representations.
        @param s the input string
        @param indent the indent string; this will be appended as needed
        @return the output string
        """
        ...

    @staticmethod
    def indexOfWord(text: unicode, searchWord: unicode) -> int:
        """
        Returns the index of the first whole word occurrence of the search word within
         the given text.  A whole word is defined as the character before and after the occurrence
         must not be a JavaIdentifierPart.
        @param text the text to be searched.
        @param searchWord the word to search for.
        @return the index of the first whole word occurrence of the search word within
         the given text, or -1 if not found.
        """
        ...

    @staticmethod
    def isAllBlank(sequences: List[java.lang.CharSequence]) -> bool:
        """
        Returns true if all the given sequences are either null or only whitespace
        @param sequences the sequences to check
        @return true if all the given sequences are either null or only whitespace.
        @see StringUtils#isNoneBlank(CharSequence...)
        @see StringUtils#isNoneEmpty(CharSequence...)
        @see StringUtils#isAnyBlank(CharSequence...)
        @see StringUtils#isAnyEmpty(CharSequence...)
        """
        ...

    @overload
    @staticmethod
    def isAsciiChar(c: int) -> bool:
        """
        Returns true if the given character is within the ascii range.
        @param c the char to check
        @return true if the given character is within the ascii range.
        """
        ...

    @overload
    @staticmethod
    def isAsciiChar(c: int) -> bool:
        """
        Returns true if the given character is within the ascii range.
        @param c the char to check
        @return true if the given character is within the ascii range.
        """
        ...

    @overload
    @staticmethod
    def isControlCharacterOrBackslash(c: int) -> bool:
        """
        Returns true if the given character is a special character.
         For example a '\n' or '\\'.  A value of 0 is not considered special for this purpose
         as it is handled separately because it has more varied use cases.
        @param c the character
        @return true if the given character is a special character
        """
        ...

    @overload
    @staticmethod
    def isControlCharacterOrBackslash(c: int) -> bool:
        """
        Returns true if the given character is a special character.
         For example a '\n' or '\\'.  A value of 0 is not considered special for this purpose
         as it is handled separately because it has more varied use cases.
        @param c the character
        @return true if the given character is a special character
        """
        ...

    @staticmethod
    def isDisplayable(c: int) -> bool:
        """
        Returns true if the character is in displayable character range
        @param c the character
        @return true if the character is in displayable character range
        """
        ...

    @staticmethod
    def isDoubleQuoted(str: unicode) -> bool:
        """
        Determines if a string is enclosed in double quotes (ASCII 34 (0x22))
        @param str String to test for double-quote enclosure
        @return True if the first and last characters are the double-quote character,
         false otherwise
        """
        ...

    @staticmethod
    def isValidCLanguageChar(c: int) -> bool:
        """
        Returns true if the character is OK to be contained inside C language string. That
         is, the string should not be tokenized on this char.
        @param c the char
        @return boolean true if it is allows in a C string
        """
        ...

    @staticmethod
    def isWholeWord(text: unicode, startIndex: int, length: int) -> bool:
        """
        Returns true if the substring within the text string starting at startIndex and having
         the given length is a whole word. A whole word is defined as the character before and after
         the occurrence must not be a JavaIdentifierPart.
        @param text the text containing the potential word.
        @param startIndex the start index of the potential word within the text.
        @param length the length of the potential word
        @return true if the substring within the text string starting at startIndex and having
         the given length is a whole word.
        """
        ...

    @staticmethod
    def isWordChar(c: int, charsToAllow: List[int]) -> bool:
        """
        Loosely defined as a character that we would expected to be an normal ascii content meant
         for consumption by a human.  Also, provided allows chars will pass the test.
        @param c the char to check
        @param charsToAllow characters that will cause this method to return true
        @return true if it is a 'word char'
        """
        ...

    @staticmethod
    def mergeStrings(string1: unicode, string2: unicode) -> unicode:
        """
        Merge two strings into one.
         If one string contains the other, then the largest is returned.
         If both strings are null then null is returned.
         If both strings are empty, the empty string is returned.
         If the original two strings differ, this adds the second string
         to the first separated by a newline.
        @param string1 the first string
        @param string2 the second string
        @return the merged string
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def pad(source: unicode, filler: int, length: int) -> unicode:
        """
        Pads the source string to the specified length, using the filler string
         as the pad. If length is negative, left justifies the string, appending
         the filler; if length is positive, right justifies the source string.
        @param source the original string to pad.
        @param filler the type of characters with which to pad
        @param length the length of padding to add (0 results in no changes)
        @return the padded string
        """
        ...

    @staticmethod
    def startsWithIgnoreCase(string: unicode, prefix: unicode) -> bool:
        """
        Returns true if the given string starts with <code>prefix</code> ignoring case.
         <p>
         Note: This method is equivalent to calling:
         <pre>
         	string.regionMatches( true, 0, prefix, 0, prefix.length() );
         </pre>
        @param string the string which may contain the prefix
        @param prefix the prefix to test against
        @return true if the given string starts with <code>prefix</code> ignoring case.
        """
        ...

    @staticmethod
    def toFixedSize(s: unicode, pad: int, size: int) -> unicode:
        """
        Enforces the given length upon the given string by trimming and then padding as
         necessary.
        @param s the String to fix
        @param pad the pad character to use if padding is required
        @param size the desired size of the string
        @return the fixed string
        """
        ...

    @overload
    @staticmethod
    def toLines(str: unicode) -> List[unicode]:
        """
        Parses a string containing multiple lines into an array where each
         element in the array contains only a single line. The "\n" character is
         used as the delimiter for lines.
         <p>
         This methods creates an empty string entry in the result array for initial and trailing
         separator chars, as well as for consecutive separators.
        @param str the string to parse
        @return an array of lines; an empty array if the given value is null or empty
        @see StringUtils#splitPreserveAllTokens(String, char)
        """
        ...

    @overload
    @staticmethod
    def toLines(s: unicode, preserveTokens: bool) -> List[unicode]:
        """
        Parses a string containing multiple lines into an array where each
         element in the array contains only a single line. The "\n" character is
         used as the delimiter for lines.
        @param s the string to parse
        @param preserveTokens true signals to treat consecutive newlines as multiple lines; false
                signals to treat consecutive newlines as a single line break
        @return an array of lines; an empty array if the given value is null or empty
        """
        ...

    @overload
    @staticmethod
    def toQuotedString(bytes: List[int]) -> unicode:
        """
        Generate a quoted string from US-ASCII character bytes assuming 1-byte chars.
         <p>
         Special characters and non-printable characters will be escaped using C character escape
         conventions (e.g., \t, \n, \\uHHHH, etc.).  If a character size other than 1-byte is
         required the alternate form of this method should be used.
         <p>
         The result string will be single quoted (ie. "'") if the input byte array is
         1 byte long, otherwise the result will be double-quoted ('"').
        @param bytes character string bytes
        @return escaped string for display use
        """
        ...

    @overload
    @staticmethod
    def toQuotedString(bytes: List[int], charSize: int) -> unicode:
        """
        Generate a quoted string from US-ASCII characters, where each character is charSize bytes.
         <p>
         Special characters and non-printable characters will be escaped using C character escape
         conventions (e.g., \t, \n, \\uHHHH, etc.).
         <p>
         The result string will be single quoted (ie. "'") if the input byte array is
         1 character long (ie. charSize), otherwise the result will be double-quoted ('"').
        @param bytes array of bytes
        @param charSize number of bytes per character (1, 2, 4).
        @return escaped string for display use
        """
        ...

    @staticmethod
    def toStingJson(o: object) -> unicode:
        """
        Creates a JSON string for the given object using all of its fields.  To control the
         fields that are in the result string, see {@link Json}.

         <P>This is here as a marker to point users to the real {@link Json} String utility.
        @param o the object for which to create a string
        @return the string
        """
        ...

    @overload
    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def toString(value: int) -> unicode:
        """
        Converts an integer into a string.
         For example, given an integer 0x41424344,
         the returned string would be "ABCD".
        @param value the integer value
        @return the converted string
        """
        ...

    @staticmethod
    def toStringWithIndent(o: object) -> unicode: ...

    @staticmethod
    def trim(original: unicode, max: int) -> unicode:
        """
        Limits the given string to the given <code>max</code> number of characters.  If the string is
         larger than the given length, then it will be trimmed to fit that length <b>after adding
         ellipses</b>

         <p>The given <code>max</code> value must be at least 4.  This is to ensure that, at a
         minimum, we can display the {@value #ELLIPSES} plus one character.
        @param original The string to be limited
        @param max The maximum number of characters to display (including ellipses, if trimmed).
        @return the trimmed string
        @throws IllegalArgumentException If the given <code>max</code> value is less than 5.
        """
        ...

    @staticmethod
    def trimMiddle(s: unicode, max: int) -> unicode:
        """
        Trims the given string the <code>max</code> number of characters.  Ellipses will be
         added to signal that content was removed.  Thus, the actual number of removed characters
         will be <code>(s.length() - max) + {@value StringUtilities#ELLIPSES}</code> length.

         <p>If the string fits within the max, then the string will be returned.

         <p>The given <code>max</code> value must be at least 5.  This is to ensure that, at a
         minimum, we can display the {@value #ELLIPSES} plus one character from the front and
         back of the string.
        @param s the string to trim
        @param max the max number of characters to allow.
        @return the trimmed string
        """
        ...

    @staticmethod
    def trimTrailingNulls(s: unicode) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...
