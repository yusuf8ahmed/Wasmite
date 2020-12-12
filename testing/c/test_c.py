from wasmite import WasiModule, WasmiteCase, main
from wasmite import FuncType, Function
from wasmite import I32, I64


class Test(WasmiteCase):
    module = WasiModule("test_c.wasm")
    exports = module.exports
    
    def test_main(self):
        # test and check main function
        self.module.run_main()
    
    def test_even(self):
        # test the "even" function in test_cpp.wasm
        result = self.exports.even(1)
        self.assertEqual(result, 0) 
        
    def test_squared(self):
        # test the "squared" function in test_cpp.wasm
        result = self.exports.squared(1) # 2**3
        self.assertEqual(result, 1)
        
# Hi don't forget to add me         
if __name__ == "__main__":
    main()