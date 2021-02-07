from wasmer import engine, wasi, Store, Module, Instance
from wasmer_compiler_cranelift import Compiler

class WasiModule:
    """ Complied some code from c, c++ or rust please use me """
    def __init__(self, path):
        store = Store(engine.JIT(Compiler))
        module = Module(store, open(path, 'rb').read())
        wasi_version = wasi.get_version(module, strict=True)
        wasi_env = wasi.StateBuilder('test-program').finalize()
        import_object = wasi_env.generate_import_object(store, wasi_version)
        self.instance = Instance(module, import_object)
        self.exports = self.instance.exports
        
    def run_main(self):
        try:
            # Here we go, let's start main function (the program).
            print(f"\nMain function(output):")
            self.instance.exports._start()
        except RuntimeError as e:
            if not (str(e) == "RuntimeError: WASI exited with code: 0"):   
                msg = f"WASI exited uncleanly: {str(e)}"
                msg = self._formatMessage(msg, "WASI exited")
                raise self.failureException(msg)     