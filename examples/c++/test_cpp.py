from wasmite import WasiModule, WasmiteCase
from wasmite import main

class Test(WasmiteCase):
    module = WasiModule("test_cpp.wasm")
    exports = module.get_exports()
    
    def test_main(self):
        # test and check main function
        self.module.run_main()
    
    def test_add(self):
        # test the "addone" function
        result = self.exports.addone(1)
        self.assertEqual(result, 2) 
        
    def test_sub(self):
        # test the "cubed" function
        result = self.exports.cubed(1)
        self.assertEqual(result, 1)
        
# Hi don't forget to add me         
if __name__ == "__main__":
    main()