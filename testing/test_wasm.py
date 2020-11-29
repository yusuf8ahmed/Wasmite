import wasmite
from wasmite import types, result
from wasmite import I32, I64

# create a Test class the inherits wasmite.TestWasm
class Test(wasmite.TestWasm):
    # create a variable the hold all the functions from a specific wasm file.
    exports = wasmite.wasm_module("test.wasm")
    # create any amount of function that test you codes functionality
    def test_add(self):
        # test the "add" function in test.wasm
        result = self.exports.add(1,2)
        self.assertEqual(result, 3) 
        
    def test_sub(self):
        # test the "sub" function in test.wasm
        result = self.exports.sub(2,2) # 2-2 = 0 != -1
        self.assertEqual(result, -1)
        
    def test_sub_notequal(self):
        # test the "sub" function in test.wasm
        result = self.exports.sub(5,2) # 5-2 = 3 != -1
        self.assertNotEqual(result, -1)
        
    def test_args_add(self):
        # check that the param types of the function "add" is I32, I32
        add_function = self.exports.add
        self.assertTypes(add_function, types(I32, I32))
        
    def test_result_add(self):
        # check that the return types of the function "add" is I32
        add_function = self.exports.add
        self.assertResult(add_function, result(I32))
        
if __name__ == "__main__":
    wasmite.main()
        
        
        