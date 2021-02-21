from wasmite import WasiModule, WasmiteCase
from wasmite import main


class Test(WasmiteCase):
    module = WasiModule("test_c.wasm")
    exports = module.get_exports()
    
    def test_even(self):
        # test the "even" function
        result = self.exports.even(1)
        self.assertEqual(result, 0) 
        
    def test_squared(self):
        # test the "squared" function
        result = self.exports.squared(1) # 2**3
        self.assertEqual(result, 1)
        
    def test_main(self):
        # test and check main function
        self.module.run_main()
        
# Hi don't forget to add me         
if __name__ == "__main__":
    main()