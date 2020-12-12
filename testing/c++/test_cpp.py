from wasmite import Module, WasmiteCase, main
from wasmite import FuncType, Function
from wasmite import I32, I64

from wasmite import WasiModule


class Test(WasmiteCase):
    module = WasiModule("test_cpp.wasm")
    exports = module.exports
    
    def test_main(self):
        # test and check main function
        self.module.run_main()
    
    def test_add(self):
        # test the "addone" function in test_cpp.wasm
        result = self.exports.addone(1)
        self.assertEqual(result, 2) 
        
    def test_sub(self):
        # test the "cubed" function in test_cpp.wasm
        result = self.exports.cubed(1) # 2**3
        self.assertEqual(result, 1)
        
# Hi don't forget to add me         
if __name__ == "__main__":
    main()