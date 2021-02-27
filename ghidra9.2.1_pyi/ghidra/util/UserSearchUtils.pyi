import java.lang
import java.util.regex


class UserSearchUtils(object):
    """
    This class converts user inputted strings and creates Patterns from them
     that can be used to create Matcher objects.  Some methods create patterns that
     are meant to be used with Matcher#matches(), while others create patterns
     meant to be used with Matcher#find().  Please see each method javadoc for clarification.

     Note: methods in the class will escape regex characters, which means that normal regex
     queries will not work, but will be instead interpreted as literal string searches.
    """

    NON_GLOB_BACKSLASH_PATTERN: java.util.regex.Pattern = \\(?![\*\?])
    STAR: unicode = u'*'



    def __init__(self): ...



    @staticmethod
    def createContainsPattern(input: unicode, allowGlobbing: bool, options: int) -> java.util.regex.Pattern:
        """
        Creates a regular expression Pattern that will <b>match</b>
         all strings that <b>contain</b> the given input string.
         <p>
         This method should only be used with {@link Matcher#matches()}.
        @param input the string that you want to your matched strings to contain.
        @param allowGlobbing if true, globing characters (* and ?) will converted to regex wildcard patterns;
                  otherwise, they will be escaped and searched as literals.
        @param options any {@link Pattern} options desired.  For example, you can pass
         			{@link Pattern#CASE_INSENSITIVE} to get case insensitivity.
        @return a regular expression Pattern that will <b>match</b>
         all strings that contain the given input string.
        """
        ...

    @staticmethod
    def createEndsWithPattern(input: unicode, allowGlobbing: bool, options: int) -> java.util.regex.Pattern:
        """
        Creates a regular expression Pattern that will <b>match</b>
         all strings that <b>end with</b> the given input string.
         <p>
         This method should only be used with {@link Matcher#matches()}.
         <p>
         The returned regular expression Pattern should be used
         with the "matches" method on a Matcher.  (As opposed to "find").
        @param input the string that you want to your matched strings to end with.
        @param allowGlobbing if true, globing characters (* and ?) will converted to regex wildcard patterns;
                  otherwise, they will be escaped and searched as literals.
        @param options any {@link Pattern} options desired.  For example, you can pass
         			{@link Pattern#CASE_INSENSITIVE} to get case insensitivity.
        @return a regular expression Pattern that will <b>match</b>
         		   	all strings that end with the given input string.
        """
        ...

    @staticmethod
    def createLiteralSearchPattern(text: unicode) -> java.util.regex.Pattern:
        """
        Generate a compiled representation of a regular expression, ignoring regex special
         characters  . The resulting pattern will match the literal text string.
         <p>
         This method can be used with {@link Matcher#matches()} or {@link Matcher#find()}.
         <p>
         This method will <b><u>not</u></b> turn globbing characters into regex characters.
         If you need that, then see the other methods of this class.
        @param text search string
        @return Pattern the compiled regular expression
        @throws java.util.regex.PatternSyntaxException if the input could be compiled
        """
        ...

    @staticmethod
    def createPattern(input: unicode, allowGlobbing: bool, options: int) -> java.util.regex.Pattern:
        """
        Creates a regular expression Pattern that will match all strings that
         <b>match exactly</b> the given input string.
         <p>
         This method can be used with {@link Matcher#matches()} or {@link Matcher#find()}.
         <p>
        @param input the string that you want to your matched strings to exactly match.
        @param allowGlobbing if true, globing characters (* and ?) will converted to regex wildcard patterns;
                  otherwise, they will be escaped and searched as literals.
        @param options any {@link Pattern} options desired.  For example, you can pass
         			{@link Pattern#CASE_INSENSITIVE} to get case insensitivity.
        @return a regular expression Pattern that will <b>match</b>
         			all strings that exactly match with the given input string.
        """
        ...

    @staticmethod
    def createPatternString(input: unicode, allowGlobbing: bool) -> unicode:
        """
        Creates a regular expression that can be used to create a Pattern that will <b>match</b>
         all strings that match the given input string.
         <p>
         This method can be used with {@link Matcher#matches()} or {@link Matcher#find()}.
         <p>
        @param input the string that you want to your matched strings to exactly match.
        @param allowGlobbing if true, globing characters (* and ?) will converted to regex wildcard patterns;
                  otherwise, they will be escaped and searched as literals.
        @return a regular expression Pattern String that will <b>match</b>
         			all strings that exactly match with the given input string.
        """
        ...

    @staticmethod
    def createSearchPattern(input: unicode, caseSensitive: bool) -> java.util.regex.Pattern:
        """
        <b>
         Note: this is the default model of how to let users search for things in Ghidra.  This
         is NOT a tool to allow regex searching, but instead allows users to perform searches while
         using familiar globbing characters such as '*' and '?'.
         </b>
         <p>
         This method can be used with {@link Matcher#matches()} or {@link Matcher#find()}.
         <p>
         Create a regular expression from the given input. <b>Note:</b> the regular expression
         created by this method is not a pure regular expression.  More specifically, many
         regular expression characters passed to this method will be escaped
         (see {@link #escapeAllRegexCharacters(String)}.
         <p>
         Also, globbing characters
         <b><u>will</u></b> be changed from a regular expression meaning to a
         command-line style glob meaning.

         <p>
         <b>Note: </b>This method <b>will</b> escape regular expression
         characters, such as:
         <ul>
         <li>?
         <li>.
         <li>$
         <li>...and many others
         </ul>
         Thus, this method is not meant to <b>accept</b> regular expressions, but
         rather <b>generates</b> regular expressions.
        @param input string to create a regular expression from
        @param caseSensitive true if the regular expression is case sensitive
        @return Pattern the compiled regular expression
        @throws java.util.regex.PatternSyntaxException if the input could be compiled
        """
        ...

    @staticmethod
    def createStartsWithPattern(input: unicode, allowGlobbing: bool, options: int) -> java.util.regex.Pattern:
        """
        Creates a regular expression Pattern that will <b>match</b>
         all strings that <b>start with</b> the given input string.
         <p>
         This method should only be used with {@link Matcher#matches()}.
         <p>
         The returned regular expression Pattern should be used
         with the "matches" method on a Matcher.  (As opposed to "find").
        @param input the string that you want to your matched strings to start with.
        @param allowGlobbing if true, globing characters (* and ?) will converted to regex wildcard patterns;
                  otherwise, they will be escaped and searched as literals.
        @param options any {@link Pattern} options desired.  For example, you can pass
         			{@link Pattern#CASE_INSENSITIVE} to get case insensitivity.
        @return a regular expression Pattern that will <b>match</b>
         		   	all strings that start with the given input string.
        """
        ...

    def equals(self, __a0: object) -> bool: ...

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
