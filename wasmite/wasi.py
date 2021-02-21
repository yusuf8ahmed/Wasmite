from wasmer import engine, wasi, Store, Module
from wasmer_compiler_cranelift import Compiler

from .globals import BaseModule


class WasiModule(BaseModule):
    TYPE = "WASI"

    def _import_module(self):
        """ import a module: implemented in subclasses """
        self._IMPORT_FLAG = True
        self.store = Store(engine.JIT(Compiler))
        self.wasm_bytes = open(self.path, "rb").read()
        self.module = Module(self.store, self.wasm_bytes)

        wasi_version = wasi.get_version(self.module, strict=True)
        wasi_env = wasi.StateBuilder("test-program").finalize()
        self.import_object = wasi_env.generate_import_object(self.store, wasi_version)

    def run_main(self):
        """ could raise runtime Error """
        self.exports._start()
