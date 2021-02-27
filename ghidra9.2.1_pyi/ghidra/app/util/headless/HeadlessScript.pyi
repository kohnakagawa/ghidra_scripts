from typing import List
import generic.jar
import ghidra.app.script
import ghidra.app.script.GhidraScript
import ghidra.app.tablechooser
import ghidra.app.util.headless
import ghidra.app.util.headless.HeadlessScript
import ghidra.framework.cmd
import ghidra.framework.model
import ghidra.program.model.address
import ghidra.program.model.data
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.program.model.mem
import ghidra.program.model.symbol
import ghidra.program.util.string
import ghidra.util.task
import java.awt
import java.io
import java.lang
import java.util


class HeadlessScript(ghidra.app.script.GhidraScript):
    """
    This class is analogous to GhidraScript, except that is only meant to be used with
     the HeadlessAnalyzer.  That is, if a user writes a script that extends HeadlessScript,
     it should only be run in the Headless environment.
    """






    class HeadlessContinuationOption(java.lang.Enum):
        ABORT: ghidra.app.util.headless.HeadlessScript.HeadlessContinuationOption = ABORT
        ABORT_AND_DELETE: ghidra.app.util.headless.HeadlessScript.HeadlessContinuationOption = ABORT_AND_DELETE
        CONTINUE: ghidra.app.util.headless.HeadlessScript.HeadlessContinuationOption = CONTINUE
        CONTINUE_THEN_DELETE: ghidra.app.util.headless.HeadlessScript.HeadlessContinuationOption = CONTINUE_THEN_DELETE







        @overload
        def compareTo(self, __a0: java.lang.Enum) -> int: ...

        @overload
        def compareTo(self, __a0: object) -> int: ...

        def equals(self, __a0: object) -> bool: ...

        def getClass(self) -> java.lang.Class: ...

        def getDeclaringClass(self) -> java.lang.Class: ...

        def hashCode(self) -> int: ...

        def name(self) -> unicode: ...

        def notify(self) -> None: ...

        def notifyAll(self) -> None: ...

        def ordinal(self) -> int: ...

        def toString(self) -> unicode: ...

        @overload
        @staticmethod
        def valueOf(__a0: unicode) -> ghidra.app.util.headless.HeadlessScript.HeadlessContinuationOption: ...

        @overload
        @staticmethod
        def valueOf(__a0: java.lang.Class, __a1: unicode) -> java.lang.Enum: ...

        @staticmethod
        def values() -> List[ghidra.app.util.headless.HeadlessScript.HeadlessContinuationOption]: ...

        @overload
        def wait(self) -> None: ...

        @overload
        def wait(self, __a0: long) -> None: ...

        @overload
        def wait(self, __a0: long, __a1: int) -> None: ...



    def __init__(self): ...



    def addEntryPoint(self, address: ghidra.program.model.address.Address) -> None:
        """
        Adds an entry point at the specified address.
        @param address address to create entry point
        """
        ...

    def addInstructionXref(self, from_: ghidra.program.model.address.Address, to: ghidra.program.model.address.Address, opIndex: int, type: ghidra.program.model.symbol.FlowType) -> ghidra.program.model.symbol.Reference:
        """
        Adds a cross reference (XREF).
        @param from the source address of the reference
        @param to the destination address of the reference
        @param opIndex the operand index (-1 indicates the mnemonic)
        @param type the flow type
        @return the newly created reference
        @see ghidra.program.model.symbol.FlowType
        @see ghidra.program.model.symbol.Reference
        """
        ...

    def analysisTimeoutOccurred(self) -> bool:
        """
        Returns whether analysis for the current program has timed out.
         <p>
         Analysis will time out only in the case where:
         <ol>
         		<li>the users has set an analysis timeout period using the <code>-analysisTimeoutPerFile</code>
         	parameter</li>
         		<li>analysis is enabled and has completed</li>
         		<li>the current script is being run as a postScript (since postScripts run after
         analysis)</li>
         </ol>
        @return whether analysis timeout occurred
        @throws ImproperUseException if not in headless mode or headless instance not set
        """
        ...

    def analyze(self, program: ghidra.program.model.listing.Program) -> None:
        """
        Starts auto-analysis on the specified program and performs complete analysis
         of the entire program.  This is usually only necessary if full analysis was never
         performed. This method will block until analysis completes.
        @param program the program to analyze
        @deprecated the method {@link #analyzeAll} or {@link #analyzeChanges} should be invoked.
         These separate methods were created to clarify their true behavior since many times it is
         only necessary to analyze changes and not the entire program which can take much
         longer and affect more of the program than is necessary.
        """
        ...

    def analyzeAll(self, program: ghidra.program.model.listing.Program) -> None: ...

    def analyzeChanges(self, program: ghidra.program.model.listing.Program) -> None: ...

    def askAddress(self, title: unicode, message: unicode) -> ghidra.program.model.address.Address:
        """
        Returns an Address, using the String parameters for guidance.  The actual behavior of the
         method depends on your environment, which can be GUI or headless.
         <p>
         Regardless of environment -- if script arguments have been set, this method will use the
         next argument in the array and advance the array index so the next call to an ask method
         will get the next argument.  If there are no script arguments and a .properties file
         sharing the same base name as the Ghidra Script exists (i.e., Script1.properties for
         Script1.java), then this method will then look there for the String value to return.
         The method will look in the .properties file by searching for a property name that is a
         space-separated concatenation of the input String parameters (title + " " + message).
         If that property name exists and its value represents a valid Address value, then the
         .properties value will be used in the following way:
         <ol>
         		<li>In the GUI environment, this method displays a popup dialog that prompts the user
         			for an address value. If the same popup has been run before in the same session,
         			the address input field will be pre-populated with the last-used address. If not,
         			the	address input field will be pre-populated with the .properties value (if it
         			exists).</li>
        		<li>In the headless environment, this method returns an Address representing the
        			.properties value (if it exists), or throws an Exception if there is an invalid or
        			missing .properties value.</li>
         </ol>
        @param title the title of the dialog (in GUI mode) or the first part of the variable name
         			(in headless mode or when using .properties file)
        @param message the message to display next to the input field (in GUI mode) or the
         			second part of the variable name (in headless mode or when using .properties file)
        @return the user-specified Address value
        @throws CancelledException if the user hit the 'cancel' button in GUI mode
        @throws IllegalArgumentException if in headless mode, there was a missing or	invalid Address
         			specified in the .properties file
        """
        ...

    def askBytes(self, title: unicode, message: unicode) -> List[int]:
        """
        Returns a byte array, using the String parameters for guidance. The actual behavior of the
         method depends on your environment, which can be GUI or headless.
         <p>
         Regardless of environment -- if script arguments have been set, this method will use the
         next argument in the array and advance the array index so the next call to an ask method
         will get the next argument.  If there are no script arguments and a .properties file
         sharing the same base name as the Ghidra Script exists (i.e., Script1.properties for
         Script1.java), then this method will then look there for the String value to return.
         The method will look in the .properties file by searching for a property name that is a
         space-separated concatenation of the input String parameters (title + " " + message).
         If that property name exists and its value represents valid bytes, then the
         .properties value will be used in the following way:
         <ol>
         		<li>In the GUI environment, this method displays a popup dialog that prompts the
         			user for a byte pattern. If the same popup has been run before in the same session,
         			the byte pattern input field will be pre-populated with	the last-used bytes string.
         			If not, the byte pattern input field will be pre-populated with the .properties
         			value (if it exists).</li>
        		<li>In the headless environment, this method returns a byte array representing the
        			.properties byte pattern value (if it exists), or throws an Exception if there is
        			an invalid or missing .properties value.</li>
         </ol>
        @param title the title of the dialog (in GUI mode) or the first part of the variable
         			name (in headless mode or when using .properties file)
        @param message the message to display next to the input field (in GUI mode) or the
         			second part of the variable name (in headless mode or when using .properties file)
        @return the user-specified byte array
        @throws CancelledException if the user hit the 'cancel' button in GUI mode
        @throws IllegalArgumentException if in headless mode, there was a missing or invalid bytes
         			string specified in the .properties file
        """
        ...

    def askChoice(self, title: unicode, message: unicode, choices: List[object], defaultValue: object) -> object:
        """
        Returns an object that represents one of the choices in the given list. The actual behavior
         of the method depends on your environment, which can be GUI or headless.
         <p>
         Regardless of environment -- if script arguments have been set, this method will use the
         next argument in the array and advance the array index so the next call to an ask method
         will get the next argument.  If there are no script arguments and a .properties file
         sharing the same base name as the Ghidra Script exists (i.e., Script1.properties for
         Script1.java), then this method will then look there for the String value to return.
         The method will look in the .properties file by searching for a property name that is a
         space-separated concatenation of the input String parameters (title + " " + message).
         If that property name exists and its value represents a valid choice, then the
         .properties value will be used in the following way:
         <ol>
         		<li>In the GUI environment, this method displays a popup dialog that prompts the user
         			to choose from the given list of objects. The pre-chosen choice will be the last
         			user-chosen value (if the dialog has been run before). If that does not exist, the
         			pre-chosen value is the .properties value. If that does not exist or is invalid,
         			then the 'defaultValue' parameter is used (as long as it is not null).</li>
        		<li>In the headless environment, this method returns an object representing the
        			.properties value (if it exists and is a valid choice), or throws an Exception if
        			there is an invalid or missing .properties value.</li>
         </ol>
        @param title the title of the dialog (in GUI mode) or the first part of the variable name
         			(in headless mode or when using .properties file)
        @param message the message to display next to the input field (in GUI mode) or the second
         			part of the variable name (in headless mode or when using .properties file)
        @param choices set of choices (toString() value of each object will be displayed in the dialog)
        @param defaultValue the default value to display in the input field; may be
                             null, but must be a valid choice if non-null.
        @return the user-selected value
        @throws CancelledException if the user hit the 'cancel' button
        @throws IllegalArgumentException if in headless mode, there was a missing or invalid	choice
         			specified in the .properties file
        """
        ...

    @overload
    def askChoices(self, title: unicode, message: unicode, choices: List[object]) -> List[object]:
        """
        Returns an array of Objects representing one or more choices from the given list. The actual
         behavior of the method depends on your environment, which can be GUI or headless.
         <p>
         Regardless of environment -- if script arguments have been set, this method will use the
         next argument in the array and advance the array index so the next call to an ask method
         will get the next argument.  If there are no script arguments and a .properties file
         sharing the same base name as the Ghidra Script exists (i.e., Script1.properties for
         Script1.java), then this method will then look there for the String value to return.
         The method will look in the .properties file by searching for a property name that is a
         space-separated concatenation of the input String parameters (title + " " + message).
         If that property name exists and its value represents valid choices, then the
         .properties value will be used in the following way:
         <ol>
         		<li>In the GUI environment, this method displays a pop-up dialog that presents the user
         		    with checkbox choices (to allow a more flexible option where the user can pick
         			some, all, or none).</li>
         		<li>In the headless environment, if a .properties file sharing the same base name as the
         			Ghidra Script exists (i.e., Script1.properties for Script1.java), then this method
         			looks there for the choices to return. The method will look in the .properties file
         			by searching for a property name equal to a space-separated concatenation of the
         			String parameters (title + " " + message). If that property name exists and
         			represents a list (one or more) of valid choice(s) in the form
         			"choice1;choice2;choice3;..." (&lt;-- note the quotes surrounding the choices), then
         			an Object array of those choices is returned. Otherwise, an Exception is thrown if
         			there is an invalid or missing .properties value.</li>
        </ol>
        @param title the title of the dialog (in GUI mode) or the first part of the variable name
         			(in headless mode or when using .properties file)
        @param message the message to display with the choices (in GUI mode) or the second
         			part of the variable name (in headless mode or when using .properties file)
        @param choices set of choices (toString() value of each object will be displayed in the dialog)
        @return the user-selected value(s); an empty list if no selection was made
        @throws CancelledException if the user hits the 'cancel' button
        @throws IllegalArgumentException if in headless mode, there was a missing or invalid	set of
         			choices specified in the .properties file
        """
        ...

    @overload
    def askChoices(self, __a0: unicode, __a1: unicode, __a2: List[object], __a3: List[object]) -> List[object]: ...

    def askDirectory(self, title: unicode, approveButtonText: unicode) -> java.io.File:
        """
        Returns a directory File object, using the String parameters for guidance. The actual
         behavior of the method depends on your environment, which can be GUI or headless.
         <p>
         Regardless of environment -- if script arguments have been set, this method will use the
         next argument in the array and advance the array index so the next call to an ask method
         will get the next argument.  If there are no script arguments and a .properties file
         sharing the same base name as the Ghidra Script exists (i.e., Script1.properties for
         Script1.java), then this method will then look there for the String value to return.
         The method will look in the .properties file by searching for a property name that is a
         space-separated concatenation of the input String parameters (title + " " + approveButtonText).
         If that property name exists and its value represents a valid <b>absolute path</b> of a valid
         directory File, then the .properties value will be used in the following way:
         <ol>
         		<li>In the GUI environment, this method displays a file chooser dialog that allows the
         			user to select a directory. If the file chooser dialog has been run before in the
         			same session, the directory selection will be pre-populated with the last-selected
         			directory. If not, the directory selection will be pre-populated with the
         			.properties	value (if it exists).</li>
        		<li>In the headless environment, this method returns a directory File representing
        			the .properties value (if it exists), or throws an Exception if there is an invalid
        			or missing .properties value.</li>
         </ol>
        @param title the title of the dialog (in GUI mode) or the first part of the variable name
         			(in headless mode or when using .properties file)
        @param approveButtonText the approve button text (in GUI mode - typically, this would be
         			"Open" or "Save") or the second part of the variable name (in headless mode or
         			when using .properties file)
        @return the selected directory or null if no tool was available
        @throws CancelledException if the user hit the 'cancel' button in GUI mode
        @throws IllegalArgumentException if in headless mode, there was a missing or invalid
         				directory name specified in the .properties file
        """
        ...

    def askDomainFile(self, title: unicode) -> ghidra.framework.model.DomainFile:
        """
        Returns a DomainFile, using the title parameter for guidance.  The actual behavior of the
         method depends on your environment, which can be GUI or headless.
         <p>
         Regardless of environment -- if script arguments have been set, this method will use the
         next argument in the array and advance the array index so the next call to an ask method
         will get the next argument.  If there are no script arguments and a .properties file
         sharing the same base name as the Ghidra Script exists (i.e., Script1.properties for
         Script1.java), then this method will then look there for the String value to return.
         The method will look in the .properties file by searching for a property name that is the
         title String parameter.  If that property name exists and its value represents a valid
         domain file, then the .properties value will be used in the following way:
         <ol>
         		<li>In the GUI environment, this method displays a popup dialog listing all domain files
         			in the current project, allowing the user to select one.</li>
        		<li>In the headless environment, if a .properties file sharing the same base name as the
        			Ghidra Script exists (i.e., Script1.properties for Script1.java), then this method
        			looks there for the name of the DomainFile to return. The method will look in the
        			.properties file by searching for a property name equal to the 'title' parameter. If
        			that property name exists and its value represents a valid DomainFile in the project,
        			then that value is returned. Otherwise, an Exception is thrown if there is an invalid
        			or missing .properties value.</li>
         </ol>
        @param title the title of the pop-up dialog (in GUI mode) or the variable name (in headless
         		mode or when using .properties file)
        @throws IllegalArgumentException if in headless mode, there was a missing or invalid	domain
         			file specified in the .properties file
        @return the user-selected domain file
        @throws CancelledException if the operation is cancelled
        """
        ...

    def askDouble(self, title: unicode, message: unicode) -> float:
        """
        Returns a double, using the String parameters for guidance. The actual behavior of the
         method depends on your environment, which can be GUI or headless.
         <p>
         Regardless of environment -- if script arguments have been set, this method will use the
         next argument in the array and advance the array index so the next call to an ask method
         will get the next argument.  If there are no script arguments and a .properties file
         sharing the same base name as the Ghidra Script exists (i.e., Script1.properties for
         Script1.java), then this method will then look there for the String value to return.
         The method will look in the .properties file by searching for a property name that is a
         space-separated concatenation of the input String parameters (title + " " + message).
         If that property name exists and its value represents a valid double value, then the
         .properties value will be used in the following way:
         <ol>
         		<li>In the GUI environment, this method displays a popup dialog that prompts the user
         			for a double value. If the same popup has been run before in the same session, the
         			double input field will be pre-populated with the last-used double. If not, the
         			double input field will be pre-populated with the .properties value (if it exists).
         		</li>
        		<li>In the headless environment, this method returns a double value representing the
        			.properties value (if it exists), or throws an Exception if there is an	invalid or
        			missing .properties value.</li>
         </ol>
         <p>
         Note that in both headless and GUI modes, you may specify "PI" or "E" and get the
         corresponding floating point value to 15 decimal places.
         <p>
        @param title the title of the dialog (in GUI mode) or the first part of the variable name
         			(in headless mode or when using .properties file)
        @param message the message to display next to the input field (in GUI mode) or the second
         			part of the variable name (in headless mode or when using .properties file)
        @return the user-specified double value
        @throws CancelledException if the user hit the 'cancel' button in GUI mode
        @throws IllegalArgumentException if in headless mode, there was a missing or	invalid double
         			specified in the .properties file
        """
        ...

    def askFile(self, title: unicode, approveButtonText: unicode) -> java.io.File:
        """
        Returns a File object, using the String parameters for guidance.  The actual behavior of the
         method depends on your environment, which can be GUI or headless.
         <p>
         Regardless of environment -- if script arguments have been set, this method will use the
         next argument in the array and advance the array index so the next call to an ask method
         will get the next argument.  If there are no script arguments and a .properties file
         sharing the same base name as the Ghidra Script exists (i.e., Script1.properties for
         Script1.java), then this method will then look there for the String value to return.
         The method will look in the .properties file by searching for a property name that is a
         space-separated concatenation of the input String parameters (title + " " + approveButtonText).
         If that property name exists and its value represents a valid <b>absolute path</b> of a valid
         File, then the .properties value will be used in the following way:
         <ol>
         		<li>In the GUI environment, this method displays a file chooser dialog that allows the
         			user to select a file. If the file chooser dialog has been run before in the same
         			session, the File selection will be pre-populated with the last-selected file. If
         			not, the File selection will be pre-populated with the .properties value (if it
         			exists).
         		</li>
        		<li>In the headless environment, this method returns a File object representing	the
        			.properties	String value (if it exists), or throws an Exception if there is an
        			invalid or missing .properties value.
        		</li>
         </ol>
        @param title the title of the dialog (in GUI mode) or the first part of the variable name
         			(in headless mode or when using using .properties file)
        @param approveButtonText the approve button text (in GUI mode - typically, this would
         		  	be "Open" or "Save") or the second part of the variable name (in headless mode
         			or when using .properties file)
        @return the selected file or null if no tool was available
        @throws CancelledException if the user hit the 'cancel' button in GUI mode
        @throws IllegalArgumentException if in headless mode, there was a missing or invalid file
         			name specified in the .properties file
        """
        ...

    def askInt(self, title: unicode, message: unicode) -> int:
        """
        Returns an int, using the String parameters for guidance.  The actual behavior of the
         method depends on your environment, which can be GUI or headless.
         <p>
         Regardless of environment -- if script arguments have been set, this method will use the
         next argument in the array and advance the array index so the next call to an ask method
         will get the next argument.  If there are no script arguments and a .properties file
         sharing the same base name as the Ghidra Script exists (i.e., Script1.properties for
         Script1.java), then this method will then look there for the String value to return.
         The method will look in the .properties file by searching for a property name that is a
         space-separated concatenation of the input String parameters (title + " " + message).
         If that property name exists and its value represents a valid int value, then the
         .properties value will be used in the following way:
         <ol>
         		<li>In the GUI environment, this method displays a popup dialog that prompts the user
         			for an int value. If the same popup has been run before in the same session, the int
         			input field will be pre-populated with the last-used int. If not, the int input
         			field will be pre-populated with the .properties value (if it exists).
          	</li>
        		<li>In the headless environment, this method returns an int value representing the
        			.properties value (if it exists), or throws an Exception if there is an invalid
        			or missing .properties value.
        		</li>
         </ol>
        @param title the title of the dialog (in GUI mode) or the first part of the variable name
         			(in headless mode or when using .properties file)
        @param message the message to display next to the input field (in GUI mode) or the second
         			part of the variable name (in headless mode or when using .properties file)
        @return the user-specified int value
        @throws CancelledException if the user hit the 'cancel' button in GUI mode
        @throws IllegalArgumentException if in headless mode, there was a missing or invalid int
         			specified in the .properties file
        """
        ...

    def askLanguage(self, title: unicode, approveButtonText: unicode) -> ghidra.program.model.lang.LanguageCompilerSpecPair:
        """
        Returns a LanguageCompilerSpecPair, using the String parameters for guidance. The actual
         behavior of the method depends on your environment, which can be GUI or headless.
         <p>
         Regardless of environment -- if script arguments have been set, this method will use the
         next argument in the array and advance the array index so the next call to an ask method
         will get the next argument.  If there are no script arguments and a .properties file
         sharing the same base name as the Ghidra Script exists (i.e., Script1.properties for
         Script1.java), then this method will then look there for the String value to return.
         The method will look in the .properties file by searching for a property name that is a
         space-separated concatenation of the input String parameters (title + " " + message).
         If that property name exists and its value represents a valid LanguageCompilerSpecPair value,
         then the .properties value will be used in the following way:
         <ol>
         		<li>In the GUI environment, this method displays a language table dialog and returns
         			the selected language. If the same popup has been run before in the same session,
         			the last-used language will be pre-selected. If not, the language specified in the
         			.properties file will be pre-selected (if it exists).</li>
        		<li>In the headless environment, this method returns a LanguageCompilerSpecPair
        			representing the .properties value (if it exists), or throws an Exception if there
        			is an invalid or missing .properties value.</li>
         </ol>
        @param title the title of the dialog (in GUI mode) or the first part of the variable name
         			(in headless mode or when using .properties file)
        @param approveButtonText the approve button text (in GUI mode - typically, this would be
         			"Open" or "Save") or the second part of the variable name (in headless mode or
         			when using .properties file)
        @return the selected LanguageCompilerSpecPair
        @throws CancelledException if the user hit the 'cancel' button
        @throws IllegalArgumentException if in headless mode, there was a missing or invalid	language
         			specified in the .properties file
        """
        ...

    def askLong(self, title: unicode, message: unicode) -> long:
        """
        Returns a long, using the String parameters for guidance.  The actual behavior of the
         method depends on your environment, which can be GUI or headless.
         <p>
         Regardless of environment -- if script arguments have been set, this method will use the
         next argument in the array and advance the array index so the next call to an ask method
         will get the next argument.  If there are no script arguments and a .properties file
         sharing the same base name as the Ghidra Script exists (i.e., Script1.properties for
         Script1.java), then this method will then look there for the String value to return.
         The method will look in the .properties file by searching for a property name that is a
         space-separated concatenation of the input String parameters (title + " " + message).
         If that property name exists and its value represents a valid long value, then the
         .properties value will be used in the following way:
         <ol>
         		<li>In the GUI environment, this method displays a popup dialog that prompts the user
         			for a long value. If the same popup has been run before in the same session, the
         			long input field will be pre-populated with the last-used long. If not, the long
         			input field will be pre-populated with the .properties value (if it exists).
         		</li>
        		<li>In the headless environment, this method returns a long value representing the
        			.properties value (if it exists), or throws an Exception if there is an invalid or
        			missing .properties	value.</li>
         </ol>
        @param title the title of the dialog (in GUI mode) or the first part of the variable name
         			(in headless mode or when using .properties file)
        @param message the message to display next to the input field (in GUI mode) or the second
         			part of the	variable name (in headless mode or when using .properties file)
        @return the user-specified long value
        @throws CancelledException if the user hit the 'cancel' button in GUI mode
        @throws IllegalArgumentException if in headless mode, there was a missing or invalid	long
         			specified in the .properties file
        """
        ...

    def askProgram(self, title: unicode) -> ghidra.program.model.listing.Program:
        """
        Returns a Program, using the title parameter for guidance. The actual behavior of the
         method depends on your environment, which can be GUI or headless.
         <br>
         Regardless of environment -- if script arguments have been set, this method will use the
         next argument in the array and advance the array index so the next call to an ask method
         will get the next argument.  If there are no script arguments and a .properties file
         sharing the same base name as the Ghidra Script exists (i.e., Script1.properties for
         Script1.java), then this method will then look there for the String value to return.
         The method will look in the .properties file by searching for a property name that is the
         title String parameter.  If that property name exists and its value represents a valid
         program, then the .properties value will be used in the following way:
         <ol>
         		<li>In the GUI environment, this method displays a popup dialog that prompts the user
         			to select a program.</li>
        		<li>In the headless environment, if a .properties file sharing the same base name as the
        			Ghidra Script exists (i.e., Script1.properties for Script1.java), then this method
        			looks there for the name of the program to return. The method will look in the
        			.properties file by searching for a property name equal to the 'title' parameter. If
        			that property name exists and its value represents a valid Program in the project,
        			then that value	is returned. Otherwise, an Exception is thrown if there is an
        			invalid or missing .properties value.</li>
         </ol>
        @param title the title of the pop-up dialog (in GUI mode) or the variable name (in
         			headless mode)
        @return the user-specified Program
        @throws VersionException if the Program is out-of-date from the version of GHIDRA
        @throws IOException if there is an error accessing the Program's DomainObject
        @throws CancelledException if the operation is cancelled
        @throws IllegalArgumentException if in headless mode, there was a missing or invalid	program
         			specified in the .properties file
        """
        ...

    def askProjectFolder(self, title: unicode) -> ghidra.framework.model.DomainFolder:
        """
        Returns a DomainFolder object, using the supplied title string for guidance.  The actual
         behavior of the method depends on your environment, which can be GUI or headless.
         <p>
         Regardless of environment -- if script arguments have been set, this method will use the
         next argument in the array and advance the array index so the next call to an ask method
         will get the next argument.  If there are no script arguments and a .properties file
         sharing the same base name as the Ghidra Script exists (i.e., Script1.properties for
         Script1.java), then this method will then look there for the String value to return.
         The method will look in the .properties file by searching for a property name that is the
         title String parameter.  If that property name exists and its value represents a valid
         project folder, then the .properties value will be used in the following way:
         <ol>
         		<li>In the GUI environment, this method displays a file chooser dialog that allows the
         			user to select a project folder. The selected folder will be returned.</li>
        		<li>In the headless environment, if a .properties file sharing the same base name as the
        			Ghidra Script exists (i.e., Script1.properties for Script1.java), then this method
        			looks there for the name of the project folder to return. The method will look in
        			the .properties	file by searching for a property name equal to the 'title' parameter.
        			If that property name exists and its value represents a valid DomainFolder in the
        			project, then that value is returned. Otherwise, an Exception is thrown if there is
        			an invalid or missing .properties value.</li>
         </ol>
        @param title the title of the dialog (GUI) or the variable name	(headless or when
         			using .properties file)
        @return the selected project folder or null if there was an invalid .properties value
        @throws CancelledException if the user hit the 'cancel' button in GUI mode
        @throws IllegalArgumentException if in headless mode, there was a missing or invalid	project
         			folder specified in the .properties file
        """
        ...

    @overload
    def askString(self, title: unicode, message: unicode) -> unicode:
        """
        Returns a String, using the String input parameters for guidance. The actual behavior of
         the method depends on your environment, which can be GUI or headless.
         <p>
         Regardless of environment -- if script arguments have been set, this method will use the
         next argument in the array and advance the array index so the next call to an ask method
         will get the next argument.  If there are no script arguments and a .properties file
         sharing the same base name as the Ghidra Script exists (i.e., Script1.properties for
         Script1.java), then this method will then look there for the String value to return.
         The method will look in the .properties file by searching for a property name that is a
         space-separated concatenation of the input String parameters (title + " " + message).
         If that property name exists and its value represents a valid String value, then the
         .properties value will be used in the following way:
         <ol>
         		<li>In the GUI environment, this method displays a popup dialog that prompts the user
         			for a String value. If the same popup has been run before in the same session, the
         			String input field will be pre-populated with the last-used String. If not, the
         			String input field will be pre-populated with the .properties value (if it exists).
         		</li>
        		<li>In the headless environment, this method returns a String value	representing the
        			.properties value (if it exists), or throws an Exception if there is an invalid or
        			missing .properties value.</li>
         </ol>
        @param title the title of the dialog (in GUI mode) or the first part of the variable	name
         			(in headless mode or when using .properties file)
        @param message the message to display next to the input field (in GUI mode) or the second
         			part of the variable name (in headless mode or when using .properties file)
        @return the user-specified String value
        @throws CancelledException if the user hit the 'cancel' button in GUI mode
        @throws IndexOutOfBoundsException if in headless mode and arguments are being used, but not
                  enough arguments were passed in to accommodate the request.
        @throws IllegalArgumentException if in headless mode, there was an invalid String
         			specified in the arguments, or an invalid or missing String specified in the
                  .properties file
        """
        ...

    @overload
    def askString(self, title: unicode, message: unicode, defaultValue: unicode) -> unicode:
        """
        Returns a String, using the String input parameters for guidance. The actual behavior of the
         method depends on your environment, which can be GUI or headless.
         <p>
         Regardless of environment -- if script arguments have been set, this method will use the
         next argument in the array and advance the array index so the next call to an ask method
         will get the next argument.  If there are no script arguments and a .properties file
         sharing the same base name as the Ghidra Script exists (i.e., Script1.properties for
         Script1.java), then this method will then look there for the String value to return.
         The method will look in the .properties file by searching for a property name that is a
         space-separated concatenation of the input String parameters (title + " " + message).
         If that property name exists and its value represents a valid String value, then the
         .properties value will be used in the following way:
         <ol>
         		<li>In the GUI environment, this method displays a popup dialog that prompts the user
         			for a String value. The pre-populated value for the String input field will be the
         			last-used String (if the dialog has been run before). If that does not exist, the
         			pre-populated value is the .properties value. If that does	not exist or is invalid,
         			then the 'defaultValue' parameter is used (as long as it is not	null or the empty
         			String).</li>
        		<li>In the headless environment, this method returns a String value representing the
        			.properties value (if it exists). Otherwise, if the 'defaultValue' parameter is
        			not null or an empty String, it is returned. In all other cases, an exception
        			is thrown.</li>
         </ol>
        @param title the title of the dialog (in GUI mode) or the first part of the variable name
         			(in headless mode or when using .properties file)
        @param message the message to display next to the input field (in GUI mode) or the second
         			part of the variable name (in headless mode or when using .properties file)
        @param defaultValue the optional default value
        @return the user-specified String value
        @throws CancelledException if the user hit the 'cancel' button in GUI mode
        @throws IllegalArgumentException if in headless mode, there was a missing or invalid String
         			specified in the .properties file
        """
        ...

    def askYesNo(self, title: unicode, question: unicode) -> bool:
        """
        Returns a boolean value, using the String parameters for guidance. The actual behavior of
         the method depends on your environment, which can be GUI or headless.
         <p>
         Regardless of environment -- if script arguments have been set, this method will use the
         next argument in the array and advance the array index so the next call to an ask method
         will get the next argument.  If there are no script arguments and a .properties file
         sharing the same base name as the Ghidra Script exists (i.e., Script1.properties for
         Script1.java), then this method will then look there for the String value to return.
         The method will look in the .properties file by searching for a property name that is a
         space-separated concatenation of the input String parameters (title + " " + question).
         If that property name exists and its value represents a valid boolean value, then the
         .properties value will be used in the following way:
         <ol>
         		<li>In the GUI environment, this method displays a popup dialog that prompts the user
         			with a yes/no dialog with the specified title and question. Returns true if the user
         			selects "yes" to the question or false if the user selects "no".</li>
         		<li>In the headless environment, if a .properties file sharing the same base name as the
         			Ghidra Script exists (i.e., Script1.properties for Script1.java), then this method
         			looks there for the boolean value to return. The method will look in the .properties
         			file by searching for a property name that is a space-separated concatenation of the
         			String parameters (title + " " + question). If that property name exists and its
         			value represents a valid boolean value (either 'true' or 'false', case insensitive),
         			then that value	is returned. Otherwise, an Exception is thrown if there is an
         			invalid or missing .properties value.</li>
         </ol>
        @param title the title of the dialog (in GUI mode) or the first part of the variable name
         			(in headless mode)
        @param question the question to display to the user (in GUI mode) or the second part of the
         			variable name (in headless mode)
        @return true if the user selects "yes" to the question (in GUI mode) or "true" (in headless
         			mode)
        @throws IllegalArgumentException if in headless mode, there was a missing or invalid boolean
         			specified in the .properties file
        """
        ...

    def cleanup(self, success: bool) -> None: ...

    @overload
    def clearBackgroundColor(self, address: ghidra.program.model.address.Address) -> None:
        """
        Clears the background of the Listing at the given address to the given color.  See the
         Listing help page in Ghidra help for more information.
         <p>
         This method is unavailable in headless mode.
         <p>
         Note: you can use the {@link ColorizingService} directly to access more color changing
         functionality.  See the source code of this method to learn how to access services from
         a script.
        @param address The address at which to clear the color
        @see #setBackgroundColor(AddressSetView, Color)
        @see #clearBackgroundColor(AddressSetView)
        @see ColorizingService
        @throws ImproperUseException if this method is run in headless mode
        """
        ...

    @overload
    def clearBackgroundColor(self, addresses: ghidra.program.model.address.AddressSetView) -> None:
        """
        Clears the background of the Listing at the given addresses to the given color.  See the
         Listing help page in Ghidra help for more information.
         <p>
         This method is unavailable in headless mode.
         <p>
         Note: you can use the {@link ColorizingService} directly to access more color changing
         functionality.  See the source code of this method to learn how to access services from
         a script.
        @param addresses The address at which to clear the color
        @see #setBackgroundColor(AddressSetView, Color)
        @see #clearBackgroundColor(AddressSetView)
        @see ColorizingService
        @throws ImproperUseException if this method is run in headless mode
        """
        ...

    @overload
    def clearListing(self, address: ghidra.program.model.address.Address) -> None:
        """
        Clears the code unit (instruction or data) defined at the address.
        @param address the address to clear the code unit
        @throws CancelledException
        """
        ...

    @overload
    def clearListing(self, set: ghidra.program.model.address.AddressSetView) -> None:
        """
        Clears the code units (instructions or data) in the specified set
        @param set the set to clear
        @throws CancelledException
        """
        ...

    @overload
    def clearListing(self, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> None:
        """
        Clears the code units (instructions or data) in the specified range.
        @param start the start address
        @param end the end address
        @throws CancelledException
        """
        ...

    @overload
    def clearListing(self, set: ghidra.program.model.address.AddressSetView, code: bool, symbols: bool, comments: bool, properties: bool, functions: bool, registers: bool, equates: bool, userReferences: bool, analysisReferences: bool, importReferences: bool, defaultReferences: bool, bookmarks: bool) -> bool:
        """
        Clears the listing in the specified address set.
        @param set the address set where to clear
        @param code true if code units should be cleared (instructions and defined data)
        @param symbols true if symbols should be cleared
        @param comments true if comments should be cleared
        @param properties true if properties should be cleared
        @param functions true if functions should be cleared
        @param registers true if registers should be cleared
        @param equates true if equates should be cleared
        @param userReferences true if user references should be cleared
        @param analysisReferences true if analysis references should be cleared
        @param importReferences true if import references should be cleared
        @param defaultReferences true if default references should be cleared
        @param bookmarks true if bookmarks should be cleared
        @return true if the address set was successfully cleared
        """
        ...

    def closeProgram(self, program: ghidra.program.model.listing.Program) -> None:
        """
        Closes the specified program in the current tool.
        @param program the program to close
        """
        ...

    def createAddressSet(self) -> ghidra.program.model.address.AddressSet:
        """
        Creates a new mutable address set.
        @return a new mutable address set
        """
        ...

    @overload
    def createAsciiString(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        Creates a null terminated ascii string starting
         at the specified address.
        @param address the address to create the string
        @return the newly created Data object
        """
        ...

    @overload
    def createAsciiString(self, address: ghidra.program.model.address.Address, length: int) -> ghidra.program.model.listing.Data:
        """
        Create an ASCII string at the specified address.
        @param address
        @param length length of string (a value of 0 or negative will force use
         of dynamic null terminated string)
        @return string data created
        @throws CodeUnitInsertionException
        @throws DataTypeConflictException
        """
        ...

    def createBookmark(self, address: ghidra.program.model.address.Address, category: unicode, note: unicode) -> ghidra.program.model.listing.Bookmark:
        """
        Creates a <code>NOTE</code> bookmark at the specified address
         <br>
         NOTE: if a <code>NOTE</code> bookmark already exists at the address, it will be replaced.
         This is intentional and is done to match the behavior of setting bookmarks from the UI.
        @param address the address to create the bookmark
        @param category the bookmark category (it may be null)
        @param note the bookmark text
        @return the newly created bookmark
        """
        ...

    def createByte(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        Creates a byte datatype at the given address.
        @param address the address to create the byte
        @return the newly created Data object
        """
        ...

    def createChar(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        Creates a char datatype at the given address.
        @param address the address to create the char
        @return the newly created Data object
        """
        ...

    def createDWord(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        Creates a dword datatype at the given address.
        @param address the address to create the dword
        @return the newly created Data object
        """
        ...

    def createData(self, address: ghidra.program.model.address.Address, datatype: ghidra.program.model.data.DataType) -> ghidra.program.model.listing.Data:
        """
        Creates a new defined Data object at the given address.
        @param address the address at which to create a new Data object.
        @param datatype the Data Type that describes the type of Data object to create.
        @return the newly created Data object
        """
        ...

    def createDouble(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        Creates a double datatype at the given address.
        @param address the address to create the double
        @return the newly created Data object
        """
        ...

    def createDwords(self, start: ghidra.program.model.address.Address, count: int) -> None:
        """
        Creates a list of dword datatypes starting at the given address.
        @param start the start address to create the dwords
        @param count the number of dwords to create
        """
        ...

    @overload
    def createEquate(self, data: ghidra.program.model.listing.Data, equateName: unicode) -> ghidra.program.model.symbol.Equate:
        """
        Creates a new equate on the scalar value
         at the value of the data.
        @param data the data
        @param equateName the name of the equate
        @return the newly created equate
        @throws InvalidInputException if a scalar does not exist on the data
        """
        ...

    @overload
    def createEquate(self, instruction: ghidra.program.model.listing.Instruction, operandIndex: int, equateName: unicode) -> ghidra.program.model.symbol.Equate:
        """
        Creates a new equate on the scalar value
         at the operand index of the instruction.
        @param instruction the instruction
        @param operandIndex the operand index on the instruction
        @param equateName the name of the equate
        @return the newly created equate
        @throws Exception if a scalar does not exist of the specified
         operand index of the instruction
        """
        ...

    @overload
    def createExternalReference(self, data: ghidra.program.model.listing.Data, libraryName: unicode, externalLabel: unicode, externalAddr: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.Reference:
        """
        Creates an external reference from the given data.  The reference type {@link RefType#DATA}
         will be used.
        @param data the data
        @param libraryName the name of the library being referred
        @param externalLabel the name of function in the library being referred
        @param externalAddr the address of the function in the library being referred
        @return the newly created external reference
        @throws Exception if an exception occurs
        """
        ...

    @overload
    def createExternalReference(self, instruction: ghidra.program.model.listing.Instruction, operandIndex: int, libraryName: unicode, externalLabel: unicode, externalAddr: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.Reference:
        """
        Creates an external reference from the given instruction.
         For instructions with flow, the FlowType will be assumed, otherwise
         {@link RefType#DATA} will be assumed.  To specify the appropriate
         RefType use the alternate form of this method.
        @param instruction the instruction
        @param operandIndex the operand index on the instruction
        @param libraryName the name of the library being referred
        @param externalLabel the name of function in the library being referred
        @param externalAddr the address of the function in the library being referred
        @return the newly created external reference
        @throws Exception if an exception occurs
        """
        ...

    @overload
    def createExternalReference(self, instruction: ghidra.program.model.listing.Instruction, operandIndex: int, libraryName: unicode, externalLabel: unicode, externalAddr: ghidra.program.model.address.Address, refType: ghidra.program.model.symbol.RefType) -> ghidra.program.model.symbol.Reference:
        """
        Creates an external reference from the given instruction.
        @param instruction the instruction
        @param operandIndex the operand index on the instruction
        @param libraryName the name of the library being referred
        @param externalLabel the name of function in the library being referred
        @param externalAddr the address of the function in the library being referred
        @param refType the appropriate external reference type (e.g., DATA, COMPUTED_CALL, etc.)
        @return the newly created external reference
        @throws Exception if an exception occurs
        """
        ...

    def createFloat(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        Creates a float datatype at the given address.
        @param address the address to create the float
        @return the newly created Data object
        """
        ...

    @overload
    def createFragment(self, fragmentName: unicode, start: ghidra.program.model.address.Address, length: long) -> ghidra.program.model.listing.ProgramFragment:
        """
        Creates a fragment in the root folder of the default program tree.
        @param fragmentName the name of the fragment
        @param start the start address
        @param length the length of the fragment
        @return the newly created fragment
        @throws DuplicateNameException if the given fragment name already exists
        @throws NotFoundException if any address in the fragment would be outside of the program
        """
        ...

    @overload
    def createFragment(self, fragmentName: unicode, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> ghidra.program.model.listing.ProgramFragment:
        """
        Creates a fragment in the root folder of the default program tree.
        @param fragmentName the name of the fragment
        @param start the start address
        @param end the end address (NOT INCLUSIVE)
        @return the newly created fragment
        @throws DuplicateNameException if the given fragment name already exists
        @throws NotFoundException if any address in the fragment would be outside of the program
        @deprecated This method is deprecated because it did not allow you to include the
         largest possible address.  Instead use the one that takes a start address and a length.
        """
        ...

    @overload
    def createFragment(self, module: ghidra.program.model.listing.ProgramModule, fragmentName: unicode, start: ghidra.program.model.address.Address, length: long) -> ghidra.program.model.listing.ProgramFragment:
        """
        Creates a fragment in the given folder of the default program tree.
        @param module the parent module (or folder)
        @param fragmentName the name of the fragment
        @param start the start address
        @param length the length of the fragment
        @return the newly created fragment
        @throws DuplicateNameException if the given fragment name already exists
        @throws NotFoundException if any address in the fragment would be outside of the program
        """
        ...

    @overload
    def createFragment(self, module: ghidra.program.model.listing.ProgramModule, fragmentName: unicode, start: ghidra.program.model.address.Address, end: ghidra.program.model.address.Address) -> ghidra.program.model.listing.ProgramFragment:
        """
        Creates a fragment in the given folder of the default program tree.
        @param module the parent module (or folder)
        @param fragmentName the name of the fragment
        @param start the start address
        @param end the end address (NOT INCLUSIVE)
        @return the newly created fragment
        @throws DuplicateNameException if the given fragment name already exists
        @throws NotFoundException if any address in the fragment would be outside of the program
        @deprecated This method is deprecated because it did not allow you to include the
         largest possible address.  Instead use the one that takes a start address and a length.
        """
        ...

    def createFunction(self, entryPoint: ghidra.program.model.address.Address, name: unicode) -> ghidra.program.model.listing.Function:
        """
        Creates a function at entry point with the specified name
        @param entryPoint the entry point of the function
        @param name the name of the function or null for a default function
        @return the new function or null if the function was not created
        """
        ...

    def createHighlight(self, set: ghidra.program.model.address.AddressSetView) -> None:
        """
        Sets this script's highlight state (both the local variable
         <code>currentHighlight</code> and the
         <code>GhidraState</code>'s currentHighlight) to the given address set.  Also sets the tool's highlight
         if the tool exists. (Same as calling setCurrentHightlight(set);
        @param set the set of addresses to include in the highlight.  May be null.
        """
        ...

    @overload
    def createLabel(self, address: ghidra.program.model.address.Address, name: unicode, makePrimary: bool) -> ghidra.program.model.symbol.Symbol:
        """
        Creates a label at the specified address in the global namespace.
         If makePrimary==true, then the new label is made primary.
        @param address the address to create the symbol
        @param name the name of the symbol
        @param makePrimary true if the symbol should be made primary
        @return the newly created code or function symbol
        """
        ...

    @overload
    def createLabel(self, address: ghidra.program.model.address.Address, name: unicode, makePrimary: bool, sourceType: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.symbol.Symbol:
        """
        Creates a label at the specified address in the global namespace.
         If makePrimary==true, then the new label is made primary.
         If makeUnique==true, then if the name is a duplicate, the address
         will be concatenated to name to make it unique.
        @param address the address to create the symbol
        @param name the name of the symbol
        @param makePrimary true if the symbol should be made primary
        @param sourceType the source type.
        @return the newly created code or function symbol
        """
        ...

    @overload
    def createLabel(self, address: ghidra.program.model.address.Address, name: unicode, namespace: ghidra.program.model.symbol.Namespace, makePrimary: bool, sourceType: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.symbol.Symbol:
        """
        Creates a label at the specified address in the specified namespace.
         If makePrimary==true, then the new label is made primary if permitted.
         If makeUnique==true, then if the name is a duplicate, the address
         will be concatenated to name to make it unique.
        @param address the address to create the symbol
        @param name the name of the symbol
        @param namespace label's parent namespace
        @param makePrimary true if the symbol should be made primary
        @param sourceType the source type.
        @return the newly created code or function symbol
        """
        ...

    @overload
    def createMemoryBlock(self, name: unicode, start: ghidra.program.model.address.Address, bytes: List[int], overlay: bool) -> ghidra.program.model.mem.MemoryBlock:
        """
        Create a new memory block.
        @param name the name of the block
        @param start start address of the block
        @param bytes the bytes of the memory block
        @param overlay true will create an overlay, false will not
        @return the newly created memory block
        """
        ...

    @overload
    def createMemoryBlock(self, name: unicode, start: ghidra.program.model.address.Address, input: java.io.InputStream, length: long, overlay: bool) -> ghidra.program.model.mem.MemoryBlock:
        """
        Create a new memory block.
         If the input stream is null, then an uninitialized block will be created.
        @param name the name of the block
        @param start start address of the block
        @param input source of the data used to fill the block.
        @param length the size of the block
        @param overlay true will create an overlay, false will not
        @return the newly created memory block
        """
        ...

    @overload
    def createMemoryReference(self, data: ghidra.program.model.listing.Data, toAddress: ghidra.program.model.address.Address, dataRefType: ghidra.program.model.symbol.RefType) -> ghidra.program.model.symbol.Reference:
        """
        Creates a memory reference from the given data.
        @param data the data
        @param toAddress the TO address
        @param dataRefType the type of the reference
        @return the newly created memory reference
        """
        ...

    @overload
    def createMemoryReference(self, instruction: ghidra.program.model.listing.Instruction, operandIndex: int, toAddress: ghidra.program.model.address.Address, flowType: ghidra.program.model.symbol.RefType) -> ghidra.program.model.symbol.Reference:
        """
        Creates a memory reference from the given instruction.
        @param instruction the instruction
        @param operandIndex the operand index on the instruction
        @param toAddress the TO address
        @param flowType the flow type of the reference
        @return the newly created memory reference
        """
        ...

    @overload
    def createProgram(self, programName: unicode, languageID: ghidra.program.model.lang.LanguageID) -> ghidra.program.model.listing.Program:
        """
        Creates a new program with specified name and language name. The actual language object
         is located using the language name provided.
         <p>
         Please note: the program is not automatically saved into the program.
        @param programName the program name
        @param languageID the language name
        @return the new unsaved program
        @throws Exception the language name is invalid or an I/O error occurs
        """
        ...

    @overload
    def createProgram(self, programName: unicode, language: ghidra.program.model.lang.Language, compilerSpec: ghidra.program.model.lang.CompilerSpec) -> ghidra.program.model.listing.Program:
        """
        Creates a new program with specified name and language. It uses the default compilerSpec
         for the given language.
         <p>
         Please note: the program is not automatically saved into the project.
        @param programName the program name
        @param language the language
        @param compilerSpec the compilerSpec to use.
        @return the new unsaved program
        @throws Exception the language name is invalid or an I/O error occurs
        """
        ...

    @overload
    def createProgram(self, programName: unicode, languageID: ghidra.program.model.lang.LanguageID, compilerSpecID: ghidra.program.model.lang.CompilerSpecID) -> ghidra.program.model.listing.Program:
        """
        Creates a new program with specified name and language name. The actual language object
         is located using the language name provided.
         <p>
         Please note: the program is not automatically saved into the program.
        @param programName the program name
        @param languageID the language ID
        @param compilerSpecID the compiler Spec ID
        @return the new unsaved program
        @throws Exception the language name is invalid or an I/O error occurs
        """
        ...

    def createQWord(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        Creates a qword datatype at the given address.
        @param address the address to create the qword
        @return the newly created Data object
        """
        ...

    def createSelection(self, set: ghidra.program.model.address.AddressSetView) -> None:
        """
        Calling this method is equivalent to calling {@link #setCurrentSelection(AddressSetView)}.
        @param set the addresses
        """
        ...

    def createStackReference(self, instruction: ghidra.program.model.listing.Instruction, operandIndex: int, stackOffset: int, isWrite: bool) -> ghidra.program.model.symbol.Reference:
        """
        Create a stack reference from the given instruction
        @param instruction the instruction
        @param operandIndex the operand index on the instruction
        @param stackOffset the stack offset of the reference
        @param isWrite true if the reference is WRITE access or false if the
         reference is READ access
        @return the newly created stack reference
        """
        ...

    @overload
    def createSymbol(self, address: ghidra.program.model.address.Address, name: unicode, makePrimary: bool) -> ghidra.program.model.symbol.Symbol:
        """
        @deprecated use {@link #createLabel(Address, String, boolean)} instead.
         Deprecated in Ghidra 7.4
        """
        ...

    @overload
    def createSymbol(self, address: ghidra.program.model.address.Address, name: unicode, makePrimary: bool, makeUnique: bool, sourceType: ghidra.program.model.symbol.SourceType) -> ghidra.program.model.symbol.Symbol:
        """
        @deprecated use {@link #createLabel(Address, String, boolean, SourceType)} instead. Deprecated in Ghidra 7.4
        """
        ...

    @overload
    def createTableChooserDialog(self, title: unicode, executor: ghidra.app.tablechooser.TableChooserExecutor) -> ghidra.app.tablechooser.TableChooserDialog:
        """
        Creates a TableChooserDialog that allows the script to display a list of addresses (and
         associated column data) in a table and also provides the capability to execute an
         action from a selection in the table.
         <p>
         This method is unavailable in headless mode.
        @param title the title of the dialog
        @param executor the TableChooserExecuter to be used to apply operations on table entries.
        @return a new TableChooserDialog.
        @throws ImproperUseException if this method is run in headless mode
        """
        ...

    @overload
    def createTableChooserDialog(self, title: unicode, executor: ghidra.app.tablechooser.TableChooserExecutor, isModal: bool) -> ghidra.app.tablechooser.TableChooserDialog:
        """
        Creates a TableChooserDialog that allows the script to display a list of addresses (and
         associated column data) in a table and also provides the capability to execute an
         action from a selection in the table.
         <p>
         This method is unavailable in headless mode.
        @param title of the dialog
        @param executor the TableChooserExecuter to be used to apply operations on table entries.
        @param isModal indicates whether the dialog should be modal or not
        @return a new TableChooserDialog.
        @throws ImproperUseException if this method is run in headless mode; if this script is
                                      run directly via Java or another script where the state does
                                      not include a tool.
        """
        ...

    def createUnicodeString(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        Creates a null terminated unicode string starting
         at the specified address.
        @param address the address to create the string
        @return the newly created Data object
        @throws Exception
        """
        ...

    def createWord(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        Creates a word datatype at the given address.
        @param address the address to create the word
        @return the newly created Data object
        """
        ...

    def disassemble(self, address: ghidra.program.model.address.Address) -> bool:
        """
        Start disassembling at the specified address.
         The disassembler will follow code flows.
        @param address the address to begin disassembling
        @return true if the program was successfully disassembled
        """
        ...

    def enableHeadlessAnalysis(self, b: bool) -> None:
        """
        Enables or disables analysis according to the passed-in boolean value.
         <p>
         A script that calls this method should run as a 'preScript', since preScripts
         execute before analysis would typically run. Running the script as a 'postScript'
         is ineffective, since the stage at which analysis would have happened has already
         passed.
         <p>
         This change will persist throughout the current HeadlessAnalyzer session, unless
         changed again (in other words, once analysis is enabled via script for one program,
         it will also be enabled for future programs in the current session, unless changed).
        @param b true to enable analysis, false to disable analysis
        @throws ImproperUseException if not in headless mode or headless instance not set
        @see #isHeadlessAnalysisEnabled()
        """
        ...

    def end(self, commit: bool) -> None:
        """
        Ends the transactions on the current program.
        @param commit true if changes should be committed
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def execute(self, runState: ghidra.app.script.GhidraState, runMonitor: ghidra.util.task.TaskMonitor, runWriter: java.io.PrintWriter) -> None:
        """
        Execute/run script and {@link #doCleanup} afterwards.
        @param runState state object
        @param runMonitor the monitor to use during run
        @param runWriter the target of script "print" statements
        @throws Exception if the script excepts
        """
        ...

    @overload
    def find(self, text: unicode) -> ghidra.program.model.address.Address:
        """
        Finds the first occurrence of 'text' in the program listing.
         The search order is defined as:
         <ol>
         <li>PLATE comments</li>
         <li>PRE comments</li>
         <li>labels</li>
         <li>code unit mnemonics and operands</li>
         <li>EOL comments</li>
         <li>repeatable comments</li>
         <li>POST comments</li>
         </ol>
        @param text the text to search for
        @return the first address where the 'text' was found, or null
          if the text was not found
        """
        ...

    @overload
    def find(self, start: ghidra.program.model.address.Address, value: int) -> ghidra.program.model.address.Address:
        """
        Finds the first occurrence of the byte
         starting from the address. If the start address
         is null, then the find will start from the minimum address
         of the program.
        @param start the address to start searching
        @param value the byte to search for
        @return the first address where the byte was found
        """
        ...

    @overload
    def find(self, start: ghidra.program.model.address.Address, values: List[int]) -> ghidra.program.model.address.Address:
        """
        Finds the first occurrence of the byte array sequence
         starting from the address. If the start address
         is null, then the find will start from the minimum address
         of the program.
        @param start the address to start searching
        @param values the byte array sequence to search for
        @return the first address where the byte was found, or
         null if the bytes were not found
        """
        ...

    @overload
    def findBytes(self, start: ghidra.program.model.address.Address, byteString: unicode) -> ghidra.program.model.address.Address:
        """
        Finds the first occurrence of the byte array sequence that matches the given byte string,
         starting from the address. If the start address is null, then the find will start
         from the minimum address of the program.
         <p>
         The <code>byteString</code> may contain regular expressions.  The following
         highlights some example search strings (note the use of double backslashes ("\\")):
         <pre>
                     "\\x80" - A basic search pattern for a byte value of 0x80
         "\\x50.{0,10}\\x55" - A regular expression string that searches for the byte 0x50
                               followed by 0-10 occurrences of any byte value, followed
                               by the byte 0x55
         </pre>
        @param start the address to start searching.  If null, then the start of the program
                will be used.
        @param byteString the byte pattern for which to search
        @return the first address where the byte was found, or null if the bytes were not found
        @throws IllegalArgumentException if the byteString is not a valid regular expression
        @see #findBytes(Address, String, int)
        """
        ...

    @overload
    def findBytes(self, start: ghidra.program.model.address.Address, byteString: unicode, matchLimit: int) -> List[ghidra.program.model.address.Address]:
        """
        Finds the first {@code <matchLimit>} occurrences of the byte array sequence that matches
         the given byte string, starting from the address. If the start address is null, then the
         find will start from the minimum address of the program.
         <p>
         The <code>byteString</code> may contain regular expressions.  The following
         highlights some example search strings (note the use of double backslashes ("\\")):
         <pre>
                     "\\x80" - A basic search pattern for a byte value of 0x80
         "\\x50.{0,10}\\x55" - A regular expression string that searches for the byte 0x50
                               followed by 0-10 occurrences of any byte value, followed
                               by the byte 0x55
         </pre>
        @param start the address to start searching.  If null, then the start of the program
                will be used.
        @param byteString the byte pattern for which to search
        @param matchLimit The number of matches to which the search should be restricted
        @return the start addresses that contain byte patterns that match the given byteString
        @throws IllegalArgumentException if the byteString is not a valid regular expression
        @see #findBytes(Address, String)
        """
        ...

    @overload
    def findBytes(self, start: ghidra.program.model.address.Address, byteString: unicode, matchLimit: int, alignment: int) -> List[ghidra.program.model.address.Address]:
        """
        Finds the first {@code <matchLimit>} occurrences of the byte array sequence that matches
         the given byte string, starting from the address. If the start address is null, then the
         find will start from the minimum address of the program.
         <p>
         The <code>byteString</code> may contain regular expressions.  The following
         highlights some example search strings (note the use of double backslashes ("\\")):
         <pre>
                     "\\x80" - A basic search pattern for a byte value of 0x80
         "\\x50.{0,10}\\x55" - A regular expression string that searches for the byte 0x50
                               followed by 0-10 occurrences of any byte value, followed
                               by the byte 0x55
         </pre>
        @param start the address to start searching.  If null, then the start of the program
                will be used.
        @param byteString the byte pattern for which to search
        @param matchLimit The number of matches to which the search should be restricted
        @param alignment byte alignment to use for search starts. For example, a value of
            1 searches from every byte.  A value of 2 only matches runs that begin on a even
            address boundary.
        @return the start addresses that contain byte patterns that match the given byteString
        @throws IllegalArgumentException if the byteString is not a valid regular expression
        @see #findBytes(Address, String)
        """
        ...

    @overload
    def findBytes(self, set: ghidra.program.model.address.AddressSetView, byteString: unicode, matchLimit: int, alignment: int) -> List[ghidra.program.model.address.Address]:
        """
        Finds a byte pattern within an addressSet.

         Note: The ranges within the addressSet are NOT treated as a contiguous set when searching
         <p>
         The <code>byteString</code> may contain regular expressions.  The following
         highlights some example search strings (note the use of double backslashes ("\\")):
         <pre>
                     "\\x80" - A basic search pattern for a byte value of 0x80
         "\\x50.{0,10}\\x55" - A regular expression string that searches for the byte 0x50
                               followed by 0-10 occurrences of any byte value, followed
                               by the byte 0x55
         </pre>
        @param set the addressSet specifying which addresses to search.
        @param byteString the byte pattern for which to search
        @param matchLimit The number of matches to which the search should be restricted
        @param alignment byte alignment to use for search starts. For example, a value of
            1 searches from every byte.  A value of 2 only matches runs that begin on a even
            address boundary.
        @return the start addresses that contain byte patterns that match the given byteString
        @throws IllegalArgumentException if the byteString is not a valid regular expression
        @see #findBytes(Address, String)
        """
        ...

    @overload
    def findBytes(self, set: ghidra.program.model.address.AddressSetView, byteString: unicode, matchLimit: int, alignment: int, searchAcrossAddressGaps: bool) -> List[ghidra.program.model.address.Address]:
        """
        Finds a byte pattern within an addressSet.

         Note: When searchAcrossAddressGaps is set to true, the ranges within the addressSet are
         treated as a contiguous set when searching.

         <p>
         The <code>byteString</code> may contain regular expressions.  The following
         highlights some example search strings (note the use of double backslashes ("\\")):
         <pre>
                     "\\x80" - A basic search pattern for a byte value of 0x80
         "\\x50.{0,10}\\x55" - A regular expression string that searches for the byte 0x50
                               followed by 0-10 occurrences of any byte value, followed
                               by the byte 0x55
         </pre>
        @param set the addressSet specifying which addresses to search.
        @param byteString the byte pattern for which to search
        @param matchLimit The number of matches to which the search should be restricted
        @param alignment byte alignment to use for search starts. For example, a value of
                1 searches from every byte.  A value of 2 only matches runs that begin on a even
                address boundary.
        @param searchAcrossAddressGaps when set to 'true' searches for matches across the gaps
                of each addressRange contained in the addresSet.
        @return the start addresses that contain byte patterns that match the given byteString
        @throws IllegalArgumentException if the byteString is not a valid regular expression
        @see #findBytes(Address, String)
        """
        ...

    def findPascalStrings(self, addressSet: ghidra.program.model.address.AddressSetView, minimumStringLength: int, alignment: int, includePascalUnicode: bool) -> List[ghidra.program.util.string.FoundString]:
        """
        Search for sequences of Pascal Ascii strings in program memory.  See {@link AsciiCharSetRecognizer}
         to see exactly what chars are considered ASCII for purposes of this search.
        @param addressSet The address set to search. Use null to search all memory;
        @param minimumStringLength The smallest number of chars in a sequence to be considered a "string".
        @param alignment specifies any alignment requirements for the start of the string.  An alignment
         of 1, means the string can start at any address.  An alignment of 2 means the string must
         start on an even address and so on.  Only allowed values are 1,2, and 4.
        @param includePascalUnicode if true, UTF16 size strings will be included in addition to UTF8.
        @return a list of "FoundString" objects which contain the addresses, length, and type of possible strings.
        """
        ...

    def findStrings(self, addressSet: ghidra.program.model.address.AddressSetView, minimumStringLength: int, alignment: int, requireNullTermination: bool, includeAllCharWidths: bool) -> List[ghidra.program.util.string.FoundString]:
        """
        Search for sequences of Ascii strings in program memory.  See {@link AsciiCharSetRecognizer}
         to see exactly what chars are considered ASCII for purposes of this search.
        @param addressSet The address set to search. Use null to search all memory;
        @param minimumStringLength The smallest number of chars in a sequence to be considered a "string".
        @param alignment specifies any alignment requirements for the start of the string.  An alignment
         of 1, means the string can start at any address.  An alignment of 2 means the string must
         start on an even address and so on.  Only allowed values are 1,2, and 4.
        @param requireNullTermination If true, only strings that end in a null will be returned.
        @param includeAllCharWidths if true, UTF16 and UTF32 size strings will be included in addition to UTF8.
        @return a list of "FoundString" objects which contain the addresses, length, and type of possible strings.
        """
        ...

    def getAddressFactory(self) -> ghidra.program.model.address.AddressFactory: ...

    def getAnalysisOptionDefaultValue(self, program: ghidra.program.model.listing.Program, analysisOption: unicode) -> unicode:
        """
        Returns the default value for the given analysis option.  Returns empty string if
         invalid option.
        @param program the program for which we want to retrieve the default value for the
         			given analysis option
        @param analysisOption the analysis option for which we want to retrieve the default value
        @return String representation of default value (returns empty string if analysis option
         			is invalid).
        """
        ...

    def getAnalysisOptionDefaultValues(self, __a0: ghidra.program.model.listing.Program, __a1: List[object]) -> java.util.Map: ...

    def getAnalysisOptionDescription(self, program: ghidra.program.model.listing.Program, analysisOption: unicode) -> unicode:
        """
        Returns the description of an analysis option name, as provided by the analyzer. This
         method returns an empty string if no description is available.
        @param program the program to get the analysis option description from
        @param analysisOption the analysis option to get the description for
        @return the analysis description, or empty String if none has been provided
        """
        ...

    def getAnalysisOptionDescriptions(self, __a0: ghidra.program.model.listing.Program, __a1: List[object]) -> java.util.Map: ...

    def getBookmarks(self, address: ghidra.program.model.address.Address) -> List[ghidra.program.model.listing.Bookmark]:
        """
        Returns all of the NOTE bookmarks defined at the specified address
        @param address the address to retrieve the bookmark
        @return the bookmarks at the specified address
        """
        ...

    def getByte(self, address: ghidra.program.model.address.Address) -> int:
        """
        Returns the 'byte' value at the specified address in memory.
        @param address the address
        @return the 'byte' value at the specified address in memory
        @throws MemoryAccessException if the memory is not readable
        """
        ...

    def getBytes(self, address: ghidra.program.model.address.Address, length: int) -> List[int]:
        """
        Reads length number of bytes starting at the specified address.
         Note: this could be inefficient if length is large
        @param address the address to start reading
        @param length the number of bytes to read
        @return an array of bytes
        @throws MemoryAccessException if memory does not exist or is uninitialized
        @see ghidra.program.model.mem.Memory
        """
        ...

    def getCategory(self) -> unicode:
        """
        Returns the category for this script.
        @return the category for this script
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getCodeUnitFormat(self) -> ghidra.program.model.listing.CodeUnitFormat:
        """
        Returns the code unit format established for the code browser listing
         or a default format if no tool (e.g., headless).
         <p>
         This format object may be used to format any code unit (instruction/data) using
         the same option settings.
        @return code unit format when in GUI mode, default format in headless
        """
        ...

    def getCurrentAnalysisOptionsAndValues(self, program: ghidra.program.model.listing.Program) -> java.util.Map:
        """
        Gets the given program's ANALYSIS_PROPERTIES and returns a HashMap of the
         program's analysis options to current values (values represented as strings).
         <p>
         The string "(default)" is appended to the value if it represents the
         default value for the option it is assigned to.
        @param program the program to get analysis options from
        @return mapping of analysis options to current settings (represented as strings)
        """
        ...

    def getCurrentProgram(self) -> ghidra.program.model.listing.Program:
        """
        Gets the current program.
        @return the program
        """
        ...

    @overload
    def getDataAfter(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        Returns the defined data after the specified address or null if no data exists.
        @param address the data address
        @return the defined data after the specified address or null if no data exists
        """
        ...

    @overload
    def getDataAfter(self, data: ghidra.program.model.listing.Data) -> ghidra.program.model.listing.Data:
        """
        Returns the defined data after the specified data or null if no data exists.
        @param data preceeding data
        @return the defined data after the specified data or null if no data exists
        """
        ...

    def getDataAt(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        Returns the defined data at the specified address or null if no data exists.
        @param address the data address
        @return the data at the specified address or null if no data exists
        """
        ...

    @overload
    def getDataBefore(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        Returns the defined data before the specified address or null if no data exists.
        @param address the data address
        @return the defined data before the specified address or null if no data exists
        """
        ...

    @overload
    def getDataBefore(self, data: ghidra.program.model.listing.Data) -> ghidra.program.model.listing.Data:
        """
        Returns the defined data before the specified data or null if no data exists.
        @param data the succeeding data
        @return the defined data before the specified data or null if no data exists
        """
        ...

    def getDataContaining(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        Returns the defined data containing the specified address or null if no data exists.
        @param address the data address
        @return the defined data containing the specified address or null if no data exists
        """
        ...

    def getDataTypes(self, name: unicode) -> List[ghidra.program.model.data.DataType]:
        """
        Searches through the datatype manager of the current program and
         returns an array of datatypes that match the specified name.
         The datatype manager supports datatypes of the same name in different categories.
         A zero-length array indicates that no datatypes with the specified name exist.
        @param name the name of the desired datatype
        @return an array of datatypes that match the specified name
        """
        ...

    def getDefaultLanguage(self, processor: ghidra.program.model.lang.Processor) -> ghidra.program.model.lang.Language:
        """
        Returns the default language provider for the specified processor name.
        @param processor the processor
        @return the default language provider for the specified processor name
        @throws LanguageNotFoundException if no language provider exists for the processor
        @see ghidra.program.model.lang.Language
        """
        ...

    def getDemangled(self, mangled: unicode) -> unicode:
        """
        Returns a demangled version of the mangled string.
        @param mangled the mangled string to demangled
        @return a demangled version of the mangled string
        """
        ...

    def getDouble(self, address: ghidra.program.model.address.Address) -> float:
        """
        Returns the 'double' value at the specified address in memory.
        @param address the address
        @return the 'double' value at the specified address in memory
        @throws MemoryAccessException if the memory is not readable
        """
        ...

    def getEOLComment(self, address: ghidra.program.model.address.Address) -> unicode:
        """
        Returns the EOL comment at the specified address.  The comment returned is the raw text
         of the comment.  Contrastingly, calling {@link GhidraScript#getEOLCommentAsRendered(Address)} will
         return the text of the comment as it is rendered in the display.
        @param address the address to get the comment
        @return the EOL comment at the specified address or null
         if one does not exist
        @see GhidraScript#getEOLCommentAsRendered(Address)
        """
        ...

    def getEOLCommentAsRendered(self, address: ghidra.program.model.address.Address) -> unicode:
        """
        Returns the EOL comment at the specified address.  If you want the raw text,
         then you must call {@link #getEOLComment(Address)}.  This method returns the text as
         seen in the display.
        @param address the address to get the comment
        @return the EOL comment at the specified address or null if one does not exist
        @see #getEOLComment(Address)
        """
        ...

    @overload
    def getEquate(self, data: ghidra.program.model.listing.Data) -> ghidra.program.model.symbol.Equate:
        """
        Returns the equate defined on the data.
        @param data the data
        @return the equate defined on the data
        """
        ...

    @overload
    def getEquate(self, instruction: ghidra.program.model.listing.Instruction, operandIndex: int) -> ghidra.program.model.symbol.Equate:
        """
        Returns the equate defined at the operand index of the instruction.
        @param instruction the instruction
        @param operandIndex the operand index
        @return the equate defined at the operand index of the instruction
        @deprecated this form of getEquate is not supported and will throw a UnsupportedOperationException
        """
        ...

    @overload
    def getEquate(self, instruction: ghidra.program.model.listing.Instruction, operandIndex: int, value: long) -> ghidra.program.model.symbol.Equate:
        """
        Returns the equate defined at the operand index of the instruction with the given value.
        @param instruction the instruction
        @param operandIndex the operand index
        @param value scalar equate value
        @return the equate defined at the operand index of the instruction
        """
        ...

    def getEquates(self, instruction: ghidra.program.model.listing.Instruction, operandIndex: int) -> List[ghidra.program.model.symbol.Equate]:
        """
        Returns the equates defined at the operand index of the instruction.
        @param instruction the instruction
        @param operandIndex the operand index
        @return the equate defined at the operand index of the instruction
        """
        ...

    def getFirstData(self) -> ghidra.program.model.listing.Data:
        """
        Returns the first defined data in the current program.
        @return the first defined data in the current program
        """
        ...

    def getFirstFunction(self) -> ghidra.program.model.listing.Function:
        """
        Returns the first function in the current program.
        @return the first function in the current program
        """
        ...

    @overload
    def getFirstInstruction(self) -> ghidra.program.model.listing.Instruction:
        """
        Returns the first instruction in the current program.
        @return the first instruction in the current program
        """
        ...

    @overload
    def getFirstInstruction(self, function: ghidra.program.model.listing.Function) -> ghidra.program.model.listing.Instruction:
        """
        Returns the first instruction in the function.
        @return the first instruction in the function
        """
        ...

    def getFloat(self, address: ghidra.program.model.address.Address) -> float:
        """
        Returns the 'float' value at the specified address in memory.
        @param address the address
        @return the 'float' value at the specified address in memory
        @throws MemoryAccessException if the memory is not readable
        """
        ...

    def getFragment(self, module: ghidra.program.model.listing.ProgramModule, fragmentName: unicode) -> ghidra.program.model.listing.ProgramFragment:
        """
        Returns the fragment with the specified name
         defined in the given module.
        @param module the parent module
        @param fragmentName the fragment name
        @return the fragment or null if one does not exist
        """
        ...

    def getFunction(self, name: unicode) -> ghidra.program.model.listing.Function:
        """
        Returns the function with the specified name, or
         null if no function exists. (Now returns the first one it finds with that name)
        @param name the name of the function
        @return the function with the specified name, or
         null if no function exists
        @deprecated this method makes no sense in the new world order where function  names
         			   no longer have to be unique. Use {@link #getGlobalFunctions(String)}
         			   Deprecated in Ghidra 7.4
        """
        ...

    @overload
    def getFunctionAfter(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Function:
        """
        Returns the function defined after the specified address.
        @param address the address
        @return the function defined after the specified address
        """
        ...

    @overload
    def getFunctionAfter(self, function: ghidra.program.model.listing.Function) -> ghidra.program.model.listing.Function:
        """
        Returns the function defined before the specified function in address order.
        @param function the function
        @return the function defined before the specified function
        """
        ...

    def getFunctionAt(self, entryPoint: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Function:
        """
        Returns the function with the specified entry point, or
         null if no function exists.
        @param entryPoint the function entry point address
        @return the function with the specified entry point, or
         null if no function exists
        """
        ...

    @overload
    def getFunctionBefore(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Function:
        """
        Returns the function defined before the specified address.
        @param address the address
        @return the function defined before the specified address
        """
        ...

    @overload
    def getFunctionBefore(self, function: ghidra.program.model.listing.Function) -> ghidra.program.model.listing.Function:
        """
        Returns the function defined before the specified function in address order.
        @param function the function
        @return the function defined before the specified function
        """
        ...

    def getFunctionContaining(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Function:
        """
        Returns the function containing the specified address.
        @param address the address
        @return the function containing the specified address
        """
        ...

    def getGhidraVersion(self) -> unicode:
        """
        Returns the version of the Ghidra being run.
        @return the version of the Ghidra being run
        """
        ...

    def getGlobalFunctions(self, name: unicode) -> List[ghidra.program.model.listing.Function]:
        """
        Returns a list of all functions in the global namespace with the given name.
        @param name the name of the function
        @return the function with the specified name, or
        """
        ...

    def getHeadlessContinuationOption(self) -> ghidra.app.util.headless.HeadlessScript.HeadlessContinuationOption:
        """
        Returns the continuation option for the current script (if one has not been set in this
         script, the option defaults to CONTINUE).
         <p>
         The continuation option specifies whether to continue or abort follow-on processing,
         and whether to delete or keep the current program.
        @return the current HeadlessContinuationOption
        @see #setHeadlessContinuationOption(HeadlessContinuationOption)
        """
        ...

    @overload
    def getInstructionAfter(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Instruction:
        """
        Returns the instruction defined after the specified address or null
         if no instruction exists.
         The instruction that is returned does not have to be contiguous.
        @param address the address of the prior instruction
        @return the instruction defined after the specified address or null if no instruction exists
        """
        ...

    @overload
    def getInstructionAfter(self, instruction: ghidra.program.model.listing.Instruction) -> ghidra.program.model.listing.Instruction:
        """
        Returns the instruction defined after the specified instruction or null
         if no instruction exists.
         The instruction that is returned does not have to be contiguous.
        @param instruction the instruction
        @return the instruction defined after the specified instruction or null if no instruction exists
        """
        ...

    def getInstructionAt(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Instruction:
        """
        Returns the instruction at the specified address or null if no instruction exists.
        @param address the instruction address
        @return the instruction at the specified address or null if no instruction exists
        """
        ...

    @overload
    def getInstructionBefore(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Instruction:
        """
        Returns the instruction defined before the specified address or null
         if no instruction exists.
         The instruction that is returned does not have to be contiguous.
        @param address the address of the instruction
        @return the instruction defined before the specified address or null if no instruction exists
        """
        ...

    @overload
    def getInstructionBefore(self, instruction: ghidra.program.model.listing.Instruction) -> ghidra.program.model.listing.Instruction:
        """
        Returns the instruction defined before the specified instruction or null
         if no instruction exists.
         The instruction that is returned does not have to be contiguous.
        @param instruction the instruction
        @return the instruction defined before the specified instruction or null if no instruction exists
        """
        ...

    def getInstructionContaining(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Instruction:
        """
        Returns the instruction containing the specified address or null if no instruction exists.
        @param address the instruction address
        @return the instruction containing the specified address or null if no instruction exists
        """
        ...

    def getInt(self, address: ghidra.program.model.address.Address) -> int:
        """
        Returns the 'integer' value at the specified address in memory.
        @param address the address
        @return the 'integer' value at the specified address in memory
        @throws MemoryAccessException if the memory is not readable
        """
        ...

    def getLanguage(self, languageID: ghidra.program.model.lang.LanguageID) -> ghidra.program.model.lang.Language:
        """
        Returns the language provider for the specified language name.
        @param languageID the language name
        @return the language provider for the specified language name
        @throws LanguageNotFoundException if no language provider exists
        @see ghidra.program.model.lang.Language
        """
        ...

    def getLastData(self) -> ghidra.program.model.listing.Data:
        """
        Returns the last defined data in the current program.
        @return the last defined data in the current program
        """
        ...

    def getLastFunction(self) -> ghidra.program.model.listing.Function:
        """
        Returns the last function in the current program.
        @return the last function in the current program
        """
        ...

    def getLastInstruction(self) -> ghidra.program.model.listing.Instruction:
        """
        Returns the last instruction in the current program.
        @return the last instruction in the current program
        """
        ...

    def getLong(self, address: ghidra.program.model.address.Address) -> long:
        """
        Returns the 'long' value at the specified address in memory.
        @param address the address
        @return the 'long' value at the specified address in memory
        @throws MemoryAccessException if the memory is not readable
        """
        ...

    @overload
    def getMemoryBlock(self, name: unicode) -> ghidra.program.model.mem.MemoryBlock:
        """
        Returns the first memory block with the specified name.
         NOTE: if more than block exists with the same name, the first
         block with that name will be returned.
        @param name the name of the requested block
        @return the the memory block with the specified name
        """
        ...

    @overload
    def getMemoryBlock(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.mem.MemoryBlock:
        """
        Returns the memory block containing the specified address,
         or null if no memory block contains the address.
        @param address the address
        @return the memory block containing the specified address
        """
        ...

    def getMemoryBlocks(self) -> List[ghidra.program.model.mem.MemoryBlock]:
        """
        Returns an array containing all the memory blocks
         in the current program.
        @return an array containing all the memory blocks
        """
        ...

    def getMonitor(self) -> ghidra.util.task.TaskMonitor:
        """
        Gets the current task monitor.
        @return the task monitor
        """
        ...

    def getNamespace(self, parent: ghidra.program.model.symbol.Namespace, namespaceName: unicode) -> ghidra.program.model.symbol.Namespace:
        """
        Returns the non-function namespace with the given name contained inside the
         specified parent namespace.
         Pass <code>null</code> for namespace to indicate the global namespace.
        @param parent the parent namespace, or null for global namespace
        @param namespaceName the requested namespace's name
        @return the namespace with the given name or null if not found
        """
        ...

    def getPlateComment(self, address: ghidra.program.model.address.Address) -> unicode:
        """
        Returns the PLATE comment at the specified address.  The comment returned is the raw text
         of the comment.  Contrastingly, calling {@link GhidraScript#getPlateCommentAsRendered(Address)} will
         return the text of the comment as it is rendered in the display.
        @param address the address to get the comment
        @return the PLATE comment at the specified address or null
         if one does not exist
        @see GhidraScript#getPlateCommentAsRendered(Address)
        """
        ...

    def getPlateCommentAsRendered(self, address: ghidra.program.model.address.Address) -> unicode:
        """
        Returns the PLATE comment at the specified address, as rendered.  Comments support
         annotations, which are displayed differently than the raw text.  If you want the raw text,
         then you must call {@link #getPlateComment(Address)}.  This method returns the text as
         seen in the display.
        @param address the address to get the comment
        @return the PLATE comment at the specified address or null
         			if one does not exist
        @see #getPlateComment(Address)
        """
        ...

    def getPostComment(self, address: ghidra.program.model.address.Address) -> unicode:
        """
        Returns the POST comment at the specified address.  The comment returned is the raw text
         of the comment.  Contrastingly, calling {@link GhidraScript#getPostCommentAsRendered(Address)} will
         return the text of the comment as it is rendered in the display.
        @param address the address to get the comment
        @return the POST comment at the specified address or null
         if one does not exist
        @see GhidraScript#getPostCommentAsRendered(Address)
        """
        ...

    def getPostCommentAsRendered(self, address: ghidra.program.model.address.Address) -> unicode:
        """
        Returns the POST comment at the specified address.  If you want the raw text,
         then you must call {@link #getPostComment(Address)}.  This method returns the text as
         seen in the display.
        @param address the address to get the comment
        @return the POST comment at the specified address or null if one does not exist
        @see #getPostComment(Address)
        """
        ...

    def getPreComment(self, address: ghidra.program.model.address.Address) -> unicode:
        """
        Returns the PRE comment at the specified address.  The comment returned is the raw text
         of the comment.  Contrastingly, calling {@link GhidraScript#getPreCommentAsRendered(Address)} will
         return the text of the comment as it is rendered in the display.
        @param address the address to get the comment
        @return the PRE comment at the specified address or null
         if one does not exist
        @see GhidraScript#getPreCommentAsRendered(Address)
        """
        ...

    def getPreCommentAsRendered(self, address: ghidra.program.model.address.Address) -> unicode:
        """
        Returns the PRE comment at the specified address.  If you want the raw text,
         then you must call {@link #getPreComment(Address)}.  This method returns the text as
         seen in the display.
        @param address the address to get the comment
        @return the PRE comment at the specified address or null
         		if one does not exist
        @see #getPreComment(Address)
        """
        ...

    def getProgramFile(self) -> java.io.File:
        """
        Returns the path to the program's executable file.
         For example, <code>c:\temp\test.exe</code>.
        @return path to program's executable file
        """
        ...

    def getProjectRootFolder(self) -> ghidra.framework.model.DomainFolder: ...

    @overload
    def getReference(self, data: ghidra.program.model.listing.Data, toAddress: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.Reference:
        """
        Returns the reference from the data to the given address.
        @param data the data
        @param toAddress the destination address
        @return the reference from the data to the given address
        """
        ...

    @overload
    def getReference(self, instruction: ghidra.program.model.listing.Instruction, toAddress: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.Reference:
        """
        Returns the reference from the instruction to the given address.
        @param instruction the instruction
        @param toAddress the destination address
        @return the reference from the instruction to the given address
        """
        ...

    def getReferencesFrom(self, address: ghidra.program.model.address.Address) -> List[ghidra.program.model.symbol.Reference]:
        """
        Returns an array of the references FROM the given address.
        @param address the from address of the references
        @return an array of the references FROM the given address
        """
        ...

    def getReferencesTo(self, address: ghidra.program.model.address.Address) -> List[ghidra.program.model.symbol.Reference]:
        """
        Returns an array of the references TO the given address.
         Note: If more than 4096 references exists to this address,
         only the first 4096 will be returned.
         If you need to access all the references, please
         refer to the method <code>ReferenceManager::getReferencesTo(Address)</code>.
        @param address the from address of the references
        @return an array of the references TO the given address
        """
        ...

    def getRepeatableComment(self, address: ghidra.program.model.address.Address) -> unicode:
        """
        Returns the repeatable comment at the specified address.  The comment returned is the raw text
         of the comment.  Contrastingly, calling {@link GhidraScript#getRepeatableCommentAsRendered(Address)} will
         return the text of the comment as it is rendered in the display.
        @param address the address to get the comment
        @return the repeatable comment at the specified address or null
         if one does not exist
        @see GhidraScript#getRepeatableCommentAsRendered(Address)
        """
        ...

    def getRepeatableCommentAsRendered(self, address: ghidra.program.model.address.Address) -> unicode:
        """
        Returns the repeatable comment at the specified address.  If you want the raw text,
         then you must call {@link #getRepeatableComment(Address)}.  This method returns the text as
         seen in the display.
        @param address the address to get the comment
        @return the repeatable comment at the specified address or null if one does not exist
        @see #getRepeatableComment(Address)
        """
        ...

    def getScriptAnalysisMode(self) -> ghidra.app.script.GhidraScript.AnalysisMode:
        """
        Determines the behavior of Auto-Analysis while this script is executed and the manner
         in which this script is executed.  If a script overrides this method and returns DISABLED
         or SUSPENDED, this script will execute as an AnalysisWorker.  Note that this will only
         work reliably when the script is working with the currentProgram only and is not opening
         and changing other programs.  If multiple programs will be modified
         and auto-analysis should be disabled/suspended, the AutoAnalysisManager.scheduleWorker
         method should be used with the appropriate AutoAnalysisManager instance.
        @return the analysis mode associated with this script.
        @see AutoAnalysisManager#getAnalysisManager(Program)
        @see AutoAnalysisManager#scheduleWorker(AnalysisWorker, Object, boolean, TaskMonitor)
        @see AutoAnalysisManager#setIgnoreChanges(boolean)
        """
        ...

    def getScriptArgs(self) -> List[unicode]:
        """
        Returns the script-specific arguments
        @return The script-specific arguments.  Could be an empty array, but won't be null.
        """
        ...

    def getScriptName(self) -> unicode:
        """
        Returns name of script
        @return name of script
        """
        ...

    def getShort(self, address: ghidra.program.model.address.Address) -> int:
        """
        Returns the 'short' value at the specified address in memory.
        @param address the address
        @return the 'short' value at the specified address in memory
        @throws MemoryAccessException if the memory is not readable
        """
        ...

    def getSourceFile(self) -> generic.jar.ResourceFile:
        """
        Returns the script source file.
        @return the script source file
        """
        ...

    def getState(self) -> ghidra.app.script.GhidraState:
        """
        Returns the state object for this script after first synchronizing its state with its
         corresponding convenience variables.
        @return the state object
        """
        ...

    def getStoredHeadlessValue(self, key: unicode) -> object:
        """
        Get stored value by key from the HeadlessAnalyzer instance.
         <p>
         This method, along with the 'storedHeadlessValue' method, is useful for debugging and
         testing the Headless Analyzer (when the user has directly instantiated the HeadlessAnalyzer
         instead of running it from analyzeHeadless.sh or analyzeHeadless.bat). This method is
         intended to allow a HeadlessScript to store variables that reflect the current state of
         processing (at the time the script is being run). Storing variables in the HeadlessAnalyzer
         instance may be the only way to access the state of processing during cases when the user
         is forced to run in -readOnly mode, or if there is a value that is only accessible at the
         scripts stage.
        @param key key to retrieve the desired stored value
        @return stored Object, or null if none exists for that key
        @throws ImproperUseException if not in headless mode or headless instance not set
        @see #storeHeadlessValue(String, Object)
        @see #headlessStorageContainsKey(String)
        """
        ...

    def getSymbol(self, name: unicode, namespace: ghidra.program.model.symbol.Namespace) -> ghidra.program.model.symbol.Symbol:
        """
        Returns the symbol with the given name in the given namespace if there is only one.
         Pass <code>null</code> for namespace to indicate the global namespace.
        @param name the name of the symbol
        @param namespace the parent namespace, or null for global namespace
        @return the symbol with the given name in the given namespace
        @throws IllegalStateException if there is more than one symbol with that name.
        @deprecated use {@link #getSymbols(String, Namespace)}
        """
        ...

    @overload
    def getSymbolAfter(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.Symbol:
        """
        Returns the next non-default primary symbol defined
         after the given address.
        @param address the address to use as a starting point
        @return the next non-default primary symbol
        """
        ...

    @overload
    def getSymbolAfter(self, symbol: ghidra.program.model.symbol.Symbol) -> ghidra.program.model.symbol.Symbol:
        """
        Returns the next non-default primary symbol defined
         after the given symbol.
        @param symbol the symbol to use as a starting point
        @return the next non-default primary symbol
        """
        ...

    @overload
    def getSymbolAt(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.Symbol:
        """
        Returns the PRIMARY symbol at the specified address, or
         null if no symbol exists.
        @param address the symbol address
        @return the PRIMARY symbol at the specified address, or
         null if no symbol exists
        """
        ...

    @overload
    def getSymbolAt(self, address: ghidra.program.model.address.Address, name: unicode) -> ghidra.program.model.symbol.Symbol:
        """
        Returns the symbol with the specified address and name, or
         null if no symbol exists.
        @param address the symbol address
        @param name the symbol name
        @return the symbol with the specified address and name, or
         null if no symbol exists
        @deprecated Since the same label name can be at the same address if in a different namespace,
         this method is ambiguous. Use {@link #getSymbolAt(Address, String, Namespace)} instead.
        """
        ...

    @overload
    def getSymbolAt(self, address: ghidra.program.model.address.Address, name: unicode, namespace: ghidra.program.model.symbol.Namespace) -> ghidra.program.model.symbol.Symbol:
        """
        Returns the symbol with the specified address, name, and namespace
        @param address the symbol address
        @param name the symbol name
        @param namespace the parent namespace for the symbol.
        @return the symbol with the specified address, name, and namespace, or
         null if no symbol exists
        """
        ...

    @overload
    def getSymbolBefore(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.symbol.Symbol:
        """
        Returns the previous non-default primary symbol defined
         after the previous address.
        @param address the address to use as a starting point
        @return the next non-default primary symbol
        """
        ...

    @overload
    def getSymbolBefore(self, symbol: ghidra.program.model.symbol.Symbol) -> ghidra.program.model.symbol.Symbol:
        """
        Returns the previous non-default primary symbol defined
         before the given symbol.
        @param symbol the symbol to use as a starting point
        @return the previous non-default primary symbol
        """
        ...

    def getSymbols(self, name: unicode, namespace: ghidra.program.model.symbol.Namespace) -> List[ghidra.program.model.symbol.Symbol]:
        """
        Returns a list of all the symbols with the given name in the given namespace.
        @param name the name of the symbols to retrieve.
        @param namespace the namespace containing the symbols, or null for the global namespace.
        @return a list of all the symbols with the given name in the given namespace.
        """
        ...

    def getUndefinedDataAfter(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        Returns the undefined data after the specified address or null if no undefined data exists.
        @param address the undefined data address
        @return the undefined data after the specified address or null if no undefined data exists
        """
        ...

    def getUndefinedDataAt(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        Returns the undefined data at the specified address or null if no undefined data exists.
        @param address the undefined data address
        @return the undefined data at the specified address or null if no undefined data exists
        """
        ...

    def getUndefinedDataBefore(self, address: ghidra.program.model.address.Address) -> ghidra.program.model.listing.Data:
        """
        Returns the undefined data before the specified address or null if no undefined data exists.
        @param address the undefined data address
        @return the undefined data before the specified address or null if no undefined data exists
        """
        ...

    def getUserName(self) -> unicode:
        """
        Returns the username of the user running the script.
        @return the username of the user running the script
        """
        ...

    @overload
    def goTo(self, address: ghidra.program.model.address.Address) -> bool:
        """
        Sends a 'goto' event that navigates the listing to the specified
         address.
        @param address the address to 'goto'
        @return true if the address is valid
        """
        ...

    @overload
    def goTo(self, function: ghidra.program.model.listing.Function) -> bool:
        """
        Sends a 'goto' event that navigates the listing to the specified function.
        @param function the function to 'goto'
        @return true if the function is valid
        """
        ...

    @overload
    def goTo(self, symbol: ghidra.program.model.symbol.Symbol) -> bool:
        """
        Sends a 'goto' event that navigates the listing to the specified symbol.
        @param symbol the symbol to 'goto'
        @return true if the symbol is valid
        """
        ...

    def hashCode(self) -> int: ...

    def headlessStorageContainsKey(self, key: unicode) -> bool:
        """
        Returns whether the specified key was stored in the HeadlessAnalyzer instance.
        @param key value of key to check for in Headless Analyzer instance
        @return true if the specified key exists
        @throws ImproperUseException if not in headless mode or headless instance not set
        @see #storeHeadlessValue(String, Object)
        @see #getStoredHeadlessValue(String)
        """
        ...

    def importFile(self, file: java.io.File) -> ghidra.program.model.listing.Program:
        """
        Attempts to import the specified file. It attempts to detect the format and
         automatically import the file. If the format is unable to be determined, then
         null is returned.
        @param file the file to import
        @return the newly imported program, or null
        @throws Exception if any exceptions occur while importing
        """
        ...

    def importFileAsBinary(self, file: java.io.File, language: ghidra.program.model.lang.Language, compilerSpec: ghidra.program.model.lang.CompilerSpec) -> ghidra.program.model.listing.Program:
        """
        Imports the specified file as raw binary.
        @param file the file to import
        @param language the language of the new program
        @param compilerSpec the compilerSpec to use for the import.
        @return the newly created program, or null
        @throws Exception if any exceptions occur when importing
        """
        ...

    def isAnalysisOptionDefaultValue(self, program: ghidra.program.model.listing.Program, analysisOption: unicode, analysisValue: unicode) -> bool:
        """
        Returns a boolean value representing whether the specified value for the specified
         analysis option is actually the default value for that option.
        @param program the program for which we want to verify the analysis option value
        @param analysisOption the analysis option whose value we want to verify
        @param analysisValue the analysis value to be compared to the option's default value
        @return whether the given value for the given option is default or not
        """
        ...

    def isHeadlessAnalysisEnabled(self) -> bool:
        """
        Returns whether analysis is currently enabled or disabled in the HeadlessAnalyzer.
        @return whether analysis has been enabled or not
        @throws ImproperUseException if not in headless mode or headless instance not set
        @see #enableHeadlessAnalysis(boolean)
        """
        ...

    def isImporting(self) -> bool:
        """
        Returns whether the headless analyzer is currently set to -import mode or not (if not,
         it is in -process mode). The use of -import mode implies that binaries are actively being
         imported into the project (with optional scripts/analysis). The use of -process mode implies
         that existing project files are being processed (using scripts and/or analysis).
        @return whether we are in -import mode or not
        @throws ImproperUseException if not in headless mode or headless instance not set
        """
        ...

    def isRunningHeadless(self) -> bool:
        """
        Returns whether this script is running in a headless (Non GUI) environment.
         <p>
         This method should not be using GUI type script calls like showAddress()
        @return true if the script is running without a GUI.
        """
        ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def openDataTypeArchive(self, archiveFile: java.io.File, readOnly: bool) -> ghidra.program.model.data.FileDataTypeManager:
        """
        Opens a Data Type Archive
        @param archiveFile the archive file to open
        @param readOnly should file be opened read only
        """
        ...

    def openProgram(self, program: ghidra.program.model.listing.Program) -> None:
        """
        Opens the specified program in the current tool.
        @param program the program to open
        """
        ...

    def parseAddress(self, val: unicode) -> ghidra.program.model.address.Address:
        """
        Parses an address from a string.
        @param val The string to parse.
        @return The address that was parsed from the string.
        @throws IllegalArgumentException if there was a problem parsing an address from the string.
        """
        ...

    def parseBoolean(self, val: unicode) -> bool:
        """
        Parses a boolean from a string.
        @param val The string to parse.
        @return The boolean that was parsed from the string.
        @throws IllegalArgumentException if the parsed value is not a valid boolean.
        """
        ...

    def parseBytes(self, val: unicode) -> List[int]:
        """
        Parses bytes from a string.
        @param val The string to parse.
        @return The bytes that were parsed from the string.
        @throws IllegalArgumentException if there was a problem parsing bytes from the string.
        """
        ...

    def parseChoice(self, val: unicode, validChoices: List[object]) -> object:
        """
        Parses a choice from a string.
        @param val The string to parse.
        @param validChoices An array of valid choices.
        @return The choice
        @throws IllegalArgumentException if the parsed string was not a valid choice.
        """
        ...

    @overload
    def parseChoices(self, s: unicode, validChoices: List[object]) -> List[object]:
        """
        Parses choices from a string.  The string must be surrounded by quotes, with a ';' as the
         separator.
        @param s The string to parse.
        @param validChoices An array of valid choices.
        @return The choices, if they found in the array of choices.
        @throws IllegalArgumentException if the parsed string did not contain any valid choices.
        """
        ...

    @overload
    def parseChoices(self, __a0: unicode, __a1: List[object], __a2: List[object]) -> List[object]: ...

    def parseDirectory(self, val: unicode) -> java.io.File:
        """
        Parses a directory from a string.
        @param val The string to parse.
        @return The directory that was parsed from the string.
        @throws IllegalArgumentException if the parsed value is not a valid directory.
        """
        ...

    def parseDomainFile(self, val: unicode) -> ghidra.framework.model.DomainFile:
        """
        Parses a DomainFile from a string.
        @param val The string to parse.
        @return The DomainFile that was parsed from the string.
        @throws IllegalArgumentException if the parsed value is not a valid DomainFile.
        """
        ...

    def parseDouble(self, val: unicode) -> float:
        """
        Parses a double from a string.
        @param val The string to parse.
        @return The double that was parsed from the string.
        @throws IllegalArgumentException if the parsed value is not a valid double.
        """
        ...

    def parseFile(self, s: unicode) -> java.io.File:
        """
        Parses a file from a string.
        @param s The string to parse.
        @return The file that was parsed from the string.
        @throws IllegalArgumentException if the parsed value is not a valid file.
        """
        ...

    def parseInt(self, val: unicode) -> int:
        """
        Parses an integer from a string.
        @param val The string to parse.
        @return The integer that was parsed from the string.
        @throws IllegalArgumentException if the parsed value is not a valid integer.
        """
        ...

    def parseLanguageCompileSpecPair(self, val: unicode) -> ghidra.program.model.lang.LanguageCompilerSpecPair:
        """
        Parses a LanguageCompilerSpecPair from a string.
        @param val The string to parse.
        @return The directory that was parsed from the LanguageCompilerSpecPair.
        @throws IllegalArgumentException if the parsed value is not a valid LanguageCompilerSpecPair.
        """
        ...

    def parseLong(self, val: unicode) -> long:
        """
        Parses a long from a string.
        @param val The string to parse.
        @return The long that was parsed from the string.
        @throws IllegalArgumentException if the parsed value is not a valid long.
        """
        ...

    def parseProjectFolder(self, val: unicode) -> ghidra.framework.model.DomainFolder:
        """
        Parses a ProjectFolder from a string.
        @param val The string to parse.
        @return The ProjectFolder that was parsed from the string.
        @throws IllegalArgumentException if the parsed value is not a valid ProjectFolder.
        """
        ...

    def popup(self, message: unicode) -> None:
        """
        Displays a popup dialog with the specified message. The dialog title
         will be the name of this script.
         <p>
         In headless mode, the message is displayed in the log output.
        @param message the message to display in the dialog
        """
        ...

    def print(self, message: unicode) -> None:
        """
        Prints the message to the console - no line feed
         <p>
         <b><u>Note:</u> This method will not print out the name of the script,
         as does {@link #println(String)}
         </b>
         <p>
         If you would like the name of the script to precede you message, then you must add that
         yourself.  The {@link #println(String)} does this via the following code:
         <pre>
             String messageWithSource = getScriptName() + "&gt; " + message;
         </pre>
        @param message the message to print
        @see #printf(String, Object...)
        """
        ...

    def printerr(self, message: unicode) -> None:
        """
        Prints the error message to the console followed by a line feed.
        @param message the error message to print
        """
        ...

    def printf(self, message: unicode, args: List[object]) -> None:
        """
        A convenience method to print a formatted String using Java's <code>printf</code>
         feature, which is similar to that of the C programming language.
         For a full description on Java's
         <code>printf</code> usage, see {@link java.util.Formatter}.
         <p>
         For examples, see the included <code>FormatExampleScript</code>.
         <p>
         <b><u>Note:</u> This method will not:</b>
         <ul>
         	<li><b>print out the name of the script, as does {@link #println(String)}</b></li>
          <li><b>print a newline</b></li>
         </ul>
         If you would like the name of the script to precede you message, then you must add that
         yourself.  The {@link #println(String)} does this via the following code:
         <pre>
             String messageWithSource = getScriptName() + "&gt; " + message;
         </pre>
        @param message the message to format
        @param args formatter arguments (see above)
        @see String#format(String, Object...)
        @see java.util.Formatter
        @see #print(String)
        @see #println(String)
        """
        ...

    @overload
    def println(self) -> None:
        """
        Prints a newline.
        @see #printf(String, Object...)
        """
        ...

    @overload
    def println(self, message: unicode) -> None:
        """
        Prints the message to the console followed by a line feed.
        @param message the message to print
        @see #printf(String, Object...)
        """
        ...

    def removeBookmark(self, bookmark: ghidra.program.model.listing.Bookmark) -> None:
        """
        Removes the specified bookmark.
        @param bookmark the bookmark to remove
        """
        ...

    def removeData(self, data: ghidra.program.model.listing.Data) -> None:
        """
        Removes the given data from the current program.
        @param data the data to remove
        """
        ...

    def removeDataAt(self, address: ghidra.program.model.address.Address) -> None:
        """
        Removes the data containing the given address from the current program.
        @param address the address to remove data
        """
        ...

    def removeEntryPoint(self, address: ghidra.program.model.address.Address) -> None:
        """
        Removes the entry point at the specified address.
        @param address address of entry point to remove
        """
        ...

    @overload
    def removeEquate(self, data: ghidra.program.model.listing.Data) -> None:
        """
        Removes the equate defined on the data.
        @param data the data
        """
        ...

    @overload
    def removeEquate(self, instruction: ghidra.program.model.listing.Instruction, operandIndex: int) -> None:
        """
        Removes the equate defined at the operand index of the instruction.
        @param instruction the instruction
        @param operandIndex the operand index
        @deprecated this form of getEquate is not supported and will throw a UnsupportedOperationException
        """
        ...

    @overload
    def removeEquate(self, instruction: ghidra.program.model.listing.Instruction, operandIndex: int, value: long) -> None:
        """
        Removes the equate defined at the operand index of the instruction with the given value.
        @param instruction the instruction
        @param operandIndex the operand index
        @param value scalar value corresponding to equate
        """
        ...

    def removeEquates(self, instruction: ghidra.program.model.listing.Instruction, operandIndex: int) -> None:
        """
        Removes the equates defined at the operand index of the instruction.
        @param instruction the instruction
        @param operandIndex the operand index
        """
        ...

    def removeFunction(self, function: ghidra.program.model.listing.Function) -> None:
        """
        Removes the function from the current program.
        @param function the function to remove
        """
        ...

    def removeFunctionAt(self, entryPoint: ghidra.program.model.address.Address) -> None:
        """
        Removes the function with the given entry point.
        @param entryPoint the entry point of the function to remove
        """
        ...

    def removeHighlight(self) -> None:
        """
        Clears the current highlight. Sets this script's highlight state (both the local variable
         currentHighlight and the ghidraState's currentHighlight) to null.  Also clears the tool's
         highlight if the tool exists.
        """
        ...

    def removeInstruction(self, instruction: ghidra.program.model.listing.Instruction) -> None:
        """
        Removes the given instruction from the current program.
        @param instruction the instruction to remove
        """
        ...

    def removeInstructionAt(self, address: ghidra.program.model.address.Address) -> None:
        """
        Removes the instruction containing the given address from the current program.
        @param address the address to remove instruction
        """
        ...

    def removeMemoryBlock(self, block: ghidra.program.model.mem.MemoryBlock) -> None:
        """
        Remove the memory block.
         NOTE: ALL ANNOTATION (disassembly, comments, etc) defined in this
         memory block will also be removed!
        @param block the block to be removed
        """
        ...

    def removeReference(self, reference: ghidra.program.model.symbol.Reference) -> None:
        """
        Removes the given reference.
        @param reference the reference to remove
        """
        ...

    def removeSelection(self) -> None:
        """
        Clears the current selection.  Calling this method is equivalent to calling
         {@link #setCurrentSelection(AddressSetView)} with a null or empty AddressSet.
        """
        ...

    def removeSymbol(self, address: ghidra.program.model.address.Address, name: unicode) -> bool:
        """
        Deletes the symbol with the specified name at the specified address.
        @param address the address of the symbol to delete
        @param name the name of the symbol to delete
        @return true if the symbol was deleted
        """
        ...

    def resetAllAnalysisOptions(self, program: ghidra.program.model.listing.Program) -> None:
        """
        Reset all analysis options to their default values.
        @param program the program for which all analysis options should be reset
        """
        ...

    def resetAnalysisOption(self, program: ghidra.program.model.listing.Program, analysisOption: unicode) -> None:
        """
        Reset one analysis option to its default value.
        @param program the program for which the specified analysis options should be reset
        @param analysisOption the specified analysis option to reset (invalid options will be
         		  	ignored)
        """
        ...

    def resetAnalysisOptions(self, __a0: ghidra.program.model.listing.Program, __a1: List[object]) -> None: ...

    @overload
    def runCommand(self, cmd: ghidra.framework.cmd.BackgroundCommand) -> bool:
        """
        Runs the specified background command using the current program.
         The command will be given the script task monitor.
        @param cmd the background command to run
        @return true if the background command successfully ran
        """
        ...

    @overload
    def runCommand(self, cmd: ghidra.framework.cmd.Command) -> bool:
        """
        Runs the specified command using the current program.
        @param cmd the command to run
        @return true if the command successfully ran
        """
        ...

    @overload
    def runScript(self, scriptName: unicode) -> None:
        """
        Runs a script by name (allows current state to be changed by script).
         <p>
         It attempts to locate the script in the directories
         defined in <code>GhidraScriptUtil.getScriptDirectories()</code>.
         <p>
         The script being run uses the same {@link GhidraState} (e.g., script variables) as
         this calling script.  Also, any changes to the state by the script being run will be
         reflected in this calling script's state.
        @param scriptName the name of the script to run
        @throws IllegalArgumentException if the script does not exist
        @throws Exception if any exceptions occur while running the script
        @see #runScriptPreserveMyState(String)
        @see #runScript(String, GhidraState)
        """
        ...

    @overload
    def runScript(self, scriptName: unicode, scriptArguments: List[unicode]) -> None:
        """
        Runs a script by name with the provided arguments (allows current state to be changed by
         script).
         <p>
         It attempts to locate the script in the directories
         defined in <code>GhidraScriptUtil.getScriptDirectories()</code>.
         <p>
         The script being run uses the same {@link GhidraState} (e.g., script variables) as
         this calling script.  Also, any changes to the state by the script being run will be
         reflected in this calling script's state.
        @param scriptName the name of the script to run
        @param scriptArguments the arguments to pass to the script
        @throws IllegalArgumentException if the script does not exist
        @throws Exception if any exceptions occur while running the script
        @see #runScriptPreserveMyState(String)
        @see #runScript(String, GhidraState)
        """
        ...

    @overload
    def runScript(self, scriptName: unicode, scriptState: ghidra.app.script.GhidraState) -> None:
        """
        Runs a script by name using the given state.
         <p>
         It attempts to locate the script in the directories
         defined in <code>GhidraScriptUtil.getScriptDirectories()</code>.
         <p>
         The script being run uses the given {@link GhidraState} (e.g., script variables)
         Any changes to the state by the script being run will be reflected in the given state
         object.  If the given object is the current state, the this scripts state may be changed
         by the called script.
        @param scriptName the name of the script to run
        @param scriptState the Ghidra state
        @throws IllegalArgumentException if the script does not exist
        @throws Exception if any exceptions occur while running the script
        @see #runScriptPreserveMyState(String)
        @see #runScript(String)
        """
        ...

    @overload
    def runScript(self, scriptName: unicode, scriptArguments: List[unicode], scriptState: ghidra.app.script.GhidraState) -> None: ...

    def runScriptPreserveMyState(self, scriptName: unicode) -> ghidra.app.script.GhidraState:
        """
        Runs a script by name (does not allow current state to change).
         <p>
         It attempts to locate the script in the directories
         defined in <code>GhidraScriptUtil.getScriptDirectories()</code>.
         <p>
         The script being run uses the same {@link GhidraState} (e.g., script variables) as
         this calling script.  However, any changes to the state by the script being run will NOT
         be reflected in this calling script's state.
        @param scriptName the name of the script to run
        @return a GhidraState object containing the final state of the run script.
        @throws IllegalArgumentException if the script does not exist
        @throws Exception if any exceptions occur while running the script
        @see #runScript(String)
        @see #runScript(String, GhidraState)
        """
        ...

    @overload
    def saveProgram(self, program: ghidra.program.model.listing.Program) -> None:
        """
        Saves the changes to the specified program.
         If the program does not already exist in the current project
         then it will be saved into the root folder.
         If a program already exists with the specified
         name, then a time stamp will be appended to the name to make it unique.
        @param program the program to save
        @throws Exception
        """
        ...

    @overload
    def saveProgram(self, __a0: ghidra.program.model.listing.Program, __a1: List[object]) -> None: ...

    def set(self, state: ghidra.app.script.GhidraState, monitor: ghidra.util.task.TaskMonitor, writer: java.io.PrintWriter) -> None:
        """
        Set the context for this script.
        @param state state object
        @param monitor the monitor to use during run
        @param writer the target of script "print" statements
        """
        ...

    def setAnalysisOption(self, program: ghidra.program.model.listing.Program, optionName: unicode, optionValue: unicode) -> None:
        """
        Allows user to set one analysis option by passing in the analysis option to
         be changed and the new value of that option. This method does the work of
         converting the option value to its actual object type (if needed).
        @param program the program for which analysis options should be set
        @param optionName the name of the option to be set
        @param optionValue the new value of the option
        """
        ...

    def setAnalysisOptions(self, program: ghidra.program.model.listing.Program, analysisSettings: java.util.Map) -> None:
        """
        Allows user to set analysis options by passing a mapping of analysis option to
         desired value.  This method does the work of converting the option value to its
         actual object type (if needed).
        @param program the program for which analysis options should be set
        @param analysisSettings a mapping from analysis options to desired new settings
        """
        ...

    def setAnonymousServerCredentials(self) -> bool:
        """
        Enable use of anonymous read-only user connection to Ghidra Server in place of
         fixed username/password credentials.
         <p>
         NOTE: Only used for Headless environment, other GUI environments should
         continue to prompt user for login credentials as needed.
        @return true if active project is either private or shared project is
         connected to its server repository.  False is returned if not active
         project or an active shared project failed to connect.
        """
        ...

    @overload
    def setBackgroundColor(self, address: ghidra.program.model.address.Address, color: java.awt.Color) -> None:
        """
        Sets the background of the Listing at the given address to the given color.  See the
         Listing help page in Ghidra help for more information.
         <p>
         This method is unavailable in headless mode.
         <p>
         Note: you can use the {@link ColorizingService} directly to access more color changing
         functionality.  See the source code of this method to learn how to access services from
         a script.
        @param address The address at which to set the color
        @param color The color to set
        @see #setBackgroundColor(AddressSetView, Color)
        @see #clearBackgroundColor(Address)
        @see ColorizingService
        @throws ImproperUseException if this method is run in headless mode
        """
        ...

    @overload
    def setBackgroundColor(self, addresses: ghidra.program.model.address.AddressSetView, color: java.awt.Color) -> None:
        """
        Sets the background of the Listing at the given addresses to the given color.  See the
         Listing help page in Ghidra help for more information.
         <p>
         This method is unavailable in headless mode.
         <p>
         Note: you can use the {@link ColorizingService} directly to access more color changing
         functionality.  See the source code of this method to learn how to access services from
         a script.
        @param addresses The addresses at which to set the color
        @param color The color to set
        @see #setBackgroundColor(Address, Color)
        @see #clearBackgroundColor(AddressSetView)
        @see ColorizingService
        @throws ImproperUseException if this method is run in headless mode
        """
        ...

    def setByte(self, address: ghidra.program.model.address.Address, value: int) -> None:
        """
        Sets the 'byte' value at the specified address.
        @param address the address to set the 'byte'
        @param value the value to set
        @throws MemoryAccessException if memory does not exist or is uninitialized
        """
        ...

    def setBytes(self, address: ghidra.program.model.address.Address, values: List[int]) -> None:
        """
        Sets the 'byte' values starting at the specified address.
        @param address the address to set the bytes
        @param values the values to set
        @throws MemoryAccessException if memory does not exist or is uninitialized
        """
        ...

    def setCurrentHighlight(self, addressSet: ghidra.program.model.address.AddressSetView) -> None:
        """
        Sets the highlight state to the given address set.
         <p>
         The actual behavior of the method depends on your environment, which can be GUI or
         headless:
         <ol>
         		<li>In the GUI environment this method will set the {@link #currentHighlight}
         			variable to the given value, update the {@link GhidraState}'s highlight variable,
         			<b>and</b> will set the Tool's highlight to the given value.</li>
         		<li>In the headless environment this method will set the {@link #currentHighlight}
         			variable to	the given value and update the GhidraState's highlight variable.</li>
         </ol>
         <p>
        @param addressSet the set of addresses to include in the highlight.  If this value is null,
         the current highlight will be cleared and the variables set to null.
        """
        ...

    def setCurrentLocation(self, address: ghidra.program.model.address.Address) -> None:
        """
        Set the script {@link #currentAddress}, {@link #currentLocation}, and update state object.
        @param address the new address
        """
        ...

    def setCurrentSelection(self, addressSet: ghidra.program.model.address.AddressSetView) -> None:
        """
        Sets the selection state to the given address set.
         <p>
         The actual behavior of the method depends on your environment, which can be GUI or
         headless:
         <ol>
         		<li>In the GUI environment this method will set the {@link #currentSelection}
         			variable to the given value, update the {@link GhidraState}'s selection
         			variable, <b>and</b> will set the Tool's selection to the given value.</li>
         		<li>In the headless environment this method will set the {@link #currentSelection}
         			variable to the given value and update the GhidraState's selection variable.</li>
         </ol>
         <p>
        @param addressSet the set of addresses to include in the selection.  If this value is null,
         the current selection will be cleared and the variables set to null.
        """
        ...

    def setDouble(self, address: ghidra.program.model.address.Address, value: float) -> None:
        """
        Sets the 'double' value at the specified address.
        @param address the address to set the 'double'
        @param value the value to set
        @throws MemoryAccessException if memory does not exist or is uninitialized
        """
        ...

    def setEOLComment(self, address: ghidra.program.model.address.Address, comment: unicode) -> bool:
        """
        Sets an EOL comment at the specified address
        @param address the address to set the EOL comment
        @param comment the EOL comment
        @return true if the EOL comment was successfully set
        """
        ...

    def setFloat(self, address: ghidra.program.model.address.Address, value: float) -> None:
        """
        Sets the 'float' value at the specified address.
        @param address the address to set the 'float'
        @param value the value to set
        @throws MemoryAccessException if memory does not exist or is uninitialized
        """
        ...

    def setHeadlessContinuationOption(self, option: ghidra.app.util.headless.HeadlessScript.HeadlessContinuationOption) -> None:
        """
        Sets the continuation option for this script
         <p>
         The continuation option specifies whether to continue or abort follow-on processing,
         and whether to delete or keep the current program.
        @param option HeadlessContinuationOption set by this script
        @see #getHeadlessContinuationOption()
        """
        ...

    def setHeadlessImportDirectory(self, importDir: unicode) -> None:
        """
        Changes the path <i>in the Ghidra project</i> where imported files are saved.
         The passed-in path is assumed to be relative to the project root. For example,
         if the directory structure for the Ghidra project looks like this:

         <pre>
         		MyGhidraProject:
         		  /dir1
         		    /innerDir1
         		    /innerDir2
         </pre>

         Then the following usage would ensure that any files imported after this call would
         be saved in the <code>MyGhidraProject:/dir1/innerDir2</code> folder.
         <pre>
         		setHeadlessImportDirectory("dir1/innerDir2");
         </pre>
         In contrast, the following usages would add new folders to the Ghidra project and save
         the imported files into the newly-created path:
         <pre>
         		setHeadlessImportDirectory("innerDir2/my/folder");
         </pre>
         changes the directory structure to:
         <pre>
         		MyGhidraProject:
         		  /dir1
         		    /innerDir1
         		    /innerDir2
         		      /my
         		        /folder
         </pre>
         and:
         <pre>
         		setHeadlessImportDirectory("newDir/saveHere");
         </pre>
         changes the directory structure to:
         <pre>
         		MyGhidraProject:
         		  /dir1
         		    /innerDir1
         			/innerDir2
        		  /newDir
         		    /saveHere
         </pre>
         As in the examples above, if the desired folder does not already exist, it is created.
         <p>
         A change in the import save folder will persist throughout the current HeadlessAnalyzer
         session, unless changed again (in other words, once the import directory has been changed,
         it will remain the 'save' directory for import files in the current session, unless changed).
         <p>
         To revert back to the default import location (that which was specified via command line),
         pass the null object as the argument to this method, as below:
         <pre>
         		setHeadlessImportDirectory(null);	// Sets import save directory to default
         </pre>
         If a file with the same name already exists in the desired location, it will only be
         overwritten if "-overwrite" is true.
         <p>
         This method is only applicable when using the HeadlessAnalyzer <code>-import</code> mode and
         is ineffective in <code>-process</code> mode.
        @param importDir the absolute path (relative to root) where inputs will be saved
        @throws ImproperUseException if not in headless mode or headless instance not set
        @throws IOException if there are issues creating the folder
        @throws InvalidNameException if folder name is invalid
        """
        ...

    def setInt(self, address: ghidra.program.model.address.Address, value: int) -> None:
        """
        Sets the 'integer' value at the specified address.
        @param address the address to set the 'integer'
        @param value the value to set
        @throws MemoryAccessException if memory does not exist or is uninitialized
        """
        ...

    def setLong(self, address: ghidra.program.model.address.Address, value: long) -> None:
        """
        Sets the 'long' value at the specified address.
        @param address the address to set the 'long'
        @param value the value to set
        @throws MemoryAccessException if memory does not exist or is uninitialized
        """
        ...

    def setPlateComment(self, address: ghidra.program.model.address.Address, comment: unicode) -> bool:
        """
        Sets a PLATE comment at the specified address
        @param address the address to set the PLATE comment
        @param comment the PLATE comment
        @return true if the PLATE comment was successfully set
        """
        ...

    def setPostComment(self, address: ghidra.program.model.address.Address, comment: unicode) -> bool:
        """
        Sets a POST comment at the specified address
        @param address the address to set the POST comment
        @param comment the POST comment
        @return true if the POST comment was successfully set
        """
        ...

    def setPotentialPropertiesFileLocations(self, __a0: List[object]) -> None: ...

    def setPreComment(self, address: ghidra.program.model.address.Address, comment: unicode) -> bool:
        """
        Sets a PRE comment at the specified address
        @param address the address to set the PRE comment
        @param comment the PRE comment
        @return true if the PRE comment was successfully set
        """
        ...

    def setPropertiesFile(self, propertiesFile: java.io.File) -> None:
        """
        Explicitly set the .properties file (used if a ResourceFile representing the
         GhidraScript is not available -- i.e., if running GhidraScript from a .class file
         or instantiating the actual GhidraScript object directly).
        @param propertiesFile the actual .properties file for this GhidraScript
        @throws IOException if there is an exception reading the properties
        """
        ...

    def setPropertiesFileLocation(self, dirLocation: unicode, basename: unicode) -> None:
        """
        Explicitly set the .properties file location and basename for this script (used
         if a ResourceFile representing the GhidraScript is not available -- i.e., if
         running GhidraScript from a .class file or instantiating the actual GhidraScript
         object directly).
        @param dirLocation String representation of the path to the .properties file
        @param basename base name of the file
        @throws IOException if there is an exception loading the new properties file
        """
        ...

    @overload
    def setReferencePrimary(self, reference: ghidra.program.model.symbol.Reference) -> None:
        """
        Sets the given reference as primary.
        @param reference the reference to mark as primary
        """
        ...

    @overload
    def setReferencePrimary(self, reference: ghidra.program.model.symbol.Reference, primary: bool) -> None:
        """
        Sets the given reference as primary.
        @param reference the reference
        @param primary true if primary, false not primary
        """
        ...

    def setRepeatableComment(self, address: ghidra.program.model.address.Address, comment: unicode) -> bool:
        """
        Sets a repeatable comment at the specified address
        @param address the address to set the repeatable comment
        @param comment the repeatable comment
        @return true if the repeatable comment was successfully set
        """
        ...

    def setScriptArgs(self, scriptArgs: List[unicode]) -> None:
        """
        Sets script-specific arguments
        @param scriptArgs The script-specific arguments to use.  For no scripts, use null or an
           empty array.
        """
        ...

    def setServerCredentials(self, username: unicode, password: unicode) -> bool:
        """
        Establishes fixed login credentials for Ghidra Server access.
         <p>
         NOTE: Only used for Headless environment, other GUI environments should
         continue to prompt user for login credentials as needed.
        @param username login name or null if not applicable or to use default name
        @param password login password
        @return true if active project is either private or shared project is
         connected to its server repository.  False is returned if not active
         project or an active shared project failed to connect.
        """
        ...

    def setShort(self, address: ghidra.program.model.address.Address, value: int) -> None:
        """
        Sets the 'short' value at the specified address.
        @param address the address to set the 'short'
        @param value the value to set
        @throws MemoryAccessException if memory does not exist or is uninitialized
        """
        ...

    def setSourceFile(self, sourceFile: generic.jar.ResourceFile) -> None:
        """
        Set associated source file
        @param sourceFile the source file
        """
        ...

    def setToolStatusMessage(self, msg: unicode, beep: bool) -> None:
        """
        Display a message in tools status bar.
         <p>
         This method is unavailable in headless mode.
        @param msg the text to display.
        @param beep if true, causes the tool to beep.
        @throws ImproperUseException if this method is run in headless mode
        """
        ...

    @overload
    def show(self, addresses: List[ghidra.program.model.address.Address]) -> None:
        """
        Displays the address array in a table component. The table contains an address
         column, a label column, and a preview column.
         <p>
         This method is unavailable in headless mode.
        @param addresses the address array to display
        @throws ImproperUseException if this method is run in headless mode
        """
        ...

    @overload
    def show(self, title: unicode, addresses: ghidra.program.model.address.AddressSetView) -> None:
        """
        Displays the given AddressSet in a table, in a dialog.
         <p>
         This method is unavailable in headless mode.
        @param title The title of the table
        @param addresses The addresses to display
        @throws ImproperUseException if this method is run in headless mode
        """
        ...

    def start(self) -> None:
        """
        Starts a transaction on the current program.
        """
        ...

    def storeHeadlessValue(self, key: unicode, value: object) -> None:
        """
        Stores a key/value pair in the HeadlessAnalyzer instance for later use.
         <p>
         This method, along with the 'getStoredHeadlessValue' method, is useful for debugging and
         testing the Headless Analyzer (when the user has directly instantiated the HeadlessAnalyzer
         instead of running it from analyzeHeadless.sh or analyzeHeadless.bat). This method is
         intended to allow a HeadlessScript to store variables that reflect the current state of
         processing (at the time the script is being run). Storing variables in the HeadlessAnalyzer
         instance may be the only way to access the state of processing during cases when the user
         is forced to run in -readOnly mode, or if there is a value that is only accessible at the
         scripts stage.
        @param key storage key in String form
        @param value value to store
        @throws ImproperUseException if not in headless mode or headless instance not set
        @see #getStoredHeadlessValue(String)
        @see #headlessStorageContainsKey(String)
        """
        ...

    @overload
    def toAddr(self, offset: long) -> ghidra.program.model.address.Address:
        """
        Returns a new address with the specified offset in the default address space.
        @param offset the offset for the new address
        @return a new address with the specified offset in the default address space
        """
        ...

    @overload
    def toAddr(self, offset: int) -> ghidra.program.model.address.Address:
        """
        Returns a new address with the specified offset in the default address space.
        @param offset the offset for the new address
        @return a new address with the specified offset in the default address space
        """
        ...

    @overload
    def toAddr(self, addressString: unicode) -> ghidra.program.model.address.Address:
        """
        Returns a new address inside the specified program as indicated by the string.
        @param addressString string representation of the address desired
        @return the address. Otherwise, return null if the string fails to evaluate
         to a legitimate address
        """
        ...

    @overload
    def toHexString(self, l: long, zeropad: bool, header: bool) -> unicode:
        """
        Returns a hex string representation of the long.
        @param l the long
        @param zeropad true if the value should be zero padded
        @param header true if "0x" should be prepended
        @return the hex formatted string
        """
        ...

    @overload
    def toHexString(self, b: int, zeropad: bool, header: bool) -> unicode:
        """
        Returns a hex string representation of the byte.
        @param b the integer
        @param zeropad true if the value should be zero padded
        @param header true if "0x" should be prepended
        @return the hex formatted string
        """
        ...

    @overload
    def toHexString(self, b: int, zeropad: bool, header: bool) -> unicode:
        """
        Returns a hex string representation of the byte.
        @param b the integer
        @param zeropad true if the value should be zero padded
        @param header true if "0x" should be prepended
        @return the hex formatted string
        """
        ...

    @overload
    def toHexString(self, b: int, zeropad: bool, header: bool) -> unicode:
        """
        Returns a hex string representation of the byte.
        @param b the integer
        @param zeropad true if the value should be zero padded
        @param header true if "0x" should be prepended
        @return the hex formatted string
        """
        ...

    def toString(self) -> unicode: ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def headlessAnalysisEnabled(self) -> bool: ...

    @property
    def headlessContinuationOption(self) -> ghidra.app.util.headless.HeadlessScript.HeadlessContinuationOption: ...

    @headlessContinuationOption.setter
    def headlessContinuationOption(self, value: ghidra.app.util.headless.HeadlessScript.HeadlessContinuationOption) -> None: ...

    @property
    def headlessImportDirectory(self) -> None: ...  # No getter available.

    @headlessImportDirectory.setter
    def headlessImportDirectory(self, value: unicode) -> None: ...

    @property
    def importing(self) -> bool: ...
