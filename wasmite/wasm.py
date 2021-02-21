from wasmer import engine, Store, Module
from wasmer_compiler_cranelift import Compiler

from .globals import BaseModule


class WasmModule(BaseModule):
    TYPE = "WASM"

    def _import_module(self):
        """ import a WASM module """
        self.store = Store(engine.JIT(Compiler))
        self.wasm_bytes = open(self.path, "rb").read()
        self.module = Module(self.store, self.wasm_bytes)
