from wasmer import wasi, Store, Module, Instance

class WasiModule:
    """ Complied some code from c, c++ or rust please use me """
    def __init__(self, path):
        store = Store()
        module = Module(store, open(path, 'rb').read())
        # Get the WASI version.
        wasi_version = wasi.get_version(module, strict=True)
        # Build a WASI environment for the imports.
        wasi_env = wasi.StateBuilder('test-program').finalize()
        # Generate an `ImportObject` from the WASI environment.
        import_object = wasi_env.generate_import_object(store, wasi_version)
        # Now we are ready to instantiate the module.
        self.instance = Instance(module, import_object)
        # … But (!) WASI needs an access to the memory of the
        # module. Simple, pass it.
        wasi_env.memory = self.instance.exports.memory  
        # Export functions
        self.exports = self.instance.exports
        
    def run_main(self):
        try:
            # Here we go, let's start main function (the program).
            print("\nMain function(output):")
            self.instance.exports._start()
        except RuntimeError as e:
            if not (str(e) == "RuntimeError: WASI exited with code: 0"):   
                msg = f"WASI exited uncleanly: {str(e)}"
                msg = self._formatMessage(msg, "WASI exited")
                raise self.failureException(msg)   
            
        
        
        

    