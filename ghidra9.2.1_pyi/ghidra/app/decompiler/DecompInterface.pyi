import ghidra.app.decompiler
import ghidra.program.model.address
import ghidra.program.model.lang
import ghidra.program.model.listing
import ghidra.program.model.pcode
import ghidra.util.task
import java.io
import java.lang


class DecompInterface(object):
    """
    This is a self-contained interface to a single decompile
     process, suitable for an open-ended number of function
     decompilations for a single program. The interface is
     persistent. It caches all the initialization data passed
     to it, and if the underlying decompiler process crashes,
     it automatically respawns the process and reinitializes
     it the next time it is needed.  The basic usage pattern
     is as follows

       // Instantiate the interface
       DecompInterface ifc = new DecompInterface();

       // Setup any options or other initialization
       ifc.setOptions(xmlOptions); // Inform interface of global options
       // ifc.toggleSyntaxTree(false);  // Don't produce syntax trees
       // ifc.toggleCCode(false);       // Don't produce C code
       // ifc.setSimplificationStyle("normalize"); // Alternate analysis style

       // Setup up the actual decompiler process for a
       // particular program, using all the above initialization
       ifc.openProgram(program,language);

       // Make calls to the decompiler:
       DecompileResults res = ifc.decompileFunction(func,0,taskmonitor);

       // Check for error conditions
       if (!res.decompileCompleted()) {
       	system.out.println(res.getErrorMessage());
          return;
       }

       // Make use of results
          // Get C code
       ClangTokenGroup tokgroup = res.getCCodeMarkup();
       ...
          // Get the function object/syntax tree
       HighFunction hfunc = res.getHighFunction();
       ...


    """





    def __init__(self): ...



    def closeProgram(self) -> None:
        """
        Shutdown any existing decompiler process and free
         resources.  The interface cannot be used again
         to perform decompilations until an openProgram call
         is made again.
        """
        ...

    def debugEnabled(self) -> bool:
        """
        @return true if debug has been enabled for the current/next decompilation.
        """
        ...

    def decompileFunction(self, func: ghidra.program.model.listing.Function, timeoutSecs: int, monitor: ghidra.util.task.TaskMonitor) -> ghidra.app.decompiler.DecompileResults:
        """
        Decompile function
        @param func function to be decompiled
        @param timeoutSecs if decompile does not complete in this time a null value
         will be returned and a timeout error set.
        @param monitor optional task monitor which may be used to cancel decompile
        @return decompiled function text
        """
        ...

    def dispose(self) -> None: ...

    def enableDebug(self, debugfile: java.io.File) -> None:
        """
        Turn on debugging dump for the next decompiled
         function
        @param debugfile the file to enable debug dubp
        """
        ...

    def equals(self, __a0: object) -> bool: ...

    def flushCache(self) -> int:
        """
        Tell the decompiler to clear any function and symbol
         information it gathered from the database.  Its a good
         idea to call this after any decompileFunction call,
         as the decompile process caches and reuses this kind
         of data, and there is no explicit method for keeping
         the cache in sync with the data base. Currently the
         return value has no meaning.
        @return -1
        """
        ...

    def getClass(self) -> java.lang.Class: ...

    def getCompilerSpec(self) -> ghidra.program.model.lang.CompilerSpec: ...

    def getDataTypeManager(self) -> ghidra.program.model.pcode.PcodeDataTypeManager: ...

    def getLanguage(self) -> ghidra.program.model.lang.Language: ...

    def getLastMessage(self) -> unicode:
        """
        Get the last message produced by the decompiler process.
         If the message is non-null, it is probably an error
         message, but not always.  It is better to use the
         getErrorMessage method off of DecompileResults.
        @return the message string or null
        """
        ...

    def getOptions(self) -> ghidra.app.decompiler.DecompileOptions:
        """
        Get the options currently in effect for the decompiler
        @return options that will be passed to the decompiler
        """
        ...

    def getProgram(self) -> ghidra.program.model.listing.Program: ...

    def getSimplificationStyle(self) -> unicode:
        """
        Return the identifier for the current simplification style
        @return the identifier as a String
        """
        ...

    def hashCode(self) -> int: ...

    def notify(self) -> None: ...

    def notifyAll(self) -> None: ...

    def openProgram(self, prog: ghidra.program.model.listing.Program) -> bool:
        """
        This call initializes a new decompiler process to do
         decompilations for a new program. This method only
         needs to be called once per program.  Even if the
         underlying decompiler process crashes, the interface
         will automatically restart and reinitialize a new
         process when it needs it, and the openProgram call
         does not need to be made again. The call can be made
         multiple times, in which case, each call terminates
         the process initialized the last time and starts a
         new process
        @param prog = the program on which to perform decompilations
        @return true if the decompiler process is successfully initialized
        """
        ...

    def resetDecompiler(self) -> None:
        """
        Resets the native decompiler process.  Call this method when the decompiler's view
         of a program has been invalidated, such as when a new overlay space has been added.
        """
        ...

    def setOptions(self, xmloptions: ghidra.app.decompiler.DecompileOptions) -> bool:
        """
        Set the object controlling the list of global options
         used by the decompiler. Ideally this is called once,
         before the openProgram call is made. But it can be
         used at any time, if the options change in the middle
         of a sequence of decompiles.
         If there is no change to the options, this method
         does NOT need to be called repeatedly.  Even after
         recovering from decompiler process crash, the interface
         keeps the options object around and automatically
         sends it to the new decompiler process.
        @param xmloptions the new (or changed) option object
        @return true if the decompiler process accepted the new options
        """
        ...

    def setSimplificationStyle(self, actionstring: unicode) -> bool:
        """
        This allows the application to the type of analysis
         performed by the decompiler, by giving the name of
         an analysis class. Right now, there are a few
         predefined classes. But there soon may be support
         for applications to define their own class and
         tailoring the decompiler's behaviour for that class.
         <p>
         The current predefined analysis class are:
         <ul>
           <li>"decompile" - this is the default, and performs all
              analysis steps suitable for producing C code.
           <li>"normalize" - omits type recovery from the analysis
              and some of the final clean-up steps involved in
              making valid C code.  It is suitable for creating
              normalized pcode syntax trees of the dataflow.
           <li>"firstpass" - does no analysis, but produces an
              unmodified syntax tree of the dataflow from the
           <li>"register" - does ???.
           <li>"paramid" - does required amount of decompilation
              followed by analysis steps that send parameter
              measure information for parameter id analysis.
              raw pcode.
         </ul>

         <p>
         This property should ideally be set once before the
         openProgram call is made, but it can be used repeatedly
         if the application needs to change analysis style in the
         middle of a sequence of decompiles.  Unless the style
         changes, the method does NOT need to be called repeatedly.
         Even after a crash, the new decompiler process will
         automatically configured with the cached style value.
        @param actionstring "decompile"|"normalize"|"register"|"firstpass"|"paramid"
        @return true - if the decompiler process was successfully configured
        """
        ...

    def stopProcess(self) -> None:
        """
        Stop the decompile process.

         NOTE: Subsequent calls made from another
         thread to this DecompInterface object may fail since the decompiler
         process is being yanked away.
        """
        ...

    def structureGraph(self, ingraph: ghidra.program.model.pcode.BlockGraph, factory: ghidra.program.model.address.AddressFactory, timeoutSecs: int, monitor: ghidra.util.task.TaskMonitor) -> ghidra.program.model.pcode.BlockGraph: ...

    def toString(self) -> unicode: ...

    def toggleCCode(self, val: bool) -> bool:
        """
        Toggle whether or not calls to the decompiler process
         (via the decompileFunction method) produce C code.
         The default is to always compute C code, but some
         applications may only need the syntax tree or other
         function information. Ideally this method should
         be called once before the openProgram call, but it
         can be used at any time, if the application wants
         to change before in the middle of a sequence of
         decompiles. Unless the desired value changes, the
         method does NOT need to be called repeatedly. Even
         after a decompiler process crash, the old value is
         cached and automatically sent to the new process
        @param val = true, to produce C code, false otherwise
        @return true if the decompiler process accepted the new state
        """
        ...

    def toggleJumpLoads(self, val: bool) -> bool:
        """
        Toggle whether or not the decompiler process should return information about tables
         used to recover switch statements.  Most compilers implement switch statements using a
         so called "jumptable" of addresses or offsets.  The decompiler can frequently recover this
         and can return a description of the table
        @param val = true, to have the decompiler return table info, false otherwise
        @return true if the decompiler process accepted the new state
        """
        ...

    def toggleParamMeasures(self, val: bool) -> bool:
        """
        Toggle whether or not calls to the decompiler process
         (via the decompileFunction method) produce Parameter
         Measures. The default is to not compute Parameter
         Measures. Ideally this method should
         be called once before the openProgram call, but it
         can be used at any time, if the application wants
         to change before in the middle of a sequence of
         decompiles. Unless the desired value changes, the
         method does NOT need to be called repeatedly. Even
         after a decompiler process crash, the old value is
         cached and automatically sent to the new process
        @param val = true, to produce C code, false otherwise
        @return true if the decompiler process accepted the new state
        """
        ...

    def toggleSyntaxTree(self, val: bool) -> bool:
        """
        This method toggles whether or not the decompiler
         produces a syntax tree (via calls to decompileFunction).
         The default is to always produce a syntax tree, but
         some applications may only need C code.  Ideally this method should
         be called once before the openProgram call, but it
         can be used at any time, if the application wants
         to change before in the middle of a sequence of
         decompiles. Unless the desired value changes, the
         method does NOT need to be called repeatedly. Even
         after a decompiler process crash, the old value is
         cached and automatically sent to the new process
        @param val = true, to produce a syntax tree, false otherwise
        @return true if the decompiler process, accepted the change of state
        """
        ...

    @overload
    def wait(self) -> None: ...

    @overload
    def wait(self, __a0: long) -> None: ...

    @overload
    def wait(self, __a0: long, __a1: int) -> None: ...

    @property
    def compilerSpec(self) -> ghidra.program.model.lang.CompilerSpec: ...

    @property
    def dataTypeManager(self) -> ghidra.program.model.pcode.PcodeDataTypeManager: ...

    @property
    def language(self) -> ghidra.program.model.lang.Language: ...

    @property
    def lastMessage(self) -> unicode: ...

    @property
    def options(self) -> ghidra.app.decompiler.DecompileOptions: ...

    @options.setter
    def options(self, value: ghidra.app.decompiler.DecompileOptions) -> None: ...

    @property
    def program(self) -> ghidra.program.model.listing.Program: ...

    @property
    def simplificationStyle(self) -> unicode: ...

    @simplificationStyle.setter
    def simplificationStyle(self, value: unicode) -> None: ...
