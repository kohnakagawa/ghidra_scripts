import java.awt
import java.lang


class HTMLUtilities(object):
    """
    A helper class providing static methods for formatting text with common HTML tags.

     Many clients use this class to render content as HTML.  Below are a few use cases along
     with the method that should be used for each.


     			Use CaseFunctionDescription



     				A client wishes to display a simple text message (that itself contains no HTML
     				markup) as HTML.  The message may contain newline characters.


     				#toHTML(String)


     				The given text has all newline characters (\n) replaced with BR tags so
     				that the HTML display of the text will visually display multiple lines.  Also,
     				the final text is prepended with HTML so that the Java HTML rendering
     				engine will render the result as HTML.




     				A client wishes to display a simple text message (that itself may or may not
     				contain HTML markup) as HTML.  Further, the client wishes to not only split
     				lines at newline characters, but also wishes to ensure that no line is longer
     				than a specified limit.


     				#toWrappedHTML(String) or #toWrappedHTML(String, int)


     				This text works the same as #toHTML(String) with the addition of
     				line-wrapping text that passes the given cutoff.




     				A client wishes to display a text message with dynamic content, unknown at the
     				time of programming.


     				#toLiteralHTML(String, int)


     				This method works the same as #toWrappedHTML(String), with the addition
     				of 'friendly encoding', or escaping, any embedded HTML content.  The effect of
     				this is that any existing HTML markup is not rendered as HTML, but is displayed
     				as plain text.




     				A client wishes to display, as a tooltip, a text message with
     				dynamic content, unknown at the time of programming.  Tooltips are unique from
     				general HTML in that we want them to share a common line wrapping length.


     				#toLiteralHTMLForTooltip(String)


     				This method works the same as #toLiteralHTML(String, int), with the
     				addition of capping the max text length, as well as setting the line-wrap length
     				to #DEFAULT_MAX_LINE_LENGTH.




     				A client wishes to convert newlines in text into HTML line breaks, without adding
     				HTML tags around the text, which allows them to embed this text into a
     				larger HTML document.


     				#lineWrapWithHTMLLineBreaks(String) or
     				#lineWrapWithHTMLLineBreaks(String, int)


     				This first method will simply convert all newline characters to
     				BR tags.  The second method adds the ability to trigger line-wrapping
     				at the given length as well.



    """

    BLUE: unicode = u'#000099'
    BR: unicode = u'<BR>'
    DARK_CYAN: unicode = u'#009999'
    GRAY: unicode = u'#888888'
    GREEN: unicode = u'#009900'
    HTML: unicode = u'<HTML>'
    HTML_CLOSE: unicode = u'</HTML>'
    HTML_NEW_LINE: unicode
    HTML_SPACE: unicode
    LINK_PLACEHOLDER_CLOSE: unicode = u'<!-- /LINK -->'
    LINK_PLACEHOLDER_OPEN: unicode = u'<!-- LINK __CONTENT__ -->'
    MAROON: unicode = u'#990000'
    OLIVE: unicode = u'#999900'
    ORANGE: unicode = u'#FF9900'
    PINK: unicode = u'#FF9999'
    PRE: unicode = u'<PRE>'
    PRE_CLOSE: unicode = u'</PRE>'
    PURPLE: unicode = u'#990099'
    YELLOW: unicode = u'#FFFF00'



    def __init__(self): ...



    @staticmethod
    def bold(text: unicode) -> unicode:
        """
        Surrounds the specified text with the HTML begin and end tags for bold.
        @param text the original text
        @return the text with the bold HTML tags
        """
        ...

    @staticmethod
    def charNeedsHTMLEscaping(codePoint: int) -> bool:
        """
        Tests a unicode code point (i.e., 32 bit character) to see if it needs to be escaped before
         being added to a HTML document because it is non-printable or a non-standard control
         character
        @param codePoint character to test
        @return boolean true if character should be escaped
        """
        ...

    @overload
    @staticmethod
    def colorString(rgbColor: unicode, value: int) -> unicode:
        """
        Surrounds the indicated numeric value with HTML font coloring tags so that the
         numeric value will display in color within HTML.
        @param rgbColor (eg. "#8c0000") a string indicating the RGB hexadecimal color
        @param value the numeric value to be converted to text and wrapped with color tags.
        @return the string for the HTML colored number
        """
        ...

    @overload
    @staticmethod
    def colorString(rgbColor: unicode, text: unicode) -> unicode:
        """
        Surrounds the indicated text with HTML font coloring tags so that the
         text will display in color within HTML.
        @param rgbColor (eg. "#8c0000") a string indicating the RGB hexadecimal color
        @param text the original text
        @return the string for HTML colored text
        """
        ...

    @overload
    @staticmethod
    def colorString(color: java.awt.Color, text: unicode) -> unicode:
        """
        Surrounds the indicated text with HTML font coloring tags so that the
         text will display in color within HTML.  The given color will be converted to its
         hex value.
        @param color The Java color object to use
        @param text the original text
        @return the string for HTML colored text
        """
        ...

    @staticmethod
    def convertLinkPlaceholdersToHyperlinks(text: unicode) -> unicode:
        """
        Takes HTML text wrapped by {@link #wrapWithLinkPlaceholder(String, String)} and replaces
         the custom link comment tags with HTML anchor (<code>A</code>) tags, where the <code>HREF</code>
         value is the value that was in the <code>CONTENT</code> attribute.
        @param text the text for which to replace the markup
        @return the updated text
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    @staticmethod
    def escapeHTML(text: unicode) -> unicode:
        """
        Escapes any HTML special characters in the specified text.
         <p>
         Does not otherwise modify the input text or wrap lines.
         <p>
         Calling this twice will result in text being double-escaped, which will not display correctly.
         <p>
         See also <code>StringEscapeUtils#escapeHtml3(String)</code> if you need quote-safe html encoding.
         <p>
        @param text plain-text that might have some characters that should NOT be interpreted as HTML
        @return string with any html characters replaced with equivalents
        """
        ...

    @staticmethod
    def friendlyEncodeHTML(text: unicode) -> unicode:
        """
        Converts any special or reserved characters in the specified string into HTML-escaped
         entities.  Use this method when you have content containing HTML that you do not want
         interpreted as HTML, such as when displaying text that uses angle brackets around words.

         <P>For example, consider the following<br><br>

         <table border=1><caption></caption>
         		<tr>
         			<th>Input</th><th>Output</th><th>Rendered as</th><th>(Without Friendly Encoding)</th>
         		</tr>
         		<tr>
         			<td>
         				Hi &lt;b&gt;mom &lt;/b&gt;
         			</td>
         			<td>
         				Hi<span style="color:green">
          &#x26;nbsp;<b>&#x26;lt;</b></span>b<span style="color:green"><b>&#x26;gt;</b></span>mom
          <span style="color:green">&#x26;nbsp;<b>&#x26;lt;</b></span>/b<span style="color:green"><b>&#x26;gt;</b>
          </span>
         			</td>
         			<td>
         				Hi &lt;b&gt;mom &lt;/b&gt;
         			</td>
         			<td>
         				Hi <b>mom </b>
         			</td>
         		</tr>
         </table>

          <br><br><br>
        @param text string to be encoded
        @return the encoded HTML string
        """
        ...

    @staticmethod
    def fromHTML(text: unicode) -> unicode:
        """
        Checks the given string to see it is HTML, according to {@link BasicHTML} and then
         will return the text without any markup tags if it is.
        @param text the text to convert
        @return the converted String
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def hashCode(self) -> int: ...

    @staticmethod
    def isHTML(text: unicode) -> bool:
        """
        Returns true if the given text is HTML.  For this to be true, the text must begin with
         the &lt;HTML&gt; tag.
        @param text the text to check
        @return true if the given text is HTML
        """
        ...

    @staticmethod
    def italic(text: unicode) -> unicode:
        """
        Surrounds the specified text with the HTML begin and end tags for italic.
        @param text the original text
        @return the text with the italic HTML tags
        """
        ...

    @overload
    @staticmethod
    def lineWrapWithHTMLLineBreaks(text: unicode) -> unicode:
        """
        This is just a convenience call to {@link #lineWrapWithHTMLLineBreaks(String, int)} with
         a max line length of 0, which signals to not to wrap on line length, but only on
         newline characters.
        @param text the text to wrap
        @return the updated text
        @see #lineWrapWithHTMLLineBreaks(String, int)
        """
        ...

    @overload
    @staticmethod
    def lineWrapWithHTMLLineBreaks(text: unicode, maxLineLength: int) -> unicode:
        """
        Replaces all newline characters with HTML &lt;BR&gt; tags.

         <P>Unlike {@link #toWrappedHTML(String)}, this method does <B>not</B> add the
         &lt;HTML&gt; tag to the given text.

         <P>Call this method when you wish to create your own HTML content, with parts of that
         content line wrapped.
        @param text the text to wrap
        @param maxLineLength the max length of the line; 0 if no max is desired
        @return the updated text
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    @staticmethod
    def setFont(text: unicode, color: java.awt.Color, ptSize: int) -> unicode:
        """
        Sets the font size and color of the given text by wrapping it in &lt;font&gt; tags.
        @param text the text to size
        @param color the color of the text
        @param ptSize the point size of the text
        @return the updated String
        """
        ...

    @staticmethod
    def setFontSize(text: unicode, ptSize: int) -> unicode:
        """
        Sets the font size of the given text by wrapping it in &lt;font&gt; tags.
        @param text the text to size
        @param ptSize the point size of the text
        @return the updated String
        """
        ...

    @staticmethod
    def spaces(num: int) -> unicode:
        """
        Creates a string with the indicated number of HTML space characters (<code>&#x26;nbsp;</code>).
        @param num the number of HTML spaces
        @return the string o HTML spaces
        """
        ...

    @staticmethod
    def toHTML(text: unicode) -> unicode:
        """
        Convert the given string to HTML by adding the HTML tag and
         replacing new line chars with HTML &lt;BR&gt; tags.
        @param text The text to convert to HTML
        @return the converted text
        """
        ...

    @staticmethod
    def toHexString(color: java.awt.Color) -> unicode:
        """
        Returns a color string of the format #RRGGBB.  As an example, {@link Color#RED} would be
         returned as #FF0000 (the values are padded with 0s to make to fill up 2 digits per
         component).
        @param color The color to convert.
        @return a string of the format #RRGGBB.
        """
        ...

    @staticmethod
    def toLiteralHTML(text: unicode, maxLineLength: int) -> unicode:
        """
        A convenience method to split the given HTML into lines, based on the given length, and
         then to {@link #friendlyEncodeHTML(String)} the text.

         <P>This method preserves all whitespace between line breaks.

         <P><B>Note: </B>This method is not intended to handle text that already contains
         entity escaped text.  The result will not render correctly as HTML.
        @param text the text to update
        @param maxLineLength the max line length upon which to wrap; 0 for no max length
        @return the updated text
        """
        ...

    @staticmethod
    def toLiteralHTMLForTooltip(text: unicode) -> unicode:
        """
        A very specific method that will:
         <ol>
         	<li>
         	Make sure the HTML length is clipped to a reasonable size
          </li>
          <li>
          <b>Escape any embedded HTML</b> (so that it is not interpreted as HTML)
          </li>
          <li>
          Put the entire result in HTML
          </li>
         </ol>
        @param text the text to convert
        @return the converted value.
        """
        ...

    @staticmethod
    def toRGBString(color: java.awt.Color) -> unicode:
        """
        Returns a color string of the format rrrgggbbb.  As an example, {@link Color#RED} would be
         returned as 255000000 (the values are padded with 0s to make to fill up 3 digits per
         component).
        @param color The color to convert.
        @return a string of the format rrrgggbbb.
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    @staticmethod
    def toWrappedHTML(text: unicode) -> unicode:
        """
        This is just a convenience method to call {@link #toWrappedHTML(String, int)} with a
         max line length of {@value #DEFAULT_MAX_LINE_LENGTH}.
        @param text The text to convert
        @return converted text
        """
        ...

    @overload
    @staticmethod
    def toWrappedHTML(text: unicode, maxLineLength: int) -> unicode:
        """
        Similar to {@link #toHTML(String)} in that it will wrap the given text in
         HTML tags and split the content into multiple lines.  The difference is that this method
         will split lines that pass the given maximum length <b>and</b> on <code>'\n'</code>
         characters.  Alternatively, {@link #toHTML(String)} will only split the given
         text on <code>'\n'</code> characters.
        @param text The text to convert
        @param maxLineLength The maximum number of characters that should appear in a line;
         		  0 signals not to wrap the line based upon length
        @return converted text
        """
        ...

    @staticmethod
    def underline(text: unicode) -> unicode:
        """
        Surrounds the specified text with the HTML begin and end tags for underlined text.
        @param text the original text
        @return the text with the underline HTML tags
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @staticmethod
    def wrapAsHTML(text: unicode) -> unicode:
        """
        Marks the given text as HTML in order to be rendered thusly by Java widgets.
        @param text the original text
        @return the text marked as HTML
        """
        ...

    @staticmethod
    def wrapWithLinkPlaceholder(htmlText: unicode, content: unicode) -> unicode:
        """
        Returns the given text wrapped in {@link #LINK_PLACEHOLDER_OPEN} and close tags.
         If <code>foo</code> is passed for the HTML text, with a content value of <code>123456</code>, then
         the output will look like:
         <pre>
         	&lt;!-- LINK CONTENT="123456" --&gt;foo&lt;!-- /LINK --&gt;
         </pre>
        @param htmlText the HTML text to wrap
        @param content the value that will be put into the <code>CONTENT</code> section of the
         		  generated HTML.  This can later be retrieved by clients transforming this text.
        @return the wrapped text
        """
        ...
