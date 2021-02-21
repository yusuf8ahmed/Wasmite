from wasmer import Store, wat2wasm, Module

from .globals import BaseModule


class WatModule(BaseModule):
    TYPE = "WAT"

    def _import_module(self):
        """ import a WAT module """
        self.store = Store()
        self.wasm_bytes = wat2wasm(open(self.path, "r").read())
        self.module = Module(self.store, self.wasm_bytes)
