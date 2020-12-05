import wasmite
from wasmite import FuncType
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
        # check the types for results and parameter of the function "add"
        # param is I32, I32 and result is I32
        add_function = self.exports.add
        self.checkFunctionTypes(add_function, FuncType([I32, I32], [I32])) # result will fail
        
# Hi don't forget to add me         
if __name__ == "__main__":
    wasmite.main()